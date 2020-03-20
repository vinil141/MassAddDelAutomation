# Date : 20-Dec-2020
# Code version 0.1
import datetime
import datetime as dt
import os
import os.path
import win32com.client
import tarfile

"""
Objective:
Read email recursively 
download attachments to a folder
zip those folders
FTP the zipped folder
"""

now = dt.datetime.now()
suffix = now.strftime("%d-%m-%y")

d = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d-%m-%y")  # Yesterday's date


def download_attachment():
    with open("log.txt", "w") as log_file:

        # global count_attachment
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.GetDefaultFolder(6).Folders("ROTA")
        messages = inbox.Items

        for message in messages:

            subject, sender, attachment, count_attachment = message.Subject, message.Sender, \
                                                            message.Attachments, \
                                                            message.Attachments.Count

            print(
                f"Email Sender Name:- {sender} \nEmail Subject :- {subject} \nNo of attachments : {count_attachment}\n")
            log_file.write(
                f"Email Sender Name:- {sender} \nEmail Subject :- {subject} \nNo of attachments : {count_attachment}\n")

            new_name = "Mass Request_" + str(sender) + '_' + str(suffix)  # name of each new folder
            if new_name in os.listdir():  # Checking if the folder exist in current working dir. If not, creating it
                pass
            else:
                os.mkdir(new_name)

            path = os.path.join(os.getcwd(), new_name)

            if count_attachment > 0:
                for i in range(1, count_attachment + 1):
                    attach = attachment.Item(i)
                    attach.SaveAsFile(path + '\\' + str(attach))
                    count_attachment += i
                # print("File(s) downloaded successfully : {0} \n ".format(i))
                # log_file.write("File(s) downloaded successfully : {0} \n ".format(i))
                # create tar files now
                #     for j in range(count_attachment+1):
                #         out = tarfile.open("new_name.tar", mode='w')
                #         try:
                #             print ('adding file')
                #             out.add(j)
                #         finally:
                #             print ('closing')
                #             out.close()
            else:
                print("No attachment found !")
                log_file.write("No attachment found !")
            # exit(2)

        messages.GetNext()


def compress_ftp_file():
     #Objective: Compress folder created today in current directory\n'
     #FTP those folders\n'
     #:return:\n'
    

if __name__ == "__main__":
    download_attachment()
    #compress_ftp_file()
