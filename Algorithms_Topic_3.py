# Task 1
import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Recursive file sorting script')
    parser.add_argument('source_dir', type=str, help='Path to the source directory')
    parser.add_argument('--destination_dir', type=str, default='dist', help='Path to the destination directory (default: dist)')
    args = parser.parse_args()
    return args.source_dir, args.destination_dir

def recursive_copy(source_dir, destination_dir):
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path):
            recursive_copy(item_path, destination_dir)
        else:
            _, file_extension = os.path.splitext(item)
            new_subdir = os.path.join(destination_dir, file_extension[1:])
            os.makedirs(new_subdir, exist_ok=True)
            shutil.copy(item_path, new_subdir)

def main():
    source_dir, destination_dir = parse_arguments()
    
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    recursive_copy(source_dir, destination_dir)
    print("Files copied and sorted successfully.")

if __name__ == "__main__":
    main()

# Task 2
import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Prompt user for the recursion level
    while True:
        try:
            order = int(input("Enter the recursion level (an integer >= 0): "))
            if order < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a non-negative integer.")

    # Initialize turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title(f"Koch Snowflake (Level {order})")
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    t.color("blue")

    # Draw the Koch snowflake
    for _ in range(3):
        koch_snowflake(t, order, 300)
        t.right(120)

    # Hide turtle and display
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()

