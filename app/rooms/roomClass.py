from app.person.personClass import people_data
from app.amity.amityClass import rooms


class Room(object):
    """
    Room
    """
    #Replace the '+=' with .format()

    def __init__(self):
        self.room_name = ""
        self.room_type = ""

    def get_names(self, identifier):
        # map(function, sequence)
        # .get(val, msg) to retrieve dict item

        person = people_data.get(identifier, None)
        if person == None:
            return "Person Does not exist"
        return person['name']

    def print_room(self, args):
        room_name = args["<room_name>"]
        # name = rooms.get(identifier, None)

        room = rooms.get(room_name, None)
        if room == None:
            return "{} Does Not Exist".format(room_name)

        occupants = map(self.get_names, room['occupants'])
        print "\n".join(occupants)
        return occupants


    def print_allocations(self, args):
        """
        Loops through the rooms object printing the room and the occupants
        """

        data = ""
        for room_type in rooms.keys():
            data += room_type.upper()
            data += "\n"
            if len(rooms[room_type].keys()) is 0:
                data += "No " + room_type + " created\n"
            else:
                for room_name in rooms[room_type].keys():
                    data += room_name.upper()
                    data += "\n"
                    data += "-" * 65
                    data += "\n"
                    if len(rooms[room_type][room_name]) is 0:
                        data += "No Occupants"
                    else:
                        for identifier in rooms[room_type][room_name]:
                            data += self.get_names(identifier, people_data)
                            data += ", "
                    data += "\n"
                    data += "\n"

        if args["-o"]:
            with open(args["<filename>"], 'wt') as output_file:
                output_file.write(data)
                print "The list of allocations has been saved " \
                    "to the following file: " + args["<filename>"]
        else:
            print data

    def print_unallocated(self, args):
        """
        Loops through the people_data dictionary
        Checks if an identifier in the people_data has been allocated an office,
        if not prints the name.
        Checks if a persons who wants accomodation has been allocated a living space,
        if not prints the name and missing room
        """
        data = ""
        data += "Those unallocated:\n"

        if len(rooms["Office"].keys()) is 0:
            data += "No Offices Created\n"
        else:
            for person_role in people_data.keys():
                for identifier in people_data[person_role].keys():
                    for room in rooms["Office"].keys():
                        if identifier in rooms["Office"][room]:
                            data += ""
                        else:
                            data += self.get_names(identifier,
                                                   people_data) + ": No Office"
                    if people_data[person_role][identifier]["accomodation"] is 'Y':
                        for room in rooms["LivingSpace"].keys():
                            if identifier in rooms["LivingSpace"][room]:
                                data += ""
                        else:
                            data += self.get_names(identifier,
                                                   people_data) + ": No Living Space"
                    data += "\n"

        if args["-o"]:
            with open(args["<filename>"], 'wt') as output_file:
                output_file.write(data)
                print "The list of unallocated people has been saved " \
                    "to the following file: " + args["<filename>"]
        else:
            print data
