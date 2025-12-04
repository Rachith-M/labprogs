

try:
    row, col = map(int, input("Enter your move (row and column 0-2, space separated): ").split())
    if(0<=row<=2 and 0<=col<=2):
        pass
    else:
        raise ValueError
    
except ValueError:
    print("Invalid input. Please enter two numbers between 0 and 2.")
