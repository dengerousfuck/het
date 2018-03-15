import os
import shutil
import zipfile

from functools import partial


def _unzip(file, dstpath=None):
    filename, filetype = os.path.basename(file).split(".")
    z = zipfile.ZipFile(file, 'r')
    z.extractall(path=os.path.join(dstpath,filename))

def unzip(srcdir, dstdir,case_name):
    """将源目录文件解压到目的目录，解压文件保留
    :param srcdir:原始文件路径
    :param dstdir:解压后文件存放路径
    """
    temp = os.path.join(os.getcwd(),'utils/het_fiddler/datas/temp')
    _newunzip = partial(_unzip,dstpath=dstdir)
    if os.path.exists(temp):
        shutil.rmtree(temp)
    shutil.copytree(srcdir, temp)
    # files = [os.path.join(temp,eachfile) for eachfile in os.listdir(temp)]
    files = [os.path.join(temp,case_name)]
    list(map(_newunzip,files))
    shutil.rmtree(temp)
