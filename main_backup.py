import os
import time

source = ["/home/pda/Documents/Self-development"]
target_dir = "/home/pda/Documents/"
today = target_dir + os.sep + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")

comment = input("Please, input commit:")
if len(comment) == 0:
    target_name = today + os.sep + now + '.zip'
else:
    target_name = today + os.sep + now + '_' \
                  + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print("directory created successfully", today)
target_name = today + os.sep + now + '.zip'
zip_command = "zip -qr {0} {1}".format(target_name, ' '.join(source))
if os.system(zip_command) == 0:
    print("Copy is sucсessfully created", target_name)
else:
    print("No copy created")
