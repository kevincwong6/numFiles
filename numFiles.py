import os
from sys import exit

def NumFiles():
    print("Welcome to Python NumFile Utility\n")
    print("This utility will enumerate all files inside a directory\n\n")

    print("Please enter the path name : ", end="")
    path=input()
    if (os.path.isdir(path)==False):
      print("\n\nInvalid path name!!!\n\n")
      return

    print("Please enter the starting squence : ", end="")
    startSeqNum=int(input())

    arr=os.listdir(path)
    count=100;
    for a in arr:
      # if "pdf" in a:    # if we want to enumerate certain file extension
      oldname=path+"\\"+a
      if (os.path.isdir(oldname)==True):
        continue
      print(oldname)
      newname=path+"\\"+str(startSeqNum)+" - "+a
      os.rename(oldname, newname)
      print(newname)
      startSeqNum+=1

NumFiles()

###########################################################################
#
# Directory listing before runing NumFiles.py
#
###########################################################################
#Directory of L:\test-numfiles
#
#04/12/2019  01:13 AM    <DIR>          .
#04/12/2019  01:13 AM    <DIR>          ..
#04/12/2019  01:06 AM                31 abc.txt
#04/12/2019  01:04 AM    <DIR>          archived
#04/12/2019  01:06 AM                16 def.txt
#04/12/2019  01:06 AM                16 something.txt
#               3 File(s)             63 bytes
#               3 Dir(s)  17,858,084,864 bytes free
#
###########################################################################
#
#Welcome to Python NumFile Utility
#
#This utility will enumerate all files inside a directory
#
#Please enter the path name : L:\test-numfiles
#Please enter the starting squence : 100
#L:\test-numfiles\abc.txt
#L:\test-numfiles\100 - abc.txt
#L:\test-numfiles\def.txt
#L:\test-numfiles\101 - def.txt
#L:\test-numfiles\something.txt
#L:\test-numfiles\102 - something.txt
#
###########################################################################
#
# Directory listing after runing NumFiles.py
#
###########################################################################
#
# Directory of L:\test-numfiles

#04/12/2019  01:17 AM    <DIR>          .
#04/12/2019  01:17 AM    <DIR>          ..
#04/12/2019  01:06 AM                31 100 - abc.txt
#04/12/2019  01:06 AM                16 101 - def.txt
#04/12/2019  01:06 AM                16 102 - something.txt
#04/12/2019  01:04 AM    <DIR>          archived
#               3 File(s)             63 bytes
#               3 Dir(s)  17,858,084,864 bytes free


