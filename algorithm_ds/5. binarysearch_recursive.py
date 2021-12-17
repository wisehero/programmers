def binarysearch(L, x, lower, upper):
    if lower > upper:
        return -1
    mid = (lower + upper)

    if x == L[mid]:
        return

    elif x < L[mid]:
        return binarysearch(L, x, lower, mid - 1)
    else:
        return binarysearch(L, x, mid + 1, upper)
