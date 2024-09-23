def to_latex(data):
    """Converts the input data to LaTeX format based on its type."""
    if not data:  # Check if data is empty
        return "No data provided."

    # Check if the input is a string
    if type(data) is str:
        return f"${data}$"

    # Check for 1D data (list of numbers or strings)
    if type(data) is list and all(type(i) in (str, float, int) for i in data):
        latex = " \\\\ ".join(map(str, data))  # Use \\\\ for new lines in a column
        return f"${{\\begin{{bmatrix}} {latex} \\end{{bmatrix}}}}$"

    # Check for 2D data (list of lists)
    elif type(data) is list and all(type(i) is list for i in data):
        latex = " \\\\ ".join(" & ".join(map(str, row)) for row in data)
        return f"${{\\begin{{bmatrix}} {latex} \\end{{bmatrix}}}}$"

    # Handle N-dimensional arrays (nested lists)
    elif type(data) is list:
        flat_data = []

        def flatten(nested_list):
            """Recursively flatten a nested list."""
            for item in nested_list:
                if type(item) is list:
                    flatten(item)
                else:
                    flat_data.append(item)

        flatten(data)  # Flatten the N-dimensional data

        # Convert flat data to LaTeX matrix format
        latex = " & ".join(map(str, flat_data))
        return f"${{\\begin{{bmatrix}} {latex} \\end{{bmatrix}}}}$"

    return "Unsupported data type."
