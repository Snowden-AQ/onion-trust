#config
import requests; response = requests.get('http://check.torproject.org/', proxies={'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}); print(response.text)
import stem.control
import stem.control; with stem.control.Controller.from_port() as controller: controller.authenticate(); print('Tor is running' if controller.is_alive() else 'Tor is not running')
import socket; socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050); socket.socket = socks.socksocket; print('Sockets redirected over Tor')
print('Checking Tor status...')
import stem.control; with stem.control.Controller.from_port() as controller: controller.authenticate(); print('Tor is running' if controller.is_alive() else 'Tor is not running')
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
import requests
import socket; socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050); socket.socket = socks.socksocket; print('Sockets redirected over Tor')
print('Checking Tor status...')
import socks
import socket; socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050); socket.socket = socks.socksocket; print('Sockets redirected over Tor')
import socks
import requests; response = requests.get('http://check.torproject.org/', proxies={'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}); print(response.text)
some_variable = 'example data'
import stem.control; with stem.control.Controller.from_port() as controller: controller.authenticate(); print('Tor is running' if controller.is_alive() else 'Tor is not running')
some_variable = 'example data'
print('Checking Tor status...')
import socket; socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050); socket.socket = socks.socksocket; print('Sockets redirected over Tor')
import hashlib
