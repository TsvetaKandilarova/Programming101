def sevens_in_a_row(arr, n):
    count_ = 0
    for item in arr:
        if item == 7:
            count_ += 1
            if count_ == n:
                return True
        else:
            count_ = 0
    return False
