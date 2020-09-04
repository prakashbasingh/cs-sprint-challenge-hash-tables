def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    dup_pos_neg_num = {}
    
    for num in a:
        target_num = num * -1
        
        if target_num in dup_pos_neg_num:
            
            if num > target_num:
                result.append(num)
            else:
                result.append(target_num)
                
        else:
            dup_pos_neg_num[num] = target_num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
