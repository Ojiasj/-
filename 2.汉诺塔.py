def hanni(n, A, B, C):
    """
    :param n:目标规模
    :param A:起始位置
    :param B:经过位置
    :param C:目标位置
    :return:
    """
    if n > 0:
        hanni(n - 1, A, C, B)
        print("%s->%s" % (A, C))
        hanni(n - 1, B, A, C)


hanni(4, "A", "B", "C")
