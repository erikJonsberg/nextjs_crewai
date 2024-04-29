from agents import CompanyResearchAgents
from job_manager import append_event
from tasks import CompanyResearchTasks
from crewai import Crew
from langchain_openai import ChatOpenAI


class CompanyResearchCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id
        self.crew = None
        self.llm = ChatOpenAI(model="gpt-4-turbo-preview")

    def setup_crew(self, companies: list[str], positions: list[str]):

        agents = CompanyResearchAgents()
        research_manager = agents.research_manager(companies, positions)
        company_research_agent = agents.company_research_agent()

        tasks = CompanyResearchTasks(job_id=self.job_id)

        company_research_tasks = [
            tasks.company_research(company_research_agent, companies, positions)
            for company in companies
        ]

        manage_research_task = tasks.manage_research(
            research_manager, companies, positions, company_research_tasks)

        self.crew = Crew(
            agents=[research_manager, company_research_agent],
            tasks=[*company_research_tasks, manage_research_task],
            verbose=2,
        )

    def kickoff(self):
        if not self.crew:
            print(f'Crew for {self.job_id} not set up. Please call setup_crew() first.')
            return
        append_event(self.job_id, "Crew started")
        try:
            print(f'Running crew for {self.job_id}')
            results = self.crew.kickoff()
            append_event(self.job_id, "Crew finished")
            return results

        except Exception as e:
            append_event(self.job_id, f"An error occurred: {e}")
            return str(e)
