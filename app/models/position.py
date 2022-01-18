"""
Position
"""
from app.db import BASE
from sqlalchemy import Column, String, Integer
from app.db import DBConnection

# DB Object
db = DBConnection()


class Positions(BASE):
    """
    Positions model
    """
    __tablename__ = 'positions'
    guid = Column(String(length=100), nullable=False, primary_key=True)
    name = Column(String(length=100), nullable=False)
    status = Column(Integer, nullable=False)
    action = Column(String(length=100), nullable=False)
    timestamp = Column(String(length=10), nullable=False)

    @classmethod
    def update_position(cls, data):
        """
        Update Position
        """
        try:
            session = db.get_session()
            # Getting position data from session
            position_data = session.query(Positions).filter(Positions.guid == data.get('guid')).first()
            if position_data:
                # Setting data in position object
                position_data.name = data.get('name')
                position_data.status = data.get('status')
                position_data.action = data.get('action')
                position_data.timestamp = data.get('timestamp')
                # Commiting the changes into session
                session.commit()
                print(f"Updated Position record with GUID: {data.get('guid')}")
            # Closing session
            session.close()
        except:
            raise

    @classmethod
    def delete_position(cls, data):
        """
        Delete positions
        """
        try:
            session = db.get_session()
            # Getting position data object
            position_data = session.query(Positions).filter(Positions.guid == data.get('guid')).first()
            if position_data:
                # Deleting the object from this session
                session.delete(position_data)
                # Commiting the changes
                session.commit()
                print(f"Deleted Position recored with GUID: {data.get('guid')}")
            # Closing session
            session.close()
        except:
            raise
