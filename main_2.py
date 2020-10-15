from flask import Flask, render_template, request
from fibonacci_n_value import fibonacci_n_value, MAX_FIBONACCI_VALUE
from ackermann import ackermann
import sys, math
from validate_fraction import validate
from is_string_or_num import is_string_or_num
from datetime import datetime

sys.setrecursionlimit(1500)

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('indexd.html')

@app.route("/calc1", methods = ["POST"])
def calc1():
    # Get the input number
    input_number = request.form.get("number1")
    
    if validate(input_number):
        return "Fraction not accepted. Please input positive integer"
        # No number input, show "Please input postive number"
    if not input_number:
        return "Please input postive number"
    
    # Convert string to integer
    input_number = int(input_number)
    # negative number input, show " Please input postive and integer number"
    if input_number < 0:
        return " Please input postive and integer number"
    # input number exceeding limit, show " The input value is exceeding limit"
    elif input_number > MAX_FIBONACCI_VALUE:
        return f"The input value is: {format(input_number)} + exceeding limit + {MAX_FIBONACCI_VALUE}"
    else:
        return fibonacci_n_value(input_number)
    
@app.route("/calc2", methods = ["POST"])
def calc2():
    from datetime import datetime
    # Get input string
    input_number_m = request.form.get("number2")
    input_number_n = request.form.get("number3")
    # if input is fraction, return message "Fraction not accepted. Please input positive integer"
    if validate(input_number_m) and validate(input_number_n):
        return "Fraction not accepted. Please input positive integer"
    
    # No number input or string input, show "Please input postive number"
    if not input_number_m or not input_number_n:
        return "Please input postive integer"
    
    # convert string to int
    input_number_m = int(input_number_m)
    input_number_n = int(input_number_n)
    # if input numbers less than 0, show "Please input positive numbes"
    if input_number_m <0 or input_number_n <0:
        return " Please input postive integers"
    # call ackermann function, return result and running time
    else:
        print(input_number_m)
        print(input_number_n)
        start_time = datetime.now()
        ack = ackermann(input_number_m, input_number_n)
        end_time = datetime.now()
        time_diff = end_time - start_time
        return str(ack), print(f"Running time: {time_diff}")
   
@app.route("/calc3", methods = ["POST"])
def calc3():
    # Get input string
    input_number = request.form.get("number4")
    
    # if input is fraction, return message "Fraction not accepted. Please input positive integer"
    if validate(input_number):
        return "Fraction not accepted. Please input positive integer"
    
    
     # No number input, show "Please input postive number"
    if not input_number:
        return "Please input postive integer"

    input_number = int(input_number)
    # negative number input, show " Please input postive and integer number"
    if input_number < 0:
        return " Please input postive integer"
    # calculate factorial and time used to run 
    else:
        print(f"Input number is {input_number}")
        start_time = datetime.now()
        run_factorial = math.factorial(input_number)
        end_time = datetime.now()
        time_diff = end_time - start_time
        return str(run_factorial), print(f"Runnng time: {time_diff}")

if __name__ == "__main__":
    app.run(debug = True)