from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print(calculate_salary(),datetime.today())
    print(get_employees(),datetime.today())