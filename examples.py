class MyNum(object):
    classy = 10
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value
    def increment(self):
        self.val += 1


a = MyNum('hello')
a.increment()
a.increment()
print(a.val)

class InstCount(object):
    count = 0
    def __init__(self, val):
        self.val = val
        InstCount.count += 1
    def set_val(self, newval):
        self.val = newval
    def get_val(self):
        return self.val
    def get_count(self):
        return InstCount.count

a = InstCount(10)
b = InstCount(20)
a.set_val(11)
b.set_val(21)
print('a.val=', a.val)
print('b.val=', b.val)
print('InstCoun=', InstCount.count)
print('a.count=', a.get_count())
print('b.count=', b.get_count())