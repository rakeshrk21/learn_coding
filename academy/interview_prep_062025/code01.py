    # Input:
        # "Chennai" -> "Bangalore"
        # "Bombay" -> "Delhi"
        # "Goa"    -> "Chennai"
        # "Delhi"  -> "Goa"

    # 1. Find start and end cities in itinerary
    # 2. Find complete itinerary
    # Output:
        # Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Bangalore,

def print_itinerary():
    d = {
            "Chennai": "Bangalore",
            "Bombay": "Delhi",
            "Goa" : "Chennai",
            "Delhi" : "Goa"
        }
        # source - find a key which is not in the value
        # destination - find a value which is not in the key
    destinations  = d.values()
    sources = d.keys()
    for key in sources:
        if key not in destinations:
            source = key
            break

    for val in destinations:
        if val not in sources:
            destination = val
            break

    x = filter(lambda s: s not in destinations, sources)
    print(x)
    while True:
        destination = d[source]
        print( f'{source} -> {destination}')
        source = destination
        try:
            d[source]
        except KeyError:
            pass

if __name__ == "__main__":
    print_itinerary()