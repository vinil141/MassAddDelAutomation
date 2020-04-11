
"""

test code. Never tried this
"""
# FTP File from AMDENV1 to another machine using Python v2.6
"""
Input - Source file name, destination, hostname , id, pwd from a file
Processing :
Read input file from a location.
Read destination location from a file.
Read connection details from connection file.
Use FTP Library along with these information and send input file.
Output - FTP CTN list to remote server for CSM Job to process.
FTP File tasks:
hostname : blp13626005
Server -->exprdbt1
Username- pc089472
password-: Password@207 
sudo -iu xfrmadd 
Password@207
/prd1/exbvar/o2o/ftp/xfrmadd
"""
import ftplib
import sys
import os
from os.path import isfile, join
server = exprdbt1
username = pc089472
password = Password@207
# loop into INPUT Folder for all the CTN files.
# Send all of them to Destination location
# INPUT = os.path.join("INPUT_CTN")
#
# with open("output_path.txt") as file:
#     output = file.read()
#
# for file in os.listdir(INPUT):
#     filename = os.fsdecode(file)
#     if filename.endswith(".txt"):
#         input_file = filename
INPUT = os.path.join("INPUT_CTN")
with open("output_path.txt") as file:
    output = file.read()
    print("Content of Output file: ", output)
    # directory on production where to push the file(s)

for file in os.listdir(INPUT):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        print(filename)

# Read a config file for reading details fo server


onlyfiles = [f for f in os.listdir(INPUT) if isfile(join(INPUT, f))]
print(onlyfiles)


def ssh_ftp_file(onlyfiles,output):
    print("From Function", onlyfiles)
    print("From Function", output)
    myFTP = ftplib.FTP(server, username, password)
    fh = open(filename, 'rb')
    myFTP.storbinary('STOR %s' % f, fh)
    fh.close()
"""
print("Current File Location: {0}.".format(sys.argv[0]))
def upload_file_ftp(filename, OUTPUT_PATH, server, username, password):
    print(filename)
    myFTP = ftplib.FTP(server, username, password)
    fh = open(filename, 'rb')
    myFTP.storbinary('STOR %s' % f, fh)
    fh.close()
"""
ssh_ftp_file(onlyfiles,output,server,username,password)