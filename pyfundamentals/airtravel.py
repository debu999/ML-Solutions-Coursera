"""Module for aircraft flights"""

from pprint import pprint as pp


class Flight:
    """A Flight with a particular passenger aircraft"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}".format(number))
        if not number[2:].isdigit() and int(number[2:]) <= 9999:
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()

        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]


    def number(self):
        return self._number


    def airline(self):
        return self._number


    def aircraft_model(self):
        return self._aircraft.model()


    def _parse_seat(self,seat):
        """Parse a seat designator into a valid row and letter

        Args:
            seat: A seat designator such as '12C' or '21F'.

        Returns:
              A tuple containing an integer and a string for row and seat.
        """

        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]

        if letter not in seat_letters:
            raise ValueError("Invalid seat selection. Seat with letter {} not found".format(letter))

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row selection. Seat with Row# {} not found.".format(row_text))

        if row not in rows:
            raise ValueError("Invlid row selection. No Row with value {} found in aircraft.".format(row))

        return row, letter


    def allocate_seat(self, seat, passenger):
        """Allocate a seat to passenger

        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The Passenger Name.

        Raises:
            ValueError: If the seat is unavailable.

        """

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {}{} already occupied".format(row,letter))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger from a given seat to a new seat

        Args:
            from_seat: The existing seat designator for the passenger to be moved.
            to_seat: The new seat designator.

        """

        from_row, from_letter = self._parse_seat(from_seat)

        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate from seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} is already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating if row is not None)


    def make_boarding_cards(self, boardingpass_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            boardingpass_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating allocations"""
        row_num, seat_let = self._aircraft.seating_plan()
        for row in row_num:
            for let in seat_let:
                passenger = self._seating[row][let]
                if passenger is not None:
                    yield(passenger, "{}{}".format(row,let))


class Aircraft:

    def __init__(self, registration):
        self._registration = registration


    def registration(self):
        return self._registration


    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(row_seats) * len(rows)


class AB123(Aircraft):
    """Test class to facilitate Polymorphism"""

    def model(self):
        return "Airbus 319"

    def seating_plan(self):
        return range(1, 24) , "ABCDEFGHI"


class CD123(Aircraft):
    """Test class to facilitate Polymorphism"""

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        """For simplicity we ignore first class arrangements"""
        return range(1, 85) , "ABCDEFGHIJKL"


def make_flight():
    f = Flight("BA0234",Aircraft("B-GDSER", "Boening 223", num_rows=25, num_seats_per_row=7))
    f.allocate_seat("3F","Debabrata Patnaik")
    f.allocate_seat("5A","Ramesh Surapaneni")
    f.allocate_seat("6F", "Suresh Patnaik")
    f.allocate_seat("11D", "Divesh Surapaneni")
    f.allocate_seat("15C", "Sarath Patnaik")
    f.allocate_seat("20E", "D Surapaneni")

    return f

def make_flights():
    f = Flight("AB4785",AB123("A-DHFKHLS"))
    f.allocate_seat("3F","Debabrata Patnaik")
    f.allocate_seat("5A","Ramesh Surapaneni")
    f.allocate_seat("6F", "Suresh Patnaik")
    f.allocate_seat("11D", "Divesh Surapaneni")
    f.allocate_seat("15C", "Sarath Patnaik")
    f.allocate_seat("20E", "D Surapaneni")

    g = Flight("BA8201", CD123("B-KPWLD"))
    g.allocate_seat("3F", "Debabrata Patnaik")
    g.allocate_seat("5A", "Ramesh Surapaneni")
    g.allocate_seat("6F", "Suresh Patnaik")
    g.allocate_seat("11D", "Divesh Surapaneni")
    g.allocate_seat("15C", "Sarath Patnaik")
    g.allocate_seat("20E", "D Surapaneni")

    return f, g


def boardingpass_printer(passenger, seat, flight_number, aircraft):
    output = """| Name: {0} \
     Flight: {1} \
     Seat: {2} \
     Aircraft{3} \
    |""".format(passenger, flight_number, seat, aircraft)

    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print("")
    print("")



if __name__ == "__main__":
    f , g = make_flights()
    pp(f._seating)
