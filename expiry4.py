# import cv2
# from ultralytics import YOLO
# import tkinter as tk
# from tkinter import ttk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt

# # Function to perform object detection and display the image in the dashboard
# def detect_expiry_date():
#     # Load the trained model
#     model = YOLO('best(epochs 15) (1).pt')  # Replace with your YOLOv8 model

#     # Path to the image to be processed
#     image_path = r'C:\Users\uvara\OneDrive\Desktop\lets begin\Flipkart product analysis\Expiry\IMG_20241019_144318.jpg'
    
#     # Load the image using OpenCV
#     image = cv2.imread(image_path)
    
#     # Convert the image to grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Convert grayscale image back to 3-channel format (so YOLO can accept it)
#     gray_image_3_channel = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

#     # Perform object detection on the 3-channel grayscale image
#     results = model(gray_image_3_channel)

#     # Draw bounding boxes on the image
#     annotated_img = results[0].plot()

#     # Clear any previous plot
#     for widget in frame.winfo_children():
#         widget.destroy()

#     # Display the image using Matplotlib
#     fig, ax = plt.subplots(figsize=(8, 8))
#     ax.imshow(annotated_img)
#     ax.axis('off')

#     # Embed the Matplotlib figure inside the Tkinter dashboard
#     canvas = FigureCanvasTkAgg(fig, master=frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack()

# # Create the Tkinter window
# root = tk.Tk()
# root.title("YOLO Expiry Date Detection Dashboard")

# # Create a frame to hold the Matplotlib plot
# frame = ttk.Frame(root)
# frame.pack(pady=20)

# # Call the detect_expiry_date function to process and display the image in the dashboard
# detect_expiry_date()

# # Start the Tkinter event loop
# root.mainloop()
import cv2
from ultralytics import YOLO
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Function to perform object detection and display the image in the dashboard
def detect_expiry_date():
    # Load the trained model
    model = YOLO('best(epochs 15) (1).pt')  # Replace with your YOLOv8 model

    # Path to the image to be processed
    image_path = r'C:\Users\uvara\OneDrive\Desktop\lets begin\Flipkart product analysis\Expiry\Test_Image\IMG_20241019_144318.jpg'
    
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert grayscale image back to 3-channel format (so YOLO can accept it)
    gray_image_3_channel = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

    # Perform object detection on the 3-channel grayscale image
    results = model(gray_image_3_channel)

    # Draw bounding boxes on the image
    annotated_img = results[0].plot()

    # Clear any previous plot
    for widget in frame.winfo_children():
        widget.destroy()

    # Display the image using Matplotlib
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(annotated_img)
    ax.axis('off')

    # Embed the Matplotlib figure inside the Tkinter dashboard
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create the Tkinter window
root = tk.Tk()
root.title("YOLO Expiry Date Detection Dashboard")

# Set the background color of the window
root.configure(bg="#add8e6")  # Light blue background

# Create a frame with a background color to hold the Matplotlib plot
frame = ttk.Frame(root, padding=10)
frame.pack(pady=20, padx=20)

# Add a title label with a background color
title_label = tk.Label(root, text="Expiry Date Detection", font=("Helvetica", 16, "bold"), bg="#add8e6", fg="white")
title_label.pack(pady=10)

# Call the detect_expiry_date function to process and display the image in the dashboard
detect_expiry_date()

# Start the Tkinter event loop
root.mainloop()
