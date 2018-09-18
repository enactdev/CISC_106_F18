
# Notes for September 18, 2018

General Announcements:
* Tests -- Dates posted in Canvas:
  * First test Thursday Oct. 4
  * Second test Thursday Nov. 1
  * Final TBD


Piazza message: We are fortunate to have a Peer Assisted Study Sessions (PASS) program this semester for this course. These sessions are optional but strongly recommended. Our PASS leader is a student named Hunter Suchyj.  He will be holding these sessions every week on Wednesdays at 5:30pm and Thursdays at 6:00pm.  (Location Sharp Lab - Room 105.)




Note on attendence: The two lowest attendance "grades" are dropped, which means you can miss two classes without penalty. Excused absenses are not counted in the final attendance "grade."





Test format -- half scan tron, half written


Absenses -- excused vs missed


Colons go at the end of: if statement, while loop declaration -- any time there's a new code block!
* Code blocks -- signaled by a colon!
* Missing colon error message?
```
>>> 3 2 %
  File "<stdin>", line 1
    3 2 %
      ^
SyntaxError: invalid syntax

```

Go over truth tables



Thursday: When writing an if-else statement, you can change the conditional test to decide which case you want to run first. 

Example

```
>>> cisc_106 = 'fun'
>>> cisc_106 is 'fun'
True
>>> cisc_106 is not 'fun'
False
>>> if cisc_106 is 'fun':
...     print ('This class is fun')
... else:
...     print ('This class is not fun')
... 
This class is fun
>>> if cisc_106 is not 'fun':
...     print ('This class is not fun')
... else:
...     print ('This class is fun')
... 
This class is fun

```

Generally, I will decide which to use based on the length of the blocks of code. I try to put the short block of code at the top. Example in today's workbook.


---

Note on if statements -- You can use multiople in a row, and also embed within an if statement. 

---


Hacker rank -- arrow showing error?


Use parenthesis!


Syntax Errors: They basically show you where you're wrong:
```
>>> if 3 % 2 == 1
  File "<stdin>", line 1
    if 3 % 2 == 1
                ^
SyntaxError: invalid syntax

```


```
>>> 3 % 2 == 1
True
>>> (3 % 2) == 1
True
>>> ((3 % 2) == 1)
True

```
