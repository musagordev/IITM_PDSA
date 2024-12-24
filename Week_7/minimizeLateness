# Greedy Algorithm
# In a factory to work with N independent job lines. Each job requires amount of time to be completed.
# Optimize scheduling jobs for minimizing lateness to complete all jobs.
# N is number of working lines. jobs is a list of tuples, (job_id, time_required, due_time)

def minimizeLateness(N,jobs):
    jobs = sorted(jobs, key=lambda x: x[2])
    processors = [[] for i in range(N)]
    processor_end_times = [0] * N
    total_lateness = 0
    
    for job in jobs:
        job_id, time_required, due_time = job
        min_processor_idx = processor_end_times.index(min(processor_end_times))
        start_time = processor_end_times[min_processor_idx]
        end_time = start_time + time_required
        lateness = max(0, end_time - due_time)
        total_lateness += lateness
        processors[min_processor_idx].append(job_id)
        processor_end_times[min_processor_idx] = end_time
    return processors
    
