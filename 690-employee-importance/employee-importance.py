"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        emp_map = {}

        for emp in employees:
            emp_map[emp.id] = emp

        def dfs(emp_id):
            employee = emp_map[emp_id]
            total = employee.importance

            for sub in employee.subordinates:
                total += dfs(sub)

            return total

        return dfs(id)