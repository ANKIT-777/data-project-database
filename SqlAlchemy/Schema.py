from sqlalchemy import create_engine, Column, String, Integer, Boolean,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




Base = declarative_base()

username = "ankit69"
password = "ankit69"
hostname = "localhost"  # Replace with your PostgreSQL server's hostname or IP address
port = "5432"  # Replace with the port where PostgreSQL is running (usually 5432)
database_name = "ipls"  # Replace with the name of your PostgreSQL databaseSchema

# Create the SQLAlchemy engine 
# Create the SQLAlchemy engine
try:
    engine = create_engine(f"postgresql://{username}:{password}@{hostname}:{port}/{database_name}", echo=True)
except Exception as e:
    print("Error creating the engine:", e)

try:
    engine = create_engine(f"postgresql://{username}:{password}@{hostname}:{port}/{database_name}", echo=True)
except Exception as e:
    print("Error creating the engine:", e)



Session = sessionmaker(bind=engine)
session = Session()

class Matches(Base):
    __tablename__ = "Matches"
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer,unique=True)
    team_name = Column(String)
    season = Column(String)
    city = Column(String)
    date = Column(String)  # Assuming date is a string
    team1 = Column(String)
    team2 = Column(String)
    toss_winner = Column(String)
    toss_decision = Column(String)
    result = Column(String)
    dl_applied = Column(Integer)
    winner = Column(String)
    win_by_runs = Column(Integer)
    win_by_wickets = Column(Integer)
    player_of_match = Column(String)
    venue = Column(String)
    umpire1 = Column(String)  
    umpire2 = Column(String)
    umpire3 = Column(String)

class Deliveries(Base):
    __tablename__ = "Deliveries"
    
    id = Column(Integer, primary_key=True)
    match_id = Column("match_id", Integer, ForeignKey("Matches.match_id"))
    inning = Column("inning", Integer)
    batting_team = Column("batting_team", String)
    bowling_team = Column("bowling_team", String)
    over = Column("over", Integer)
    ball = Column("ball", Integer)
    batsman = Column("batsman", String)
    non_striker = Column("non_striker", String)
    bowler = Column("bowler", String)
    is_super_over = Column("is_super_over", Boolean)
    wide_runs = Column("wide_runs", Integer)
    bye_runs = Column("bye_runs", Integer)
    legbye_runs = Column("legbye_runs", Integer)
    noball_runs = Column("noball_runs", Integer)
    penalty_runs = Column("penalty_runs", Integer)
    batsman_runs = Column("batsman_runs", Integer)
    extra_runs = Column("extra_runs", Integer)
    total_runs = Column("total_runs", Integer)
    player_dismissed = Column("player_dismissed", String)
    dismissal_kind = Column("dismissal_kind", String)
    fielder = Column("fielder", String)

    
class Umpire(Base):
    __tablename__ = "Umpires"
    id = Column(Integer, primary_key=True)
    umpire_name = Column("umpire_name", String)
    country_name = Column("country_name", String)


Base.metadata.create_all(engine)

