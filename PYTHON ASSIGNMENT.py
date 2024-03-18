def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Fibonacci sequence starts with 0 and 1
    
    # Generate Fibonacci sequence up to nth term
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence[:n]

def main():
    # Ask the user to input the value of n
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))
    
    # Generate Fibonacci sequence
    fibonacci_sequence = generate_fibonacci(n)
    
    # Print the generated Fibonacci sequence
    print("The Fibonacci sequence up to term", n, "is:", fibonacci_sequence)

if __name__ == "__main__":
    main()
    
def main():
    # Prompt the user to enter their age
    age = int(input("Please enter your age: "))
    
    # Check if the age is greater than or equal to 18
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

if __name__ == "__main__":
    main()


