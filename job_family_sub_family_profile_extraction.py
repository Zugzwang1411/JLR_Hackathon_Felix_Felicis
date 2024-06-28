import json

with open('extracted_jobs.json', 'r') as file:
    data = json.load(file)

result = []

for job_family_id, job_family_data in data.items():
    job_family_entry = [job_family_id, []]

    for job_sub_family in job_family_data['job_sub_family']:
        job_sub_family_id = job_sub_family['job_sub_family_id']

        job_sub_family_entry = [job_sub_family_id, []]

        for profile in job_sub_family['profile']:
            profile_name = profile['profile_name']

            profile_ids = []

            for job in profile['jobs']:
                job_id = job['JobID']

                profile_ids.append(job_id)

            job_sub_family_entry[1].append([profile_name, profile_ids])

        job_family_entry[1].append(job_sub_family_entry)

    result.append(job_family_entry)
