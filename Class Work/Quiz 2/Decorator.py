def upper(function):
    def wrapper():
        return function().upper()
    
    return wrapper

@upper
def relay_message():
    return "warning"

print(relay_message())