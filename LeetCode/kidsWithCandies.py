# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        
        bessiethecow = []
        for i in range(len(candies)):
            bessiethecow.append(candies[i]+extraCandies>=mx)
            
        return bessiethecow