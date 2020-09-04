def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_indices = {}
    
    for i in range(length): #looping through the weights length
        weight_needed = limit - weights[i] # substracting each numbers in weights from limit and storing in weight_needed
        
        if weight_needed in weight_indices:# storing calculated number (weight_needed) in the weight_indices dictionary
            j = weight_indices[weight_needed] # getting index from weight_indices associated withthe number and setting up to j which must be other number that is added to number in i to give total 21
            return [i, j]
        weight_indices[weights[i]] = i # getting index as i of other number that add to j to give 21 

    return None

print(get_indices_of_item_weights([ 4, 6, 10, 15, 16], 5, 21))