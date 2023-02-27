# PDS
Personal data storage  
个人数据存储项目，确认个人对自己数据的拥有权  

# 快速开始
 安装mongodb
 执行exe文件

# 主要框架
 主体以mongodb存储数据，bjson格式；  
 客户端管理可以访问数据的应用，包括通信地址、秘钥、权限等；  
 客户端管理数据访问日志；  
 数据包括根数据和应用数据，开源数据结构； 

# 要解决的问题
 数据安全，包括鉴权和权限；  
 数据传输；  
 数据冲突，多个应用使用同份数据冲突问题；  

# 相关文件
 标准json文件见standard.json;key为字段名称，value为字段意义；
 安装包见requirements.txt； 
 安装包命令为 pip install -r requirements.txt
 
# 可能的应用方向
 聊天 应用服务器可以不保存数据  
 财务 财务信息属于企业，可以直接换平台，甚至对于有私有云要求的客户可以把服务部署到云上，数据部署在本地；这样及方便又安全；  
 购物 需要将订单数据加密与用户数据做核实，可以单独提供个核实字段  
 论坛 保留自己发的文章以及他人的评论  
 可以尝试用ipv6及类似技术做点对点数据传输  

# 关于我们
不管是Dao、Web3还是个人网盘，强调的都是个人对数据的拥有权。但是拥有后是不是一定有权利呢？我们不仅要保证自己对自己数据的拥有，更要确定拥有后的数据价值。  
只有应用对数据不在依赖或者说应用开发跟数据开发可以分开，人们随时随地可以因为应用服务不好而替换掉应用，这样个人持有数据才有价值。  
当然也不会因为应用服务的停服或者异常，导致个人数据的丢失。保证个人数据的完整性和持续性，也为未来不同个性的人工智能服务提供基础。  
 
# 任务列表
 20220216 读取mongodb的数据库并展示出来  
 20220217 把界面搭出来  
 20220222 把逻辑demo写出来  