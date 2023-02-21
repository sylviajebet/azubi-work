# Python program to draw a christmas tree

# Function to draw the stars to form the tree
def draw_tree(space, star):
    print((' ' * int(space/2)) + ('*' * star) + (' ' * int(space/2)))

# Main function
def main():
    # Define the space and start with one star 
    star = 1; space = 10; rows = 6
    for i in range(rows):
        draw_tree(space, star)
        space -= 2
        star += 2

    # Create a stem with hashes
    stem = 2
    for i in range(stem):
        print((' ' * 4) + ('#' * 3) + (' ' * 4))

if __name__ == "__main__":
    main()