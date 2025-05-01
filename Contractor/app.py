class Logger:
    def __init__(self):
        # Constructor: Called when an object is created
        print("Logger object has been created.")

    def __del__(self):
        # Destructor: Called when an object is destroyed
        print("Logger object has been destroyed.")

# Example usage
if __name__ == "__main__":
    log = Logger()  # Create an object (constructor is called)
    del log          # Explicitly delete the object (destructor is called)