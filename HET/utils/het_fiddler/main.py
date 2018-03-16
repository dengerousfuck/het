import os


from utils.het_fiddler.util._myunzip import unzip
from utils.het_fiddler.util._read import read
from utils.het_fiddler.util._find import find
from utils import restful
from utils.het_fiddler.addcase import addcase_main


REPTYPE = "*_c.txt"
RSPTYPE = "*_s.txt"

def main(case_name):
    DSTDIR = os.path.join(os.getcwd(), 'utils/het_fiddler/datas/dst/%s'%case_name)
    RESULTDIR = os.path.join(os.getcwd(), 'utils/het_fiddler/datas/result/%s.txt'%case_name)
    SRCDIR = os.path.join(os.getcwd(), 'utils/het_fiddler/datas/saz')
    unzip(SRCDIR, DSTDIR,case_name)
    req = find(DSTDIR, REPTYPE)
    rsp = find(DSTDIR, RSPTYPE)
    read(req, rsp, RESULTDIR)
    addcase_main(case_name)
    return restful.success()

