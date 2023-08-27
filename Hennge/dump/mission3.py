import requests
import json


def main():
    url = 'https://api.challenge.hennge.com/challenges/003'
    data = {"github_url": "https://gist.github.com/rbarmon/35d7fed1d7ee4e196fcef74d37f21fbe", "contact_email": "rbar0032@student.monash.edu", "solution_language": "python"}
    userid = 'rbar0032@student.monash.edu'
    password = 'your_password'
    # auth = "Basic rbar0032@student.monash.edu:your_password"
    authenticate = 'Basic cmJhcjAwMzJAc3R1ZGVudC5tb25hc2guZWR1OjI1NTc0NzY3ODI='
    # bmluamFAZXhhbXBsZS5jb206


    # Convert the data to a JSON string
    json_data = json.dumps(data)

    headers = {'Content-Type': 'application/json'}

    # response = requests.post(url, data=json_data, headers=headers, auth=(userid, password))
    response = requests.post(url, data=json_data, headers=headers, auth=authenticate)

    if response.status_code == 200:
        print("POST request successful!")
        print(response.text)
    else:
        print("POST request failed with status code:", response.status_code)


if __name__ == '__main__':
    main()