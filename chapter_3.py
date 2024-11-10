# Chapter 3: Stacks and Queues

# <!-- Problem 1 --!>

"""One way we can use a single list to implement three stacks is by
using primes indices. The first three prime numbers are 2, 3, and 5. 

For stack number one, we can stores its values at locations list[2^n] for n
a natural number. Similarly, we can store the values of stack number two
at locations list[3^n], and the values of stack number three at listp[5^p].
The reason why we will not run into any problems is because 2, 3, and 5 are
primes. 

To see this let p and p' be distinct primes. Then the equation p = n * p' has 
no solutions for n a natural number. This is because if such a solution 
existed, then p' would divide p which would mean that p is not a prime."""

# <!-- Problem 2 --!>

"""We can construct stacks in the same way we constructed Linked Lists; 
in other words, by using class attributes val and next to keep track
of the chain of values. Since we also want to keep track of the minimum value
in a given chain, what we can do is compare every new value to the current
minimum value and record the smallest out of the two. This way we have
O(1) access to a chain's minimum value at all times (note that when we
remove the top element from the stack, we must adjust the stack min 
appropiately)."""

class StackMin:

    def __init__(self):
        self.val = None
        self.min = None
        self.next = None

    def push(self, val: int) -> None:
        cur_top = StackMin()
        cur_top.val = self.val
        cur_top.min = self.min
        cur_top.next = self.next

        self.val = val
        if self.min is not None:
            self.min = min(self.val, self.min)
        else:
            self.min = self.val
        self.next = cur_top

    def pop(self) -> None:
        self.val = self.next.val
        self.min = self.next.min
        self.next = self.next.next
        
    def top(self) -> int:
        return self.val

    def getMin(self) -> int:
        return self.min

# N = Number of elements in stack

# Runtime: O(1)    Space Complexity: O(N)

"""Alternatively, we can construct a stack by using a list. Since we
also have to keep track of the minimum value in the stack, we create 
an additional list where we store the minimum values of the chain and the number 
of times this minimum value appears in the stack without a lower number
appearing (and thus replacing it as a new minimum of the stack). This way,
whenever we remove the top element of the stack, we can easily modify 
the minimum value list."""

class StackMin:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            cur_min = self.minStack[-1][0]
            if val < cur_min:
                self.minStack.append([val, 1])
            elif val == cur_min:
                self.minStack[-1][-1] += 1
        else:
            self.minStack.append([val, 1])
        
    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1][0]:
            if self.minStack[-1][-1] > 1:
                self.minStack[-1][-1] -= 1
            else:
                self.minStack.pop()
        self.stack.pop()
 
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1][0]

# N = Number of elements in stack

# Runtime: O(1)    Space Complexity: O(N)
