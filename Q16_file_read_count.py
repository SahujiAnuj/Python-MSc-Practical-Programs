# Program 16: Count Lines, Words, and Characters in a File

# Take filename input from user
filename = input("Enter the filename (with .txt extension): ")

try:
    # Open the file in read mode
    file = open(filename, "r")
    
    lines = file.readlines()
    
    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        # Count words by splitting the line
        words = line.split()
        word_count += len(words)
        
        # Count characters (including spaces)
        char_count += len(line)

    file.close()

    # Display results
    print("\nFile Statistics:")
    print("Total Lines      :", line_count)
    print("Total Words      :", word_count)
    print("Total Characters :", char_count)

except FileNotFoundError:
    print("Error: The file was not found. Please make sure the filename is correct.")
