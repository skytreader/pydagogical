"""
Some "exotic" sorts. Will sooner or later deprecate some scripts in clrs_3e.

Will not optimize for anything other than asymptotic time.
"""

def flipsort(numlist):
    """
    This is basically just bubble sort but with the added caveat that "bubbling"
    the biggest element leftwards affects not just the biggest element but those
    in between.

    On the surface, it seems to me that the running time is the same as as bubble
    sort (O(n^2)) but the nature of the adversarial input for this algorithm
    might be different.

    Returns the list sorted in descending order.
    """
    def flip(i):
        """
        flip the first $i$ elements of numlist. Returns the list.
        """
        sublist = numlist[0:i]
        return sublist.extend(numlist[i:len(numlist)])

    for i in range(len(numlist)):
        max_item = max(numlist[0:i])
        max_item_index = numlist.index(max_item)
        
        numlist = flip(i)

    return numlist
