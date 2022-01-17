from bz2 import _WriteTextMode
import imp
import re
from threading import local


import dropbox
import os

class TransferData :
    def __init__(self,accessToken) :
        self.accessToken = accessToken

    def upload_files(self,file_from , file_to) :
        dbx = dropbox.Dropbox(self.accessToken)

        for root,dirs,files in os.walk(file_from) :
            for filename in files :
                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

        with open(local_path,"rb") as f:
            dbx.files_upload(f.read(),dropbox_path, mode = WriteMode("overwrite"))
        print("Upload Successful !!")

def main():
    access_token = "OnYZ1R0HB5UAAAAAAAAAAQ8S1Q3dTRmkdnxvCajMO_qOWA_CzC41K5_-gKmy80xX"
    transferData = TransferData(access_token)

    file_from = input("Please enter the path of the file you want to upload: ")
    file_to = "/"+input("Enter the full path to upload to along with the file name: ")

    transferData.uploadFiles(file_from,file_to)

if __name__ == "__main__" :
    main()