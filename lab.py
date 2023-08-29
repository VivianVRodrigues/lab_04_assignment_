class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_flight_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None

    def search_by_source(self, source):
        result = []
        for flight in self.flights:
            if flight.source == source:
                result.append(flight)
        return result

    def search_by_destination(self, destination):
        result = []
        for flight in self.flights:
            if flight.destination == destination:
                result.append(flight)
        return result

# Create flight objects and add them to the flight table
flight_table = FlightTable()
flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

# Get user input
user_input = input("Enter Flight ID, Source, or Destination: ")

# Search and print flight details based on user input
if user_input.isalpha():
    # User input is source or destination
    source_results = flight_table.search_by_source(user_input)
    destination_results = flight_table.search_by_destination(user_input)

    if source_results:
        print("Flights from", user_input, ":")
        for flight in source_results:
            print(flight.flight_id, flight.source, "->", flight.destination, "Price:", flight.price)
    if destination_results:
        print("Flights to", user_input, ":")
        for flight in destination_results:
            print(flight.flight_id, flight.source, "->", flight.destination, "Price:", flight.price)
else:
    # User input is flight ID
    flight = flight_table.search_by_flight_id(user_input)
    if flight:
        print("Flight ID:", flight.flight_id)
        print("Source:", flight.source)
        print("Destination:", flight.destination)
        print("Price:", flight.price)
    else:
        print("Flight not found with ID:", user_input)
