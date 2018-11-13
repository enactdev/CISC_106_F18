# Light introduction to Matlab

**Quick show of hands, how many of you are famililar with UD AppsAnywhere?**

**Those who do have access to Matlab. Those who do not can use Matlab for free for 30 days. Our final exam is scheduled for Wednesday Dec. 12, so you are fine if you download it now.**

*Alternatively, Octave is a free and open source implementation of Matlab, and is what I will probably be using for examples in class. I'll know more on Thursday.**

## Lesson 1:

**Indexing starts at 1.**

**Any questions?**

## Syntax:

Python: lists and nested lists

Matlab: vectors and matrixes ('Mat' in Matlab stands for matrixes)

## Code Examples

**Get the diagonal of a nested list in Python:**

```
nested_list = [[1, 2, 3], 
               [4, 5, 6], 
               [7, 8, 9]]

nested_list_diagonal = []

for i in range(len(nested_list)):
    nested_list_diagonal.append(nested_list[i][i])

# This statement is a SUCCESS
assertEqual(nested_list_diagonal, [1, 5, 9])
```

**Get the diagonal of a matrix in Matlab (Note: My syntax might be off, but this is the general idea):**

```
my_matrix = [[1, 2, 3], 
             [4, 5, 6], 
             [7, 8, 9]]

my_matrix_diagonal = diag(v)

```


