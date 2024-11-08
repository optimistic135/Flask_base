# Flask_base
### 简单说明
1. 项目结构
```
D:.
├─models
│  └─bule_print.py  #蓝图文件，使用蓝图方便flask项目的扩展
│  └─restful_class.py   #restful风格开发
├─venv  #虚拟环境
│
└─app.py
└─requirements.txt  #python依赖项
└─README.md     #注释文档，添加功能修改项目时标记
└─test.http     #测试的请求（使用postman也可测试）
```

### 运行项目

1. 在win中，创建虚拟环境（有则不用创建）
```cmd
python -m venv venv
```

2. 进入虚拟环境
```cmd
.\venv\Scripts\activate
```

2. 安装flask等依赖
```cmd
pip install -r requirements.txt
```
如果安装了新的包，使用：```pip freeze > requirements.txt```更新信息

3. 启动！
```cmd
python app.py
```

___

### Use `Git` 
1. if you are developing login model, you can run the command blow:
```
git checkout dev
git checkout -b feature/login_module
git branch -v
git push origin feature/login_module:feature/login_module
git add <new files>
git commit -m "login module finished"
git push origin feature/login_module
```

2. Then you can submit PR in github!

you can learn more details from: https://blog.csdn.net/sculpta/article/details/104448310

___

## Interface Infomation

1. examlpe :
##### Request
- Method: **POST**
- URL: **/result_class** 
- Headers：
- Body:
```
{
    "name" : "your/name"
}
```
##### Response
- Body
```
{
  "code": 200,
  "msg": "Hello your/name, This is restful POST"
}
```

2. ...(you can add more api information when you compete)