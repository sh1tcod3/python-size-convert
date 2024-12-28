def size_converter():
    print("Welcome to the Rich Python Size Converter!")
    print("Available sizes:")
    sizes = [
        "Bytes",
        "Kilobytes (KB)",
        "Megabytes (MB)",
        "Gigabytes (GB)",
        "Terabytes (TB)",
        "Petabytes (PB)"
    ]

    for i, size in enumerate(sizes, start=1):
        print(f"{i}. {size}")

    def convert_size(value, from_unit, to_unit):
        size_units = {
            "Bytes": 1,
            "Kilobytes": 1024,
            "Megabytes": 1024 ** 2,
            "Gigabytes": 1024 ** 3,
            "Terabytes": 1024 ** 4,
            "Petabytes": 1024 ** 5,
        }
        value_in_bytes = value * size_units[from_unit]
        result = value_in_bytes / size_units[to_unit]
        return result

    try:
        from_unit_index = int(input("Enter the number of the size you want to convert from: ")) - 1
        if from_unit_index not in range(len(sizes)):
            print("Invalid selection for the input unit.")
            return

        to_unit_index = int(input("Enter the number of the size you want to convert to: ")) - 1
        if to_unit_index not in range(len(sizes)):
            print("Invalid selection for the target unit.")
            return

        value = float(input(f"Enter the size in {sizes[from_unit_index]}: "))

        # Perform conversion
        from_unit = sizes[from_unit_index].split(" ")[0]
        to_unit = sizes[to_unit_index].split(" ")[0]
        result = convert_size(value, from_unit, to_unit)

        print(f"{value} {sizes[from_unit_index]} is equal to {result:.2f} {sizes[to_unit_index]}")
    except ValueError:
        print("Invalid input. Please enter numeric values for size and valid options for units.")
    except Exception as e:
        print(f"An error occurred: {e}")

    choice = input("Do you want to convert another size? (yes/no): ").lower()
    if choice == "yes":
        size_converter()
    else:
        print("Thank you for using the Rich Python Size Converter. Goodbye!")

size_converter()
