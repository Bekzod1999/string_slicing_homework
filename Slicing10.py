def main(s,n,k):
    """
    The s string variable is given. return from index n to index k.
    Args:
        s(str): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        str: answer
    """
    if n == k:
        p = s[n]
    else:
        p = s[n:k]
    return p
x=main('codeschool', 2, 5)
print(x)