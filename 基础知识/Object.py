'''
类（模板） = 面向对象
1.封装
2.继承
3.多态
类最基本的作用：封装
*方法 ！= 函数
方法：设计层面  函数：程序运行、过程式的一种称谓
这里面的self可以代换为任何其他的，相当于其他语言里面的this
*可以通过给类方法的functionName前面加__用来表示私有private的，外部不可以访问
用子类对象调用父类方法： super(cls,self).fun(*arg)
**当子类方法与父类方法同名的时候，python不会报错，但是优先调用子类方法**

'''
'''
                    |————类变量
             |——变量 ————实例变量
             |——方法 ————@classmethod实例方法(管理对象)
python类 ———        |————类方法（管理类）
             |——构造函数
             |——成员的可见性
'''

class Student():
    name = "李蒙"  
    age = 18
    sum = 0
    #类变量；实例变量
    def __init__(self,name,age):
        #构造函数
        #初始化对象的属性
        self.name = name      #——必须通过self实例化变量—— 
        self.age = age
       # self.__class__.sum += 1
       # print("当前班级的学生总数为：" + str(self.__class__.sum))
       # print(Student.sum)     #当打印print(self.__class__.sum)是会显示同样的结果
       # print(name)
       # print(age)          在这里调用nam、age打印出来的是类里面的“李蒙”“18”

    #方法
    '''
    def print_file(self,name,age):
        print("name: " + self.name)
        print("age: " + str(self.age))
    '''
    @classmethod     #类方法
    def plus_sum(self):
        self.sum += 1
        print(self.sum)
    @staticmethod    #静态方法（与面向对象关联不大，不建议使用）
    def add(x,y):
        pass

student1 = Student('limeng',18)
Student.plus_sum()
student2 = Student('李蒙',19)
Student.plus_sum()
print(student1.__dict__)     #__dict__是一个字典，里面保存着当前对象里面的所有变量
print(Student.__dict__)
print(student1.name)
print(Student.name)


#函数的调用在injection.py里面
#Student = Student()       *——————实例化———————*
#Student.print_file()










#------------------------------------好难，后面几乎没看------------------------
