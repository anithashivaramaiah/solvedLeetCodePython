#programming skills - 1
#Count Odd Numbers in an Interval Range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return int(((high + high%2)-(low - low%2))/2)
    
  
