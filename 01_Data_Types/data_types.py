def boolean():
    """
    Question 1 - Boolean

    Using the variable below, give it the value 'True', then print it.
    """
    # enter your code here
    staying_alive = None
    staying_alive=True
    print(staying_alive)


def integer():
    """
    Question 2 - Integer

    Create a program to accept two numbers from a user and multiply them, then print the product.
    """

    num1 = int(input("Enter first number\n"))
    num2 = int(input("Enter second number\n"))

    # enter your code here
    product=num1*num2
    print(product)

def string():
    """
    Question 3 - String

    Assign a name to the variable below and print it.
    """

    # enter your code here

    your_name = None
    your_name="Simphiwe"
    print(your_name)

def convert_to_float():
    """
    Question 4 - Float

    Convert the following integer to a float then print it.
    """

    int_num = 60

    #enter your code here
    int_num=float(60)
    print(int_num)

def all_data_types():
    """
    Question 5 - All Data Types

    Output the following sentence using the given variables.

    Welcome to the 2023 WeThinkCode_ bootcamp where True learning costs R0.00
    """

    string_one = "Welcome to the "
    string_two = " WeThinkCode_ bootcamp where "
    string_3 = " learning costs R"
    bool_condition = True
    int_year = 2023
    float_cost = 0.00

    #enter your code here
    print(str(string_one),int(int_year),str(string_two),bool(bool_condition),str(string_3),float(float_cost))

if __name__ == "__main__":
    """
    Run the entire program from here
    """
    # boolean()
    # integer()
    # string()
    # convert_to_float()
    # all_data_types()
