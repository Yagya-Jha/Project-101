#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Uploading Files to Dropbox

import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A4MgynxVh-7_fX2MsCfTGlZgO9rpLC0U0nfnW7vOPGQ407swNR191uP8b9Ru5oAUUk5q0WIpOxk6AGCevMZHiuNxu520XLCuDSCgprvfO4xYn8gTcRp4sH52ud4Z3M0OKHDdOC4'
    transferData = TransferData(access_token)

    file_from = input('Enter Path of File to be uploaded:- ')
    file_to = '/Project_101/'  # The full path to upload the file to, including the file name
    fileto = input('Enter The File name to be saved with:- ')
    file_to = file_to + fileto
    # API v2
    transferData.upload_file(file_from, file_to)
    print('File Uploaded !!')

main()