def get_employee_info(name, emp_id, department, salary):
    return (
        f" Employee Name : {name},\n"
        f" Employee ID : {emp_id},\n"
        f" Department : {department},\n"
        f" Salary : {salary}"
    )

if __name__ == "__main__":
    print(get_employee_info("Alice Smith" ,"E202", "HR", 60000))
