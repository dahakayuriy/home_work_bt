#1
def oops():

    my_list = [1, 2, 3]
    print(my_list[4])

def handle_exception():
    try:

        oops()
    except IndexError as e:
        print(f"An error of type IndexError: {e}")
    except KeyError as e:
        print(f"An error of type KeyError: {e}")
    else:
        print("The operation was successful")


handle_exception()

#2
def calculate_square_divided_by_b():
    try:
    
        a = float(input("Enter number a: "))
        b = float(input("Enter the number b: "))
        
    
        result = a**2 / b
        return result
    except ValueError:
     
        print("Error: The entered data must be numbers.")
    except ZeroDivisionError:
  
        print("Error: Division by zero is not possible.")
    except Exception as e:
   
        print(f"Error: {e}")


result = calculate_square_divided_by_b()
if result is not None:
    print(f"Result: {result}")
else:
    print("The operation failed.")