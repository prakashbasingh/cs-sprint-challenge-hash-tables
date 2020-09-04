#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    ticket_idx = {}
    
    # creating a ticket index
    for ticket in tickets:
        ticket_idx[ticket.source] = ticket.destination # storing source and destination in the ticket(index)
    
    route.append(ticket_idx["NONE"]) # it initiate the trip 
    
    for i in range(length-1): # looping through ticket list
        current_ticket = route[-1] # sets current ticket to next to first NONE
        route.append(ticket_idx[current_ticket])# insert teh current airport to the route list

    return route



tickets = [
    Ticket( "PIT", "ORD" ),
    Ticket( "XNA", "CID" ),
    Ticket( "SFO", "BHM" ),
    Ticket( "FLG", "XNA" ),
    Ticket( "NONE", "LAX"),
    Ticket( "LAX", "SFO" ),
    Ticket( "CID", "SLC" ),
    Ticket( "ORD", "NONE"),
    Ticket( "SLC", "PIT" ),
    Ticket( "BHM", "FLG" )
]

print(reconstruct_trip(tickets, 10))