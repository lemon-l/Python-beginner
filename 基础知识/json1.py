'''
-------------------------------- * 跨语言交换数据 * ------------------------------
json(JavaScript Object Notation)是JavaScript对象标记，是一种轻量级的数据交换格式
{a:'limeng'  ----NO    {'name' : 'limeng'}  ----YES
优点：易于阅读；易于解析；网络传输效率高；
*千万不要把文件名设为json，不然他会以为你是导入的文件，而不是一个模块
REST服务的标准格式
---------------------------------------------------------------------------------
            json                 python
            object                dict
            array                 list
            string                str
            number                int/float
            true/false            True/False
            null                  None
--------------------------------------------------------------------------------
json 对象：
json：与Javascript不一样，尽管很相似；
json 字符串：
'''
import json
'''
json_str1 = '{"name":"qiyue", "age":18}'    #json里面的东西必须用双引号，非字符串不用引号
json_str2 = '[{"name":"qiyue", "age":18, "flag":false},{"name":"qiyue", "age":18}]'

#反序列化    
student1 = json.loads(json_str1)
student2 = json.loads(json_str2)

print(type(student1))          #dict 字典
print(type(student2))          #list 列表
print(student1)
print(student2)
print(student1['age'])
'''

#序列化
student  = [
            {"name":"qiyue", "age":18, "flag":False},
            {"name":"qiyue", "age":18}
           ]

json_str = json.dumps(student)
print(type(json_str))
print(json_str)