"""
Query Service to save update or delete data from DB
"""

from app.db import DBConnection
from app.models.employee import Employee
from app.models.job import Job
from app.models.position import Positions

# Database Object
db = DBConnection()


class Query:
    """
    Query class
    """
    @staticmethod
    def employee(data):
        """
        Handle Employee data
        """
        if data.get('action').lower() == "insert":
            Query.insert_employee(data)
        if data.get('action').lower() == "update":
            Employee.update_employee(data)
        if data.get('action').lower() == "delete":
            Employee.delete_employee(data)

    @staticmethod
    def insert_employee(data):
        """
        Inseting new employee
        """
        try:
            if not data:
                raise Exception("Data is not provided")
            session = db.get_session()

            # Setting value of data into data model
            emp = Employee()
            emp.guid = data.get('guid')
            emp.action = data.get('action')
            emp.state = data.get('state')
            emp.status = data.get('status')
            emp.timestamp = data.get('timestamp')

            # Adding object to database session
            session.add(emp)

            # Commit the changes (new object)
            session.commit()

            # Closing session
            session.close()
            print(f"Added new record of Employee with GUID: {data.get('guid')}")
        except:
            raise

    @staticmethod
    def job(data):
        """
        Handle job data
        """
        if data.get('action').lower() == "insert":
            Query.insert_job(data)
        if data.get('action').lower() == "update":
            Job.update_employee(data)
        if data.get('action').lower() == "delete":
            Job.delete_employee(data)

    @staticmethod
    def insert_job(data):
        """
        Inserting Job
        """
        try:
            if not data:
                raise Exception("Data is not provided")
            session = db.get_session()

            # Setting value of data into data model
            job = Job()
            job.guid = data.get('guid')
            job.action = data.get('action')
            job.company_guid = data.get('company_guid')
            job.employee_guid = data.get('employee_guid')
            job.timestamp = data.get('timestamp')

            # Adding object to database session
            session.add(job)

            # Commit the changes
            session.commit()

            # Closing the session
            session.close()
            print(f"Added new record of Job with GUID: {data.get('guid')}")
        except:
            raise

    @staticmethod
    def position(data):
        """
        Handling data of position
        """
        if data.get('action').lower() == "insert":
            Query.insert_position(data)
        if data.get('action').lower() == "update":
            Positions.update_position(data)
        if data.get('action').lower() == "delete":
            Positions.delete_position(data)

    @staticmethod
    def insert_position(data):
        """
        Inserting new positions
        """
        try:
            if not data:
                raise Exception("Data not provided")
            session = db.get_session()

            # Setting value of data into data model
            position = Positions()
            position.guid = data.get('guid')
            position.name = data.get('name')
            position.status = data.get('status')
            position.action = data.get('action')
            position.timestamp = data.get('timestamp')

            # Adding object to database session
            session.add(position)

            # Commit the session
            session.commit()

            # Closing session
            session.close()
            print(f"New recored of Position added with GUID: {data.get('guid')}")
        except:
            raise
