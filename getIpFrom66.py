#从66ip获取页面地址
def getUrlFrom66Ip(page):
	if page == 1:
		return "http://www.66ip.cn/index.html"
	else:
		return "http://www.66ip.cn/%d.html"%page


#循环获取ip列表
def getIps():
	page=1
	while(True):
		#获取当页的url
		url=getUrlFrom66Ip(page)
		#获取当页面上的ip列表
		ips=getIpsFromUrl(url)
		if (!len(ips)) {
			break;
		}
		#保存列表到数据库
		saveIpsToDb(ips)
		#页数增加
		page++