# 这里尝试用websocket向服务器传输岗位信息
# 每次与服务器交互要保存日志

import websockets
import pymongo
import asyncio

IP_ADDR = "127.0.0.1"
IP_PORT = '8888'


# 向服务器握手
async def clientHands(websocket):
    while True:
        await websocket.send('hello')
        response_str = await websocket.recv()
        if 'hello world' in response_str:
            print('connected success')
            return True
        else:
            print('connected fail')


'''获取信息，
因为根数据在本地所以这个可以不要，或者只作为比对使用；
获取作为个人从应用备份自己的数据
还有就第一次同步，做全量同步
'''


async def clientSend(websocket, database, collection):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[database]  # 连接新数据库
    mycol = mydb[collection]
    doc_list = mycol.find()
    for i in doc_list:
        # print(i)
        await websocket.send(str(i))


'''添加信息，
将本地新增的信息新增到应用中；只同步添加时间为上次同步时间之后的新增；'''

''' 修改信息，
将本地修改的信息同步到应用中；只同步更新时间为上次同步时间之后的更新；'''

'''删除信息，
将本地已经删除的信息同步到应用中修改数据状态；删除很多时候都是逻辑删除，
除非这里作为唯一数据源，否则无法杜绝应用的数据备份；
实际应用也会使用自己数据库，只是用应用数据库和用户的个人数据做同步
'''


# 进行websocket连接
async def clientRun():
    ipdress = f'ws://{IP_ADDR}:{IP_PORT}'
    async  with websockets.connect(ipdress) as websocket:
        await clientHands(websocket)
        await clientSend(websocket, "private", 'EmployeeInformation')


if __name__ == "__main__":
    print("-----client main begin--")
    asyncio.get_event_loop().run_until_complete(clientRun())
