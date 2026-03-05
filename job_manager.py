import asyncio
from database import db
from models import Job, JobStatus

class JobManager:
    def __init__(self, max_concurrent):
        self.queue = asyncio.Queue()
        self.active_jobs = {}
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.workers = []
        self.running = True

    async def start(self):
        for i in range(self.semaphore._value):
            worker = asyncio.create_task(self._worker(f"worker-{i}"))
            self.workers.append(worker)

    async def add_job(self, job: Job):
        db.add_job(job)
        await self.queue.put(job.id)
        return job.id

    async def _worker(self, name):
        while self.running:
            job_id = await self.queue.get()
            job = db.get_job(job_id)
            if not job or job.status == JobStatus.CANCELLED:
                self.queue.task_done()
                continue
            async with self.semaphore:
                # Process job
                # 1. music analysis
                # 2. scene detection
                # 3. timeline
                # 4. render
                # update DB
            self.queue.task_done()

    def cancel_job(self, job_id):
        job = db.get_job(job_id)
        if job and job.status in (JobStatus.PENDING, JobStatus.PROCESSING):
            job.cancel_requested = True
            db.update_job(job)
