#config
print('Checking Tor status...')
import hashlib
import stem.control; with stem.control.Controller.from_port() as controller: controller.authenticate(); print('Tor is running' if controller.is_alive() else 'Tor is not running')
import requests
import hashlib
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
import requests; response = requests.get('http://check.torproject.org/', proxies={'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}); print(response.text)
some_variable = 'example data'
import stem.control
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
some_variable = 'example data'
some_variable = 'example data'
print('Checking Tor status...')
