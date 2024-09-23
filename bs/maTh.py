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
