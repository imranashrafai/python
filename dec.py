import base64

encoded_string = "sdds322ssa=aesda"

decoded_bytes = base64.b64decode(encoded_string)
decoded_string = decoded_bytes.decode('utf-8')

print(decoded_string)
