from line import LineClient, LineGroup, LineContact
import time

USERNAME = 'saranpong.kom@gmail.com'
PASSWORD = ''
GROUPNAME = 'Bnz'
MYID = 'forgetz'
 
#optional
COMPUTERNEME = 'Bnz-PC'
TOKEN = ''

try:
	client = LineClient(id=USERNAME, password=PASSWORD)
	TOKEN = client.authToken
	print "TOKEN : %s\r\n" % TOKEN
	text_file = open("token.txt", "w")
	text_file.write("%s" % TOKEN)
	text_file.close()

except Exception as ex:
	print "Login Failed"
	print ex
	exit()

client_group = client.getGroupByName(GROUPNAME)
client_group.sendMessage("Hello!!")

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
		#fromwhom.sendMessage("Hi")

		if msg == "exit":
			time.sleep(3)
			receiver.sendMessage("%s\r\n" % ("goodbye!"))
			exit()

		if msg.startswith("sel"):
			time.sleep(3)
			receiver.sendMessage("%s\r\n" % (msg))
			receiver.sendImage("screen.png")
			print msg