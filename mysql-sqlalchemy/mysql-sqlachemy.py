from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Connecting to our database
engine = create_engine("mysql+mysqlconnector://oruko:<P1r$Hg02ram/>@localhost:\
                        3306/household", echo=True)

Base = declarative_base()

# Models
class Project(Base):
    __tablename__ = 'projects'
    __table_args__ = {'schema':'household'}

    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return f'Project {self.title}, {self.description}'


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'schema':'household'}

    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('household.projects.project_id'))
    description = Column(String(length=50))

    project = relationship("Project")

    def __repr__(self):
        return f'Task={self.description}'

# Create database tables
Base.metadata.create_all(engine)

# Sessions
session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

# Creating our database objects

# Project Objects
organize_closet_project= Project(title="Organize Closet",
        description="Organize closet by color and stlye"
        )

session.add(organize_closet_project)
session.commit()

# Task Objects
tasks = [Task(project_id=organize_closet_project.project_id,
              description='Decide what clothes to donate'),
         Task(project_id=organize_closet_project.project_id,
              description='Organizee winter clothes'),
         Task(project_id=organize_closet_project.project_id,
              description='Organize summer clothes')
        ]


session.bulk_save_objects(tasks)
session.commit()

# Performing Queries
our_project = session.query(Project).filter_by(title='Organize Closet').first()
print(our_project)

our_task = session.query(Task).all()
print(our_task)
