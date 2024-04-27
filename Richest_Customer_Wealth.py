from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for customer_accounts in accounts:
            current_wealth = sum(customer_accounts)
            max_wealth = max(max_wealth, current_wealth)
        
        return max_wealth
    

s= Solution()
accounts = [[1,2,3],[3,2,1]]
print(s.maximumWealth(accounts))
accounts = [[1,5],[7,3],[3,5]]
print(s.maximumWealth(accounts))