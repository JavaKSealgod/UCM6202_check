import requests
import json
import time
import threading



# r = requests.post(url = url , data = "action=getInfo" , verify = False)

# s = json.loads(r.content)

# print s['response']['prog_version']

f = oepn('url.txt','r')

fp = open('url_version.txt','a')

all = []

for i in f.readlines():
	x = i.strip('\n')
	ip = x.split(':')[0]
	all.append(ip)

def check():
	lock = threading.Lock()
	while (len(all)>0):
		lock.acquire()
		url = 'http://'+all[0]+':8089/cgi'
		del all[0]
		lock.release()
		try:
			r = requests.post(url = url , data='action=getInfo' ,verify = False)
			s = json.loads(r.content)
			if '6202' in s['response']['model_name']:
				lock.acquire()
				print '[*] Success ---- '+str(url)
				lock.release()
				fp.write('%s\n'%str(url))
			else:
				pass
		except Exception as e:
			pass
count = 50
th = []

for i in range(count):
	t = threading.Thread(target = check)
	th.append(t)
for i in range(count):
	th[i].start()
for i in range(count):
	th[i].join()

