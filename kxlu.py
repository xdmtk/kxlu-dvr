from urllib import request
stream = open("./alien.mp3", "wb")
conn = request.urlopen("http://kxlu.streamguys1.com/kxlu-hi")
while True:
    stream.write(conn.read(4096))

