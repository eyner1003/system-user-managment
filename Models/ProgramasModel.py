from sqlalchemy import Column, String, DateTime, Integer
from Database.conn import Base
from sqlalchemy.sql.functions import current_timestamp


class ProgramsModel(Base):
    
    __tablename__ = "programs"

    program_id = Column(Integer, nullable=False, primary_key=True,
                        autoincrement=True)
    name_program = Column(String(50), nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                       onupdate=current_timestamp())

    def __init__(self, data):
        self.name = data.get("program_name").title()

    def __repr__(self):
        return {
            "program_id": self.program_id,
            "program_name": self.name,
            "active": self.active

        }
