# STACK #

A stack is a linear data structure that stores items last in - first out. 
Elements are added ad removed from the same end, and that end only.

These operations are often called push or pop.
Python operations for a stack:
	- empty() – Returns whether the stack is empty – Time Complexity: O(1)
	- size() – Returns the size of the stack – Time Complexity: O(1)
	- top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
	- push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
	- pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

Can be implementet with python array and replacing push() with append.

It is faster to use deque from collections.

"""
from collectoins import deque
stack = deque()
stack.append('a')
stack.pop()

""" 