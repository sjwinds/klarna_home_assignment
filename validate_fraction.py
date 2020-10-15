# Function to check if fraction is input
def validate(n):
    values = n.split('.')
    return len(values) == 2 and all(i.isdigit() for i in values)