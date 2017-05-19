from line import LineClient, LineGroup, LineContact
from config import *
from function import *
import time

configlist = config_list()
GROUPNAME = configlist[2]
TOKEN = ''

try:
	client = LineClient(id=configlist[0], password=configlist[1], authToken=TOKEN)
	TOKEN = client.authToken
	print "TOKEN : %s\r\n" % TOKEN

except:
	print "Login Failed\r\n"
	exit()

client_group = client.getGroupByName(GROUPNAME)
client_group.sendMessage("Login Complete!!")

recent_group_msg = client_group.getRecentMessages(count=10)
print "RecentMessages : %s\r\n" % recent_group_msg

while True:
	op_list = []
	for op in client.longPoll():
		op_list.append(op)

	for op in op_list:
		sender   = op[0]
		receiver = op[1]
		message  = op[2]
		msg = message.text

		fromwhom = client.getContactByName(sender.name)
		print "fromwhom : %s\r\n" % fromwhom

		result = process(msg)

		if result != "":
			receiver.sendMessage("%s" % result)
		
		if msg == "exit":
			time.sleep(3)
			receiver.sendMessage("GoodBye %s" % sender.name)
			exit()