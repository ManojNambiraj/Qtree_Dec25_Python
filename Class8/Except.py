# Exception Handling:

try:
    print("xyz")

except NameError:
    print("Name Error")
except ZeroDivisionError:
    print("Zero 0 Error")
except:
    print("Something went wrong")
finally: # else
    print("Nothing went wrong")