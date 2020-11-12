import requests

VIDEO_PATH = './Hermeco Oficinas_10.50.60.47_1_20201001161330_20201001161924_1601609295690.mp4.jpg'
url = "http://ec2-54-227-15-49.compute-1.amazonaws.com"

with open(VIDEO_PATH, 'rb') as f:
    print(f)
    requests.post(url, data=f)
