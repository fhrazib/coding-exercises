

---

## OOP Basics
While traditional procedural programming languages are great to solve many programming problems efficiently they are inherently not good enough to model real world problems.
Because in real world each entity has both - attributes and behaviors. Procedural programming are good to represent attributes of real world entity in a single structure using different data types. For example the number of doors in a `Car` with `int` data type, the color of the `Car` with `String` datatype. But but a car is not all about the collection of these attributes. The car has some behaviors like - it accelerate, it turns left or right. These could not be incorporated into a single structure in procedural programming language. 

OOP (object oriented programming) comes here to solve these problems. OOP represent a real world entity (`Car`, `Student`, `Person`, `Account`... anything you could think) more efficiently by encompassing both attributes and behaviors in a single structure. To represent attributes OOP use different data types like - `int`, `float` etc and to represent behavior OOP use methods like `turnLeft()`, `turnRight()` etc.

To represent these real world object more efficiently OOP introduce 2 new concepts - ***Class*** and ***Object***

### Class and Object
#### Class
A class is the blueprint of a real world entity. Class encapsulates both attributes (via different data types) and behaviors (via methods/functions) of real world's entity in a single structure.

Class also could be think as user defined (or derived) data type. While the programming language provided data type like `int`, `float` etc could represent simple real world data like - number of doors/wheels in a `Car`, age of a person, but they can not represent real world complex data like `Car`. Because car has both - attribute and behaviors. OOP give you the opportunity to make a complex data type for `Car` using class. That's why class is often called user defined data type or derived data type.

#### Object
Object is the instance of class. It is the 

Object could also think as class type data. You define a class - `Car` as your complex data type. Now you can create your own data from that data type `Car` that will reside in memory. 

#### Difference Between Class and Object
![](car-class-object.png)
Just like you can not drive a blueprint or engineering design of a car you can not use a class directly. Before using class you have to create instance (object) from the class. This object will stay in memory, and you can use it in your program.

| <span style="width=40%">Class</span>                          | <span style="width:40%">Object</span>                           |
| ------------------------------------------------------------- | --------------------------------------------------------------- |
| Class is a template for declaring and creating objects        | An object is an instance of class                               |
| When a class is created, no memory allocated                  | Objects are allocated to memory space whenever they are created |
| Class has to be declared only once                            | An object is created many times per requirements                |
| As class can not be manipulated as they are not in the memory | An object can be manipulated                                    |
| A class is logical entity                                     | An object is physical entity                                    |      


##### Creating Class
```python
class Car:  
    no_of_wheels, no_of_doors = 4, 4  
  
 def __init__(self, color, producer, model, fuel):  
        self.color = color  
        self.producer = producer  
        self.model = model  
        self.fuel = fuel  
  
    def turn(self, direction: str):  
        print(self.model + ':' + 'Turning ' + direction + '...')  
  
    def accelerate(self, factor: float):  
        print(self.model + ':' + 'Accelerating its speed by ' + str(factor) + 'x...')  
  
    def __str__(self):  
        return self.producer + ' ' + self.color + ' ' + self.model + ' ' + self.fuel
```

##### Creating Object
```python
toyota = Car('Red', 'Toyota', 'Prius', 'Electricity')  
  
print('Car:', toyota)  
print('Total wheels:' + str(toyota.no_of_wheels))  
print('Color: ' + toyota.color)  
toyota.accelerate(2.5)  
toyota.turn('left')


OUTPUT:
Car: Toyota Red Prius Electricity
Total wheels:4
Color: Red
Prius:Accelerating its speed by 2.5x...
Prius:Turning left...

```

### Four Pillars of OOP

#### Abstraction
Abstraction allow us only to show the essential things to users. It hides the  details' implementation, trivial or the non-essential units from the users. In other words abstraction is the hiding details and complexities and showing only the necessary part to the users. Its one of the most fundamental concepts of OOP. 
**Example**:  when you login to your email account online, you enter your `user_id` and `password` to login. What happens when you hit login, how the input data sent to server, how it gets verified is all abstracted away from the you.

Data Abstraction may also be defined as the process of identifying only the required characteristics of an object ignoring the irrelevant details. The properties and behaviors of an object differentiate it from other objects of similar type and also help in classifying/grouping the objects.
**Example:** Say you are designing a student management system for a university. You have to model a student's attributes and behaviors in `Student` class. A student in real life may have a lot of attributes like - roll number, registration number, CGPA, SSN, height, weight and so on. Similarly as student might have a lot of behavior like - enrolling himself to a particular course, paying semester fees,  taking part in exam, traveling, listening to musics. 
But abstraction tell us only to take the attributes and behaviors those are relevant to student management system and ignore all others attributes and behaviors. 

#### Encapsulation
As we already know real world entity has both attributes and behaviors. Encapsulation is the ***process of binding these attributes and behaviors in a single entity***. 	If you are creating class, you are doing encapsulation.
To achieve encapsulation OOP language like java do the following  two things - 
- Make the instance variables private so that they cannot be accessed directly from outside the class. You can only set and get values of these variables through the methods of the class.  
- Have `getter` and `setter` methods in the class to set and get the values of the fields.

The whole idea behind encapsulation is to hide the implementation details from users. If a data member is private it means it can only be accessed within the same class. No outside class can access private data member (variable) of other class.
However, if we set up public `getter` and `setter` methods to update the private data fields then the outside class can access those private data fields via public methods.

This way data can only be accessed by public methods thus making the private fields, and their implementation hidden for outside classes. That’s why encapsulation is known as **data hiding.** 

--- 
#### Abstraction vs. Encapsulation
It seems both encapsulation and abstraction hide something from the users but here are some key difference between these two concepts - 
- Encapsulation is **data hiding(information hiding)** while Abstraction is **detail hiding(implementation hiding).**
- While encapsulation groups together data and methods that act upon the data, data abstraction deals with exposing the interface to the user and hiding the details of implementation.
--- 
#### Inheritance
Inheritance is the process by which one class acquires the properties(data members) and functionalities(methods) of another class.  In, inheritance there are 2 class involved - 
- **Parent Class:**  
	- The class whose properties and functionalities are used(inherited) by another class  
	-  also known as super class or base class.
- **Child Class:**  
	- The class that extends the features of another class 
	- also known as child class, subclass or derived class.
- The aim of inheritance is to provide the re-usability of code so that a class has to write only the unique features and rest of the common properties and functionalities can be extended from the another class
- The biggest **advantage of Inheritance** is that the code that is already present in base class need not be rewritten in the child class

#### Polymorphism
- Polymorphism allows you to have multiple methods by the same name.  These same named multiple method could be found in same class or subclasses of a same parent classes.
- Based on this fact where polymorphism will happen, polymorphism could be either of static or dynamic. Method Overloading is static polymorphism while, method overriding is dynamic polymorphism.
	-   **Overloading** Overloading means having multiple method with same method name but with different method signatures. Method signature composed by - (1) method name  (2) number of arguments (3) types of arguments. Method signature dosen't depends on return type. Overloaded methods are resolved at compile time. Compiler decides which method it should actually call from the overloaded methods (multiple method with same name). Its also known as static polymorphism.
	-   **Overriding** Its happen when a derived class **override** the method of a parent class. Say you have a parent class  `Animal` which has a method `makeSound()`.  `Cat` and `Dog` are 2 subclass of the `Animal` class. They both implement the `makeSound()` method by their own way - `Cat` 'Meaw's and `Dog`  'Woof's. Now you can use a reference type say `dog` of `Animal` to store the `Dog` object and another reference type say - `cat` of type `Animal` to store the `Cat` object. 
		- Now if you call the method like this `dog.makeSound()`  you will gate 'Woof'
		- If you call the method `cat.makeSound()` you will get 'Mew'
	- Even both `dog` and `cat` object are subclass of `Animal`  class, and they both implement the same method `makeSound()`but here they are acting differently based on their implementation. This behavior is known as method overriding.
	- Also known as dynamic polymorphism,  or run time polymorphism. 















---
### Immutable 
## Two pointers technique
### Problem-solving example with two pointers - Palindrome Check
#### 1st Attempt
#### 2nd Attempt
#### 3rd Attempt
