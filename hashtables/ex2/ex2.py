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
        ticket_idx[ticket.source] = ticket.destination
    
    route.append(ticket_idx["NONE"]) # it initiate the trip 
    
    for i in range(length-1):
        current_ticket = route[-1]
        route.append(ticket_idx[current_ticket])

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


# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
print(reconstruct_trip(tickets, 10))