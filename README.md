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