class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        arr = ['0'] * (len(a) + 1)
        carry = False

        stop = -len(a) - 1
        for i in range(-1, stop, -1):
            if i < -len(b):
                if carry:
                    if a[i] == '1':
                        arr[i] = '0'
                    else:
                        arr[i] = '1'
                        carry = False
                else:
                    arr[i] = a[i]
            else:
                if carry:
                    if a[i] == b[i]:
                        arr[i] = '1'
                        carry = True if a[i] == '1' else False
                    else:
                        arr[i] = '0'
                else:
                    if a[i] == b[i]:
                        arr[i] = '0'
                        carry = True if a[i] == '1' else False
                    else:
                        arr[i] = '1'
        
        if carry:
            arr[0] = '1'
        
        start = 0
        while start < len(arr) - 1 and arr[start] == '0':
            start += 1
        
        return ''.join(arr[start:])
