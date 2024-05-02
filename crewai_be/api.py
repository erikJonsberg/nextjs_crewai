from datetime import datetime
import json
from threading import Thread

from uuid import uuid4
from flask import Flask, abort, jsonify, request
from flask_cors import CORS

from crew import CompanyResearchCrew
from job_manager import jobs, jobs_lock, append_event, Event

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
def kickoff_crew(job_id: str, companies: list[str], positions: list[str]):
    print(f'Running crew.ai with job_id={job_id}, companies={
          companies}, positions={positions}')

    results = None
    try:
        company_research_crew = CompanyResearchCrew(job_id)
        company_research_crew.setup_crew(companies, positions)
        results = company_research_crew.kickoff()

    except Exception as e:
        print(f'An error occurred: {str(e)}')
        append_event(job_id, f"An error occurred: {str(e)}")
        with jobs_lock:
            jobs[job_id].status = "ERROR"
            jobs[job_id].result = str(e)

    with jobs_lock:
            jobs[job_id].status = "COMPLETE"
            jobs[job_id].result = results
            jobs[job_id].events.append(Event(data="Crew finished", timestamp=datetime.now()))

@app.route('/api/crew', methods=['POST'])
def run_crew():
    data = request.json
    if not data or 'companies' not in data or 'positions' not in data:
        abort(400, description="Invalid input data provided.")

    job_id = str(uuid4())
    companies = data['companies']
    positions = data['positions']

    # Run the crew.ai algorithm
    thread = Thread(target=kickoff_crew, args=(job_id, companies, positions))
    thread.start()

    return jsonify({'job_id': job_id}), 200


@app.route('/api/crew/<job_id>', methods=['GET'])
def get_status(job_id):
    with jobs_lock:
        job = jobs.get(job_id)
        if job_id not in jobs:
            abort(404, description=f"Job with id {job_id} not found.")

    try:
        result_json = json.loads(job.result)
    except:
        result_json = job.result
        
    return jsonify({
        'status': job.status,
        'events': [{"timestamp": event.timestamp.isoformat(), "data": event.data} for event in job.events],
        'result': result_json
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=3001)
