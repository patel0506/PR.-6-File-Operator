import os
from datetime import datetime

class journal_manager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def create_journal_file(self):
        try:
            with open(self.filename, "x") as file:
                pass
            print("Journal file created successfully.")
        except FileExistsError:
            pass

    def add_entry(self):
        try:
            self.create_journal_file()
            entry = input("Enter your journal entry:\n")
            timestamp = datetime.now().strftime("%H:%M:%S %d-%m-%Y")

            with open(self.filename, "a") as file:
                file.write(f"[{timestamp}] {entry}\n")

            print("Entry added successfully!\n")

        except PermissionError:
            print("Error: Permission denied while writing to the file.")

        except Exception as e:
            print(f"Unexpected Error: {e}")

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()

                if content.strip():
                    print("\nYour Journal Entries:")
                    print(content)
                else:
                    print("No journal entries found.")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied while reading the file.")

        except Exception as e:
            print(f"Unexpected Error: {e}")

    def search_entry(self):
        try:
            keyword = input("Enter a keyword or date to search: ")

            with open(self.filename, "r") as file:
                lines = file.readlines()

            matches = []

            for line in lines:
                if keyword.lower() in line.lower():
                    matches.append(line)

            if matches:
                print("\nMatching Entries:")
                for match in matches:
                    print(match.strip())
            else:
                print(f"No entries were found for the keyword: {keyword}")

        except FileNotFoundError:
            print("Error: The journal file does not exist.")

        except PermissionError:
            print("Error: Permission denied while accessing the file.")

        except Exception as e:
            print(f"Unexpected Error: {e}")

    def delete_all_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("No journal entries to delete.")
                return

            confirm = input(
                "Are you sure you want to delete all entries? (yes/no): "
            ).lower()

            if confirm == "yes":
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            else:
                print("Deletion cancelled.")

        except PermissionError:
            print("Error: Permission denied while deleting the file.")

        except Exception as e:
            print(f"Unexpected Error: {e}")


def main():
    journal = journal_manager()

    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit\n")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                journal.add_entry()

            elif choice == 2:
                journal.view_entries()

            elif choice == 3:
                journal.search_entry()

            elif choice == 4:
                journal.delete_all_entries()

            elif choice == 5:
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break

            else:
                print("Invalid Input.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()