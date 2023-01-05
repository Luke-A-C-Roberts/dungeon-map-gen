#selects the strings of a list with a specific character in their substring
#may also be negated so its an inverted selection
def selector (
    l   : list[str],
    s   : str,
    N   : bool
) -> list[str]:
    if not N:
        if len(s) == 1:
            return [i for i in l if s in i]
        elif len(s) > 1:
            temp = []
            for c in s:
                temp += [i for i in l if c in i]
            return list(set(temp))
        else:
            return []
    else:
        if len(s) == 1:
            return [i for i in l if s not in i]
        elif len(s) > 1:
            temp = []
            for c in s:
                temp += [i for i in l if c not in i]
            return list(set(temp))
        else:
            return l


#creates a union of list[str]s and converts back to a list[str]
def list_union (
    l1 : list[str],
    l2 : list[str]
) -> list[str]:
    return list(set(l1).union(set(l2)))


#same but intersection
def list_intersection (
    l1 : list[str],
    l2 : list[str]
) -> list[str]:
    return list(set(l1).intersection(set(l2)))


#shorthand for a range between start and end-1
def quick_range (
    start : int,
    end   : int
) -> list[int]:
    return [i for i in range(start, end)]