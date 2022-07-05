class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        count = len(needle)
        for i in range(len(haystack)):
            while count>0:
                if haystack[i] == needle[i-count] and haystack[i+1] == needle[(i+1)-count]:
                    req_value = i
                    break
                else:
                    req_value = -1
                    break
        
            if i == len(haystack)-1 and req_value == -1:
                return -1
            elif req_value != -1:
                return req_value
haystack = "hello"
needle = "ll"