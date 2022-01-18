"""
Job Module
"""
from app.db import BASE
from sqlalchemy import Column, String
from app.db import DBConnection

# Database object
db = DBConnection()


class Job(BASE):
    """
    Job Model
    """
    __tablename__ = "jobs"
    guid = Column(String(length=100), nullable=False, primary_key=True)
    company_guid = Column(String(length=100), nullable=False)
    position_guid = Column(String(length=100), nullable=True)
    employee_guid = Column(String(length=100), nullable=False)
    action = Column(String(length=100), nullable=False)
    timestamp = Column(String(length=10), nullable=False)

    @classmethod
    def update_job(cls, data):
        """
        Update record
        """
        try:
            session = db.get_session()
            # Getting Job object
            job_data = session.query(Job).filter(Job.guid == data.get('guid')).first()
            if job_data:
                # Update job object
                job_data.company_guid = data.get('company_guid')
                job_data.employee_guid = data.get('employee_guid')
                job_data.position_guid = data.get('position_guid')
                job_data.action = data.get('action')
                job_data.timestamp = data.get('timestamp')
                # Commiting the changes
                session.commit()
                print(f"Updated Job record with GUID : {data.get('guid')}")
            # Closing the session
            session.close()
        except:
            raise

    @classmethod
    def delete_job(cls, data):
        try:
            session = db.get_session()
            # Getting job object from db session
            job_data = session.query(Job).filter(Job.guid == data.get('guid')).first()
            if job_data:
                # Delete the object using session
                session.delete(job_data)
                # Commiting the changes
                session.commit()
                print(f"Deleted Job record with GUID: {data.get('guid')}")
            # Closing the session
            session.close()
        except:
            raise
