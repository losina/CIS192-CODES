""" CIS 192 Python Programming 
    Do not distribute. Collaboration is NOT permitted.
"""

# Pro tip: think long and hard about testing your code.
# In this assignment, we aren't giving you example function calls.
import copy
def my_sort(lst):
    ''' Return a sorted copy of a list. Do not modify the original list. Do
    not use Python's built in sorted method or [].sort(). You may use
    any sorting algorithm of your choice.
    '''
    sorted = copy.deepcopy(lst)
    quick_sort(sorted, 0, len(sorted) - 1)
    return sorted 
def quick_sort(lst, l, h):
    if l < h:
        mid = partition(lst, l, h)
        quick_sort(lst, l, mid)
        quick_sort(lst, mid + 1, h)
def partition(lst, l, h):
    pivot = lst[(l + h) // 2]
    i, j = l - 1, h + 1
    while True: 
        i += 1
        j -= 1 
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1

        if i >= j:
            return j
        lst[i], lst[j] = lst[j], lst[i]

def sort_dict(d):
    ''' Sort a dictionary by value. The function should return
    (not print) a list of key, value tuples, in the form (key, value).
    '''
    lst = [(k, v) for k, v in d.items()]
    lst.sort(key=lambda x : x[1])
    return lst

def prefixes(seq):
    ''' Create a generator that yields all the prefixes of a 
    given sequence. Extra credit will be rewarded for doing this 
    in a single line.
    '''
    return [seq[:i] for i in range(0, len(seq) + 1)]


def suffixes(seq):
    ''' Create a generator that yields all the suffixes of a 
    given sequence. Extra credit will be rewarded for doing this 
    in a single line.
    '''
    return [seq[i:] for i in range(0, len(seq) + 1)]

def slices(seq):
    ''' Create a generator that yields all the slices of a 
    given sequence. Extra credit will be rewarded for doing this
    in a single line.
    '''
    return [seq[i:j] for i in range(0, len(seq)) for j in range(0, len(seq) + 1) if i < j or (i == 0 and j == 0)]


# HALF WAY POINT! Wahoo!

def extract_and_apply(l, p, f):
    '''
    Implement the function below in a single line:

        def extract_and_apply(l, p, f):
            result = []
            for x in l:
                if p(x):
                    result.append(f(x))
            return result

    where l is a list, p is a predicate (boolean) and f is a function.
    '''
    return [f(x) for x in l if p(x)]

def my_reduce(function, l, initializer=None):
    '''Apply function of two arguments cumulatively to the items of list l, from left to right,
    so as to reduce l to a single value. This is equivalent to the 'fold' function from CIS 120.
    If the optional initializer is present, it is placed before the items of l in the calculation, 
    and serves as a default when the sequence is empty. 
    If initializer is not given and sequence contains only one item,
    the first item is returned. You may assume that if no initializer is given, the sequence will not
    be empty.
    '''
    if len(l) == 0:
        return initializer

    if len(l) == 1 and not initializer:
        return l[0]

    prev = function(initializer, l[0]) if initializer else l[0]
    return my_reduce(function, l[1:], prev)


 
class BSTree(object):
    ''' Implement a binary search tree.
    See here: http://en.wikipedia.org/wiki/Binary_search_tree
    or https://www.seas.upenn.edu/~cis120/current/notes/120notes.pdf
    The examples in the test file illustrate the desired behavior.

    Each method you need to implement has its own docstring
    with further instruction. You'll want to move most of the
    implementation details to the Node class below.
    '''

    def __init__(self):
        self.root = None
        self.num = 0

    def __str__(self):
        ''' Return a representation of the tree as (left, elem, right)
        where elem is the element stored in the root, and left and right
        are the left and right subtrees (which print out similarly).
        Empty trees should be represented by underscores. Do not include spaces.
        '''
        if not self.root:
            return "(_,_,_)"
        return str(self.root)

    def __len__(self):
        ''' Returns the number of nodes in the tree.'''
        return self.num

    def __contains__(self, element):
        ''' Finds whether a given element is in the tree.
        Returns True if the element is found, else returns False.
        '''
        if not self.root:
            return False 
        return self.root.find_child(element)

    def insert(self, element):
        ''' Insert a given value into the tree.
        Our implementation will allow duplicate nodes. The left subtree
        should contain all elements <= to the current element, and the
        right subtree will contain all elements > the current element.
        '''
        self.num += 1
        if not self.root:
            self.root = Node(element)
        else:
            self.root.insert(element)

    def elements(self):
        ''' Return a list of the elements visited in an inorder traversal:
        http://en.wikipedia.org/wiki/Tree_traversal
        Note that this should be the sorted order if you've inserted all
        elements using your previously defined insert function.
        '''
        if not self.root:
            return []
        result = []
        self.root.traverse(result)
        return result


class Node(object):
    ''' A Node of the BSTree.
    Important data attributes: value (or element), left and right.
    '''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def traverse(self, lst):
        if self.left:
            self.left.traverse(lst)
        lst.append(self.val)
        if self.right:
            self.right.traverse(lst)

    def find_child(self, val):
        if self.val == val:
            return True
        elif self.val > val and self.left:
            return self.left.find_child(val)
        elif self.val < val and self.right:
            return self.right.find_child(val)
        return False 

    def insert(self, val):
        if self.val >= val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)
                
    def __str__(self):
        result = "("
        result += str(self.left) if self.left else "_"
        result += "," + str(self.val) + ","
        result += str(self.right) + ")" if self.right else "_)"
        return result 
