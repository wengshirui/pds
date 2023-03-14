# 把旧的mysq数据迁移到MongoDB里面
# 这个不能提交到github上面
# python -m pwiz -e mysql -u dlrl -H localhost --password dlrl2 > testModel.py

import pymongo
from private.testModel import EmployeeResumemodel, EmployerRecruitmentmodel

job_list = EmployerRecruitmentmodel.select()  # 读取旧数据

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["private"]  # 连接新数据库
mycol = mydb['EmployeeInformation']

# 开始把旧数据写到标准数据里面
# print(len(job_list))
for i in job_list[10:]:
    print(i.position)
    if i.salary_type == '2':
        salary_type = '按月发放'
    else:
        salary_type = '其他'
    mydict = {
        "job": i.position,
        "company": i.company_name,
        "title": i.title,
        "requireStyle": i.require_style,
        "trade": i.trade,
        "skillRequirement": i.requirement,
        "simpleDesc": i.simple_desc,
        "describe": i.describe,
        "requireNumber": i.number,
        "standNumber": 0,
        "salary": i.salary,
        "salaryType": salary_type,
        "accommodation": i.accommodation,
        "insurance": i.insurance,
        "otherWelfare": i.other_welfare,
        "contact": i.contact,
        "contactPhone": "隐私不泄露",
        "city": i.city,
        "detailedAddress": i.detailed_address,
        "wxId": "隐私不泄露",
        "email": "隐私不泄露",
        "createTime": i.add_time,
        "updateTime": i.upd_time
    }
    mycol.insert_one(mydict)
