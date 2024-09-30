class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        bracket_pair={')':'(','}':'{',']':'['}
        for char in s:
            if char in bracket_pair:
                if char in bracket_pair:
                    if not stack or stack.pop() !=bracket_pair[char]:
                        return False
                else:
                    stack.append(char)
        return len(stack) == 0







    



  

