class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sum = 0
        for i in details:
            if (len(i) == 15) and (int(i[11]) * 10 + int(i[12]) > 60) and (i[10] == 'M' or i[10] == 'F' or i[10] == 'O'):
                sum += 1
        return sum
