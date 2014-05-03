
import sys
import tarfile
import os
import zipfile
import gzip

# target = raw_input("Enter target directory: ")
# files = raw_input("Enter List of files: ")
# fileList = list(files.split())
#
# print fileList


print sys.argv
def extractor(targ, l):
    print "list:: ", l
    print "TargetDIR:",targ
    for file in l:
        if file[file.find('.')+1:] == 'zip':
            print 'zip'
            with zipfile.ZipFile(file, "r") as z:
                z.extractall(targ)
            # z = zipfile.open(file, 'r')
        elif file[file.find('.')+1:] == 'tgz':
            fileExtentionless =  file[ :-4]
            y = os.path.join(targ, fileExtentionless)
            print "y::", y
            print file
            with tarfile.open(file, "r:gz") as tar:
                tar.extractall(y)
        elif file[file.find('.')+1:] == 'tar.gz':
            fileExtentionless =  file[ :-7]
            y = os.path.join(targ, fileExtentionless)
            with tarfile.open(file, "r:gz") as tar:
                tar.extractall(y)

        elif file[file.find('.')+1:] == 'tbz':
            fileExtentionless =  file[ :-4]
            y = os.path.join(targ, fileExtentionless)
            with tarfile.open(file, "r:bz2") as tar:
                tar.extractall(y)
        elif file[file.find('.')+1:] == 'tar.bz2':
            fileExtentionless =  file[ :-8]
            y = os.path.join(targ, fileExtentionless)
            with tarfile.open(file, "r:bz2") as tar:
                tar.extractall(y)
        elif file[file.find('.')+1:] == 'bz2':
            with tarfile.open(file, "r:bz2") as tar:
                tar.extractall(targ)

        elif file[file.find('.')+1:] == 'gz':
            gz = tarfile.open(file, mode='r:gz')
            gz.extractall(targ)


if __name__ == '__main__':

    extractor(sys.argv[1], sys.argv[2:])

