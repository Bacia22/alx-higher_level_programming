#!/usr/bin/python3

def safe_print_list(my_list=[],x=0):
    """Print x element of alist.

    Args:
    my_list (list): The liat to print elements from:
    x(int): The number of elements of my_list to print.

    Returns:
    The number of elemens printed

    ret = 0
    for i in range(x):
    try:
    print("{}".format(my_list[i], end="")
    ret+=1
    except indexError:
    break
    print("")
    return(ret)
