import sys
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

class Company(Base):
    __tablename__ = 'tb_companies'

    id_company = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    saplogons = relationship("SapLogon")

    def __repr__(self):
        return "\n<Company(Name='{0}')>".format(self.name)

class SapLogon(Base):
    __tablename__ = 'tb_saplogon'

    id_sap = Column(Integer, primary_key=True)
    id_company = Column(Integer, ForeignKey('tb_companies.id_company'))
    description = Column(String(length=100))
    sapusers = relationship("SapUser")

    def __repr__(self):
        return "\n<SapLogon(Description='{0}')>".format(self.description)

class SapUser(Base):
    __tablename__ = 'tb_sap_users'

    id_sap_user = Column(Integer, primary_key=True)
    id_sap = Column(Integer, ForeignKey('tb_saplogon.id_sap'))
    username = Column(String(length=100))
    password = Column(String(length=100))
    mandt = Column(Integer)
    
    def __repr__(self):
        return "<SapUser(username={0}, Password={1}, Mandt={2})>".format(self.username, self.password, self.mandt)

def app(args):

    Session.configure(bind=engine)
    session = Session()

    companies = session.query(Company).filter_by(name=args)

    for company in companies:
        print(company)
        for saplogon in company.saplogons:
            print(saplogon)
            for sapuser in saplogon.sapusers:
                print(sapuser)

if __name__ == '__main__':
    try:
        app(sys.argv[1])
    except:
        print('Informe o nome da empresa na chamada.')
