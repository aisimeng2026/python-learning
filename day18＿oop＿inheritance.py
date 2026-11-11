# === 任务A：动物类 ===
class Animal(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("动物在叫......")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} 在汪汪叫！")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} 在喵喵叫！")


# === 任务B：员工类 ===
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary,department):
        #调用父类的初始化方法，把 name 和 salary 传过去
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        print(f"经理: {self.name}, 部门: {self.department}, 薪水: {self.salary}")

# === 测试运行 ===
print("--- 任务 A 测试 ---")
my_dog = Dog("旺财")
my_cat = Cat("喵星人")

#多态的体现：同一个 speak() 方法，不同对象有不同表现
my_dog.speak()
my_cat.speak()

print("\n--- 任务 B 测试 ---")
m =Manager("李总",20000,"研发部")
m.show_info()