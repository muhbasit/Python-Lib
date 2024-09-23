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
