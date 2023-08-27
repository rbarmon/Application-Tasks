import hmac
import hashlib
import struct
import base64
import pyotp
import time
import requests

#
# def generate_totp_password(shared_secret):
#     time_interval = 30
#     t0 = 0
#     current_time = int(time.time())
#     time_steps = (current_time - t0) // time_interval
#     time_steps_bytes = struct.pack(">Q", time_steps)
#
#     hmac_sha512 = hmac.new(shared_secret.encode(), time_steps_bytes, hashlib.sha512).digest()
#
#     offset = hmac_sha512[-1] & 0x0F
#     truncated_hash = hmac_sha512[offset:offset + 8]
#     totp_integer = struct.unpack(">Q", truncated_hash)[0]
#
#     mask = 0x7FFFFFFFFFFFFF  # 63 bits set to 1
#     totp_integer &= mask
#
#     return str(totp_integer % 10**10).zfill(10)

def generate_totp_password(shared_secret):
    time_interval = 30
    t0 = 0
    current_time = int(time.time())
    time_steps = (current_time - t0) // time_interval
    time_steps_bytes = struct.pack(">Q", time_steps)  # Use time_steps, not current_time

    hmac_sha512 = hmac.new(shared_secret.encode(), time_steps_bytes, hashlib.sha512).digest()

    offset = hmac_sha512[-1] & 0x0F
    truncated_hash = hmac_sha512[offset:offset + 8]
    totp_integer = struct.unpack(">Q", truncated_hash)[0]

    mask = 0x7FFFFFFFFFFFFF  # 63 bits set to 1
    totp_integer &= mask

    return str(totp_integer % 10**10).zfill(10)


import base64
import pyotp
import hashlib  # Import hashlib to use the HMAC-SHA-512 hash function


def python_totp():
    # Replace "ninja@example.comHENNGECHALLENGE003" with your actual shared secret.
    shared_secret = "rbar0032@student.monash.eduHENNGECHALLENGE003"
    encoded_secret = base64.b32encode(shared_secret.encode()).decode()
    print("Base32 Encoded Secret:", shared_secret)

    #     print("Base32 Encoded Secret:", encoded_secret)
    # Specify the number of digits for the TOTP password (e.g., 8 digits)
    digits = 10

    # Create a TOTP object with the shared secret
    #     totp = pyotp.TOTP(shared_secret, interval=30, digits=digits, digest=hashlib.sha512)

    totp = pyotp.TOTP(encoded_secret, interval=30, digits=digits, digest=hashlib.sha512)

    # Get the current TOTP password
    totp_password = totp.now()

    print("TOTP Password:", totp_password)

    return totp_password

def main():
    # Replace "ninja@example.comHENNGECHALLENGE003" with your actual shared secret.
    # shared_secret = "ninja@example.comHENNGECHALLENGE003"
    shared_secret = "rbar0032@student.monash.eduHENNGECHALLENGE003"
    # shared_secret = "rabchuunyuu@gmail.comHENNGECHALLENGE003"

    # totp_password = generate_totp_password(shared_secret)
    # Create a TOTP object with the shared secret
    # totp = pyotp.TOTP(shared_secret, interval=30)
    #
    # # Get the current TOTP password
    # totp_password = totp.now()

    totp_password = python_totp()
    print(totp_password)

    # Construct the HTTP Basic Authentication header value.
    # username = "ninja@example.com"
    username = "rbar0032@student.monash.edu"
    # username = "rabchuunyuu@gmail.com"
    combined_string = f"{username}:{totp_password}"
    auth_header_value = base64.b64encode(combined_string.encode()).decode()

    # The auth_header_value can be included in the "Authorization" header of your HTTP request.
    auth_header = f"Basic {auth_header_value}"
    print("Authorization Header:", auth_header)
    # POST(auth_header)


def POST(auth_header):
    url = "https://api.challenge.hennge.com/challenges/003"
    headers = {
        "Authorization": auth_header,
        "Host": "api.challenge.hennge.com",
        "Accept": "*/*",
        "Content-Type": "application/json"
    }

    data = {"github_url": "https://gist.github.com/rbarmon/35d7fed1d7ee4e196fcef74d37f21fbe",
            "contact_email": "rbar0032@student.monash.edu", "solution_language": "python"}
    # data = {"github_url": "https://gist.github.com/rbarmon/35d7fed1d7ee4e196fcef74d37f21fbe",
    #         "contact_email": "rabchuunyuu@gmail.com", "solution_language": "python"}

    print(url)
    print(headers)
    print(data)

    response = requests.post(url, headers=headers, json=data)

    print("Status Code:", response.status_code)
    print("Response Content:", response.text)

# Authorization Header: Basic cmJhcjAwMzJAc3R1ZGVudC5tb25hc2guZWR1OjYyNjgzMjcyNTc=
# Authorization Header: Basic cmJhcjAwMzJAc3R1ZGVudC5tb25hc2guZWR1OjEwNjc5NTAxNjY=
# Authorization Header: Basic cmJhcjAwMzJAc3R1ZGVudC5tb25hc2guZWR1OjA0MzU0Njk3MDM=

# Authorization
# Header: Basic
# cmJhcjAwMzJAc3R1ZGVudC5tb25hc2guZWR1OjYyNjgzMjcyNTc =

if __name__ == '__main__':
    main()


# Basic cmJhcjAwMzJAc3R1ZGVudC5tb25hc2guZWR1Ojk2NTg1NjI3ODQ=
# Authorization Header: Basic cmJhcjAwMzJAc3R1ZGVudC5tb25hc2guZWR1Ojk2NTg1NjI3ODQ=


# {'Authorization': 'Basic cmJhcjAwMzJAc3R1ZGVudC5tb25hc2guZWR1OjM2MjA4MjA0MjQ=', 'Host': 'api.challenge.hennge.com', 'Accept': '*/*', 'Content-Type': 'application/json'}