from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict
from threading import Lock

jobs_lock = Lock()
jobs: Dict[str, "Job"] = {}


@dataclass
class Event:
    timestamp: datetime
    data: str


@dataclass
class Job:
    status: str
    events: List[Event]
    result: str


def append_event(job_id: str, event_data: str):
    with jobs_lock:
        if job_id not in jobs:
            jobs[job_id] = Job(
                status='STARTED',
                events=[],
                result='')
        else:
            jobs[job_id].events.append(Event(timestamp=datetime.now(), data=event_data))