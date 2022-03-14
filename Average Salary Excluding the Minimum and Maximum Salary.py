#Average Salary Excluding the Minimum and Maximum Salary
#to remove the lowest and the higest salaries, we can sort the elements and then remove the first and last element from it.
#making use of the sort() function and slicing the list using, [1:-1] and then we can calculate the average

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        new = salary[1:-1]
        lenght = len(new)
        avg = sum(new)/lenght
        return avg
