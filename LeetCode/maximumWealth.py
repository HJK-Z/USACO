# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = 0
        for i in range(len(accounts)):
            total = 0
            for j in range(len(accounts[0])):
                total += accounts[i][j]
                
            mx = max(mx, total)
        
        return mx   