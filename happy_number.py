class Solution:
    def isHappy(self, n: int) -> bool:
        hash = []
        sum_numbers = None
        sum_list = []
        initial_num = n
        while sum_numbers != 1:
            
            for number in str(initial_num):
                sum_list.append((int(number))**2)
            sum_numbers = sum(sum_list)
            initial_num = sum_numbers
            sum_list = []
            if sum_numbers in hash:
                return False
            hash.append(sum_numbers)
        print(sum_numbers)


result = Solution()
result.isHappy(2)