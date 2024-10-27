from collections import defaultdict

# Chapter 1: Arrays and Strings

# <!-- Problem 1 --!>

# Assume that the string consists only of lower case alphabetical characters.

"""If a string has all unique characters, no character repeats. 
This means that if we construct a set consisting of the characters
in the string, then the length of that set equals the length of the string
if and only if the string has all unique characters."""

def is_unique(s:str) -> bool:
    """Returns true if s has no repeated letters. Otherwise, returns False."""
    s_set = set(s)
    return len(s_set) == len(s)

# Runtime: O(len(s))    Space Complexity: O(len(s))

# What if we cannot use any additional data structures?

"""We sort the string. Then any repeated characters will be adjacent
to one another in the sorted string."""

def alt_is_unique(s:str) -> bool:
    """Returns True if s has no repeated letters. Otherwise, returns False."""
    s_sorted = sorted(s)
    for i in range(len(s)-1):
        if s_sorted[i] == s_sorted[i+1]:
            return False
    return True

# Runtime: O(len(s)*log(len(s)))    Space Complexity: O(len(s))

# <!-- Problem 2 --!>

# Assume that the strings consist only of lower case alphabetical characters.

"""A permutation of a string preserves the character count. This tells us that
if the character count of two strings is identical then one of the
strings is a permutation of the other."""

def check_permutation(s:str, t:str) -> bool:
    """Returns True if t is a permutation of s. Otherwise, returns False."""
    if len(s) != len(t):
        return False
    hashmap = defaultdict(int)
    for i in range(len(s)):
        hashmap[s[i]] += 1
        hashmap[t[i]] -= 1
    return set({0}) == set(hashmap.values())

# Runtime: O(len(s))    Space Complexity: O(1) (only 26 lowercase letters)

# <!-- Problem 3 --!>

# Assume that the string consists only of lower case alphabetical characters.

"""For a string to be a palindrome (or a permutation of one), the count 
of any letter character must be even except for when the total count 
of letters is odd; in this case, one of the letter counts is allowed 
to be odd."""

def palindrome_permutation(s:str) -> bool:
    """Returns True if s is a permutation of a palindrome. Otherwise, returns 
    False."""
    hashmap = defaultdict(int)
    count = 1 - (len(s) % 2)
    for c in s:
        hashmap[s] += 1
    for c in hashmap:
        if hashmap[c] % 2 != 0:
            count += 1
            if count > 1:
                return False
    return True

# Runtime: O(len(s))    Space Complexity: O(1) (only 26 lowercase letters)

# <!- Problem 5 --!>

# Assume that the strings have no whitespace.

"""For two strings to be at most one edit away, then their lengths must 
differ by at most one. If the strings have the same lengths, we can
compare character by character starting from the beginning of the strings.

If the lengths of the strings differ by one, then we can compare character by
character, but if we run into a mismatch, we jump by one on the string
with the longest length, and continue comparing characters."""

def one_away(s:str, t:str) -> bool:
    """Returns True if s and t are at most one edit away. Otherwise,
    returns False."""
    if abs(len(s)-len(t)) > 1:
        return False
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            if len(s) > len(t):
                return s[i+1 :] == t[i :]
            if len(s) < len(t):
                return s[i :] == t[i+1 :]
            else:
                return s[i+1:] == t[i+1:]  
    return True

# Runtime: O(len(s))    Space Complexity: O(len(s))

# <!-- Problem 6 --!>

def string_compression(s:str) -> str:
    """Compresses string and returns either the original string or 
    the compressed string depending on which one has the smallest length."""
    new_s = s[0]
    count = 1
    last_c = s[0]
    for c in s[1:]:
        if c == last_c:
            count += 1
        else:
            new_s += str(count) + c
            count = 1
            last_c = c
    new_s += str(count)
    if len(new_s) < len(s):
        return new_s
    else:
        return s

# Runtime: O(len(s))    Space Complexity: O(len(s))

# <!-- Problem 7 --!>

# Assume that the rotation is clockwise

"""Notice that we can achieve a rotation by 90 degrees CW by first flipping
the order of the entries row-wise:
    [a_(0,0) a_(0,1) ... a_(0,n-1)] -> [a_(0,n-1) ... a_(0,1) a_(0,0)]
and then exchanging the elements like this:
                    a_(i,j) <-> a(n-1-j,n-1-i)                      """

def rotate_matrix(matrix:list[list[int]]) -> None:
    """Rotates matrix by 90 degrees clockwise."""
    n = len(matrix)
    for i in range(n):
        matrix[i].reverse()
    for row in range(n):
        for col in range(n-row):
            x = matrix[row][col]
            y = matrix[n-1-col][n-1-row]

            matrix[row][col] = y
            matrix[n-1-col][n-1-row] = x

# Runtime: O(len(matrix)*len(matrix))    Space Complexity: O(1)

# <!-- Problem 8 --!>

def zero_matrix(matrix:list[list[int]]) -> None:
    """Sets the row and column of any zero element of the matrix to zero."""
    m = len(matrix)
    n = len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    for row in range(m):
        for col in range(n):
            if matrix[row][col] != 0:
                continue
            zero_rows.add(row)
            zero_cols.add(col)

    for row in zero_rows:
        matrix[row] = [0] * n
        
    for col in zero_cols:
        for row in range(m):
            matrix[row][col] = 0

# Runtime: O(m*n)    Space Complexity: O(m+n)

# <!-- Problem 9 --!>

"""If s is a rotation of t, then there exists i in range(len(s)) such that
s[i :] + s[: i] == t. In other words, t is a substring of 
s[: i]+s[i: ]+s[ :i]+s[i: ] = s + s. Note that to avoid false positives,
we first check if the length of s equals the length of t."""

def string_rotation(s:str,t:str) -> bool:
    """Returns True if s is a rotation of t. Otherwise, returns False."""
    if len(s) != len(t):
        return False
    return t in s+s

# Runtime: O(len(s))    Space Complexity: O(len(s))