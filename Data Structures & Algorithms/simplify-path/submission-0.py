class Solution:
    def simplifyPath(self, path: str) -> str:
        # first replace all '//' and '///' with '/' since they are technically the same
        
        # then make sure that the path begins with '/'

        # split the string (/)

        # then once split, iterate through the array and pop from the stack when we encounter
        # '..'


        path = path.split('/')
        print(path)
        res = ''
        stack = []

        for directory in path:
            if stack and directory == '..':
                stack.pop()
            elif directory == '.' or directory == '' or (stack == [] and directory == '..'):
                continue
            else:
                stack.append(directory)

        res = '/' + '/'.join(stack)

        return res