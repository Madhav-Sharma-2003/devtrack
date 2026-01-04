import json
DATA_FILE = "data/progress.json"

def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
    
def show_topics(data):
    topics = data["topics"]

    if not topics:
        print("No topics added yet.")
        return
    
    print("\nYour Learning Topics:")
    for idx, topic in enumerate(topics, start = 1):
        print(f"{idx}.{topic}")

def add_topic(data):
    topic = input("Enter topic name: ").strip()

    if not topic:
        print("Topic name cannot be empty.")
        return

    data["topics"].append(topic)
    save_data(data)
    print(f"Topic '{topic}' added successfully.")

def main():
    data = load_data()

    while True:
        print("\n --- DevTrack Menu ---")
        print("1. View Topics")
        print("2. Add  new Topic")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            show_topics(data)
        elif choice == "2":
            add_topic(data)
        elif choice == "3":
            print("Goodbye! Keep learning!")
            break
        else:
            print("Invalid choice .Please try again.")

if __name__ == "__main__":
    main()