def main(s,n):
    """
    The s string variable is given. return all characters except n characters at the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    
#     if n < 0:
#         k = s[0:len(s)+n]
#     else:
#         k = s[0:len(s)-n] 
#     return k
# x=main('apple', 1)
# print(x)

    
        
    return s[:-n]
x=main('cd', 1)
print(x)