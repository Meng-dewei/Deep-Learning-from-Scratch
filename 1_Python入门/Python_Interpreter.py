>>> 1 + 2
3
>>> 1 - 2
-1
>>> 4 * 5
20
>>> 7 / 5
1.4
>>> 3 ** 2
9


>>> type(10)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type("hello")
<class 'str'>


>>> x = 10 #初始化
>>> print(x)


>>> x = 100 # 赋值
>>> print(x)
100
>>> y = 3.14
>>> x * y
314.0
>>> type(x * y)
<class 'float'>


>>> a = [1,2,3,4,5] # 生成列表
>>> print(a)
[1, 2, 3, 4, 5]
>>> len(a)
5
>>> a[0]
1
>>> a[4]
5
>>> a[4] = 99 # 赋值
>>> print(a)
[1, 2, 3, 4, 99]


>>> print(a)
[1, 2, 3, 4, 99]
>>> a[0:2]
[1, 2]
>>> a[1:]
[2, 3, 4, 99]


>>> print(a)
[1, 2, 3, 4, 99]
>>> a[0:2] # 获取索引为0到2（不包括2）的元素
[1, 2]
>>> a[1:] # 获取从索引为1的元素到最后一个元素
[2, 3, 4, 99]
>>> a[:3] # 获取从第一个元素到索引为3（不包括3）的元素
[1, 2, 3]
>>> a[:-1] # 获取从第一个元素到最后一个元素的前一个元素之间的元素
[1, 2, 3, 4]
>>> a[:-2] # 获取从第一个元素到最后一个元素的前二个元素之间的元素
[1, 2, 3]


>>> me = {'height':100} # 生成字典
>>> me['height']
100
>>> me['weight'] = 70 # 添加新元素
>>> print(me)
{'height': 100, 'weight': 70}


>>> hungry = True
>>> sleepy = False
>>> type(hungry)
<class 'bool'>
>>> not hungry
False
>>> hungry and sleepy
False
>>> hungry or sleepy
True


>>> hungry = True
>>> if hungry:
...     print("I'm hungry")
...
I'm hungry
>>> hungry = False
>>> if hungry:
...     print("I'm hungry")
... else:
...     print("I'm not hungry")
...     print("I'm sleepy")
...
I'm not hungry
I'm sleepy


>>> for i in [1,2,3]:
...     print(i)
...
1
2
3


>>> def hello():
...     print("hello world")
...
>>> hello()
hello world
>>>
>>> def hello(object):
...     print("hello " + object + "!")
...
>>> hello("cat")
hello cat!