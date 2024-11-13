class student:
    def __init__(self,sid,sname,s_marks):
        self.Student_ID=sid
        self.Student_Name=sname
        self.Subject_Marks=s_marks

    def print_details(self):
        print(f'Student_Id:{self.Student_ID}, Student_Name:{self.Student_Name},Subject_marks:{self.Subject_Marks}')
        x=sum(self.Subject_Marks)
        print(f'Total marks:{x}')
        print('Avg:',x/3)

print('Student Details......')
s1=student(1,'KaSai',[80,90,70])
s2=student(60,'rohan',[88,80,60])
s3=student(158,'Sai',[95,90,99])

s1.print_details()
s2.print_details()
s3.print_details()
