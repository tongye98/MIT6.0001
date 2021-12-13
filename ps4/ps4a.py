# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

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

    #pass #delete this line and replace with your code here
    permutations = list()
    if len(sequence) == 1:
        permutations.append(sequence)
        return permutations
    else:
        assert len(sequence) > 1
        first_letter = sequence[0]
        permutations_todo = get_permutations(sequence[1:])
        for permutation_target in permutations_todo:
            # permutation_target: string; first_letteer: a character
            permutations.append(first_letter + permutation_target)
            for index in range(1,len(permutation_target)):
                a_string = permutation_target[:index] + first_letter + permutation_target[index:]
                permutations.append(a_string)
            permutations.append(permutation_target + first_letter)
        return permutations

if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
   print(len(get_permutations(example_input)))
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    #pass #delete this line and replace with your code here

