class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        employee_map = { e.id: e for e in employees}
        def calculate(employee):
            total = employee.importance
            for subordinate in employee.subordinates:
                total += calculate(employee_map[subordinate])
            return total
        
        return calculate(employee_map[id])

            