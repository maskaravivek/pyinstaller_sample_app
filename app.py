import random

def generate_random_number(max_number):
    return random.randint(1, max_number)

if __name__ == "__main__":
    max_number = int(input("Enter the maximum allowed number: "))
    random_number = generate_random_number(max_number)
    print("Random number:", random_number)