from core.oauth import *
import yadisk

y = yadisk.YaDisk(token=mytoken)
print(y.check_token())
print(y.get_disk_info())
print(list(y.listdir("/")))
y.upload("../README.md", "/README.md")
