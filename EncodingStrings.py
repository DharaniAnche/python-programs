import base64
x = "Python"
y = x.encode('ascii')
base64_bytes = base64.b64encode(y)
base64_message = base64_bytes.decode('ascii')
print(base64_message)
