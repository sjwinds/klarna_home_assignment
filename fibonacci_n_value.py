from datetime import datetime
# set the largest value for fibonacci calculation
MAX_FIBONACCI_VALUE = 1000

# def function to calculate the nth value of fibonacci series
def fibonacci_n_value(input_value):
    pos_n_int = int(input_value)

    # check if input bug
    assert isinstance(pos_n_int,(int))
    assert pos_n_int >= 0
    assert pos_n_int < MAX_FIBONACCI_VALUE

    # predefine first 2 values in fibonacci series
    sequence = [0,1]
    start_time = datetime.now()
    if pos_n_int >2:
        for f in range(2, pos_n_int):
            parent = sequence[-1]
            grandparent = sequence[-2]
            sequence.append(grandparent + parent)
            print(sequence[f])
    end_time = datetime.now()
    time_diff = end_time - start_time
    return (str(sequence[pos_n_int - 1]), print(str(time_diff)))