def write_numbers_to_file(filename):
    """
    Writes numbers from 1 to 100 into a file
    and returns the list of numbers.
    """
    numbers = []

    with open(filename, "w") as file:
        for i in range(1, 101):
            file.write(f"{i}\n")
            numbers.append(i)

    return numbers

def write_numbers_to_file(filename):

    numbers = []

    try:
        with open(filename, "w") as file:
            for i in range(1, 101):
                file.write(f"{i}\n")
                numbers.append(i)

    except FileNotFoundError:
        print("Error: The specified file path was not found.")

    except PermissionError:
        print("Error: Permission denied. You do not have access to write this file.")

    except OSError as error:
        print(f"Unexpected OS error occurred: {error}")

    return numbers