# Automated Time Blocking Tool

![automated-time-blocking-tool Jenderal92](https://github.com/user-attachments/assets/211ebb5e-e87a-450b-9c04-59881ebbe4af)


The **Automated Time Blocking Tool** allows users to automatically block time in their Google Calendar for additional tasks after existing events. By leveraging the **Google Calendar API**, this tool ensures that your calendar is always updated and optimized for productivity.

---

## Features

1. **Google Calendar Integration**: Connects directly to your Google Calendar for event management.
2. **Automatic Time Blocking**: Automatically creates a focused work block after existing calendar events.
3. **OAuth 2.0 Authentication**: Simplifies login using a saved `token.json` file.
4. **Dynamic Scheduling**: Adjusts new blocks based on the current schedule to avoid conflicts.

---

## How to Use

### **1. Prerequisites**
- **Python 2.7**: Ensure Python 2.7 is installed on your system.
- **Google Calendar API Credentials**: Download `credentials.json` from the Google Developer Console.

### **2. Setup**
- Install the required Python libraries:
  ```bash
  pip install --upgrade google-api-python-client oauth2client httplib2
  ```
- Place `credentials.json` in the same directory as the script.

### **3. Run the Tool**
- Execute the script:
  ```bash
  python time_blocker.py
  ```

### **4. Authentication**
- On the first run, the tool will prompt you to log in to your Google account and authorize access to your calendar.
- A `token.json` file will be created for future use.

---

## Example Output

Upon running the tool, you might see the following output:
```
============================================
   Automated Time Blocking Tool (Python 2.7)
============================================
Fetching upcoming events...
Existing event: Team Meeting
Start: 2024-12-24T10:00:00Z, End: 2024-12-24T11:00:00Z
Created event: Work Block - Focused Time
```

---
