from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Split the expression into parts
        parts = expression.replace('-', '+-').split('+')
        result = Fraction(0)
        
        for part in parts:
            if part:
                result += Fraction(part)
        
        # Convert the result to a string in the format of a fraction
        return f"{result.numerator}/{result.denominator}"

# Example usage
solution = Solution()
expression = "1/3-1/2+1/4"
print(solution.fractionAddition(expression))  # Output: "-1/12"