
# iClicker Practice Test 1
## October 2, 2018

---


## 1) If you need to know what the max() function does, what command will you use:
#### A) docstring(max)
#### B) help(max())
#### C) from help import max
#### D) help(max)
#### E) # Docstring max

---

---

## Given:

```
my_int = 5
larger_int = 7
my_max_num = max(my_int, larger_int)
```

## 2) In the code above, what are the **arguments** to the ```max() function```?
#### A) max
#### B) my_int, larger_int
#### C) max, my_max_num
#### D) my_int, larger_int, my_max_num
#### E) my_max_num

---

---

## Given:

```
n = 5 * 7 + 2 * 3 - 1
```

## 3) What is the value of the variable ```n```
#### A) 40
#### B) 39
#### C) 90
#### D) 134
#### E) 110


---

---

## Given:

```
x = True
y = False
var1 = not x or y and not y or x
var2 = not (x and not y)
```

## 4) Above, var1 is ___ and var2 is ____
#### A) True, True
#### B) True, False
#### C) False, True
#### D) False, False

---

---

## 5) How would you define a function called ```mult_by_three``` and then call it with variable ```my_int``` that has a value of 5?
```
* A) 
def mult_by_three(a_number):
    return a_number * 3
mult_by_three(5)

* B) 
define mult_by_three(a_number):
    return a_number * 3
my_int = 5
mult_by_three(my_int)

* C) 
function mult_by_three(a_number):
    return a_number * 3
my_int = 5
mult_by_three(my_int)

* D) 
def mult_by_three(a_number):
    return a_number * 3
my_int = 5
mult_by_three(my_int)
```


---

---

## 6) How would you import the math library and then instantiate a variable ```pi_ceil``` with the ceiling of pi?
```
* A) 
import math
pi_ceil = math.ceil(pi)

* B) 
import math
pi_ceil = ceil(pi)

* C) 
import math
pi_ceil = math.ceil(math.pi)

* D) 
import math
pi_ceil = ceil(pi)
```


---

---

## Given:

```
def my_function(an_int):
       print("You passed:",  an_int)
my_int = 5
n = my_function(my_int)
```

## 7) What is the value of ```n```
#### A) False
#### B) None
#### C) 5
#### D) "You passed: 5"
#### E) An empty string



---

---

## Given:

```
a = 3
b = 2
```

## 8) Given the above values for a and b, which of the following will produce an error?
#### A) a - b
#### B) b = b + a
#### C) x = b > a
#### D) print(a, b, a % b, b % a)
#### E) a * b = 6


---

---

## Given:

```
my_num = input("Enter any number: ")
half_my_num = my_num / 2
print(half_my_num)

```

## 9) You're trying to input a number from a user and print half the value of what they entered, but your code isn't working. What should you change in the code above to fix it? (Assume the user follows directions and enters a number.)
#### A) half_my_num = int(my_num / 2)
#### B) my_num = int(input("Enter any number: "))
#### C) my_num = float(input("Enter any number: "))
#### D) half_my_num = float(my_num / 2)
#### E) half_my_num = int(my_num) / 2

---

---

## Given:

```
mylist = [6, 8, 12, 13]

n = mylist[3] % mylist[1]
```

## 10) What is the value of ```n``` above?
#### A) 0
#### B) 7
#### C) 4
#### D) 5
#### E) 2


---

---

## Given:

```
i = 0
while i < 10:
    print(i)
    i+=1
```

## 11) How many numbers are printed by the ```print()``` function above?
#### A) 9 numbers
#### B) 10 numbers
#### C) 11 numbers 

---

---

## Given:

```
x = [10,20,30]
x[1] = 42
print(x)
```

## 12) What will be printed by the code above?
#### A) [10, 42, 30] 
#### B) [10, 20, 30]
#### C) [42, 42, 42]
#### D) [10, 20, 30]
#### E) [42, 20, 42]


---

---

## Given:

```
def swap(val1, val2):
    tmp = val1
    val1 = val2
    val2 = tmp

x = 6
y = 3
swap(x, y)
print(x, y)
```

## 13) What will be printed by the code above?
#### A) 3 6
#### B) None
#### C) 3 3
#### D) 6 3
#### E) 6 6


---

---

---

---


Answers: 1) D, 2) B, 3) A, 4) B, 5) D, 6) C, 7) B, 8) E, 9) C, 10) D, 11) B, 12) A, 13) D