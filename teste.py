import pymysql
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine(
    'mysql+pymysql://root:@localhost/letnis13',
    echo=False)

Session = sessionmaker()

Base = declarative_base()

class SapLogon(Base):
    __tablename__ = 'tb_saplogon'

    id_sap = Column(Integer, primary_key=True)
    id_company = Column(Integer)
    description = Column(String(length=100))
    sapusers = relationship("SapUser")

    def __repr__(self):
        return "<SapLogon(Description='{0}')>".format(self.description)

class SapUser(Base):
    __tablename__ = 'tb_sap_users'

    id_sap_user = Column(Integer, primary_key=True)
    id_sap = Column(Integer, ForeignKey('tb_saplogon.id_sap'))
    # id_sap = Column(Integer)
    username = Column(String(length=100))
    password = Column(String(length=100))
    mandt = Column(Integer)
    
    def __repr__(self):
        return "<SapUser(username='{0}', Password='{1}', Mandt='{2}')>".format(self.username, self.password, self.mandt)

Session.configure(bind=engine)
session = Session()

saplogons = session.query(SapLogon).filter_by(description='QBR - Contitech')
for saplogon in saplogons:
    print('\nSap User:')
    print(saplogon)
    for sapuser in saplogon.sapusers:
        print(sapuser)