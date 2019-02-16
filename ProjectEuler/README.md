# Extra Credit

## 44-550

## ??? points

The best way to get better at coding is to write code (go figure!)
This bonus assignment is designed to get you as much practice solving problems and writing C code as possible.

[Project Euler](https://projecteuler.net) is a collection of problems that range from quite easy to very difficult.  You are to write individual programs to solve as many of these problems as possible.

Each problem you solve is worth 0.5 points of extra credit in the Assignments category.  In order to receive credit for a solution, you must adhere to the following rules:

* The main file for the solution must be named `p###.c` (where `###` is the number of the problem it is solving).  For example, your solution to Problem 1 would be contained in `p001.c`, and `p015.c` would have your solution to problem 15.
* Each .c file must contain a comment header with the required information (see the course website).
* You may (and should) use multiple files to write reusable code (lots of these require prime numbers, for example).  Any function you write (whether in the main .c file or in a "library") must have a comment block next to the prototype with the required information (specified on the course website).
* You must provide a `Makefile` with rules to build each of your solutions.  To compile the solution for problem 10, the grader should be able to run `make p010`, which should take the appropriate steps to compile the executable, which must be named `p010`
* You must append a table to this README file that contains the problem number and your reported solution to the problem.
* Your solution must be fast (run in fewer than 30 seconds).  

Given the way the problems build, you should have at most one problem solved per commit to this repository.

This extra credit is goverened by the same Academic Integrity rules as regular assignments.  

You must understand that the grader and the instructor of this course have not solved all of the problems on this website; it is a test of your problem solving skills and a chance to practice coding.  Please respect the spirit of this assignment.  At any point the instructor may ask you to explain your solution verbally (or may ask you to present a particularly clever solution to the class).  You need to thoroughly understand all code you commit to this repository.
