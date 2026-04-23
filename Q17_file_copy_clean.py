# Program 17: Copy Content from One File to Another (Removing Digits)

# Input source and destination filenames
source_file = input("Enter the source filename (with .txt): ")
dest_file = input("Enter the destination filename (with .txt): ")

try:
    # Open source for reading and destination for writing
    with open(source_file, "r") as f1:
        data = f1.read()

    # Create a new string without digits
    cleaned_data = ""
    for char in data:
        if not char.isdigit():
            cleaned_data += char

    # Write the cleaned data to the destination file
    with open(dest_file, "w") as f2:
        f2.write(cleaned_data)

    print("\nSuccess! Content copied and digits removed.")
    print("Check", dest_file, "for the result.")

except FileNotFoundError:
    print("Error: Source file not found.")
