import datetime
from collections import Counter


VALID_COMMANDS = ["hello", "hi", "date", "time", "list operations", "generate prime", "search history", "bye"]


chat_history = []

def log_chat(user_input, chatbot_response):
    """Logs user input and chatbot response."""
    chat_history.append(f"User: {user_input}")
    chat_history.append(f"Chatbot: {chatbot_response}")

def get_date_time():
    """Returns the current date and time."""
    now = datetime.datetime.now()
    return now.strftime("%d %B %Y, %I:%M %p")

def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def handle_list_operations():
    """Handles list operations (sum, max, reverse, remove duplicates)."""
    print("Chatbot: Please enter a list of integers (comma-separated, integer): ")
    user_input = input("User: ").strip()
    
    try:
        numbers = list(map(int, user_input.split(",")))
    except ValueError:
        print("Chatbot: Error: The list must contain only integers separated by commas.")
        return

    sum_numbers = sum(numbers)
    max_number = max(numbers)
    reversed_list = list(reversed(numbers))
    duplicates = count_duplicate(numbers)
    
    response = f"  Sum: {sum_numbers}\n  Maximum: {max_number}\n  Reversed List: {reversed_list}\n Duplicates: {duplicates}"
    print(f"Chatbot:\n{response}")

    if duplicates:
        print("Chatbot: Would you like to remove duplicates? (yes/no)")
        choice = input("User: ").strip().lower()

        if choice == "yes":
            numbers = sorted(set(numbers))
            print(f"Chatbot:\n  Updated List: {numbers}\n  Removed duplicates successfully.")

    return response


def count_duplicate(lst):
    freq={}
    for item in lst:
        if item in freq:
            freq[item]+=1
        else:
            freq[item]=1
    dup = {}
    for key in freq:
        if freq[key] >1:
            dup [ key] = freq [key]
    return dup


    
    print("Chatbot: Would you like to remove duplicates? (yes/no)")

    choice = input("User: ").strip().lower()
    
    if choice == "yes":
        numbers = sorted(set(numbers))
        print(f"Chatbot:\n  Updated List: {numbers}\n  Removed duplicates successfully.")  # Updated message
    
    return response

def handle_prime_numbers():
    """Handles prime number generation within a range."""
    print("Chatbot: Enter the range (start and end): ")
    user_input = input("User: ").strip()
    
    try:
        start, end = map(int, user_input.split(","))
    except ValueError:
        print("Chatbot: Error: Please enter two integers separated by a comma.")
        return

    primes = [n for n in range(start, end + 1) if is_prime(n)]
    print(f"Chatbot:\n  Prime Numbers: {primes}")
    
    return f"  Prime Numbers: {primes}"


def handle_search_history():
    """Searches the chat history for a keyword."""
    print("Chatbot: Enter the keyword to search in chat history:")
    keyword = input("User: ").strip().lower()
    
    found_lines = [line for line in chat_history if keyword in line.lower()]
    
    if found_lines:
        return "\n".join(found_lines)
    else:
        return "No matching records found."

def handle_session_summary():
    """Generates and saves the session summary before asking to save."""
    
    
    commands_used = [line.split(":")[1].strip() for line in chat_history if line.startswith("User:")]
    command_count = len(commands_used)
    
    
    most_frequent_command = max(set(commands_used), key=commands_used.count) if commands_used else "None"
    
    
    summary = f"Your session:\n   - Commands Used: {command_count}\n   - Most Frequent Command: {most_frequent_command}"
    
    
    print(f"Chatbot: {summary}")
    
    
    print("Chatbot: Do you want to save this summary? (yes/no)")
    choice = input("User: ").strip().lower()
    
    if choice == "yes":
        filename = f"summary_{datetime.datetime.now().strftime('%d%m%Y')}.txt"
        with open(filename, "w") as file:
            file.write(summary)
        print(f"Chatbot: Summary saved to {filename} (saved on desktop)")
    
    print("Chatbot: Goodbye! Have a great day!")
    return "Bye, have a good day!"



def chatbot():
    """Main chatbot loop."""
    print("Chatbot: Hello! I’m your assistant! How can I help you today?")
    log_chat("", "Hello! I’m your assistant! How can I help you today?")
    
    while True:
        user_input = input("User: ").strip().lower()
        
        if user_input not in VALID_COMMANDS:
            response = "Enter correct keyword"
        elif user_input == "date" or user_input == "time":
            response = get_date_time()
        elif user_input == "list operations":
            response = handle_list_operations()
        elif user_input == "generate prime":
            response = handle_prime_numbers()
        elif user_input == "search history":
            response = handle_search_history()
        elif user_input == "bye":
            response = handle_session_summary()
            print("Chatbot: Bye, have a good day!")
            break
        else:
            response = "Hi there! How can I help you today?"
        
        log_chat(user_input, response)
        print(f"Chatbot: {response}")
        
        if user_input in ["date", "time", "list operations", "generate prime", "search history"]:
            print("Chatbot: How else can I assist you?")



if __name__ == "__main__":
    chatbot()


