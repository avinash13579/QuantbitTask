def calculate_sum_from_file(file_path):
    total_sum = 0  # Step 1: Initialize a variable to store the sum of integers.
    
    try:
        with open(file_path, 'r') as file:  # Step 2: Open the file in read mode.
            for line in file:  # Step 3: Iterate through each line in the file.
                total_sum += int(line.strip())  # Step 4: Convert the line to an integer and add it to the sum.
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return None  # Step 5: Handle the case when the file is missing.
    except ValueError:
        print("Error: The file contains non-integer values.")
        return None  # Step 6: Handle cases where the file contains invalid data.
    
    return total_sum  # Step 7: Return the total sum.

# Test the function
file_path = 'integers.txt'  # Path to the input file containing integers.
output = calculate_sum_from_file(file_path)

if output is not None:
    print("Sum of integers in the file:", output)
