def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while True:
        try:
            number = int(input("Enter a number"))
        except ValueError:
            print("Input must be numeric.")
            continue
            
    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
