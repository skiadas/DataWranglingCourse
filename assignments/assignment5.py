# Name:

import random
from datetime import datetime, timedelta
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# The Status class is used in the enum column that you create in question 3
# enum package documentation: https://docs.python.org/3/library/enum.html
import enum
class Status(enum.Enum):
    Accepted = 1
    Declined = 2
    Maybe = 3

engine = create_engine('sqlite:///:memory:', echo=True)


###### CLASS AND TABLE DEFINITIONS GO HERE



###### END OF CLASS AND TABLE DEFINITIONS

# Drop existing tables and recreate them
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

###### WRITE YOUR ANSWERS TO OTHER QUESTIONS HERE





###### BELOW THIS LINE YOU CAN ADD ANY CODE YOU WANT TO HAVE FOR TESTING


