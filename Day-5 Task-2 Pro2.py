class employee:
      def calculate_salary(self):
        return 30000
class developer(employee):
    def calculate_salary(self):
      base_salary = super().calculate_salary()
      bouns = 5000
      return base_salary + bouns

class designer(employee):
    def calculate_salary(self):
      base_salary = super().calculate_salary()
      bouns = 3000
      return base_salary + bouns

dev = developer()
des = designer()

print("Developer Salary:",dev.calculate_salary())
print("Designer Salary:",des.calculate_salary())
    
    