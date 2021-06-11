import json
import requests
import time

job_name = "first-pipeline"


def jenkins_job_status():
    try:
        url = "http://localhost:8080/job/"+job_name+"/lastBuild/api/json"
        while True:
            data = requests.get(url).json()
            if data['building']:
                time.sleep()
            else:
                if data['result'] == 'SUCCESS':
                    print("Job is success")
                    return True
                else:
                    print("Job is failed")
                    return False

    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":

    if jenkins_job_status():

        print("Put your autmation here for 'job is success' condition")

    else:
        print("Put your autmation here for 'job is failed' condition")
