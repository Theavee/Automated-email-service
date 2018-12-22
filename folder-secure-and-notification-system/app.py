import os
import sys
import time
import threading 
import smtplib

class ProtectFolder(object):

    def __init__(self):
        self.folder_location = os.getcwd()
        self.keep_record = []
    
    def total_size_of_folder_initial(self):
        total_size = 0
        for file_or_folder in os.listdir(self.folder_location):
            total_size += os.path.getsize(file_or_folder)

        print('total {} bytes'.format(total_size))
        self.keep_record.append(total_size)
        return total_size

    def total_size_of_folder_final(self):
        time.sleep(60)
        total_file_size_final = 0
        for file_or_folder in os.listdir(self.folder_location):
            total_file_size_final += os.path.getsize(file_or_folder)
        print('total size {}'.format(total_file_size_final))   
        self.keep_record.append(total_file_size_final) 
        return total_file_size_final    


    def check_difference_and_inform_user(self):
        initail = self.total_size_of_folder_initial()
        final = self.total_size_of_folder_final()
        if self.keep_record[0] != self.keep_record[len(self.keep_record)-1]:
            return True
        else:
            return False

    def email_notification_service(self):
        #Avee Chakraborty,151-35-924,department of software engineering,DIU.
        #for establishing a connection , parameters are domain name and port
        object_of_smtp = smtplib.SMTP('smtp.gmail.com',587)
        #send a simple hello message
        object_of_smtp.ehlo()
        #starting TLS encription
        object_of_smtp.starttls()
        #login requires personal email and password
        object_of_smtp.login('swe@gmail.com','password')
        #message goes from -> to -> message 
        object_of_smtp.sendmail('swe@gmail.com','x-avee@gmail.com','subject: Folder/file Changed \nHello, Someone changed your secret file or folder.Please go to your directory.')
        {}
        #disconnecting from smtb server
        object_of_smtp.quit()


            
    def final_result(self):
        result = self.check_difference_and_inform_user()
        if result == True:
            print('file or folder changed!')
            self.email_notification_service()
            threading.Timer(300, self.final_result).start()
        else:
            print('not changed!')

    
    def display_keep_record(self):
        print(self.keep_record)
                


if __name__ == "__main__":
    protection = ProtectFolder()
    protection.final_result()