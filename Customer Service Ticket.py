#2. Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:


# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }


import uuid
from datetime import datetime

# Initialize an empty dictionary to store the service tickets
service_tickets = {}

def create_ticket():
# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
    
    ticket_id = str(uuid.uuid4())  # Unique ID for each ticket (UUID)
    description = input("Enter a description for the issue: ")
    status = "Open"  # Default status when a ticket is created
    
    # Get customer details
    customer_name = input("Enter customer name: ").capitalize()
    
    ticket = {
        'ticket_id': ticket_id,
        'description': description,
        'status': status,
        'customer_info': {
            'name': customer_name,
        }
    }

    # Add the ticket to the service_tickets dictionary
    service_tickets[ticket_id] = ticket
    print(f"Ticket created successfully with ID: {ticket_id}")

def update_ticket():
#Update status of an existing ticket  
    ticket_id = input("Enter the ticket ID to update: ")
    
    # Check if the ticket exists
    if ticket_id in service_tickets:
        new_status = input("Enter new status (Open, In Progress, Closed): ").capitalize()
        
        # Update ticket status 
        ticket = service_tickets[ticket_id]
        ticket['status'] = new_status
        
        print(f"Ticket {ticket_id} updated successfully.")
    else:
        print(f"Ticket ID {ticket_id} not found.")

def view_ticket():
    
    ticket_id = input("Enter the ticket ID to view: ")
    
    # Check if the ticket exists
    if ticket_id in service_tickets:
        ticket = service_tickets[ticket_id]
        print("\nTicket Information:")
        print(f"Ticket ID: {ticket['ticket_id']}")
        print(f"Description: {ticket['description']}")
        print(f"Status: {ticket['status']}")
        print(f"Customer Name: {ticket['customer_info']['name']}")
    else:
        print(f"Ticket ID {ticket_id} not found.")

def display_all_tickets():
    
    if service_tickets:
        print("\nAll Service Tickets:")
        for ticket_id, ticket in service_tickets.items():
            print(f"\nTicket ID: {ticket['ticket_id']}")
            print(f"Description: {ticket['description']}")
            print(f"Status: {ticket['status']}")
            print(f"Customer: {ticket['customer_info']['name']}")
    else:
        print("No tickets available.")

def interactive_session():

    while True:
        print("\nOptions:")
        print("1. Create a new service ticket")
        print("2. View a service ticket")
        print("3. Update a service ticket")
        print("4. Display all tickets")
        print("5. Quit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            create_ticket()
        elif choice == '2':
            view_ticket()
        elif choice == '3':
            update_ticket()
        elif choice == '4':
            display_all_tickets()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    interactive_session()
