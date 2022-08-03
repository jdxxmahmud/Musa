def main():
    Student = get_student()
    print(f"{Student['Name']} from {Student['House']}")


def get_student():
    student = {}
    student['Name']  = input("Name:")
    student['House'] = input('House:')
    return student



if __name__ == '__main__':
    main()









