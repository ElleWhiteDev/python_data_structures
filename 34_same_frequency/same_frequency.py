def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    first_num = str(num1)
    second_num = str(num2)
    return {num: first_num.count(num) for num in first_num} == {num: second_num.count(num) for num in second_num}
