



import tkinter as tk

# Function to animate the text scroll
def animate_text(x_position=0):
    full_message = "WELCOME TO CARD SHUFFLER INTERFACE MACHINE"
    
    # Update the label's position (move it horizontally)
    label.place(x=x_position, y=root.winfo_height() // 2)  # Center vertically
    
    # Move the text to the right
    if x_position < root.winfo_width():
        # Schedule the next update (move to the right)
        root.after(20, animate_text, x_position + 5)  # Move 5 pixels every 20ms
    else:
        # Restart the animation (loop back to the start)
        root.after(5000, animate_text, -len(full_message) * 10)  # Wait 5 seconds, then reset

# Function to exit the program (disappear the interface)
def exit_program(event=None):
    root.quit()

# Create the main application window
root = tk.Tk()
root.title("Card Shuffler Interface Machine")

# Make the window fullscreen
root.attributes("-fullscreen", True)

# Create a label for the welcome message
label = tk.Label(root, text="WELCOME TO CARD SHUFFLER INTERFACE MACHINE", 
                 font=("Helvetica", 45, "bold"), fg="black", bg="white")

# Start the animation
animate_text(-len("WELCOME TO CARD SHUFFLER INTERFACE MACHINE") * 10)  # Start off-screen

# Bind the Enter key to close the application
root.bind("<Return>", exit_program)

# Start the Tkinter event loop
root.mainloop()
