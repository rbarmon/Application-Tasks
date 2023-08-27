import hashlib


def main(shared_secret_hex):

    # Decode the hex-encoded string to obtain the raw bytes
    # shared_secret_bytes = bytes.fromhex(shared_secret_hex)
    shared_secret_bytes = shared_secret_hex

    # Pad the bytes with zeroes to reach a 64-byte (512-bit) length if necessary
    if len(shared_secret_bytes) < 64:
        shared_secret_bytes = shared_secret_bytes + b'\x00' * (64 - len(shared_secret_bytes))
    elif len(shared_secret_bytes) > 64:
        shared_secret_bytes = shared_secret_bytes[:64]
    # Now, 'shared_secret_bytes' is a 64-byte (512-bit) value that can be used as the secret key in HMAC-SHA512.
    print(shared_secret_bytes)
    print(len(shared_secret_bytes))


def other(shared_secret_hex):
    # Convert the hex-encoded string to bytes and ensure it is 64 bytes long
    shared_secret_bytes = bytes.fromhex(shared_secret_hex)
    shared_secret_bytes = shared_secret_bytes.ljust(64, b'\x00')

    # Now, 'shared_secret_bytes' is a 64-byte (512-bit) value that can be used as the secret key in HMAC-SHA512.
    print(shared_secret_bytes)
    print(len(shared_secret_bytes))


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
    # Assuming the shared secret is provided in hex-encoded format
    shared_secret_hex = "72626172303033324073747564656E742E6D6F6E6173682E65647548454E4E47454348414C4C454E4745303033"

    main(shared_secret_hex)
    print("3132333435363738393031323334353637383930" +
                "3132333435363738393031323334353637383930" +
                "3132333435363738393031323334353637383930" +
                "31323334")
    print(len("3132333435363738393031323334353637383930" +
                "3132333435363738393031323334353637383930" +
                "3132333435363738393031323334353637383930" +
                "31323334"))

    other(shared_secret_hex)

    print(len("3132333435363738393031323334353637383930"))

    # Example usage:
    # username = "Aladdin"
    username = "rbar0032@student.monash.edu"
    password = "open sesame"
    password = "2291555459"
    auth_header = generate_basic_auth_header(username, password)
    print(auth_header)
    # Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ ==
