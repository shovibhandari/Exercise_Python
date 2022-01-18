"""
Model to interact with database
"""
from app.db import BASE
from sqlalchemy import Column, Integer, String
from app.db import DBConnection

# Database Object
db = DBConnection()


class Employee(BASE):
    """
    Employee Model
    """
    __tablename__ = 'employees'
    guid = Column(String(length=100), nullable=False, primary_key=True)
    status = Column(Integer, nullable=False)
    state = Column(String(length=10), nullable=False)
    action = Column(String(length=100), nullable=False)
    timestamp = Column(String(length=10), nullable=False)

    @classmethod
    def update_employee(cls, data):
        """
        Update employee
        """
        try:
            session = db.get_session()

            # Getting employee using GUID
            emp_data = session.query(Employee).filter(Employee.guid == data.get('guid')).first()
            if emp_data:
                # Updating data into the current object
                emp_data.status = data.get('status')
                emp_data.state = data.get('state')
                emp_data.action = data.get('action')
                emp_data.timestamp = data.get('timestamp')
                # Commit the changes
                session.commit()
                print(f"Updated Employee record with GUID : {data.get('guid')}")
            # Closing session
            session.close()
        except:
            raise

    @classmethod
    def delete_employee(cls, data):
        try:
            session = db.get_session()
            # Getting the employee object from db
            emp_data = session.query(Employee).filter(Employee.guid == data.get('guid')).first()
            if emp_data:
                # Delete the object
                session.delete(emp_data)
                # Commiting the changes
                session.commit()
                print(f"Deleted Employee record with GUID : {data.get('guid')}")
            # Closing session
            session.close()
        except:
            raise
