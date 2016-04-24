
def power_of_difference(x, y, p=2.0):
    """Return the power of the difference of x and y
    
    Parameters
    ----------
    x, y : float
        the values to be differenced
    p : float (optional)
        the exponent (default = 2.0)
    
    Returns
    -------
    result: float
        (x - y) ** p
    """
    diff = x - y
    return diff ** p