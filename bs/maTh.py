class maTh:
    """A class to perform various mathematical operations."""

    @staticmethod
    def add(alpha, beta):
        """This function adds two numbers or two lists element-wise."""
        is_alpha_list = type(alpha) == list
        is_beta_list = type(beta) == list

        if is_alpha_list and is_beta_list:
            if len(alpha) != len(beta):
                return "Lists must be of the same length"
            result = []
            for i in range(len(alpha)):
                result.append(alpha[i] + beta[i])
            return result
        elif not is_alpha_list and not is_beta_list:
            return alpha + beta
        else:
            return "Both inputs must be numbers or lists of the same length"

    @staticmethod
    def subtract(alpha, beta):
        """This function subtracts two numbers or two lists element-wise."""
        is_alpha_list = type(alpha) == list
        is_beta_list = type(beta) == list

        if is_alpha_list and is_beta_list:
            if len(alpha) != len(beta):
                return "Lists must be of the same length"
            result = []
            for i in range(len(alpha)):
                result.append(alpha[i] - beta[i])
            return result
        elif not is_alpha_list and not is_beta_list:
            return alpha - beta
        else:
            return "Both inputs must be numbers or lists of the same length"

    @staticmethod
    def multiply(alpha, beta):
        """This function multiplies two numbers or two lists element-wise."""
        is_alpha_list = type(alpha) == list
        is_beta_list = type(beta) == list

        if is_alpha_list and is_beta_list:
            if len(alpha) != len(beta):
                return "Lists must be of the same length"
            result = []
            for i in range(len(alpha)):
                result.append(alpha[i] * beta[i])
            return result
        elif not is_alpha_list and not is_beta_list:
            return alpha * beta
        else:
            return "Both inputs must be numbers or lists of the same length"

    @staticmethod
    def divide(alpha, beta):
        """This function divides two numbers or two lists element-wise."""
        is_alpha_list = type(alpha) == list
        is_beta_list = type(beta) == list

        if is_alpha_list and is_beta_list:
            if len(alpha) != len(beta):
                return "Lists must be of the same length"
            result = []
            for i in range(len(alpha)):
                if beta[i] != 0:
                    result.append(alpha[i] / beta[i])
                else:
                    result.append("Cannot divide by zero")
            return result
        elif not is_alpha_list and not is_beta_list:
            if beta != 0:
                return alpha / beta
            else:
                return "Cannot divide by zero"
        else:
            return "Both inputs must be numbers or lists of the same length"

    @staticmethod
    def modulus(alpha, beta):
        """This function returns the modulus of two numbers or two lists element-wise."""
        is_alpha_list = type(alpha) == list
        is_beta_list = type(beta) == list

        if is_alpha_list and is_beta_list:
            if len(alpha) != len(beta):
                return "Lists must be of the same length"
            result = []
            for i in range(len(alpha)):
                result.append(alpha[i] % beta[i])
            return result
        elif not is_alpha_list and not is_beta_list:
            return alpha % beta
        else:
            return "Both inputs must be numbers or lists of the same length"

    @staticmethod
    def remainder(alpha, beta):
        """This function returns the remainder of two numbers or two lists element-wise."""
        is_alpha_list = type(alpha) == list
        is_beta_list = type(beta) == list

        if is_alpha_list and is_beta_list:
            if len(alpha) != len(beta):
                return "Lists must be of the same length"
            result = []
            for i in range(len(alpha)):
                result.append(alpha[i] % beta[i])  # In Python, % is the remainder operator
            return result
        elif not is_alpha_list and not is_beta_list:
            return alpha % beta
        else:
            return "Both inputs must be numbers or lists of the same length"

    @staticmethod
    def exponent(alpha, beta):
        """This function raises a number to the power of another number or does so element-wise for lists."""
        is_alpha_list = type(alpha) == list
        is_beta_list = type(beta) == list

        if is_alpha_list and is_beta_list:
            if len(alpha) != len(beta):
                return "Lists must be of the same length"
            result = []
            for i in range(len(alpha)):
                result.append(alpha[i] ** beta[i])
            return result
        elif not is_alpha_list and not is_beta_list:
            return alpha ** beta
        else:
            return "Both inputs must be numbers or lists of the same length" 

    @staticmethod
    def square(value):
        """Calculate the square of a number or each element in a list."""
        is_list = type(value) == list
        if is_list:
            return [x ** 2 for x in value]
        return value ** 2

    @staticmethod
    def sq_root(value):
        """Calculate the square root of a number or each element in a list."""
        is_list = type(value) == list
        if is_list:
            return [x ** 0.5 for x in value if x >= 0]
        return value ** 0.5 if value >= 0 else "Cannot compute square root of a negative number"

    @staticmethod
    def nth_root(value, n):
        """Calculate the nth root of a number or each element in a list."""
        is_list = type(value) == list
        if is_list:
            return [x ** (1/n) for x in value]
        return value ** (1/n)

    @staticmethod
    def log(value, base):
        """Calculate logarithm using change of base formula."""
        if value <= 0:
            return float('-inf')  # Logarithm of non-positive number is undefined
        if base <= 0 or base == 1:
            return "Invalid base for logarithm"
        result = 0
        while value >= base:
            value /= base
            result += 1
        while value < 1:
            value *= base
            result -= 1
        return result

    @staticmethod
    def log2(value):
        """Calculate the base-2 logarithm of a number or each element in a list."""
        is_list = type(value) == list
        if is_list:
            return [maTh.log(x, 2) for x in value if x > 0]
        return maTh.log(value, 2) if value > 0 else "Cannot compute logarithm base 2 of non-positive number"

    @staticmethod
    def ln(value):
        """Calculate the natural logarithm of a number or each element in a list."""
        is_list = type(value) == list
        if is_list:
            return [maTh.log(x, 2.718281828459045) for x in value if x > 0]
        return maTh.log(value, 2.718281828459045) if value > 0 else "Cannot compute natural logarithm of non-positive number"

   @staticmethod
    def abs(value):
        """Calculate the absolute value of a number or each element in a list."""
        is_list = type(value) == list
        if is_list:
            return [x if x >= 0 else -x for x in value]
        return value if value >= 0 else -value

    @staticmethod
    def cube(value):
        """Calculate the cube of a number or each element in a list."""
        is_list = type(value) == list
        if is_list:
            return [x ** 3 for x in value]
        return value ** 3

    @staticmethod
    def cb_root(value):
        """Calculate the cube root of a number or each element in a list."""
        is_list = type(value) == list
        if is_list:
            return [x ** (1/3) for x in value]
        return value ** (1/3)

    @staticmethod
    def inc(value):
        """Increment a number or each element in a list by 1."""
        is_list = type(value) == list
        if is_list:
            return [x + 1 for x in value]
        return value + 1

    @staticmethod
    def dec(value):
        """Decrement a number or each element in a list by 1."""
        is_list = type(value) == list
        if is_list:
            return [x - 1 for x in value]
        return value - 1

    @staticmethod
    def assign(alpha, operation=None):
        """Perform a selected assignment operation."""
        
        def add(value):
            """Add 2 to the current value."""
            return value + 2

        def sub(value):
            """Subtract 2 from the current value."""
            return value - 2

        def mul(value):
            """Multiply the current value by 2."""
            return value * 2

        def div(value):
            """Divide the current value by 2."""
            return value / 2 if value != 0 else "Cannot divide by zero"

        def mod(value):
            """Get the modulus of the current value by 2."""
            return value % 2

        def exp(value):
            """Calculate the exponent of the current value raised to 2."""
            return value ** 2

        def and_op(value):
            """Perform bitwise AND with 1."""
            return value & 1

        def or_op(value):
            """Perform bitwise OR with 1."""
            return value | 1

        def r_shift(value):
            """Right shift the current value by 1."""
            return value >> 1

        def l_shift(value):
            """Left shift the current value by 1."""
            return value << 1

        # Check if alpha is a list
        is_list = type(alpha) == list
        results = {}

        if operation is None:  # Perform all operations
            operations = [
                'Add Assignment', 'Subtract Assignment', 'Multiply Assignment', 
                'Divide Assignment', 'Modulus Assignment', 'Exponent Assignment', 
                'Bitwise AND Assignment', 'Bitwise OR Assignment', 
                'Right Shift Assignment', 'Left Shift Assignment'
            ]
            for op in operations:
                if is_list:
                    if op == 'Add Assignment':
                        results[op] = [add(x) for x in alpha]
                    elif op == 'Subtract Assignment':
                        results[op] = [sub(x) for x in alpha]
                    elif op == 'Multiply Assignment':
                        results[op] = [mul(x) for x in alpha]
                    elif op == 'Divide Assignment':
                        results[op] = [div(x) for x in alpha]
                    elif op == 'Modulus Assignment':
                        results[op] = [mod(x) for x in alpha]
                    elif op == 'Exponent Assignment':
                        results[op] = [exp(x) for x in alpha]
                    elif op == 'Bitwise AND Assignment':
                        results[op] = [and_op(x) for x in alpha]
                    elif op == 'Bitwise OR Assignment':
                        results[op] = [or_op(x) for x in alpha]
                    elif op == 'Right Shift Assignment':
                        results[op] = [r_shift(x) for x in alpha]
                    elif op == 'Left Shift Assignment':
                        results[op] = [l_shift(x) for x in alpha]
                else:
                    if op == 'Add Assignment':
                        results[op] = add(alpha)
                    elif op == 'Subtract Assignment':
                        results[op] = sub(alpha)
                    elif op == 'Multiply Assignment':
                        results[op] = mul(alpha)
                    elif op == 'Divide Assignment':
                        results[op] = div(alpha)
                    elif op == 'Modulus Assignment':
                        results[op] = mod(alpha)
                    elif op == 'Exponent Assignment':
                        results[op] = exp(alpha)
                    elif op == 'Bitwise AND Assignment':
                        results[op] = and_op(alpha)
                    elif op == 'Bitwise OR Assignment':
                        results[op] = or_op(alpha)
                    elif op == 'Right Shift Assignment':
                        results[op] = r_shift(alpha)
                    elif op == 'Left Shift Assignment':
                        results[op] = l_shift(alpha)
            return results
        else:  # Perform the specified operation
            if is_list:
                if operation == 'Add Assignment':
                    return [add(x) for x in alpha]
                elif operation == 'Subtract Assignment':
                    return [sub(x) for x in alpha]
                elif operation == 'Multiply Assignment':
                    return [mul(x) for x in alpha]
                elif operation == 'Divide Assignment':
                    return [div(x) for x in alpha]
                elif operation == 'Modulus Assignment':
                    return [mod(x) for x in alpha]
                elif operation == 'Exponent Assignment':
                    return [exp(x) for x in alpha]
                elif operation == 'Bitwise AND Assignment':
                    return [and_op(x) for x in alpha]
                elif operation == 'Bitwise OR Assignment':
                    return [or_op(x) for x in alpha]
                elif operation == 'Right Shift Assignment':
                    return [r_shift(x) for x in alpha]
                elif operation == 'Left Shift Assignment':
                    return [l_shift(x) for x in alpha]
            else:
                if operation == 'Add Assignment':
                    return add(alpha)
                elif operation == 'Subtract Assignment':
                    return sub(alpha)
                elif operation == 'Multiply Assignment':
                    return mul(alpha)
                elif operation == 'Divide Assignment':
                    return div(alpha)
                elif operation == 'Modulus Assignment':
                    return mod(alpha)
                elif operation == 'Exponent Assignment':
                    return exp(alpha)
                elif operation == 'Bitwise AND Assignment':
                    return and_op(alpha)
                elif operation == 'Bitwise OR Assignment':
                    return or_op(alpha)
                elif operation == 'Right Shift Assignment':
                    return r_shift(alpha)
                elif operation == 'Left Shift Assignment':
                    return l_shift(alpha)
