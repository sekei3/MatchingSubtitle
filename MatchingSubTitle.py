import os
from enum import Enum
import tkinter
from tkinter import filedialog

class VideoFileEnds(Enum):
    AVI = '.avi'
    MKV = '.mvk'
    MP4 = '.mp4'

class SubtitleFileEnds(Enum):
    SMI = '.smi'
    SRT = '.srt'

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


if not path_dir:
    print('failed getting path')
    exit()

fileList = os.listdir( path_dir )

videoFileList = [ file for file in fileList if isVideoFile(file) ]
subFileList = [ file for file in fileList if isSubTitleFile(file) ]

if not videoFileList or not subFileList:
    print('empty file list')
    exit()

if len(videoFileList) != len(subFileList):
    print('check not match count videofile and subtitle')
    exit()

videoFileList.sort()
subFileList.sort()

#print ("videoFileList: {}".format(videoFileList))
#print ("subFileList: {}".format(subFileList))

for i in range(len(subFileList)):
    file = subFileList[i]
    srcExt = os.path.splitext(file)[1]
    src = os.path.join( path_dir, file )
    dstfileName = os.path.splitext(videoFileList[i])[0]
    dst = os.path.join( path_dir, dstfileName + srcExt )
    os.rename(src, dst )

#print ("videoFileList: {}".format(videoFileList))