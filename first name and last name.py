import tkinter as tk
import mysql.connector

def save_to_database():
    name = entry.get()

    # Establishing the connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kousi7023",
        database="hii"
    )

    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    # Executing an SQL query to insert the name into the database
    query = "INSERT INTO kousi (name)"
    values = (name)
    cursor.execute(query, values)

    # Committing the changes to the database
    connection.commit()

    # Closing the cursor and connection
    cursor.close()
    connection.close()

    print("Name saved to the database!")

# Creating the Tkinter window
window = tk.Tk()

# Creating the entry box
entry = tk.Entry(window)
entry.pack()

# Creating the button
button = tk.Button(window, text="Save", command=save_to_database)
button.pack()

# Running the Tkinter event loop
window.mainloop()
