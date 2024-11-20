def clear_screen():
    # Clear the console screen by printing new lines
    print("\n" * 100)

class Person:
    def __init__(self, name: str, email: str):
        if '@' not in email:
            print("Invalid email format")
        self.name = name
        self.email = email

    def get_details(self) -> str:
        return f"Name: {self.name}, Email: {self.email}"

class Admin(Person):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self.username = "dhruv"
        self.password = "Dhruv"
        self.residents = []
        self.notices = []
        self.events = []
        self.complaints = []

    def verify_credentials(self, username: str, password: str) -> bool:
        return username == self.username and password == self.password

    def add_resident(self, name: str, email: str) -> None:
        if self._find_resident(email):
            print("Resident with this email already exists.")
            return
        new_resident = Resident(name, email)
        self.residents.append(new_resident)
        print(f"Resident {name} added successfully!")

    def _find_resident(self, email: str) -> 'Resident':
        return next((resident for resident in self.residents 
                    if resident.email == email), None)

    def generate_bill(self, email: str, amount: float) -> None:
        if amount <= 0:
            print("Bill amount must be positive")
            return
            
        resident = self._find_resident(email)
        if resident:
            resident.add_bill(amount)
            print(f"Bill of {amount} assigned to {resident.name}.")
        else:
            print("Resident not found.")

    def view_complaints(self) -> None:
        print("\nComplaints:")
        if not self.complaints:
            print("No complaints found.")
            return
        for i, complaint in enumerate(self.complaints, start=1):
            print(f"{i}. {complaint}")

    def resolve_complaint(self, index: str) -> None:
        idx = int(index) - 1
        if 0 <= idx < len(self.complaints):
            resolved = self.complaints.pop(idx)
            print(f"Complaint '{resolved}' resolved!")
        else:
            print("Invalid complaint index.")

    def add_notice(self, notice: str) -> None:
        if not notice.strip():
            print("Notice cannot be empty")
            return
        self.notices.append(notice)
        print("Notice added successfully!")

    def add_event(self, event: str) -> None:
        if not event.strip():
            print("Event cannot be empty")
            return
        self.events.append(event)
        print("Event added successfully!")

class Resident(Person):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self.bills = []

    def add_bill(self, amount: float) -> None:
        if amount <= 0:
            print("Bill amount must be positive")
            return
        self.bills.append(amount)

    def pay_bill(self, amount: float) -> None:
        if amount in self.bills:
            self.bills.remove(amount)
            print(f"Bill of {amount} paid successfully!")
        else:
            print("No such bill found.")

    def raise_complaint(self, admin: Admin, description: str) -> None:
        if not description.strip():
            print("Complaint description cannot be empty")
            return
        admin.complaints.append(description)
        print("Complaint raised successfully!")

    def view_notices(self, notices: list) -> None:
        print("\nNotices:")
        if not notices:
            print("No notices found.")
            return
        for i, notice in enumerate(notices, 1):
            print(f"{i}. {notice}")

    def view_events(self, events: list) -> None:
        print("\nEvents:")
        if not events:
            print("No events found.")
            return
        for i, event in enumerate(events, 1):
            print(f"{i}. {event}")

    def view_bills(self) -> None:
        print("\nPending Bills:")
        if not self.bills:
            print("No pending bills.")
            return
        for i, bill in enumerate(self.bills, 1):
            print(f"{i}. Amount: ₹{bill}")

# Polymorphism example
def print_person_details(person: Person) -> None:
    print(person.get_details())

# Abstraction example
class SocietyManagementSystem:
    def __init__(self):
        self.admin = Admin("Dhruv", "shyam@xyz.com")

    def _authenticate_admin(self) -> bool:
        clear_screen()
        print("\nAdmin Authentication Required")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if self.admin.verify_credentials(username, password):
            return True
        else:
            print("Invalid credentials!")
            input("Press Enter to continue...")
            return False

    def _handle_admin_menu(self) -> None:
        admin_choice = None
        while admin_choice != "7":
            clear_screen()
            print("\n=== Admin Menu ===")
            print("1. Add Resident")
            print("2. Generate Bill")
            print("3. View Complaints")
            print("4. Resolve Complaint")
            print("5. Add Notice")
            print("6. Add Event")
            print("7. Logout")
            
            admin_choice = input("Choose an option: ")

            if admin_choice == "1":
                print("\n=== Add New Resident ===")
                name = input("Enter resident's name: ").strip()
                email = input("Enter resident's email: ").strip()
                self.admin.add_resident(name, email)
                input("\nPress Enter to continue...")

            elif admin_choice == "2":
                print("\n=== Generate Bill ===")
                email = input("Enter resident's email: ").strip()
                amount = float(input("Enter bill amount: "))
                self.admin.generate_bill(email, amount)
                input("\nPress Enter to continue...")

            elif admin_choice == "3":
                print("\n=== View Complaints ===")
                self.admin.view_complaints()
                input("\nPress Enter to continue...")

            elif admin_choice == "4":
                print("\n=== Resolve Complaint ===")
                self.admin.view_complaints()
                index = input("Enter complaint number to resolve: ")
                self.admin.resolve_complaint(index)
                input("\nPress Enter to continue...")

            elif admin_choice == "5":
                print("\n=== Add Notice ===")
                notice = input("Enter notice details: ").strip()
                self.admin.add_notice(notice)
                input("\nPress Enter to continue...")

            elif admin_choice == "6":
                print("\n=== Add Event ===")
                event = input("Enter event details: ").strip()
                self.admin.add_event(event)
                input("\nPress Enter to continue...")

    def _handle_resident_menu(self, resident: Resident) -> None:
        resident_choice = None
        while resident_choice != "6":
            clear_screen()
            print(f"\n=== Resident Menu - {resident.name} ===")
            print("1. View Bills")
            print("2. Pay Bill")
            print("3. Raise Complaint")
            print("4. View Notices")
            print("5. View Events")
            print("6. Logout")
            
            resident_choice = input("Choose an option: ")

            if resident_choice == "1":
                print("\n=== View Bills ===")
                resident.view_bills()
                input("\nPress Enter to continue...")

            elif resident_choice == "2":
                print("\n=== Pay Bill ===")
                resident.view_bills()
                amount = float(input("\nEnter bill amount to pay: "))
                resident.pay_bill(amount)
                input("\nPress Enter to continue...")

            elif resident_choice == "3":
                print("\n=== Raise Complaint ===")
                description = input("Enter complaint details: ").strip()
                resident.raise_complaint(self.admin, description)
                input("\nPress Enter to continue...")

            elif resident_choice == "4":
                print("\n=== View Notices ===")
                resident.view_notices(self.admin.notices)
                input("\nPress Enter to continue...")

            elif resident_choice == "5":
                print("\n=== View Events ===")
                resident.view_events(self.admin.events)
                input("\nPress Enter to continue...")

    def run(self) -> None:
        choice = None
        while choice != "3":
            clear_screen()
            print("\n=== Welcome to Society Management System ===")
            print("1. Admin")
            print("2. Resident")
            print("3. Exit")
            choice = input("Select your role: ")

            if choice == "1":
                if self._authenticate_admin():
                    self._handle_admin_menu()
            elif choice == "2":
                print("\n=== Resident Login ===")
                email = input("Enter your registered email: ").strip()
                resident = self.admin._find_resident(email)
                if resident:
                    self._handle_resident_menu(resident)
                else:
                    print("Email not registered.")
                    input("\nPress Enter to continue...")
            elif choice == "3":
                print("\nThank you for using Society Management System!")
            else:
                print("Invalid choice.")
                input("\nPress Enter to continue...")

def main():
    system = SocietyManagementSystem()
    system.run()

if __name__ == "__main__":
    main()
