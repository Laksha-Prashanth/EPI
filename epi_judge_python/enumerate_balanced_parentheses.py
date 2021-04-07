from typing import List

from test_framework import generic_test, test_utils

'''
1
()
2
()(), (())
3
()()(), ((())), ()(()), (())(), (()())

() () ()
() (())
(()())
((()))
(())()

4
()()()()
()()(())
()(())()
()((()))
(()()())
(()(()))
(((())))
((())())

 '(())(())', 

2
0,0
(())

'''
def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    '''
    result =  [ ]
    (())
    ()()
    2
    (2,2,"")
        (1,2,()
            (0,2,(()
            (1,1,())
                (0,1,()())

    '''

    def helper(left: int, right: int, solution: str, result: List[str]) -> None:
        
        if left < 0 or right < 0 or right < left:
            return

        if left == 0 and right == 0:
            result.append(solution)
        
        if left > 0:
            # add left
            helper(left-1, right, solution+"(", result)
        
        if right > 0:
            helper(left, right-1, solution+")", result)
        

    result = []
    helper(num_pairs, num_pairs, "", result)

    return list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
