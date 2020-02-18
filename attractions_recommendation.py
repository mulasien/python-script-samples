# This script will build an attractions recommendation engine based on the location a traveler is going to,
# and what they are interest in seeing.

# create sample list of destinations
destinations = [
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "São Paulo, Brazil",
    "Cairo, Egypt",
]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

# create a function to return the index location of a requested destination from our list 'destinations'


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


# print(get_destination_index("Paris, France")) should return 0

# print(get_destination_index("Hyderabad, India") # this will fail on purpose with a value error. We'll have to fix this later

# create a function to get a traveler's location index from an example traveler's info (such as test_traveler)
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


# create variable of result of passing our test traveler through our get_traveler_location function, which passes through the get_destination_index function
# this is an example of a function calling on another function
test_destination_index = get_traveler_location(test_traveler)

# print(test_destination_index)

# create an empty list of attractions, that actually creates an empty list for every location in destinations list

attractions = [[] for destination in destinations]

# print(attractions)

# create function to add an attraction, passing destination and attraction


def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(attraction)
        return
    except SyntaxError:
        return


# test above function
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])

# print(attractions)

# OK, let's add a whole bunch more attraction entries to populate our attractions list

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction(
    "Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]]
)
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# print(attractions)

# Build an INTEREST FINDER
# Write a function called find_attractions() that takes two parameters: destination,
# the name of the destination and interests, a list of interests.
# Given a list of interests that match the location, it will return an attraction to match those interests


def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []

    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]

        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])

    return attractions_with_interest


# time to test. Call on find_attractions function with a location and an interest, then print the result
la_arts = find_attractions("Los Angeles, USA", ["art"])

# print(la_arts)

# Now for what we care about: connecting people with attractions they want to see


def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]

    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    interests_string = (
        "Hi "
        + traveler[0]
        + ", we think you'll like these places around "
        + traveler_destination
        + ": "
    )
    # Check if attraction is last in list or not. This will affect formatting
    for i in range(len(traveler_attractions)):
        if traveler_attractions[-1] == traveler_attractions[i]:
            interests_string += "the " + traveler_attractions[i] + "."
        else:
            interests_string += "the " + traveler_attractions[i] + ", "

    return interests_string


# test it out
smills_france = get_attractions_for_traveler(
    ["Dereck Smill", "Paris, France", ["monument"]]
)

print(smills_france)
