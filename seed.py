import os
import django
from django.conf import settings

# Initialize Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crime_analysis.settings")
django.setup()

from user.models import user_reg, user_complaints
from higher_officer.models import station_details
from police.models import criminal_details
import random
from datetime import datetime, timedelta

def run_seed():
    print("Clearing old dummy data (optional, skipping for safety)...")
    
    print("Seeding Users...")
    users_data = [
        {"fullname": "John Doe", "email": "john.doe@example.com", "mobile": "9876543210", "gender": "Male", "location": "Downtown", "userid": "john_user", "password": "password123"},
        {"fullname": "Jane Smith", "email": "jane.smith@example.com", "mobile": "9876543211", "gender": "Female", "location": "Uptown", "userid": "jane_user", "password": "password123"},
        {"fullname": "Alice Johnson", "email": "alice.j@example.com", "mobile": "9876543212", "gender": "Female", "location": "Suburbs", "userid": "alice_user", "password": "password123"},
    ]
    for u in users_data:
        user_reg.objects.get_or_create(userid=u['userid'], defaults=u)

    print("Seeding Police Stations & Officers...")
    stations_data = [
        {"police_name": "Officer Mike", "gender": "Male", "station_name": "Central Precinct", "area_code": "001", "location": "Downtown", "email": "mike@police.gov", "userid": "mike_001", "password": "password123", "area_name": "Central District"},
        {"police_name": "Officer Sarah", "gender": "Female", "station_name": "North Precinct", "area_code": "002", "location": "Uptown", "email": "sarah@police.gov", "userid": "sarah_002", "password": "password123", "area_name": "North District"},
        {"police_name": "Officer Dave", "gender": "Male", "station_name": "East Precinct", "area_code": "003", "location": "Eastside", "email": "dave@police.gov", "userid": "dave_003", "password": "password123", "area_name": "East District"},
    ]
    for s in stations_data:
        station_details.objects.get_or_create(userid=s['userid'], defaults=s)

    print("Seeding Complaints & Cases...")
    
    complaint_types = ["Theft", "Vandalism", "Noise", "Assault", "Traffic", "Burglary", "Fraud", "Public Disturbance"]
    statuses = ["Pending", "Assigned", "Resolved", "Closed"]
    
    users = [
        {"userid": "john_user", "username": "John Doe", "email": "john.doe@example.com", "address": "123 Main St", "mobile": "9876543210"},
        {"userid": "jane_user", "username": "Jane Smith", "email": "jane.smith@example.com", "address": "456 Oak Avenue", "mobile": "9876543211"},
        {"userid": "alice_user", "username": "Alice Johnson", "email": "alice.j@example.com", "address": "789 Pine Road", "mobile": "9876543212"}
    ]
    
    complaints_data = []
    
    # Generate 30 random complaints
    for i in range(30):
        # Pick random user
        user = random.choice(users)
        
        # Pick random area out of the 3 precincts
        area_code = random.choice(["001", "002", "003"])
        
        # Pick random type & status
        ctype = random.choice(complaint_types)
        status = random.choice(statuses)
        
        # Create random date in the last year
        rand_days_ago = random.randint(1, 365)
        cdatetime = datetime.now() - timedelta(days=rand_days_ago)
        
        complaint_text = f"Random system generated complaint #{i} for {ctype}. Incident reported by {user['username']}."
        
        complaint = {
            "userid": user['userid'], 
            "username": user['username'], 
            "email": user['email'], 
            "address": user['address'], 
            "city": "Metropolis", 
            "area_code": area_code, 
            "mobile": user['mobile'], 
            "date": cdatetime.strftime("%Y-%m-%d"), 
            "complaint_type": ctype, 
            "complaint": complaint_text, 
            "complaint_status": status
        }
        
        complaints_data.append(complaint)

    for c in complaints_data:
        user_complaints.objects.get_or_create(complaint=c['complaint'], defaults=c)

    print("Seeding Complete!")

if __name__ == "__main__":
    run_seed()
