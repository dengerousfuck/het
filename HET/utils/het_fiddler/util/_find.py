
import os
import fnmatch

def find(top, filepat):
    """查找目录下文件并返回文件名称及上层目录名称

    :param top: 顶层目录名称
    :param filepat: 文件类型
    """
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            file = os.path.join(path, name)
            dirname = [each for each in os.listdir(top) if each in file]
            yield file,dirname





