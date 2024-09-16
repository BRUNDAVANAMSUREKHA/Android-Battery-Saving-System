# Desktop Battery Saver App

## Overview

The Desktop Battery Saver App is a Tkinter-based desktop application that simulates battery usage by various apps and displays alerts when an app consumes excessive battery power. The application includes a battery level indicator and a customizable background image.

## Features

- **Battery Level Indicator**: Displays the current battery level, which decreases over time.
- **App Battery Usage**: Lists apps with their battery usage, each represented by an image.
- **Battery Alerts**: Shows alerts if an app consumes more than 20% of battery power.
- **Background Image**: Allows setting a custom background image for the application window.

## Requirements

- Python 3.x
- Pillow library (for image handling)
- Tkinter library (included with Python)

## Installation

1. **Install Dependencies**:

   Install the Pillow library using pip:

   ```bash
   pip install Pillow
2. Prepare Images
   Place the following image files in the same directory as the script:
- `background.jpg` (Background image)
- `App 1.jpg` (Image for App 1)
- `App 2.jpg` (Image for App 2)
- `App 3.jpg` (Image for App 3)

3. Run the Application
   Execute the script using Python:

```bash
python ANDROID_BATTERY_SAVING_SYSTEM.py
```

4. Interact with the Application

- The app window will show the battery level and a list of apps.
- Click on any app button to view its battery usage.
- If an app consumes more than 20% of the battery, an alert will prompt to close the app.


## Code Overview

### `BatterySaverDesktopApp` Class
- **`__init__`**: Initializes the app, sets up the background image, battery level, and app buttons.
- **`set_background_image`**: Loads and sets the background image for the window.
- **`show_battery_usage`**: Displays battery usage for a selected app and triggers alerts if necessary.
- **`simulate_battery_drain`**: Simulates battery drain over time.

## Troubleshooting

- **Images Not Loading**: Ensure the image files are correctly named and located in the same directory as the script

## 

![image](https://github.com/user-attachments/assets/f488b6a4-8ced-48c5-ae2c-9ee478ce04b6)
![image](https://github.com/user-attachments/assets/920931bf-f995-4208-a026-577db1b63974)
![image](https://github.com/user-attachments/assets/102c0871-05aa-4d84-a1be-b1cef37ae152)

## License

This project is licensed under the MIT License.
