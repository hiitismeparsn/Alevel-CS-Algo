
class Binarrytree:
    def __init__(self,data):
        self.data = data
        self.leftptr = 0
        self.rightptr = 0
        self.firstchar = self.data[0]
        print("Constructor was called ")
        print(self.firstchar)


names = ["spongebob","john","laura"]
tree = [] # Create an empty array for the tree

for i in range(len(names)):                         
    student = Binarrytree(names[i])             #Create a temp variable to make an object
    if i == 0:
        tree.append(student.data)
    
    if student.firstchar > tree[0].firstchar:
        if student.leftptr == 0:
            tree.append(student)
            tree[0].leftptr = len()



# student1 = Binarrytree(names[0])
# student2 = Binarrytree(names[1])
# student3 = Binarrytree(names[2])

# if len(tree) == 0:
#     tree.append(student1)

# if student2.firstchar < student1.firstchar:
#     if student1.leftptr 





for i in range(len(names)):                         
    student = Binarrytree(names[i])             #Create a temp variable to make an object
    if i == 0:
        tree.append(student.data)
    
    if student.firstchar > tree[0].firstchar:

