##!/usr/bin/python
"""
input_data_checker()
Input : Requester's Attachement
if a file appears at source code location:
   if it is a zip file
       unzip it
       executeFileProcessing()
    else
        executeFileProcessing()

executeFileProcessing()
        read & seperate meta data & CTN list
        Send CTN list files to INPUT_CTN folder.
        process the metadata received.
        ValidateMetadata(data)

ValidateMetadata(data)
//Code to do validation of inputs .Return True if passed, else False.
If TRUE,
    ftp_ctn_file()
    SQLDataEntry(details to process)
else
    emailNotification(Fail)

ConnectDB()
 // Code to connect with DB//

ftp_ctn_file()
//Code to read list of CTN files
& FTP them to remote server//

 SQLDataEntry()
 if ValidateMetadata:
      ConnectDB()
      Generate Next Seq Val
      Generate SQL at current location
      Insert into database
      return True

If SQLDataEntry :
    emailNotification(True)


emailNotification(string)
    read string.
    If string is True:
        Send passed email
        move all input files to PASS folder
    else
        send Failure email to config team.
        move input files to FAILURE Folder

no request received. Don't do anything.

Reports after scheduled date: Input - Seq number , req email ID, date of processing.
"""