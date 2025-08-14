from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/jobs")
def get_jobs():
    with open("jobs.json") as f:
        return json.load(f)

@app.post("/apply/{job_id}")
def apply_to_job(job_id: int):
    with open("jobs.json") as f:
        jobs = json.load(f)
    for job in jobs:
        if job["id"] == job_id:
            job["applied"] = True
    with open("jobs.json", "w") as f:
        json.dump(jobs, f)
    return {"status": "applied"}
