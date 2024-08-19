class Solution:
    def minSteps(self, n: int) -> int:
        def factorize_number(n):
            factors = {}
            i = 2
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors[i] = factors.get(i, 0) + 1
            if n > 1:
                factors[n] = factors.get(n, 0) + 1
            return factors
        steps = 0
        factor_dict = factorize_number(n)
        for key in factor_dict:
            steps += key * factor_dict[key]
        return steps


