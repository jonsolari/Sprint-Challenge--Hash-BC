from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length -1)

    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    temp = None

    if hash_table_retrieve(hashtable, "NONE") is not None:
        temp = hash_table_retrieve(hashtable, "NONE")

    i = 0
    while i < len(route):
        route[i] = temp
        temp = hash_table_retrieve(hashtable, temp)
        i+=1

    return route






ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
reconstruct_trip(tickets, 3)
