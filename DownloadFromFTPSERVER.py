import ftplib

FTP_HOST = "-------------"
FTP_USER = "--------"
FTP_PASS = "---------"

# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"



# here I can generate a list of all directories in Server
#ftp.dir()
#print (ftplib.FTP.dir(ftp))

# the name of file you want to download from the FTP server
#filename = "QR-FTP"


for i in range (10, 14):
    filename = "202005"+str(i)+".log"
    with open(filename, "wb") as f:
        ftp.cwd('/QR-FTP/log/QR717/')
        localfile = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
        localfile.close()
        localfile= open(filename, "r")
        print('File Content:', localfile.read())
  
ftp.quit()


"""
for i in range (10, 14):
    ftp.cwd('/QR-FTP/log/QR717/')
    filename = "20200516.log"
    with open(filename, "wb") as f:
        localfile = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
        ftp.quit()
        localfile.close()
        localfile= open(filename, "r")
    print('File Content:', localfile.read())
"""