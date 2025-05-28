def add_ten(number):  
    try:  
        return number + 10  
    except TypeError:  
        return "Error: Give me a number, not nonsense."  

print(add_ten("hello"))  # Output: Error message  