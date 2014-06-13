#coding=utf-8
import os;
import urllib;
def update():
	print("downloading newest hosts...........");
	html=urllib.urlopen("https://raw.githubusercontent.com/autonews/python_googler/master/hosts").read().decode("utf-8");
	hosts=open("hosts","w");
	hosts.write(html);
	hosts.close();
	print("download complete...........");

	
def hasBackup():
	return os.path.isfile("hosts_bak");
def backup():
	origin=open("/etc/hosts","r");
	bak=open("hosts_bak","w");
	for line in origin:
		bak.write(line);
	origin.close();
	bak.close();

def write():
	origin=open("/etc/hosts","w");
	bak=open("hosts_bak","r");
	hosts=open("hosts","r");

	for line in bak:
		origin.write(line);
		print "add:"+line;

	origin.write("\n");

	for line in hosts:
		origin.write(line);
		print "add:"+line;
	

	origin.close();
	hosts.close();
	bak.close();
update();
if not hasBackup():
	print "begin backup.................";
	backup();
else:
	print "no need to backup............";

print "begin write.......................";
write();
