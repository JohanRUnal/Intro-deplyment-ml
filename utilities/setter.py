import os
from base64 import b64decode


def main():
    key = os.environ.get("AWS_ACCESS_KEY_ID")
    secret_access = os.environ.get("AWS_SECRET_ACCESS_KEY")
    with open("path.json", "w") as json_file:
        json_file.write(b64decode(key).decode())
    print(os.path.realpath("path.json"))



if __name__ == "__main__":
    main()
