class Solution:
    def isValid(self, s: str) -> bool:
        self.mystack = []
        if s == "":
            return True
        if s[0] == ")" or s[0] =="]" or s[0] == "}":
            return False
        
        for char in s:         
            if char == '(':
                self.mystack.append(')')
            elif char == '[':
                self.mystack.append(']')
            elif char == '{':
                self.mystack.append('}')
            elif (char == ')' or char == ']' or char == '}') and self.mystack:
                if self.mystack[-1] == char:
                    self.mystack.pop(-1)
                    continue 
                return False
            elif (char == ')' or char == ']' or char == '}') and not self.mystack:
                return False
        return not self.mystack



def main():
    s = "(])"
    ret = Solution().isValid(s)
    out = (ret);
    print(out)

if __name__ == '__main__':
    main()


