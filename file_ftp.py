#!/usr/bin/python3
"""
Created by : Vinil Mehta
Project : SRE Automation
Account : EE UK
Version :0.1
"""

import ftplib
import sys
import os
from os.path import isfile, join

INPUT = os.path.join("INPUT_CTN")
with open("output_path.txt") as file:
    output = file.read()

# onlyfiles = [f for f in os.listdir(INPUT) if isfile(join(INPUT, f))]
# READ server.txt TO RETRIEVE SERVER LOGIN DETAILS
with open("server.txt") as file:
    server_details = file.read().split(",")
    # server, username, password = server_details
    # print("Server: {0}, UserName:{1},Password:{2}".format(server, username, password))


def upload_file_ftp(*inp):
    print("Destination path ", output)
    server, username, password = server_details
    # read path of CTN files.
    for root, dirs, files in os.walk(INPUT):
        for fname in files:
            full_fname = os.path.join(root, fname)
            print(full_fname)
    with ftplib.FTP(server) as ftp:
        try:
            res = ftp.login(username, password)
            # res = ftplib.FTP(server, username, password)
            # print(full_fname)
            with open(full_fname) as fp:
                res.storlines('STOR ', fp)
                if not res.storbinary('226 Complete Transfer'):
                    print("Upload Failed:")
                else:
                    print('File Transfer Successful ! ')
        except ftplib.all_errors as e:
            print("ALERT !! There occurred error in File Transfer Process. Please check and re-try.\nError: ", e)


# Calling Function
upload_file_ftp(output, server_details)
