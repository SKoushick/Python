import tkinter as tk
import mysql.connector
import pymysql

def save_to_database():
    nam = name.get()
    age = ag.get()


    # Establishing the connection
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Kousi7023",
        database="simple"
    )

    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    # Executing an SQL query to insert the name into the database
   
    query = "INSERT INTO simp(NAME,age) VALUES (%s,%s)"
    values = (nam,age)
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
name = tk.Entry(window)
name.pack()
ag= tk.Entry(window)
ag.pack()


# Creating the button
button = tk.Button(window, text="Save", command=save_to_database)
button.pack()

# Running the Tkinter event loop
window.mainloop()
