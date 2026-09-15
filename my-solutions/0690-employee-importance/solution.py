"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {}
        for employee in employees:
            mp[employee.id] = employee
        
        return self.helper(mp, id)
    

    def helper(self, employees: dict, employeeID: int):
        importance = employees[employeeID].importance
        for subordinate in employees[employeeID].subordinates:
            importance += self.helper(employees, subordinate)
        return importance
