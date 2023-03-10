# qc-py-glues
用py做胶水，将node的cpu密集型的计算给到java, 方便弥补node短板

## connect
py作为中间层     
和java通信是使用py的subprogress   
和js通信是用socket

## run
pre : 需要有node、java和py环境   
不需要装三方包
```
#先启动胶水层
python middle.py

#再调用js就可以了
node index.js

```

