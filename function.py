def process(msg):
	if msg == "!tester":
		return "tested by nat"
	if msg == "!ver":
		return "version 1.0"
	if msg.startswith("!speak"):
		return msg.replace("!speak", "")
	return ""