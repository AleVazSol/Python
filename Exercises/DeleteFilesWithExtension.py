import os,getpass
def DeletFiles(extension,files=[]):
    user=getpass.getuser()
    directory="C:\\Users\\"+user+"\\Downloads\\"
    selectedFiles=[file for file in files if extension in file]
    print("These Files are going to be deleted: ")
    print(selectedFiles)

    if input("Enter Y to continue or any other leter to cancel: ").upper()=="Y":
        for item in selectedFiles:
            os.remove(directory+item)
        print("Files were deleted")
    else:
        print("Process was canceled")

    pass


def getDownloadedfiles():
    user=getpass.getuser()
    directory="C:\\Users\\"+user+"\\Downloads\\"
    filesInDownloads=os.listdir(directory)
    return filesInDownloads


def run():
    dowloadsFolderFiles=getDownloadedfiles()
    extensionToDelete=input("Enter the extension of the files that you want to delete: ")
    DeletFiles(extensionToDelete,dowloadsFolderFiles)

if __name__=="__main__":
    run()