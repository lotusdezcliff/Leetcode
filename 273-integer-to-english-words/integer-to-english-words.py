class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        d = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

        def split_number_into_groups(n):
            num_str = str(n)
            groups = []
            first_group_size = len(num_str) % 3
            if first_group_size > 0:
                groups.append(num_str[:first_group_size])
            for i in range(first_group_size, len(num_str), 3):
                groups.append(num_str[i:i+3])
            return groups

        def convert_group_to_words(group, group_index):
            if not group:
                return ""
            group_size = len(group)
            words = []
            if group_size == 3:
                if group[0] != "0":
                    words.append(d[int(group[0])] + " Hundred")
                group = group[1:]
            if 0 < int(group) < 20:
                words.append(d[int(group)])
            elif int(group) >= 20:
                words.append(d[int(group[0])*10])
                if group[1] != "0":
                    words.append(d[int(group[1])])
            if group_index > 0:
                words.append(d[10**(3*group_index)])
            return " ".join(words)

        groups = split_number_into_groups(num)
        result = []
        for i, group in enumerate(groups):
            if group != "000":
                result.append(convert_group_to_words(group, len(groups) - i - 1))
        return " ".join(result).strip()