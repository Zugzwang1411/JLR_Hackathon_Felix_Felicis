import json

# Load the JSON data from file (replace with your actual JSON file path)
with open('extracted_jobs.json', 'r') as file:
    data = json.load(file)

# Initialize an empty list to store the structured data
result = []

# Iterate over each job family (e.g., "SL", "FA", etc.)
for job_family_id, job_family_data in data.items():
    # Initialize a list for the job family
    job_family_entry = [job_family_id, []]

    # Iterate over each job sub-family in the job family
    for job_sub_family in job_family_data['job_sub_family']:
        job_sub_family_id = job_sub_family['job_sub_family_id']

        # Initialize a list for the job sub-family
        job_sub_family_entry = [job_sub_family_id, []]

        # Iterate over each profile in the job sub-family
        for profile in job_sub_family['profile']:
            profile_name = profile['profile_name']

            # Initialize a list for the profile IDs
            profile_ids = []

            # Iterate over each job in the profile
            for job in profile['jobs']:
                job_id = job['JobID']

                # Append job_id to the profile_ids list
                profile_ids.append(job_id)

            # Append profile_name and profile_ids to job_sub_family_entry
            job_sub_family_entry[1].append([profile_name, profile_ids])

        # Append job_sub_family_entry to job_family_entry
        job_family_entry[1].append(job_sub_family_entry)

    # Append job_family_entry to result
    result.append(job_family_entry)

# Print the result structure
# print(result)
print(result[0][1][0][1][0][1][0])
# [1][0][1][2][1])