import re 

def process_matrix_data(matrix):
    """
    Process an n×n matrix of data containing random text, headings, and formulas.
    
    Each cell in the matrix is checked to determine if it is:
    - A heading (if the string is in uppercase),
    - A mathematical formula (detected by a formula-checking function),
    - Regular text.
    
    The processed data is returned with corresponding labels for each type.
    """
    processed_data = []  # Initialize list to store processed rows

    for row in matrix:
        row_data = []  # Initialize list to store processed cells in the current row
        for cell in row:
            if isinstance(cell, str):  # Check if the cell contains a string
                if cell.isupper():  # Check if the string is a heading
                    row_data.append(f"Heading: {cell}")
                elif is_formula(cell):  # Check if the string is a formula
                    latex_formula = convert_to_latex(cell)  # Convert formula to LaTeX
                    row_data.append(f"Formula (LaTeX): {latex_formula}")
                else:  # Treat the string as regular text
                    row_data.append(f"Text: {cell}")
            else:  # Handle non-string data
                row_data.append(f"Unknown Data: {cell}")
        processed_data.append(row_data)  # Add the processed row to the final list

    return processed_data
  
 def create_nxn_matrix(n):
    """Create a dynamic n×n matrix based on user input."""
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            user_input = input(f"Enter data for cell ({i+1}, {j+1}): ")
            row.append(user_input)
        matrix.append(row)
    return matrix

def is_formula(data):
    """Detect if a string is a mathematical formula by simple regex patterns."""
    formula_patterns = [r'\d+', r'[=+\-*/^]', r'[a-zA-Z]\(', r'\)', r'\sin', r'\cos']  # Simplified patterns
    for pattern in formula_patterns:
        if re.search(pattern, data):
            return True
    return False

def convert_to_latex(formula):
    """Convert mathematical formula to LaTeX format."""
    latex_formula = formula.replace('^', '**')  # Handle exponents
    latex_formula = latex_formula.replace('*', '\\cdot ')  # Handle multiplication
    latex_formula = latex_formula.replace('=', '\\equiv ')  # Handle equality
    return f"${latex_formula}$"  # Encapsulate in LaTeX math mode

def process_data_recursive(data, depth=1):
    """Recursively process n-dimensional data."""
    processed_data = []

    if isinstance(data, list):  # If it's a list, recurse further
        for element in data:
            processed_data.append(process_data_recursive(element, depth + 1))
    else:
        # Base case: process individual elements (text, heading, or formula)
        if isinstance(data, str):
            if data.isupper():  # Assume uppercase strings are headings
                return f"{'  ' * depth}Heading: {data}"
            elif is_formula(data):  # Detect if it's a formula
                latex_formula = convert_to_latex(data)
                return f"{'  ' * depth}Formula (LaTeX): {latex_formula}"
            else:
                return f"{'  ' * depth}Text: {data}"
        else:
            return f"{'  ' * depth}Unknown Data: {data}"
    
    return processed_data

def create_nd_matrix(dimensions, depth=0):
    """Recursively create an n-dimensional matrix based on user input."""
    if depth >= len(dimensions):
        # Base case: collect user input at the deepest level
        return input(f"Enter data for depth {depth + 1}: ")

    matrix = []
    for i in range(dimensions[depth]):
        print(f"Entering data for dimension {depth + 1}, index {i + 1}")
        matrix.append(create_nd_matrix(dimensions, depth + 1))  # Recurse for the next level

    return matrix

