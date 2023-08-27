import hmac
import hashlib
import struct
import time
import pyotp

def python_totp():
    # Replace "ninja@example.comHENNGECHALLENGE003" with your actual shared secret.
    shared_secret = "rbar0032@student.monash.eduHENNGECHALLENGE003"
    encoded_secret = base64.b32encode(shared_secret.encode()).decode()
    print("Base32 Encoded Secret:", encoded_secret)
    # Create a TOTP object with the shared secret
    totp = pyotp.TOTP(encoded_secret, interval=30)

    # Get the current TOTP password
    totp_password = totp.now()

    print("TOTP Password:", totp_password)

def generate_totp_password(secret_key):
    # Get the current Unix time
    current_time = int(time.time())

    # Divide the current time by the time interval (30 seconds)
    time_interval = 30
    time_steps = current_time // time_interval

    # Convert the time steps to bytes
    time_steps_bytes = struct.pack(">Q", time_steps)

    # Create an HMAC-SHA-512 hash using the secret key and time steps bytes
    hmac_sha512 = hmac.new(secret_key.encode(), time_steps_bytes, hashlib.sha512).digest()

    # Get the last 8 bits of the hash to use as an index
    offset = hmac_sha512[-1] & 0x0F

    # Extract an 8-byte slice from the hash starting from the index
    truncated_hash = hmac_sha512[offset:offset + 8]

    # Convert the 8-byte slice to an integer (big endian)
    totp_integer = struct.unpack(">Q", truncated_hash)[0]

    # Apply a mask to get a 10-digit number
    mask = 0x7FFFFFFFFFFFFF  # 63 bits set to 1
    totp_integer &= mask

    # Convert the integer to a 10-digit TOTP password
    totp_password = str(totp_integer % 10**10).zfill(10)

    return totp_password


import base64


def generate_basic_auth_header(username, password):
    # Combine the username and password with a colon separator
    combined_string = f"{username}:{password}"

    # Encode the combined string using Base64
    encoded_string = base64.b64encode(combined_string.encode()).decode()

    # Generate the Authorization header value
    auth_header = f"Basic {encoded_string}"
    return auth_header


if __name__ == '__main__':

    # Example usage:
    # secret_key = "your_secret_key_here"
    # secret_key = "rbar0032@student.monash.eduHENNGECHALLENGE003"
    # secret_key = "ninja@example.comHENNGECHALLENGE003"
    secret_key = "rabchuunyuu@gmail.comHENNGECHALLENGE003"
    totp_password = generate_totp_password(secret_key)
    #Changes every minute
    # 0628269772
    # 6181912964
    print(totp_password)

    username = "rbar0032@student.monash.edu"
    # username = "ninja@example.com"
    username = "rabchuunyuu@gmail.com"
    password = totp_password
    auth_header = generate_basic_auth_header(username, password)
    print(auth_header)
    print("pyotp")
    python_totp()