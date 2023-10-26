from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Team(Base):
    __tablename__ = "Teams"
    
    team_id = Column(Integer, primary_key=True)
    team_name = Column(String)
    
    
    matches = relationship("IPL_match", back_populates="team")


class IPL_match(Base):
    __tablename__ = "IPL_match"
    
    match_id = Column(Integer, primary_key=True)
    inning = Column(Integer)
    team_id = Column(Integer, ForeignKey("Teams.team_id"))  
    over = Column(Integer)
    
    
    
    team = relationship("Team", back_populates="matches")




    
username = "ankit69"
password = "ankit69"
hostname = "sample"  
port = "5432"  
database_name = "postgres"  

engine = create_engine(
    f"postgresql://{username}:{password}@localhost:{port}/{database_name}", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


team1 = Team(team_name="Sunrisers Hyderabad")
team2 = Team(team_name="Royal Challengers Bangalore")

match1 = IPL_match(inning=1, team=team1, over=1)
match2 = IPL_match(inning=1, team=team2, over=2)

session.add_all([team1, team2, match1, match2])
session.commit()