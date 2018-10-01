## Debugging -- Finding and fixing errors

There are three types of errors:
* Syntax errors [(httlacs 1.7)](http://interactivepython.org/runestone/static/thinkcspy/GeneralIntro/Syntaxerrors.html) -- Bad structure. Examples: (misspell ```whle``` or add extra parentheis ```print('Hello'))```
* Runtime Errors [(httlacs 1.8)](http://interactivepython.org/runestone/static/thinkcspy/GeneralIntro/RuntimeErrors.html) -- Something fatal happens during execution. Example: Converting input from a string to an integer, then trying to call a string method on it. I caused this error in last week's workbook, then explained it in [week_04_sept_18_20/workbook_help_-_2018_09_20.ipynb
](https://github.com/enactdev/CISC_106_F18/blob/master/week_04_sept_18_20/workbook_help_-_2018_09_20.ipynb) 
* Semantic Errors [(httlacs 1.9)](http://interactivepython.org/runestone/static/thinkcspy/GeneralIntro/SemanticErrors.html) -- Also calle a software bug. Basically, you do not get an error message from Python, but your code isn't going to do what you expect. Example: I demonstrated this by editing the function we used calculated the price of an amusement park admission to not accout for the age of 18. (Used ```age < 18``` in one conditional and ```age > 18``` in another when the second should have been ```age >= 18```.)

Generally debugging consists of fixing runtime and semantic errors. You *should* understand the difference, but you do not need to for this class. 

I'm repeating myself from week 2 here. Don't worry, I'll be repeating this again and again in this course.
* When reading code you should constantly be thinking: "Under what conditions will this code run?"
* When writing code you should be constantly asking yourself, "But what if..." 

Now, more on that "what if..."

### Edge Cases
* Informal defintion of an edge case for this class is when a slight change in value causes a big change in expected outcome.
* Remeber when we wrote a function to calcualte the admission price for an amusement park? It was on [Tues. Sept. 18](https://github.com/enactdev/CISC_106_F18/blob/master/week_04_sept_18_20/notebook_-_2018_09_18.ipynb). Here, the edge cases occur when the price changes for different age groups:
 * Under 4 is free, so there's a big change between the ages of 3 and 4. 
 * Kids 4-17 cost $20, adults are 35. So the next change is between the ages of 17 and 18
 * Senior citizens get a discount, so there's also a big change at 65.

Basic age timeline here would be:
```
|--|---------|--------------------------------|---------------|

0  4         18                               65              Infinity
```

Feel free to use scratch paper when coding! I do.

One falacy many new programmers have is that debugging is more about reading code than writing code. That is wrong! Reading code is the easy part. Understanding how all the different parts of a program work together is the hard part. I spend more time thinking about code than I do writing code. When debugging, you will spend more time thinking about how all the different parts of the program work together than you will spend typing out code. 

For every change you make, you need to ask yourself how this change will affect the rest of the program.

### Tips on debugging:
 * Turn off distractions. You need to juggle lots of things in your head.
 * Read the requirements. Sketch out the edge cases. Re-read the requirements. Update your sketch of the edge cases. Repeat until you're confident that you have thought of everything.
 * For each edge case, decide which conditional you need: <, <=, >, >=, !=, ==
 * Read the problem again. Have you thought of everything? 

---

There was an anonymous question on Moodle this weekend regarding the error: local variable 'variable_name' referenced before assignment. The student wrote: "I haven't used these variable names anywhere else besides within the bodies of their respective 'if statements' and when returning them."

I hope this was not from this class. If it is that's ok, I don't expect everyone to remember everything I've said. Who remembers my advice against initializing variables within an if statement? This is that. 

For reference, remember when I changed the price of admission for an adult from ```elif (age >= 18) and (age < 65):``` to ```elif (age > 18) and (age < 65):```? In the later case, none of the conditional statements match the exact age of 18, and the function as written returns a cost of 0 for an age of 18. But what happens when you comment out the line that initializes price to 0?
