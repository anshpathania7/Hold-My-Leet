class Solution:
    def average(self, salary: List[int]) -> float:
        minimumSalary, maximumSalary = salary[0],salary[0]
        totalSalaries = 0
        for i in salary:
            if i>maximumSalary:
                maximumSalary=i
            if i<minimumSalary:
                minimumSalary=i
            totalSalaries+=i
        return (totalSalaries-minimumSalary-maximumSalary) / (len(salary)-2)
        