from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
username = "ankit69"
password = "ankit69"
hostname = "sample"  # Replace with your PostgreSQL server's hostname or IP address
port = "5432"  # Replace with the port where PostgreSQL is running (usually 5432)
database_name = "postgres"  # Replace with the name of your PostgreSQL database

# Create the SQLAlchemy engine 
engine = create_engine(
    f"postgresql://{username}:{password}@localhost:{port}/{database_name}", echo=True
)

Session = sessionmaker(bind=engine)
session = Session()


class IPL(Base):
    __tablename__ = "Cricket_match"

    match_id = Column("match_id", Integer, primary_key=True)
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

    def __repr__(self):
        return f"<IPL match_id={self.match_id}, inning={self.inning}, batting_team={self.batting_team}, bowling_team={self.bowling_team}>"


Base.metadata.create_all(engine)

# Sample data (you can load your data from a file or another source)

data = [
    {
        "match_id": 1,
        "inning": 1,
        "batting_team": "Sunrisers Hyderabad",
        "bowling_team": "Royal Challengers Bangalore",
        "over": 1,
        "ball": 1,
        "batsman": "DA Warner",
        "non_striker": "S Dhawan",
        "bowler": "TS Mills",
        "is_super_over": 0,
        "wide_runs": 0,
        "bye_runs": 0,
        "legbye_runs": 0,
        "noball_runs": 0,
        "penalty_runs": 0,
        "batsman_runs": 0,
        "extra_runs": 0,
        "total_runs": 0,
        "player_dismissed": None,
        "dismissal_kind": None,
        "fielder": None,
    },
    # Add more rows here...
]

# Use bulk_insert_mappings to insert data
session.bulk_insert_mappings(IPL, data)

# Commit all the changes to the database
session.commit()
 
