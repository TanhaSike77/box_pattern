import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("Start of the program.")

def factorial(n):
    logging.debug(f"calculating factorial of {n}")
    fact = 1
    for i in range(1, n+1):
        fact *= i
        logging.debug(f"i={i}, fact={fact}")
    logging.debug(f"End of factorial of {n}: {fact}")
    return fact
print(factorial(5))
logging.debug("End of the program.")