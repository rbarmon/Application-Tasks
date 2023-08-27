import requests

def main():
    url = "https://api.challenge.hennge.com/challenges/003"
    headers = {
        # "Authorization": "Basic bmluamFAZXhhbXBsZS5jb206MTU5NTk0MjU2MA==",
        "Authorization": "",
        "Host": "api.challenge.hennge.com",
        "Accept": "*/*",
        "Content-Type": "application/json"
    }

    data = {"github_url": "https://gist.github.com/rbarmon/35d7fed1d7ee4e196fcef74d37f21fbe",
            "contact_email": "rbar0032@student.monash.edu", "solution_language": "python"}

    response = requests.post(url, headers=headers, json=data)

    print("Status Code:", response.status_code)
    print("Response Content:", response.text)
if __name__ == '__main__':
    main()