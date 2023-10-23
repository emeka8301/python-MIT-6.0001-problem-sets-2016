# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import random

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    
    
    '''
    
    if len(sequence)==1:
        return sequence
    else:
        permutation=[]
        for i in range(len(sequence)):
            results= get_permutations(sequence[0:i]+sequence[i+1:])
            for j in results:
                permutation.append(sequence[i]+j)
        return permutation

    pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
    print(random.choice(get_permutations('aEiou'))[0])
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

