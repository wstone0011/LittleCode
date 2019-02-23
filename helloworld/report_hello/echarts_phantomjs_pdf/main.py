#encoding:utf8
from __future__ import unicode_literals

from pyecharts import Bar
from pyecharts.conf import PyEchartsConfig
from pyecharts.engine import EchartsEnvironment
from pyecharts.utils import write_utf8_html_file
import os
import uuid
import hashlib
import shutil
import time
import subprocess

class Report(object):
    OUT_DIR = "output"
    TEMPLATE_DIR = "templates"
    REPORT_HTML = "report.html"
    
    def __init__(self):
        if not os.path.exists(Report.OUT_DIR):
            os.mkdir(Report.OUT_DIR)
        
        for filename in os.listdir(Report.TEMPLATE_DIR):
            if filename==Report.REPORT_HTML:
                continue
                
            inpath  = "%s/%s"%(Report.TEMPLATE_DIR, filename)
            outpath = "%s/%s"%(Report.OUT_DIR, filename)
            if not os.path.exists(outpath):
                shutil.copyfile(inpath, outpath)
                
    def PopenWithTimeout(self, cmd, cwd="./", timeout=3600):
        env = None
        if "posix"==os.name:
            cmd = cmd.split()  #windows下面，cmd参数是字符串，而linux下面，cmd参数是数组
            env = os.environ.copy()
            env["PATH"] = os.getcwd()+":"+env["PATH"]
            
        proc = subprocess.Popen(cmd, cwd=cwd, shell=False, env=env)
        #print(proc.pid)  #shell=True 的话，则proc.pid的pid为shell的pid

        bFlag = True
        while timeout>0:
            if proc.poll()!=None:
                bFlag = False
                break
            time.sleep(1)
            timeout = timeout-1

        if bFlag:
            proc.kill()
            
    def getUID(self):
        h = hashlib.sha1()
        h.update(str(uuid.uuid1()))
        return h.hexdigest()
        
    def genReport(self, filetype="html", timeout=60):
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [5, 20, 36, 10, 75, 90]
        v2 = [10, 25, 8, 60, 20, 80]
        bar = Bar("柱状图数据堆叠示例")
        bar.add("商家A", attr, v1, is_stack=True, is_toolbox_show=False)
        bar.add("商家B", attr, v2, is_stack=True)

        config = PyEchartsConfig(echarts_template_dir=Report.TEMPLATE_DIR)
        env = EchartsEnvironment(pyecharts_config=config)
        tpl = env.get_template(Report.REPORT_HTML)
        html = tpl.render(bar=bar)
        name = 'report_%s'%self.getUID()
        write_utf8_html_file("%s/%s.html"%(Report.OUT_DIR, name), html)
        
        if "pdf"==filetype:
            cmd = "phantomjs make_pdf.js %s"%name
            self.PopenWithTimeout(cmd, cwd=Report.OUT_DIR, timeout=timeout)
        
def main():
    m = Report()
    m.genReport(filetype="pdf", timeout=80)
    
if "__main__"==__name__:
    main()
