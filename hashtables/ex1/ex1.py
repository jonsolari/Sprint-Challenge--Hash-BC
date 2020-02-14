from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    output1 = None
    output2 = None

    i = 0
    while i < len(weights):
        hash_table_insert(ht, weights[i], i)
        i += 1

    for j in weights:
        if hash_table_retrieve(ht, (limit - j)) is not None:
            output1 = hash_table_retrieve(ht, (limit - j))
            output2 = hash_table_retrieve(ht, j)
            j+=1
        

    output = [output2, output1]

    

    if output1 is None or output2 is None:
        return None
    else:
        return output
  
    
  
    # return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

get_indices_of_item_weights([4, 4], 2, 8)