import Dbcon

dbcon = Dbcon.Dbcon()
ips = dbcon.select("select * from iplist where isinuse=1")
print(ips)