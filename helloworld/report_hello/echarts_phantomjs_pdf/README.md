# 利用pyecharts生成报表
## 目录结构
```
├── main.py
├── phantomjs
├── README.md
└── templates
    ├── bootstrap.min.css
    ├── make_pdf.js
    └── report.html
```

## 代码说明
### pyecharts
#### echarts_js_dependencies
```
功能：
嵌入渲染图表时所需的js代码，已去重。

模板函数：
{{ echarts_js_dependencies(bar) }}

什么参数，好像不影响输出的内容，hash相同。


输出：
</script>
!function(t,e){...}(this, function(t){...})
</script>
```

#### echarts_container
```
{{ echarts_container(bar) }}

渲染图表容器，为一个<div></div> 元素。

<div id="5abadf5a19a747918e7b78cce58bd52d" style="width:800px;height:400px;"></div>
```
#### echarts_js_content
```
图表初始化的js代码，根据元素id进行渲染。

输出：
<script type="text/javascript">

var myChart_xxx = echarts.init(document.getElementById(xxx), ...);
var option_xxx = {...}
myChart_xxx.setOption(option_xxx);

</script>
```

### PopenWithTimeout 阻塞执行，带超时
```
def PopenWithTimeout(cmd, cwd="./", timeout=3600):
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


cmd = "phantomjs make_pdf.js %s"%name
PopenWithTimeout(cmd, cwd="output", timeout=80)
```
### make_pdf.js, phantomjs
```
var page = require('webpage').create();
var name = require("system").args[1];
var html_file = name+".html";
var pdf_file  = name+".pdf";

page.open(html_file, setInterval(function() {
    page.render(pdf_file);
    phantom.exit(0);
},30000));
```