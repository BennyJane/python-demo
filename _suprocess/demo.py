import subprocess
# res = subprocess.call(['ls', '-la'])
# print(res)
#
# res2 = subprocess.call('pwd', shell=True)
# print(res2)


res = subprocess.run(['ls', '-la'])
print(res)