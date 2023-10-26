
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Schema import Matches,Deliveries,Umpire  # Import your table and Base class
import csv
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy engine
Base = declarative_base()

username = "ankit69"
password = "ankit69"
hostname = "localhost"  # Replace with your PostgreSQL server's hostname or IP address
port = "5432"  # Replace with the port where PostgreSQL is running (usually 5432)
database_name = "ipls"  # Replace with the name of your PostgreSQL databaseSchema


engine = create_engine(
    f"postgresql://{username}:{password}@localhost:{port}/{database_name}", echo=True
)

Session = sessionmaker(bind=engine)
session = Session()
matches_path = "IPL/matches.csv"  # Replace with the path to your CSV file

with open(matches_path, newline='') as csvfile:
    Dataset = csv.DictReader(csvfile)
    # Iterate over the rows and insert data into the Matches table
    for row in Dataset:
        match = Matches(
            id=row['id'],  # Use 'id' as the primary key
            season=row['season'],
            city=row['city'],
            date=row['date'],
            team1=row['team1'],
            team2=row['team2'],
            toss_winner=row['toss_winner'],
            toss_decision=row['toss_decision'],
            result=row['result'],
            dl_applied=row['dl_applied'],
            winner=row['winner'],
            win_by_runs=row['win_by_runs'],
            win_by_wickets=row['win_by_wickets'],
            player_of_match=row['player_of_match'],
            venue=row['venue'],
            umpire1=row['umpire1'],
            umpire2=row['umpire2'],
            umpire3=row['umpire3']
        )
        session.add(match)
        session.commit()
# Commit the changes to the database
    
    
    
    
delivery_path = 'IPL/deliveries.csv'
with open(delivery_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        ipl_match = Deliveries(
            match_id=row['match_id'],
            inning=row['inning'],
            batting_team=row['batting_team'],
            bowling_team=row['bowling_team'],
            over=row['over'],
            ball=row['ball'],
            batsman=row['batsman'],
            non_striker=row['non_striker'],
            bowler=row['bowler'],
            is_super_over=row['is_super_over'],
            wide_runs=row['wide_runs'],
            bye_runs=row['bye_runs'],
            legbye_runs=row['legbye_runs'],
            noball_runs=row['noball_runs'],
            penalty_runs=row['penalty_runs'],
            batsman_runs=row['batsman_runs'],
            extra_runs=row['extra_runs'],
            total_runs=row['total_runs'],
            player_dismissed=row['player_dismissed'],
            dismissal_kind=row['dismissal_kind'],
            fielder=row['fielder']
        )

        session.add(ipl_match)
        session.commit()

umpire_path = 'IPL/umpires.csv'
with open(umpire_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        umpires = Umpire(
            id = row['id'],
            umpire_name = row['umpire'],
            country_name = row['country']
        )
        session.add(umpires)
        session.commit()    
# Close the session

session.close()
