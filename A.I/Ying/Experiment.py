import os
def createfile():
    os.chdir('/Users/fin/Desktop/testfolder/')
    with open('testfile.txt', 'r+') as f:
        old = str(f.read())
        f.seek(0)
        f.write('new line\n' + old)
createfile()