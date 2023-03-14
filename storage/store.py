# 定义个常用的存储方法
import pymongo

def store(database, collection, dict):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[database]  # 连接新数据库
    mycol = mydb[collection]
    mycol.insert_one(dict)
    return True
