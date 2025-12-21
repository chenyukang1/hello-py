
class Student(object):
    def __init__(self, name, score) -> None:
        self.__name = name # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量
        self.__score = score

    def print_score(self): # 类的方法
        print(f'{self.name}: {self.score}')
