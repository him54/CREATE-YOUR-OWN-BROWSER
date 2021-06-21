class student:
    def __init__(self,aname,amarks):
        self.name=aname
        self.marks=amarks
    def details(self):
        return f"name is {self.name} and marks are {self.marks}"

ob=student("Himanshu","456")
print(ob.details())
