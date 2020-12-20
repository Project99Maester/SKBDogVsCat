import base64

def decodeImage(imgstring, fileName):
    imgData = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgData)

