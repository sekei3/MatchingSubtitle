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
    for vdoEnd in VideoFileEnds:
        if( filename.lower().endswith(vdoEnd.value) ):
            return True

    return False

def isSubTitleFile(filename):
    for subtitle in SubtitleFileEnds:
        if( filename.lower().endswith(sutitle.value)):
            return True
    
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

merge_list = tuple(zip(videoFileList, subFileList)) 

for vdo, sub in merge_list:
    srcExt = os.path.splitext(sub)[1]
    src = os.path.join( path_dir, sub )
    dstfileName = os.path.splitext(vdo)[0]
    dst = os.path.join( path_dir, dstfileName + srcExt )
    os.rename(src, dst )

#print ("videoFileList: {}".format(videoFileList))