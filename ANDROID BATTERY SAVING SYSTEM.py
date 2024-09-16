import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

class BatterySaverDesktopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Battery Saver App Demo")

        # Call function to set background image
        self.set_background_image()

        # Battery level (initially 100%)
        self.battery_level = 100

        # List of apps and their battery usage
        self.apps = [
            {"name": "App 1", "battery_usage": random.randint(1, 30)},
            {"name": "App 2", "battery_usage": random.randint(1, 30)},
            {"name": "App 3", "battery_usage": random.randint(1, 30)},
        ]

        # Ensure at least one app starts with battery usage above 20%
        self.apps[0]["battery_usage"] = random.randint(21, 30)

        # Create labels with background colors
        self.battery_label = tk.Label(root, text=f"Battery Level: {self.battery_level}%", background="lightblue", font=("Helvetica", 16))
        self.battery_label.pack(pady=10)  # Add space below the label

        self.apps_label = tk.Label(root, text="Apps with Battery Usage:", background="lightgreen", font=("Helvetica", 16))
        self.apps_label.pack(pady=10)  # Add space below the label

        # Create app buttons with JPG images
        self.app_buttons = []
        for app in self.apps:
            app_name = app['name']
            try:
                app_image_path = f"{app_name}.jpg"
                if not os.path.isfile(app_image_path):
                    print(f"File not found: {app_image_path}")
                    continue
                print(f"Loading image for {app_name} from {app_image_path}")
                app_image = Image.open(app_image_path)
                app_image = app_image.resize((100, 100), Image.LANCZOS)  # Updated to LANCZOS
                app_photo = ImageTk.PhotoImage(app_image)
                app_button = tk.Button(root, image=app_photo, command=lambda name=app_name: self.show_battery_usage(name))
                app_button.image = app_photo
                app_button.pack(pady=10)  # Add space below the buttons
            except Exception as e:
                print(f"Error loading image for {app_name}: {e}")

        # Start battery drain simulation
        self.simulate_battery_drain()

    def set_background_image(self):
        try:
            background_image_path = "background.jpg"
            if not os.path.isfile(background_image_path):
                print(f"File not found: {background_image_path}")
                return
            print(f"Loading background image from {background_image_path}")
            # Load the background image
            background_image = Image.open(background_image_path)

            # Resize the image to fit the application window
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)  # Updated to LANCZOS

            # Create a PhotoImage object from the PIL image
            background_photo = ImageTk.PhotoImage(background_image)

            # Create a label to display the background image
            background_label = tk.Label(self.root, image=background_photo)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            # Ensure the image is not garbage-collected
            background_label.image = background_photo
        except Exception as e:
            # Handle any errors loading the image
            print(f"Error loading background image: {e}")

    def show_battery_usage(self, app_name):
        for app in self.apps:
            if app['name'] == app_name:
                battery_usage = app['battery_usage']
                self.battery_label.config(text=f"Battery Usage by {app_name}: {battery_usage}%", background="lightblue")
                if battery_usage > 20:
                    messagebox.showinfo("Battery Alert", f"{app_name} is consuming more power. Close the app.")

    def simulate_battery_drain(self):
        if self.battery_level > 0:
            # Simulate battery drain
            self.battery_level -= random.randint(1, 5)
            self.battery_label.config(text=f"Battery Level: {self.battery_level}%")
            # Call this function again after 1000 ms (1 second)
            self.root.after(1000, self.simulate_battery_drain)

# Create the main window
root = tk.Tk()
app = BatterySaverDesktopApp(root)
root.mainloop()
