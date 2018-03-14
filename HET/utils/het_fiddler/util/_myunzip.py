import os
import shutil
import zipfile

from functools import partial

here = os.path.abspath(os.path.dirname("__file__"))
get_path = partial(os.path.join, here)

SRCDIR = get_path("datas","saz")
DSTDIR = get_path("datas","dst")

def _unzip(file, dstpath=None):
    filename, filetype = os.path.basename(file).split(".")
    z = zipfile.ZipFile(file, 'r')
    z.extractall(path=os.path.join(dstpath,filename))

def unzip(srcdir, dstdir):
    """将源目录文件解压到目的目录，解压文件保留
    :param srcdir:原始文件路径
    :param dstdir:解压后文件存放路径
    """
    temp = get_path("datas","temp")
    _newunzip = partial(_unzip,dstpath=dstdir)
    if os.path.exists(temp):
        shutil.rmtree(temp)
    shutil.copytree(srcdir, temp)
    files = [os.path.join(temp,eachfile) for eachfile in os.listdir(temp)]
    list(map(_newunzip,files))
    shutil.rmtree(temp)

if __name__=="__main__":
    unzip(SRCDIR,DSTDIR)