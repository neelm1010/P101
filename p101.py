import dropbox
import os 
from dropbox.files import WriteMode

class TransferData:
    def __init__ (self,access_token):
        self.access_token=access_token

    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for root,dirs, files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)

            
            relative_path=os.path.relpath(local_path, file_from)
            dropbox_path=os.path.relpath(file_to, relative_path)

        with open(local_path,'rb'):
            dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
       
      

        
def main():
    access_token='sl.A-Ch_3mrQ8WAusCxrL0AWw-YTHK-aw6-bBj9Q4_6PgKua_MT7SwnByoa517c2h5nr60m1IyOkjzUyfNeWMMgmIq4lv--ikjthQzGrJ0YjKprJEoc4ZAhatTGI78SG-IKJhn5XgM'
    transferData=TransferData(access_token)

    file_from=input("File Path to Transfer: ")
    file_to=input("Enter Full Path to Upload to Dropbox: ")

    transferData.upload_file(file_from,file_to)
    print("File has been moved")

main()