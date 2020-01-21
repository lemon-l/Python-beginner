# 列表推导式
# 集合推倒式
# map filter
# set 也可以被推倒

a = {1,2,3,4,5,6,7,8,9}
b = {i*i for i in a if i >= 5}

students = {
    '喜小乐' : 18,
    '石敢当' : 20,
    '哼小曲' : 15
}

c = {value:key for key,value in students.items()}
d = {key for key,valus in students.items()}
e = {value for key,value in students.items()}
print(c)

for x in d:
    print(x)