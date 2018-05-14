import sys, os
from ftplib import FTP

ftp = FTP('')
ftp.connect('127.0.0.1', 21)
ftp.login('admin', 'admin')
ftp.cwd('/Server')
ftp.retrlines('LIST')

def uploadfile():
	filename = os.path.basename(sys.argv[1])
	ftp.storlines('STOR '+ filename, open(filename, 'rb'))
	ftp.quit()

def downloadfile():
	filename = os.path.basename(sys.argv[1])
	localfile = open(filename, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	ftp.quit()
	localfile.close()

uploadfile()
#downloadfile()
