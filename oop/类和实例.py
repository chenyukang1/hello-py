
class Student(object):
    def __init__(self, name, score) -> None: # __init__方法的第一个参数永远是self，表示创建的实例本身
        self.name = name
        self.score = score

    def print_score(self): # 类的方法
        print(f'{self.name}: {self.score}')

bart = Student('Bart Simpson', 59)
print(bart)
print(bart.name)
print(bart.score)

bart.print_score()
