import os
from enum import Enum
import tkinter
from tkinter import filedialog

class VideoFileEnds(Enum):
    AVI = '.avi'
    MKV = '.mvk'
    MP4 = '.mp4'

class SubtitleFileEnds(Enum):
    AVI = '.smi'
    MKV = '.srt'

def isVideoFile(filename):
    if any(filename.lower().endswith(vdoEnd.value)for vdoEnd in VideoFileEnds):
        return True
    else:
        return False

def isSubTitleFile(filename):
    if any(filename.lower().endswith(subtitle.value)for subtitle in SubtitleFileEnds):
        return True
    else:
        return False



root = tkinter.Tk()
root.withdraw()
path_dir = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

path_dir = None

if not path_dir:
    print('Failed getting path')
    exit()


fileList = os.listdir( path_dir )

videoFileList = [ file.capitalize() for file in fileList if isVideoFile(file) ]
subFileList = [ file.capitalize() for file in fileList if isSubTitleFile(file) ]

if not videoFileList or not subFileList:
    print('empty file list')


videoFileList.sort()
subFileList.sort()


print ("videoFileList: {}".format(videoFileList))
print ("subFileList: {}".format(subFileList))

iCount = 0
for file in subFileList:
    srcExt = os.path.splitext(file)[1]
    src = os.path.join( path_dir, file )
    dstfileName = os.path.splitext(videoFileList[iCount])[0]
    dst = os.path.join( path_dir, dstfileName + srcExt )
    os.rename(src, dst )
    iCount += 1

print ("videoFileList: {}".format(videoFileList))
#print(os.getcwd())