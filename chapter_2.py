from collections import defaultdict

# Chapter 2: Linked Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# <!-- Problem 1 --!>

"""We can iterate through the linked list, and create a value count. Any 
value whose count exceeds one is then stored in a set. We can then iterate
through the linked list again, and remove any nodes whose values appear
in our delete set."""

def remove_dups(head: ListNode) -> ListNode:
    """Returns a linked list consisting of the nodes whose 
    values are unique."""
    hashmap = defaultdict(int)
    node = head
    while node:
        value = node.val
        hashmap[value] += 1
        node = node.next

    del_set = set()
    for value in hashmap:
        if hashmap[value] > 1:
            del_set.add(value)
        
    new_head = ListNode()
    new_node = new_head
    node = head
    while node:
        if node.val not in del_set:
            new_node.next = ListNode(val=node.val)
            new_node = new_node.next
        node = node.next
    return new_head.next

# N = Number of elements in Linked List

# Runtime: O(N)    Space Complexity: O(N)

# <!-- Problem 2 --!>

"""We can iterate through the linked list, and store each value with its 
index in a hasmap. In addition, as we iterate we can keep track of the length
of the linked list. The kth to last element is then the value of the 
hashmap whose key is length + 1 - k."""

def return_kth_to_last(head: ListNode, k:int) -> int:
    """Returns the kth to last element of the linked list."""
    hashmap = {}
    length = 0
    node = head
    while node:
        length += 1
        hashmap[length] = node.val
        node = node.next
    return hashmap[length + 1 - k]

# N = Number of elements in Linked List

# Runtime: O(N)    Space Complexity: O(N)

# <!-- Problem 3 --!>

"""To delete a node in the middle, we just have to link the previous node
to the following node."""

def delete_middle_node(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next

# Runtime: O(1)     Space Complexity: O(1)

# <!-- Problem 4 --!>

"""We can create two linked lists to represent the partition. We can then
iterate through our linked list, and add the node values to the corresponding
partition. At the end, we can join the two linked lists."""

def partition(head:ListNode, x:int) -> ListNode:
        """Returns a new linked list which is structure such that
        all nodes in the original linked list whose value is less than x appear
        before those whose value is greater than or equal to x."""
        new_head = ListNode()
        cur = new_head
        greater_head = ListNode()
        cur_greater = greater_head
        
        node = head
        while node:
            val = node.val
            if val < x:
                cur.next = ListNode(val)
                cur = cur.next
            else:
                cur_greater.next = ListNode(val)
                cur_greater = cur_greater.next
            node = node.next
        
        cur.next = greater_head.next
        return new_head.next

# N = Number of elements in Linked List

# Runtime: O(N)    Space Complexity: O(1)

# <!-- Problem 5 --!>

"""We can iterate simultaneously through both linked lists, summing the 
values of their nodes and immediately inserting it into a new linked list.
Whenever the sum is greater than 9, then we record instead value % 10, 
and we add the extra one to the following sum."""

def sum_lists(l1:ListNode, l2:ListNode) -> ListNode:
    head = ListNode()
    node = head
    carry_over = 0
    while l1 or l2:
        new_digit = carry_over
        if l1:
            new_digit += l1.val
            l1 = l1.next
        if l2:
            new_digit += l2.val
            l2 = l2.next
        carry_over = new_digit // 10
        new_digit %= 10
        node.next = ListNode(val=new_digit)
        node = node.next
    if carry_over > 0:
        node.next = ListNode(val=carry_over)
    return head.next

# N_1 = Number of elements in Linked List l1
# N_2 = Number of elements in Linked List l2

# Runtime: O(max(N_1,N_2))    Space Complexity: O(1)

# <!-- Problem 6 --!>

"""We can iterate through the linked list and store the value of each node
on a string. We can then check if the resulting string is a palindrome."""

def palindrome(head:ListNode) -> bool:
    """Returns true if the linked list is a palindrome, otherwise it returns
    false."""
    s = ""
    node = head
    while node:
        s += str(node.val)
        node = node.next
    return s == s[::-1]

# <!-- Problem 7 --!>

"""We can iterate through one of the linked lists, and store each node's 
memory address in a set. We can then go through the other linked list, and
compare the memory address until we find a match."""

def intersection(l1:ListNode, l2:ListNode) -> ListNode:
    """Returns the intersecting node of the two linked lists."""
    memory_set = set()
    node = l1
    while node:
        memory_set.add(id(node))
        node = node.next
    node = l2
    while node:
        if id(node) in memory_set:
            return node
        node = node.next  
    return None

# N_1 = Number of elements in Linked List l1
# N_2 = Number of elements in Linked List l2

# Runtime: O(max(N_1,N_2))    Space Complexity: O(N_1)

# <!-- Problem 8 --!>

def loop_detection(head:ListNode) -> ListNode:
    """Returns the node at the beginning of the loop in head (if one exists)"""
    memory_set = set()
    node = head
    while node:
        if id(node) in memory_set:
            return node
        memory_set.add(id(node))
        node = node.next
    return None

# N = Number of elements in Linked List

# Runtime: O(N)    Space Complexity: O(N)