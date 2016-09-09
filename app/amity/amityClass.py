rooms = {}


class Amity(object):
    """Super class for amity"""

    def __init__(self):
        super(Amity, self).__init__()
        # self.rooms = {
        #     'Office': [],
        #     'LivingSpace': []
        # }

    def get_room_type(self):
        # Get the room_type from the user
        room_type = None

        # Assign a group of rooms to a room type
        while room_type not in ['O', 'L']:
            room_type = raw_input(
                "Enter room type: \n o: Office space \n l: Living space: \n")
            room_type = room_type.upper()
        return room_type

    def create_room(self, args):
        """Allows user to enter a list of room names specifying
                whether office or living spaces"""

        room_type = self.get_room_type()

        # Adds room to the rooms dict
        for room in args["<room_name>"]:
            rooms.update({room: {"occupants": [], "room_type": room_type}})

        # find a better way of doing the print

        print "You have created the following rooms: \n"
        print "OFFICES: " + ', '.join(rooms['Office'].keys())
        print "LIVING SPACES: " + ', '.join(rooms['LivingSpace'].keys())

        return rooms
