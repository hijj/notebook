## checklist
1. [review liuhui项目代码](#check1)
2. P2P实现原理
3. openssl适配dpdk代码学习，dpdk下openssl目录
4. man gcc学习
5. ECDH keygen验证方法，椭圆曲线的理解
6. 什么是SUITE B
7. 利用思维导图，让设计和checklist更加清晰
8. openssl UI组件是干什么的
9. 问题单助手使用
10. shell使用广度优先算法实现lib依赖
11. 能否基于liuye的python脚本修改，添加支持app查找函数
12. TLS1.3 HKDF是什么
13. asn1格式分析
14. 伪造证书分析，https://github.com/wllm-rbnt/asn1template 工具，改了证书，没改签名，可以用
15. core_translator脚本学习
16. GMT 0009-2012 SM2密码算法使用规范
17. openssl协程完整流程梳理
18. [~~rsa blinding实现原理，解决问题~~](#check18)
19. [~~netconf基本操作~~](#check19)

## detail
##### check1 
review liuhui项目代码     
代码路径：http://10.153.120.80/cmwcode-open/V7R1_SPRINGB75/branches_bugfix/COMWAREV700R001B75D076/TB202209011086/VPN    
lizhiming代码路径：http://10.153.120.80/cmwcode-open/V7R1_SPRINGB75/trunk/VPN  
重点关注点：    
+ _xml_IsakmpProfilesTbl_ProfileConfig lizhiming replace代码   
+ 规则：定制本次功能产品不允许下slot不带subslot
+ 因为两个命令行必须同时存在的， master和slave不能同时相同 
+ 守护进程中是转序的，插件没转序，是否存在问题

##### check18 
rsa blinding实现原理，解决问题     
参考维基，大意就是我需要对X，进行计算f(X), 但是又不想让对方知道X，先计算E(X)给对方，对方计算f(E(X))返回给我，然后D(f(E(x))) = f(x), 双射 

##### check19
netconf基本操作   
![netconf1](png/netconf1.png)
![netconf2](png/netconf2.png)
