# x = 5
# y = "Hello, World!"
# if x > 2:
#     print(y);
# if x > 10:
#     print(y+'no');

# ------------------

# x = 12
# x = 'banti'
# y = "Hello, World!"
# print(type(x));

# ------------------

x = str(12)
# x = int('5')
# x = float('5')
# x, y, z = 'Apple', 'Banana', 'Cherry'
# fruits = ["apple", 12, "cherry"]
# x, y, z = fruits;
# print(x, y, z);
# print(x + y + z);

# ------------------

# x = 'Awesome';
# def myFunc():
#     # global x;
#     x = 'Good'
#     print('Phython is', x);
# myFunc();

# ------------------

# x = 122;
# # a = float(x);
# a = complex(x);
# print(a);

# ------------------

# import random;
# print(random.randrange(1,10))

# ------------------

# a = """Lorem ipsum dolor sit amet, 
# consectetur adipiscing elit, 
# sed do eiusmod tempor incididunt."""
# print(a);
# print(a[0]);

# ------------------

# x = 'hello';
# print(len(x));
# for a in x:
#     print(a);

# ------------------

# txt = 'The best things in life are free!'
# print('hello' in txt);
# if('hello' not in txt):
#     print('not present')
# if('hello' in txt):
#     print('present')
# else:
#     print('not present')

# ------------------

# b = 'Hello world';
# print(b[0:2]);
# print(b[:2]);
# print(b[7:]);
# print(b[-5:-2]);

# ------------------

# a = 'Hello world';
# print(a.upper());
# print(a.lower());
# a = '    Hello world    ';
# print(a.strip());
# print(a.replace('H', "J"))
# print(a.split(' '))

# ------------------

# price = 200;
# itemno = 1001;
# qty = 3;
# txt = 'The product qty is {}, item no is {} and price is {}';
# txt = 'The product qty is {2}, item no is {1} and price is {0}';
# print(txt.format(price, itemno, qty));

# ------------------

# txt = "We are the so-called \"Vikings\" from the north."
# txt = "banana"
# print(txt.center(20, "O"));

# ------------------

# x = 5
# c = 4
# print(bool(x < c));

# ------------------

# x = list(("apple", "banana", "carrot"))
# print(x[1:3])
# x[1:3] = ['bool', 'grapes'];
# x.insert(1, 'App')
# x.append('App')
# arrTupple = ('App', 'Bap', 'Cap')
# x.extend(arrTupple)
# x.remove('Bap')
# x.pop()
# del x
# x.clear();
# print(x)

# ------------------

# list = list(("apple", 'xyz', "banana", "crrot"))
# for x in list:
#     print(x)
# for i in range(len(list)):
#     print(list[i])
# for item in list:
#     if('a' in item ):
#         print(item);
# print(myset) = [item for item in list if 'a' in item]
# newlist = [item if item != "banana" else "orange" for item in list]
# print(newlist);
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower, reverse = True);
# thislist.sort(reverse = True);
# print(thislist)
# mylist = thislist.copy()
# mylist = list(thislist);
# print(mylist);
# thislist2 = [1, 2, 3, 4]
# for item in thislist2:
#     thislist.append(item);
# thislist.extend(thislist2)
# print(thislist);

# ------------------

# sampleTupple = tuple(("apple", "banana", False, "carrot", 6))
# sampleTupple = ("apple", "banana", False, "carrot", 6)
# print(type(sampleTupple))

# ------------------

# myset = {"apple", "banana", "carrot", True, False, 0, 1, 2}
# myset = set(("apple", "banana", "carrot", True, False, 0, 1, 2))
# myset = ("apple", "banana", "carrot", True, False, 0, 1, 2)
# myset = tuple(("apple", "banana", "carrot", True, False, 0, 1, 2))
# myset = ["apple", "banana", "carrot", True, False, 0, 1, 2]
# myset = list(("apple", "banana", "carrot", True, False, 0, 1, 2))
# myset = {"brand": "Ford","model": "Mustang","year": 1964}
# myset = dict(brand = "Ford", model = "Mustang", year = 1964)
# print(type(myset))
# tropical = {"pineapple", "mango", "papaya"}
# myset.add("orange")
# myset.update(tropical)
# myset.discard("mango")
# print(myset);

# ------------------

# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
# thisdict = dict(brand = "Ford", model = "Mustang", year = 1964)
# print(thisdict["brand"]);
# print(thisdict.get("brand"));
# print(thisdict.keys());
# print(thisdict.items());
# for x, y in thisdict.items():
#     print(x, y);
# child1 = {"name" : "Emil", "year" : 2004}
# child2 = {"name" : "Tobias", "year" : 2007}
# child3 = {"name" : "Linus", "year" : 2011}
# myfamily = { "child1" : child1, "child2" : child2, "child3" : child3 }
# for x, obj in myfamily.items():
#     print(x);
#     for a, b in obj.items():
#         print(b);

# ------------------

# a = 5;
# b = 9;
# if a > b:
#     print("yes");
# elif a == b:
#     print("no");
# else:
#     print("not found")
# print("yes") if a > b else print("No") if a == b else print("not found")

# ------------------

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == 'banana':
#         break;
#     print(x);
# for x in range(2, 30, 3):
#   print(x)
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x, y);

# ------------------

# def _sameFunc(para):
#     print('Sample function ' + para);
# _sameFunc("test");
# def _sameFunc(*para):
#     print('Sample function ' + para[0] + ', ' + para[1] + ', ' + para[2]);
# _sameFunc("test", "test2", "test3");
# def _sameFunc(x,y,z):
#     print('Sample function ' + x);
# _sameFunc(x = "test", y = "test2", z = "test3");
# def _sameFunc(**a):
#     print('Sample function ' + a['y']);
# _sameFunc(x = "test", y = "test2", z = "test3");
# def _sameFunc(x, y, /, *, c, d):
#     print(x + " " + y, c + " " + d );
# _sameFunc("position", "only", c = "keyword", d = "only");

# ------------------

# x = lambda a,b : a * b;
# print(x(5, 5));
# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))

# ------------------

# class MyClass:
#     x = 5;
# p1 = MyClass();
# print(p1.x);

# class MyClass:
#     def __init__(self, name, age):
#         self.name = name;
#         self.age = age;
#     # def __str__(self):
#     #     return f"{self.name} {self.age}"
#     def myfunc(self):
#         print("My name is " + self.name, self.age);
# # p1 = MyClass('Banti', 33);
# # print(p1);
# # p1.myfunc();
# class Student(MyClass):
#     # pass
#     def __init__(self, name, age):
#         super().__init__(name, age)
# x = Student("Bably", 22);
# x.myfunc();

# ------------------

# mytupple = ("apple", "banana", "cherry");
# myit = iter(mytupple);
# print(next(myit));
# print(next(myit));
# print(next(myit));

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a;
#         self.a += 1
#         return x;
# myclass = MyNumbers();
# myiter = iter(myclass);

# print(next(myiter));
# print(next(myiter));
# print(next(myiter));
# print(next(myiter));
# print(next(myiter));

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1;
#             return x;
#         else:
#             raise StopIteration

# myclass = MyNumbers();
# myiter = iter(myclass);

# for x in myiter:
#     print(x);

# ------------------

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand;
#         self.model = model;
#     def move(self):
#         print("Move!")
# class Car(Vehicle):
#     pass
# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")
# class Plane(Vehicle):
#     def move(self):
#         print("Fly!")
# car1 = Car("Ford", "Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "737")
# for x in (car1, boat1, plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()

# ------------------

# import mymodule as tm
# tm.greeting('Banti')
# print(tm.person['name'])

# import platform
# x = platform.system()
# x = dir(platform)
# print(x)

# ------------------

# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# y = json.dumps(x)
# # print(y["age"]);
# print(y)

# ------------------

# username = input("Enter username:")
# print("Username is: " + username)

# price = 49
# txt = "The price is {:.2f} dollars"
# print(txt.format(price))

