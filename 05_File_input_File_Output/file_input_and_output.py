def open_file(filename):
    """
    Write a python function that will open a file
    """
    #enter your code here


def append_to_file(filename, line):
    """
    Write a python function that will append another food to the file
    """
    try:
        #enter your code here
        print("Line appended successfully.")
    except FileNotFoundError:
        print("Error: file not found.")

def print_foods(filename):
    """
    Write a python function that will print the contents 19 to 23 of the file
    """
    filename = ""
    try:
        with open(filename, 'r') as f:
            #enter your code here
            return ""
    except FileNotFoundError:
        print("Error: file not found.")


if __name__ == "__main__":
    """
    Run the entire program from here
    """
    #enter your code here
        
    
    #close the file    
