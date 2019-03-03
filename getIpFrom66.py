from urllib import request
from bs4 import BeautifulSoup
from distutils.filelist import findall
import time, datetime
import Dbcon

#从66ip获取页面地址
def getUrlFrom66Ip(page):
	if page == 1:
		return "http://www.66ip.cn/index.html"
	else:
		return "http://www.66ip.cn/%d.html"%page

def getIpsFrom66Url(url):
	page = request.urlopen(url)
	soup = BeautifulSoup(page, "html.parser")
	iplistTable = soup.find(attrs={"class":"containerbox"})
	trList = iplistTable.find_all("tr")
	ipPortList = []
	for tr in trList[1:]:
		tdList = tr.find_all("td")
		ip = tdList[0].get_text()
		port = tdList[1].get_text()
		isinuse = 1
		source = "66ip"
		addtime = int(time.time())
		ipPortList.append((ip, port, isinuse, source, addtime))

	# print(ipPortList, "\n")
	return ipPortList

def saveIpsToDb(ips):
	dbcon = Dbcon.Dbcon()
	# for list in ips :
	print(ips)
	sql = "insert into iplist (ip,port,isinuse,source,addtime) values(%s,%s,%s,%s,%s) on duplicate key update isinuse=values(isinuse),source=values(source),addtime=values(addtime)"
	res = dbcon.insert(sql, ips)
	print(res)



#循环获取ip列表
def getIps():
	page=1
	while(page<10):
		#获取当页的url
		url=getUrlFrom66Ip(page)
		#获取当页面上的ip列表
		ips=getIpsFrom66Url(url)
		if (len(ips) == 0):
			break
		# print(ips)
		#保存列表到数据库
		saveIpsToDb(ips)
		#页数增加
		page = page + 1


getIps()