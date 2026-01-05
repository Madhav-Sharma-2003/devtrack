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
    for idx, topic in enumerate(topics, start=1):
        status = topic["status"]
        print(f"{idx}. {topic['name']} [{status}]")


def add_topic(data):
    name = input("Enter topic name: ").strip()

    if not name:
        print("Topic name cannot be empty.")
        return

    topic = {
        "name": name,
        "status": "pending"
    }

    data["topics"].append(topic)
    save_data(data)
    print(f"Topic '{name}' added with status pending.")


def mark_completed(data):
    topics = data["topics"]

    if not topics:
        print("No topics to update.")
        return

    show_topics(data)

    try:
        choice = int(input("Enter topic number to mark completed: "))
        if 1 <= choice <= len(topics):
            topics[choice - 1]["status"] = "completed"
            save_data(data)
            print("Topic marked as completed ✅")
        else:
            print("Invalid topic number.")
    except ValueError:
        print("Please enter a valid number.")


def show_progress(data):
    topics = data["topics"]

    if not topics:
        print("No topics added yet.")
        return

    completed = sum(1 for t in topics if t["status"] == "completed")
    total = len(topics)
    progress = (completed / total) * 100

    print(f"\nProgress: {completed}/{total} topics completed")
    print(f"Completion Percentage: {progress:.2f}%")


def main():
    data = load_data()

    while True:
        print("\n--- DevTrack Menu ---")
        print("1. View topics")
        print("2. Add new topic")
        print("3. Mark topic as completed")
        print("4. View progress")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_topics(data)
        elif choice == "2":
            add_topic(data)
        elif choice == "3":
            mark_completed(data)
        elif choice == "4":
            show_progress(data)
        elif choice == "5":
            print("Goodbye! Keep learning 🚀")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
