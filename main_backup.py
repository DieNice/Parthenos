import os
import time

source = ["/home/pda/Documents/Self-development"]
target_dir = "/home/pda/Documents/"
target_name = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr {0} {1}".format(target_name, ' '.join(source))
if os.system(zip_command) == 0:
    print("Copy is sucсsessfully created", target_name)
else:
    print("No copy created")
