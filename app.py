from flask import Flask, render_template, request
import time

app = Flask(__name__)

def prime_eratosthenes(n):
    start_time = time.time()  # Record the start time
    prime_list = []
    non_prime_list = []  # Create an empty list to store non_prime numbers
    # Iterate through the numbers from 2 to 'n'
    for i in range(2, n+1):
        if i not in non_prime_list:
            # If 'i' is not in the 'non_prime_list,' it's a prime number; add it to prime_list
            prime_list.append(i)

            # Mark all multiples of 'i' as non-prime by adding them to 'non_prime_list'
            for j in range(i*i, n+1, i):
                non_prime_list.append(j)
    end_time = time.time()  # Record the end time
    time_taken = end_time - start_time
    highest_prime = prime_list[-1]
    prime_list_str = ', '.join(map(str, prime_list))
    return highest_prime, time_taken, prime_list_str

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num = int(request.form['num'])
        highest_prime, time_taken, prime_list = prime_eratosthenes(num)
        return render_template('result.html', highest_prime=highest_prime, time_taken=time_taken, prime_list=prime_list)

if __name__ == '__main__':
    app.run(debug=True)
