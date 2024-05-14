from School import School,ClassRoom,Subject
from Persons import Student,Teacher




def main():
    #print('main is running')
    school = School('kgc','ngc')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)
     #add students
    labanya = Student('labanya saha',eight)
    school.student_addmission(labanya)

    saha = Student('saha albu',eight)
    school.student_addmission(saha)

    shuvra = Student('shuvra sahaa',eight)
    school.student_addmission(shuvra)

    #subjects
    #cse = Subject('cse')
    cse_teacher = Teacher('dutta roy dar')
    cse = Subject('Cse',cse_teacher)
    eight.add_subject(cse)

    physics_teacher = Teacher('anuppp')
    physics = Subject('physics',physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Hardon nag')
    chemistry = Subject('chemistry',chemistry_teacher)
    eight.add_subject(chemistry)

    eight.take_semester_final()



    print(school)



if __name__ == '__main__':
    main()