from sqlalchemy import *
from sqlalchemy.orm import *
## Set up however you need to
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

Session = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = 'en_students'
    #
    id      = Column(Integer, primary_key = True)
    login   = Column(String(20), unique=True, nullable=False)
    first   = Column(String(20))
    last    = Column(String(20))
    credits = Column(Integer, default=0)
    gpa     = Column(Float(precision=32), default=0)
    favorite_id = Column(Integer, ForeignKey("en_courses.id"))
    # And we talk about the relationship:
    favoriteCourse = relationship("Course", back_populates="favoritedBy")
    #
    def __repr__(self):
        return "Student<%s %s>" % (self.first, self.last)

class Course(Base):
    __tablename__ = "en_courses"
    #
    id      = Column(Integer, primary_key=True)
    prefix  = Column(String(4), nullable=False)
    no      = Column(String(20), nullable=False)
    title   = Column(String(55), nullable=False)
    credits = Column(Integer, nullable=False, default=4)
    __table_args__ = (
        UniqueConstraint('prefix', 'no', name="fullCode"),
    )
    favoritedBy = relationship("Student", order_by=Student.id,
                               back_populates="favoriteCourse")
    #
    def __repr__(self):
        return "Course<%s%s %s>" % (self.prefix, self.no, self.title)
    #
    def isFullCredit(self):
        return self.credits == 4

Base.metadata.create_all(engine)  # Creates the tables in the database

alan = Student(last="Turing", first="Alan", login="turinga37")
intro = Course(prefix="CS", no="220", title="Fundamentals")
dataStructures = Course(prefix="CS", no="223", title="Data Structures")
alan.favoriteCourse = dataStructures
dataStructures.favoritedBy
del dataStructures.favoritedBy[0]


session = Session()
session.add_all([alan, intro, dataStructures])
