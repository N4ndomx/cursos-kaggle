def to_smash(total_candies, n_friend =3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n_friend

# Check your answer
#q3.check()

