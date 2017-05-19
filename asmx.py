from suds.client import Client
from line import LineClient, LineGroup, LineContact
from config import *
from function import *
import time

configlist = config_list()
GROUPNAME = configlist[2]
TOKEN = ''

try:
	lineclient = LineClient(id=configlist[0], password=configlist[1], authToken=TOKEN)
	TOKEN = lineclient.authToken
	print "TOKEN : %s\r\n" % TOKEN

except:
	print "Login Failed\r\n"
	exit()

url = 'http://10.10.150.187/PythonService/line.asmx?WSDL'
client = Client(url)

client_group = lineclient.getGroupByName(GROUPNAME)
client_group.sendMessage("Login Complete!!")

#recent_group_msg = client_group.getRecentMessages(count=10)
#print "RecentMessages : %s\r\n" % recent_group_msg

while True:

	result = client.service.ReceiveMessage()
	if len(result) > 0:
		for list in result[0]:
			item_id = list["ID"]
			room_name = list["ROOM"]
			value = list["VALUE"]
			client_group.sendMessage(value)

	op_list = []
	for op in lineclient.longPoll():
		op_list.append(op)

	for op in op_list:
		sender   = op[0]
		receiver = op[1]
		message  = op[2]
		msg = message.text

		fromwhom = lineclient.getContactByName(sender.name)
		#print "fromwhom : %s\r\n" % fromwhom

		result = process(msg)
		if result != "":
			receiver.sendMessage("%s" % result)
		
		if msg.startswith("!save"):
			client.service.SaveMessage(msg.replace("!save", ""))
			client_group.sendMessage("Saved!")

		if msg == "exit":
			time.sleep(3)
			receiver.sendMessage("GoodBye %s" % sender.name)
			exit()