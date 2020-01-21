'''
1.正则表达式；(是一个特殊的字符序列，一个字符串是否与我们所设定的这样的字符序列相匹配)
应用：快读检索；替换文本
2.json
贪婪：尽可能匹配多的符合条件的字符串，若要变为非贪婪，只需在后面加上“？”
#正则表达式
\d \D
\w 单词字符 \W
\s 空白字符 \S
.  匹配出了换行符中外的所有字符
^ 开始   $结束
(或关系)(且关系)
re.sub
re.match(从字符串的第一位进行匹配，如若不符合规则，则返回为空)
re.search(搜索整个字符串，指导搜到匹配的内容，与第一位是什么没有关系)
re.group
re.findall
'''

import re   #常用的检索方法
 
'''  
language = 'PythonC#JavaPHP'       
r = re.findall('c#',language,re.I | re.S)  #后面的第三个参数表示忽略大小写（re.S表示支持‘.’匹配的行为）
                                 #‘|’ 表示且的关系
'''

a = 'c|c++|java|python|javascript|php'
print(a.index('python') > -1)  #用他的索引进行判断
print('python' in a)           #用成员运算符进行判断
r = re.findall('python', a)    #用自带的方法，但是会返回列表
print(r)


'''
a = 'c2c++4java2python7javascript6php'
r = re.findall('\D', a)
print(r)

# 把函数传入字符串，并进行替换

language = 'PythonC#JavaC#PHPC#'  
def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'

r = re.sub('C#', convert, language) 
'''


'''
s = 'ABC576534df5fesdr5fsejk8gr4'

def convert(value):
    matched = value.group()
    if int(matched) >= 60:
        return '9'
    else:
        return '0'

r = re.sub('\d{2}', convert, s)
'''


s = 'life is short,i use python,i love python'
r1 = re.search('life(.*)python(.*)python', s)
r2 = re.findall('life(.*)python(.*)python', s)
print(r1.group(0,1,2))  #group 比较特殊，group(0)永远都返回的是完整的字符串，所以要获取，必须索引从1开始
print(r1.groups())
print(r2)           