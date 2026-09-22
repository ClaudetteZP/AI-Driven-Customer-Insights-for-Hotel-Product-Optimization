import pandas as pd
import pyodbc

# Load datasets.
bookings = pd.read_csv(r"C:\Users\Owner\OneDrive\Desktop\Capstone Project\hotel_bookings.csv")
reviews = pd.read_csv(r"C:\Users\Owner\OneDrive\Desktop\Capstone Project\Datafiniti_Hotel_Reviews.csv")



# Clean bookings.
bookings['children'] = bookings['children'].fillna(0)
bookings['country'] = bookings['country'].fillna("Unknown")
bookings['arrival_date'] = pd.to_datetime(
    bookings['arrival_date_year'].astype(str) + '-' +
    bookings['arrival_date_month'].astype(str) + '-' +
    bookings['arrival_date_day_of_month'].astype(str),
    errors='coerce'
)

# Clean reviews.
reviews = reviews.dropna(subset=['reviews.text'])
reviews_clean = reviews[['reviews.rating', 'reviews.text', 'reviews.date']]

# Connect to SQL Server.
conn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=BRAWL3R\\MSSQLSERVER01;'   
    'Database=HotelInsights;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Insert bookings data.
for index, row in bookings.iterrows():
    cursor.execute("""
        INSERT INTO Bookings (hotel, is_canceled, lead_time, arrival_date, country, children)
        VALUES (?, ?, ?, ?, ?, ?)
    """, row['hotel'], row['is_canceled'], row['lead_time'],
         row['arrival_date'], row['country'], row['children'])

# Insert reviews data.
for index, row in reviews_clean.iterrows():
    cursor.execute("""
        INSERT INTO Reviews (rating, review_text, review_date)
        VALUES (?, ?, ?)
    """, row['reviews.rating'], row['reviews.text'], row['reviews.date'])

conn.commit()
cursor.close()
conn.close()
