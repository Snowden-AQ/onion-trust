Wed Apr 17 16:27:44 BST 2024
import stem.control; with stem.control.Controller.from_port() as controller: controller.authenticate(); print('Tor is running' if controller.is_alive() else 'Tor is not running')
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
import requests; response = requests.get('http://check.torproject.org/', proxies={'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}); print(response.text)
