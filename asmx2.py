from suds.client import Client

url = 'http://10.10.7.220/PythonService/line.asmx?WSDL'
client = Client(url)
result = client.service.ReceiveMessage()

if len(result) > 0:
	for list in result[0]:
		print list["VALUE"]
		item_id = list["ID"]