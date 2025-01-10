import mysql.connector
from mysql.connector import Error

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mimi1998!',
    'database': 'gym_db'
}

# Establish database connection
def create_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Task 1: Add a Member
def add_member(member_id, name, age):
    """
    Adds a new member to the Members table.
    """
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(query, (member_id, name, age))
            conn.commit()
            print("Member added successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

# Task 2: Add a Workout Session
def add_workout_session(member_id, session_date, duration_minutes, calories_burned):
    """
    Adds a new workout session to the WorkoutSessions table.
    """
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (member_id, session_date, duration_minutes, calories_burned))
            conn.commit()
            print("Workout session added successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

# Task 3: Update Member Information
def update_member_age(member_id, new_age):
    """
    Updates the age of a member.
    """
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            query = "UPDATE Members SET age = %s WHERE id = %s"
            cursor.execute(query, (new_age, member_id))
            if cursor.rowcount > 0:
                conn.commit()
                print("Member age updated successfully!")
            else:
                print("Member not found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    """
    Deletes a workout session based on the session ID.
    """
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, (session_id,))
            if cursor.rowcount > 0:
                conn.commit()
                print("Workout session deleted successfully!")
            else:
                print("Session not found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

# Task 5: Retrieve Members in an Age Range
def get_members_in_age_range(start_age, end_age):
    """
    Retrieves members whose ages fall within a specified range.
    """
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            query = """
                SELECT id, name, age FROM Members
                WHERE age BETWEEN %s AND %s
            """
            cursor.execute(query, (start_age, end_age))
            results = cursor.fetchall()
            if results:
                print("Members in the age range:")
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
            else:
                print("No members found in the specified age range.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

# Example Usage
if __name__ == "__main__":
    # Adding a new member
    add_member(1, "Jane Doe", 28)
    add_member(2, "John Smith", 35)
    add_member(3, "Emily Davis", 25)

    # Adding a workout session
    add_workout_session(1, "2025-01-10", 60, 300)
    add_workout_session(2, "2025-01-11", 45, 250)

    # Updating a member's age
    update_member_age(2, 36)

    # Deleting a workout session
    delete_workout_session(1)

    # Retrieving members in an age range
    get_members_in_age_range(25, 30)
