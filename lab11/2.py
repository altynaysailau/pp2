import psycopg2

# Database connection parameters
DSN = {
    'host': 'localhost',
    'database': 'PhoneBook',
    'user': 'altynai',
    'password': '1234'
}

# Function to search contacts based on a pattern
def search_contacts(pattern):
    try:
        conn = psycopg2.connect(**DSN)
        cur = conn.cursor()
        
        # Execute the SQL function
        cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
        rows = cur.fetchall()

        if not rows:
            print("No matches found.")
        else:
            print("\nID | Name                 | Phone")
            print("---+----------------------+---------------")
            for _id, name, phone in rows:
                print(f"{_id:2d} | {name:20s} | {phone}")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

# Function to insert a user (with update if exists)
def upsert_user(name, phone):
    try:
        conn = psycopg2.connect(**DSN)
        cur = conn.cursor()
        
        # Execute the upsert procedure
        cur.execute("CALL upsert_user(%s, %s)", (name, phone))
        conn.commit()
        
        print(f"✔️  Upserted: {name} → {phone}\n")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

# Function to insert multiple users
def insert_multiple_users(user_list):
    try:
        conn = psycopg2.connect(**DSN)
        cur = conn.cursor()

        # Loop through the user list and insert/update each user
        for name, phone in user_list:
            # Perform the upsert for each user
            cur.execute("CALL upsert_user(%s, %s)", (name, phone))
        
        conn.commit()
        print("✅ All users inserted/updated successfully.")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

# Function to paginate contacts
def paginate_contacts(limit=10, offset=0):
    try:
        conn = psycopg2.connect(**DSN)
        cur = conn.cursor()

        # Execute the pagination function
        cur.execute("SELECT * FROM paginate_contacts(%s, %s)", (limit, offset))
        rows = cur.fetchall()

        if not rows:
            print("No rows to show.")
        else:
            print(f"\nShowing up to {limit} rows starting at offset {offset}:")
            print("ID | Name                 | Phone")
            print("---+----------------------+---------------")
            for _id, name, phone in rows:
                print(f"{_id:2d} | {name:20s} | {phone}")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

# Function to delete contact by username or phone
def delete_contact(name_pat=None, phone_pat=None):
    try:
        conn = psycopg2.connect(**DSN)
        cur = conn.cursor()

        # Execute the delete procedure
        cur.execute("CALL delete_contact_by_user_or_phone(%s, %s)", (name_pat, phone_pat))
        conn.commit()
        
        print("🗑️  Delete operation completed.\n")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
