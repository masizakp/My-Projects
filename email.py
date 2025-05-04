class Email:
    """
    Represents an email message.
    """

    has_been_read = False  # Class variable, default value

    def __init__(self, email_address, subject_line, email_content):
        """
        Initializes an Email object.

        Args:
            email_address (str): The sender's email address.
            subject_line (str): The email's subject line.
            email_content (str): The email's content.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        """
        Marks the email as read by setting has_been_read to True.
        """
        self.has_been_read = True


# Initialise an empty Inbox list to store email objects
inbox = []


def populate_inbox():
    """
    Populates the Inbox with three sample email objects.
    """
    email1 = Email(
    "sender1@example.com", "Welcome to HyperionDev!",
    "Dear Student,\nWelcome to the Bootcamp!"
    )
    email2 = Email(
    "sender2@example.com", "Great work on the Bootcamp!",
    "Dear Student,\nKeep up the excellent work!"
    )
    email3 = Email(
    "sender3@example.com", "Your excellent marks!",
    "Dear Student,\nCongratulations on your marks!"
    )
    inbox.append(email1)
    inbox.append(email2)
    inbox.append(email3)


def list_emails():
    """
    Lists the emails in the Inbox with their subject lines and numbers.
    """
    if not inbox:
        print("Your inbox is empty.")
    else:
        for j, email in enumerate(inbox):
            print(f"{j} {email.subject_line}")


def read_email(index):
    """
    Displays a selected email and marks it as read.

    Args:
        index (int): The index of the email to read.
    """
    try:
        email = inbox[index]
        print("\n--- Email ---")
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content:\n{email.email_content}")
        email.mark_as_read()
        print(
        f"\nEmail from {email.email_address} marked as read.\n"
        )
    except IndexError:
        print("Invalid email index.")


# Main program
populate_inbox()  # Populate inbox with initial emails

menu = """
Email Simulator

1. Read an email
2. View unread emails
3. Quit application

Enter your choice: """

while True:
    choice = input(menu)

    if choice == "1":
        list_emails()
        if inbox:
            try:
                index = int(input(
                "Enter the index of the email to read: "
            ))
                read_email(index)
            except ValueError:
                print(
                "Invalid input. Please enter a number."
            )
    elif choice == "2":
        print("\n--- Unread Emails ---")
        unread_count = 0
        for k, email in enumerate(inbox):
            if not email.has_been_read:
                print(f"{k} {email.subject_line}")
                unread_count += 1
        if unread_count == 0:
            print("You have no unread emails.")
        print()
    elif choice == "3":
        print("Quitting application.")
        break
    else:
        print("Invalid choice.")
