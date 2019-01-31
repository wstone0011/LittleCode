# 有趣的代码
## 1.一句话打印心形图案
```
python -c "print'\n'.join([''.join([('acfun!'[(x-y)%6]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)])"
```

