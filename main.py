from application.salary import calculate_salary
from application.db.people import get_employee
import datetime
import dash

if __name__ == '__main__':
    print(calculate_salary(get_employee(id)))
    print(datetime.datetime.now())