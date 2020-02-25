#coding = utf-8
class Student():
    __slots__ = ('__rabbit','__cat','cat','rabbit','student_run') # 用tuple定义允许绑定的属性名称,如果直接用Student（Student.test = "ppp"）对象名去绑定不用实例还是可以绑定的
    def __init__(self,cat,rabbit):
        self.__cat = cat
        self.__rabbit = rabbit
        self.cat = cat
        self.rabbit = rabbit

    def tests1(self):
        print("多态")
    def get_cat(self):
        return self.cat
    def set_rabbit(self,new_rabbit):
        if 0 <= new_rabbit <= 100:
            self.rabbit = new_rabbit
            return self.rabbit
        else:
            raise ValueError("请输入0 <= new_cat <= 100")
    def __god(self):
        return (self.__cat)
    def run(self):
        result = self.cat + self.rabbit
        return result
class base(Student):
    def __init__(self):
        super().__init__(1,2)
        self.agess = None
    # def run(self):
    #     result = self.rabbit-self.cat
    #     return result
    def tests1(self):
        super().tests1()
    @property
    def birth(self):
        return self.agess
    @birth.setter
    def birth(self,birth_vale):
        if not isinstance(birth_vale,int):
            raise ValueError("传入参数必须为int类型的")
        elif 0 <= birth_vale >=100:
            raise ValueError("传入参数必须在0-100之间")
        else:
             self.agess = birth_vale
    @property
    def ages(self):
        return 2020 - self.agess
class duck():
    def tests1(self):
        print("鸭子类型")
def student_run(self,set_age):
    self.age = set_age
def prin(Student):
    Student.tests1()
class Animal(object):
    def __init__(self,dog):
        self.dog = dog
    def __str__(self):
        return 'Student object (dog: %s)' % self.dog


if __name__ == "__main__":
    import os
    # # @unique
    # dic = {
    #     "bird":"1",
    #     "dog": "2",
    #     "cat": "3",
    #     "duck": "4",
    #     "rabbit": "5",
    #     "lists": {
    #         "bird2": "1",
    #         "dog2": "2",
    #         "cat2": "3",
    #         "duck2": "4",
    #         "rabbit2": "5",
    #     }
    # }
    # a = []
    # for k,v in dic.items():
    #     if k == "bird":
    #         print(v)
    #     elif k == "lists":
    #         print(v)
    #         for k2,v2 in v.items():
    #             if k2 == "bird2":
    #                 print(v2)
    # dic = dict(a = 1,b = 2)
    # print(dic.items())
    # for k,v in dic.items():
    #     if k == 'a':
    #         print(v)
    d = {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
        'f': {
            'A': '5',
            'B': '5',
            'C': '5',
            'D': {
                '~': '5',
                '@': '5',
                '$': {
                    'run':'#####!!!!!',
                    },
            },
            'E': ['L','O','O','P'],
            'F': ('L','O','O','K')
        }
    }
    # try:
    #     # a = []
    #     # seq = ('a', 'b', 'c', 'd', 'e', 'f')
    #     # for i in range(9):
    #     #     a.append(i)
    #     # print(a)
    #     # print(''.join(seq))
    #     def digui(key,dicts):
    #         for k,v in dicts.items():
    #             if k == key:
    #                 return v
    #             elif isinstance(v,dict):
    #                 result = digui(key,v)
    #                 if result is not None:
    #                     return result
    #     print(''.join(digui('F',d)))
    # except ValueError as e:
    #     raise (e)
    # w = [['A','B','C','D','E','F'],['1','2','3','4','5','6']]
    # print(w[1][0])
    # d = [9,5,3,2,6,1,2,4]
    # print(len(d))
    d = [9, 5, 3, 2, 6, 1, 2, 4]
    for i in range(len(d)-1):
        for j in range(len(d)-1-i):
            if d[j] > d[j + 1]:
                # d[j],d[j + 1] = d[j + 1],d[j]
                temp = d[j]
                d[j] = d[j+1]
                d[j+1] = temp

    print(d)

