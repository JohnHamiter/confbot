"""
This function should ingest a response and either modify, delete, or create a request

"""
from datetime import datetime

#!/usr/bin/env python

def conf_request(x):
	if response == "Y" or "y":
		reserve_date = datetime.strptime(raw_input("What day do you need the room? Use format m/d/yy: "), "%m/%d/%Y")
	elif response == "N" or "n" :
		modify = raw_input("Would you like to modify a previous reservation? (Y/N): ")



response = raw_input("Hello! Do you need to reserve a conference room? (Y/N): ") 

conf_request(response)







	