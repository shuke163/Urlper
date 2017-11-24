## Urlper

### 项目介绍
* 基于RBAC原理实现示例Demo
* 开发环境: Django(1.11.4)+BootStrap
* 通过在admin后台修改权限绑定到对应的角色上进行URL访问权限控制

### 目录结构
```
├── README.md
├── URLPER
│   ├── settings.py     # 项目配置文件
│   ├── urls.py         # URL路由
├── app
│   └── views.py        # 试图处理
├── rbac
│   ├── admin.py        # admin后台
│   ├── middleware      # 中间件
│   ├── models.py       # model模块
│   ├── service         # 初始化权限信息
│   ├── templatetags    # 生成菜单的template
├── static              # 静态文件
└── templates           # 前端Html
```

### 使用说明
1. 确保本地已经安装python3.x + Django1.10.x以上版本环境  
2. 拉取代码并运行程序  
```
# git clone git@github.com:shuke163/Urlper.git
# cd URLPER;python manage.py runserver
```
3. 浏览器访问  
登陆: http://127.0.0.1:8000/login/  
4. 测试账号  
管理员: username: shuke password: 123    
添加权限: username: jack password: 123    
查看权限：username: tom  password: 123  
5. 管理后台  
管理: http://127.0.0.1:8000/admin/  
登陆账号: username: shuke password: admin!2345
6. 验证
* 管理员账号拥有所有URL访问权限
* 添加权限账号拥有可写权限
* 查看权限账号拥有只读权限
7. URL白名单  
开启URL白名单访问需要在项目的settings.py文件中的VALID_URL列表配置项中增加URL规则  

### 原理
* 数据模型: 5个类6张表
* 权限设计: 用户关联角色，角色关联URL权限，权限赋予code代号标示并关联菜单  
* 初始化: 用户登陆时获取用户的角色的URL权限写入session中  
* 中间件作用: 匹配用户所有请求的URL，并开放白名单访问  
* template模板渲染生成菜单选项及前端读写修改展示HTML元素  

### 引入使用
1. 在自己的项目中导入rbac包
2. 修改template/menu.html模板文件，用于渲染生成菜单  
3. 配置参数: 参照setting.py文件末尾权限相关配置项
4. 在setting.py文件MIDDLEWARE配置项中注册中间件(rbac.middleware.rbac.RbacMiddleware)，使rbac组件生效，注册时需注意组件注册顺序  

### 计划
* 结合自定义admin组件实现针对所有app的models数据模型进行统一的CURD操作
* RBAC权限组件的管理维护功能在项目前端界面进行操作,不在依赖自带的Django admin后台
* 初步完成一个简版CMDB功能
* 完善项目前度展示UI

