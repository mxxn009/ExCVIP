---

## Automated Email Sender Script

This Python script automates the process of sending emails on a scheduled basis. It leverages the `schedule`, `yagmail`, and `time` libraries to provide a user-friendly way to send emails at predefined intervals. 

### Features

- **Scheduling:** Prompts the user to specify a number of days to run the script, allowing for recurring email tasks.
- **User Input:** Collects necessary details such as:
  - Application-specific password for secure access.
  - Sender's and recipient's email addresses.
  - Subject and body of the email.
- **Automation:** Automatically sends emails according to the schedule defined by the user.

### How It Works

1. **Initial Setup:** Upon running the script, you are prompted to decide if you want to schedule the script.
2. **Input Collection:** The script then collects your email details, including:
   - Application-specific password.
   - Sender's email address.
   - Recipient's email address.
   - Subject and body of the email.
3. **Scheduling:** Based on user input, the script schedules the emails to be sent at regular intervals (e.g., daily) for the specified number of days.
4. **Execution:** The script uses the `schedule` library to manage timing and `yagmail` to handle email sending.

### Requirements

- Python 3.x
- `schedule` library
- `yagmail` library

### Installation

To install the required libraries, run:

```bash
pip install schedule yagmail
```

### Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   ```
2. Navigate to the script's directory:
   ```bash
   cd your-repository
   ```
3. Run the script:
   ```bash
   python automated_email_sender.py
   ```

Follow the prompts to enter your email details and schedule preferences.

### Notes

- Ensure you have enabled access for less secure apps or generated an application-specific password for the email account you use.
- The script assumes that the system running it will be active and connected to the internet for the duration of the schedule.

---
