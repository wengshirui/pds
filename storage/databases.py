# 数据存储问题
import pymongo


def getDataList():
    '''
    查看所有的数据库，可以把默认的影藏
    :param myclient:
    :return:
    '''
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    return myclient.list_database_names()


if __name__ == "__main__":
    r = getDataList()
    print(r)
