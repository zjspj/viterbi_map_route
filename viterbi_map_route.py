# This program can calculate the shortest route from the provided map.
# The weight of each edges can be change to test the accuracy of the program.
# However, the location and day is hard coded in and cannot be change otherwise the program cannot run correctly.


import networkx as nx

Node_Dict = {'0': ['Start'],
             '1': ['Seattle', 'Newport','San Francisco','USC'],
             '2': ['Boise', 'Salt Lake', 'Las Vegas', 'Tucson'],
             '3': ['Casper', 'Denver', 'Albuquerque', 'El Paso'],
             '4': ['Pierre', 'Lincoln', 'Amarillo', 'San Antonio'],
             '5': ['Minneapolis', 'Kansas City', 'Houston', 'Ft. Smith'],
             '6': ['Chicago', 'St. Louis', 'Nashville', 'New Orleans'],
             '7': ['Pittsburg', 'Roanoke', 'Charlotte', 'Talluhassee'],
             '8': ['MIT', 'Washington', 'Daytona Beach', 'Wilmington']}

Reduced_Node_Dict = {'0': ['Start'],
                     '1': ['Seattle', 'Newport','San Francisco','USC'],
                     '2': ['Boise', 'Salt Lake', 'Las Vegas', 'Tucson'],
                     '3': ['Casper', 'Denver', 'Albuquerque', 'El Paso'],
                     '4': ['Pierre', 'Lincoln', 'Amarillo', 'San Antonio'],
                     '5': ['Minneapolis', 'Kansas City', 'Houston', 'Ft. Smith'],
                     '6': ['Chicago', 'St. Louis', 'Nashville', 'New Orleans'],
                     '7': ['Pittsburg', 'Roanoke', 'Charlotte', 'Talluhassee'],
                     '8': ['MIT', 'Washington', 'Daytona Beach', 'Wilmington'],}


def enter_data(G):
    #start node
    G.add_edge('Start', 'Seattle', weight=0)
    G.add_edge('Start', 'Newport', weight=0)
    G.add_edge('Start', 'San Francisco', weight=0)
    G.add_edge('Start', 'USC', weight=0)
    #Day1
    G.add_edge('Seattle', 'Boise', weight=494)
    G.add_edge('Newport', 'Boise', weight=561)
    G.add_edge('San Francisco', 'Boise', weight=648)
    G.add_edge('San Francisco', 'Salt Lake', weight=748)
    G.add_edge('San Francisco', 'Las Vegas', weight=630)
    G.add_edge('USC', 'Las Vegas', weight=275)
    G.add_edge('USC', 'Tucson', weight=528)
    #day 2
    G.add_edge('Boise', 'Casper', weight=669)
    G.add_edge('Salt Lake', 'Casper', weight=402)
    G.add_edge('Salt Lake', 'Denver', weight=493)
    G.add_edge('Salt Lake', 'Albuquerque', weight=609)
    G.add_edge('Las Vegas', 'Albuquerque', weight=576)
    G.add_edge('Las Vegas', 'El Paso', weight=724)
    G.add_edge('Tucson', 'Albuquerque', weight=452)
    G.add_edge('Tucson', 'El Paso', weight=320)

    #day 3
    G.add_edge('Casper', 'Pierre', weight=347)
    G.add_edge('Casper', 'Lincoln', weight=635)
    G.add_edge('Casper', 'Amarillo', weight=705)
    G.add_edge('Denver', 'Pierre', weight=526)
    G.add_edge('Denver', 'Lincoln', weight=667)
    G.add_edge('Denver', 'Amarillo', weight=424)
    G.add_edge('Albuquerque', 'Amarillo', weight=288)
    G.add_edge('Albuquerque', 'San Antonio', weight=199)
    G.add_edge('El Paso', 'Amarillo', weight=421)
    G.add_edge('El Paso', 'San Antonio', weight=555)

    #day 4
    G.add_edge('Pierre', 'Minneapolis', weight=478)
    G.add_edge('Pierre', 'Kansas City', weight=598)
    G.add_edge('Lincoln', 'Minneapolis', weight=438)
    G.add_edge('Lincoln', 'Kansas City', weight=207)
    G.add_edge('Lincoln', 'Ft. Smith', weight=567)
    G.add_edge('Amarillo', 'Kansas City', weight=613)
    G.add_edge('Amarillo', 'Ft. Smith', weight=539)
    G.add_edge('Amarillo', 'Houston', weight=614)
    G.add_edge('San Antonio', 'Houston', weight=199)

    #day 5
    G.add_edge('Minneapolis', 'Chicago', weight=465)
    G.add_edge('Minneapolis', 'St. Louis', weight=593)
    G.add_edge('Kansas City', 'Chicago', weight=527)
    G.add_edge('Kansas City', 'St. Louis', weight=256)
    G.add_edge('Kansas City', 'Nashville', weight=618)
    G.add_edge('Ft. Smith', 'St. Louis', weight=545)
    G.add_edge('Ft. Smith', 'Nashville', weight=501)
    G.add_edge('Ft. Smith', 'New Orleans', weight=601)
    G.add_edge('Houston', 'New Orleans', weight=352)

    #day 6
    G.add_edge('Chicago', 'Pittsburg', weight=532)
    G.add_edge('Chicago', 'Roanoke', weight=717)
    G.add_edge('St. Louis', 'Pittsburg', weight=659)
    G.add_edge('St. Louis', 'Roanoke', weight=689)
    G.add_edge('Nashville', 'Roanoke', weight=435)
    G.add_edge('Nashville', 'Charlotte', weight=434)
    G.add_edge('Nashville', 'Talluhassee', weight=495)
    G.add_edge('New Orleans', 'Charlotte', weight=725)
    G.add_edge('New Orleans', 'Talluhassee', weight=388)

    #day 7
    G.add_edge('Pittsburg', 'MIT', weight=680)
    G.add_edge('Pittsburg', 'Washington', weight=259)
    G.add_edge('Roanoke', 'MIT', weight=750)
    G.add_edge('Roanoke', 'Washington', weight=233)
    G.add_edge('Roanoke', 'Wilmington', weight=306)
    G.add_edge('Roanoke', 'Daytona Beach', weight=480)
    G.add_edge('Charlotte', 'Washington', weight=397)
    G.add_edge('Charlotte', 'Wilmington', weight=206)
    G.add_edge('Charlotte', 'Daytona Beach', weight=480)
    G.add_edge('Talluhassee', 'Wilmington', weight=496)
    G.add_edge('Talluhassee', 'Daytona Beach', weight=316)


    #end nodes
    G.add_edge('MIT', 'End', weight=0)
    G.add_edge('Washington', 'End', weight=0)
    G.add_edge('Wilmington', 'End', weight=0)
    G.add_edge('Daytona Beach', 'End', weight=0)
    return G


def reduce_edge_node(netwgraph):
    """
    This function takes in the networkx graph constructed
    It go through the whole graph once and reduce edges to only the shortest edges to the next edge
    It then return a dictionary with the key as the left over nodes with the shortest total distance to that node
    """
    minimum_dis_dict = {}
    for node_list in Node_Dict:
        for node in Node_Dict[node_list]:
            minimum_dis_dict[node] = ['Start', 0]
    for current_edge in range(7):
        temp_dis_dict = {}
        next_nodes = Node_Dict[str(current_edge + 2)]
        previous_nodes = Node_Dict[str(current_edge + 1)]
        for node in next_nodes:
            total_previous_nodes = {}
            for predecessor in netwgraph.predecessors(node):
                previous_weight = minimum_dis_dict[predecessor][1]
                edge_weight = netwgraph.get_edge_data(predecessor, node)['weight']
                total_previous_nodes[str(previous_weight + edge_weight)] = predecessor
            min_weight = int(min(total_previous_nodes))
            min_predecessor = total_previous_nodes[str(min_weight)]
            minimum_dis_dict[node] = [min_predecessor, min_weight]
            temp_dis_dict[node] = [min_predecessor, min_weight]
        for node in temp_dis_dict.keys():
            if temp_dis_dict[node][0] in previous_nodes:
                previous_nodes.remove(temp_dis_dict[node][0])
        if previous_nodes != []:
            for previous_node in previous_nodes:
                minimum_dis_dict.pop(previous_node)
                Reduced_Node_Dict[str(current_edge + 1)].remove(previous_node)
    minimum_dis_dict.pop('Start')
    return minimum_dis_dict


def trace_back(route_dict, minimum_dis_dict):
    """
    This function takes in a blank dictionary to map the route
    It also intake the minimum distance dictionary generated by the reduce_edge_node function
    It then calculate backward and find the shortest route from the back to the front
    It return a dictionary with the key is the day and the value is a list
    exp dictionary: {day1: [location, total_distance to this location]}
    """
    for count in range(8):
        temp_dict = {}
        count_back_day = 8 - count
        possible_loc_list = Reduced_Node_Dict[str(count_back_day)]
        for loc in possible_loc_list:
            temp_dict[str(minimum_dis_dict[loc][1])] = loc
        min_distance_list = [int(i) for i in temp_dict.keys()]
        min_distance = min(min_distance_list)
        min_location = temp_dict[str(min_distance)]
        route_dict[str(count_back_day-1)] = [min_location, min_distance]
    return route_dict


def create_route_str(route_dict):
    """
    This function takes in the route dictionary generated by the trace_back function
    It return a string with two line
    The first line is the location of the shortest route with '>' separating each location
    The second line is the total distance to the location of shortest route with '>' separating each distances
    """
    location_str = 'Shortest route is: '
    distance_str = 'The sum distance is: '
    for day in range(8):
        location = route_dict[str(day)][0]
        distance = route_dict[str(day)][1]
        location_str = location_str + location + " > "
        distance_str = distance_str + str(distance) + " > "
    return location_str[:-3] + '\n' + distance_str[:-3]


def main():
    netwgraph = enter_data(nx.DiGraph())
    minimum_dis_dict = reduce_edge_node(netwgraph)
    route_dict = {}
    for day in range(8):
        route_dict[str(day)] = ['destination', 0]
    route_dict = trace_back(route_dict, minimum_dis_dict)
    route_str = create_route_str(route_dict)
    print(route_str)


main()

