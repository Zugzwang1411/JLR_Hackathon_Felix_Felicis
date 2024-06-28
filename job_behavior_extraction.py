from pathlib import Path
import json
def check_if_file_empty(filename):
    p = Path(filename)
    return p.stat().st_size == 0

def data_json_file(data_json_filepath):
    data_JSON_file = Path(data_json_filepath)

    return_code = 0

    if not data_JSON_file.exists():
        exit("data JSON file does not exist.")
    elif check_if_file_empty(data_JSON_file) is True:
        exit("Transitions JSON config file is empty.")
    else:
        data = json.load(data_JSON_file.open())
        if not data:
            print("Transitions JSON config file is empty.")
            return_code = 1
        else:
            return_code = 0   
    return return_code, data

def extract_job_skills(data):
    job_skill_list = []
    for job in data:
        job_id = job.get("job_id")
        skills = job.get("behavior")
        skills_list = list(skills.keys())
        skill_key_value=[]
        for skill_key in skills_list:
            skill_value=skills[skill_key]
            skill_key_value.append([skill_key, skill_value])
        job_skills_pair=[job_id, skill_key_value]
        job_skill_list.append(job_skills_pair)
    return job_skill_list
        


if __name__ == "__main__" :
    project_dir = Path(__file__).parents[0]
    data_json_filepath = Path(project_dir).joinpath("behave.json")
    return_code, data = data_json_file(data_json_filepath)
    list_of_jobs_with_skills = extract_job_skills(data)
    for item in list_of_jobs_with_skills:
        print(f"Job id; {item[0]}")
        print("Skills:")
        for skills in item[1]:
            print(skills[0]," level: ",skills[1])
