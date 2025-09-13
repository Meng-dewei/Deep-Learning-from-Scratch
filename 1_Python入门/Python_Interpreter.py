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


>>> x = 10 #��ʼ��
>>> print(x)


>>> x = 100 # ��ֵ
>>> print(x)
100
>>> y = 3.14
>>> x * y
314.0
>>> type(x * y)
<class 'float'>


>>> a = [1,2,3,4,5] # �����б�
>>> print(a)
[1, 2, 3, 4, 5]
>>> len(a)
5
>>> a[0]
1
>>> a[4]
5
>>> a[4] = 99 # ��ֵ
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
>>> a[0:2] # ��ȡ����Ϊ0��2��������2����Ԫ��
[1, 2]
>>> a[1:] # ��ȡ������Ϊ1��Ԫ�ص����һ��Ԫ��
[2, 3, 4, 99]
>>> a[:3] # ��ȡ�ӵ�һ��Ԫ�ص�����Ϊ3��������3����Ԫ��
[1, 2, 3]
>>> a[:-1] # ��ȡ�ӵ�һ��Ԫ�ص����һ��Ԫ�ص�ǰһ��Ԫ��֮���Ԫ��
[1, 2, 3, 4]
>>> a[:-2] # ��ȡ�ӵ�һ��Ԫ�ص����һ��Ԫ�ص�ǰ����Ԫ��֮���Ԫ��
[1, 2, 3]


>>> me = {'height':100} # �����ֵ�
>>> me['height']
100
>>> me['weight'] = 70 # �����Ԫ��
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