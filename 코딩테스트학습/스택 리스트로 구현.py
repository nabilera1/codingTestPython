# Python program to
# demonstrate stack implementation
# using list
# deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
# 아래 코드 말고 데크 사용하기
stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty
