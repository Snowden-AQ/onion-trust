#config
import socket; socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050); socket.socket = socks.socksocket; print('Sockets redirected over Tor')
import socks
some_variable = 'example data'
import socket; socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050); socket.socket = socks.socksocket; print('Sockets redirected over Tor')
import stem.control
import hashlib
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
import socket
import hashlib
import hashlib
print('Checking Tor status...')
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
some_variable = 'example data'
import socks
import socket; socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050); socket.socket = socks.socksocket; print('Sockets redirected over Tor')
import requests; response = requests.get('http://check.torproject.org/', proxies={'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}); print(response.text)
