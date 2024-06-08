# Python Term 1 Week 6 Saturday Class

# if-else practice activity

## Building a calculator
Build a calculator that takes 3 inputs from the user
2 inputs as numbers (floats)

# Lists
Composite Data Type, meaning multiple data types can be stored in one variable. Each piece is called an element.

# Loops

Like Post Malone describes, "Run away, But we're running in circles"
Used to repeat a block of code multiple times until a certain condition is met.

DRY Coding Principle: Don't Repeat Yourself

Example: Counting coins in your piggy bank

'If' condition would decide whether or not to run the intended block. 
Whereas, 'Loops' would decide how many times the user wants to run the intended block

# While Loop
While the condition is met, keep executing the intended block. If not met, skip the block.

Things to consider
    - Program can enter the loop
    - Program can exit the loop
## Range
It's a pre-defined function that generates a sequence of numbers.

Useful: Loops for iterating a specific number of times over a sequence of numbers. 
syntax:
range(start, stop, step)
range (1, 5, 2) default step is 1
range(5) stops at 5 by default, if no start number is defined. 


## For Loop
For each item in a sequence, execute the intended statements. 

for variable_name in sequence:
    stmts

## Practice example 1
Finding the sum of the first ten numbers (1,2,3,...10)

## Practice Example 2

Find the largest number in the list
list = [3, 41, 12, 9, 74, 15]

# Loops Control Statements
Control the flow of the loops, terminate the loop early if you want or skip over some iteration.

## Break statement
Terminates loop immediately, moves to the next statement after the loop

## Continue statement
Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

## Nested loops
A loop inside another loops! Inception.
Useful for running over multi-dimensional structures, like MATRIX.

## Practice Example 1
Print a right-angled Triangle patter of stars

*
**
***
****
*****

## Practice Example 2
Count the occurence of a letter in a list

# enumerate() Function
Used to access the index and the value of the elements of the list. 
Use two variables in for loop.
