for i in range(0,3):
    def isPalindrome(x):
        '''
        :type x: int
        :rtype: bool
        '''
        str_num = str(x)[::-1]            #从后往前选定字符
        if str_num == str(x):
            return True
        else:
            return False
    
    num = int(input('Pls input a number:'))
    print(isPalindrome(num))