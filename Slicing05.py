def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return s[len(s)-n:len(s)]
x=main('codeschooluz', 3)
print(x)
