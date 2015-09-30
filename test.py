import chrome_remote_shell, json
import time
shell = chrome_remote_shell.Shell(host='localhost', port=9222)
shell.connect(0)

navcom = json.dumps({"id":0, "method":"Network.enable"})
shell.soc.send(navcom)
response = json.loads(shell.soc.recv())
print response

url = 'http://www.clift.org/fred' # shameless
navcom = json.dumps({"id":0, "method":"Page.navigate", "params":{"url":url}})
shell.soc.send(navcom)
response = json.loads(shell.soc.recv())

while (True):
	response = json.loads(shell.soc.recv())
	print response
	time.sleep(1)