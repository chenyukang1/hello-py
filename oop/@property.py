# Python内置的@property装饰器就是负责把一个方法变成属性调用

class Student(object):
    def __init__(self, birth, score) -> None:
        self._birth = birth
        self._score = score

    @property
    def score(self):
        return self._score

    @property
    def birth(self):
        return self._birth

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student('2024-09-24', 70)
s.score = 60
print(s.score)
print(s.birth)
