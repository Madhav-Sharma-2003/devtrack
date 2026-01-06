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
        print("No topics available.")
        return

    print("\nYour Learning Topics:")
    for idx, topic in enumerate(topics, start=1):
        print(f"{idx}. {topic['name']} [{topic['status']}]")

    return topics


def add_topic(data):
    name = input("Enter new topic name: ").strip()

    if not name:
        print("Topic name cannot be empty.")
        return

    data["topics"].append({
        "name": name,
        "status": "pending"
    })
    save_data(data)
    print("Topic added successfully.")


def mark_completed(data):
    topics = show_topics(data)
    if not topics:
        return

    try:
        choice = int(input("Enter topic number to mark completed: "))
        if 1 <= choice <= len(topics):
            topics[choice - 1]["status"] = "completed"
            save_data(data)
            print("Topic marked as completed.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")


def edit_topic(data):
    topics = show_topics(data)
    if not topics:
        return

    try:
        choice = int(input("Enter topic number to edit: "))
        if 1 <= choice <= len(topics):
            new_name = input("Enter new topic name: ").strip()
            if not new_name:
                print("Topic name cannot be empty.")
                return

            topics[choice - 1]["name"] = new_name
            save_data(data)
            print("Topic updated successfully.")
        else:
            print("Invalid topic number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_topic(data):
    topics = show_topics(data)
    if not topics:
        return

    try:
        choice = int(input("Enter topic number to delete: "))
        if 1 <= choice <= len(topics):
            removed = topics.pop(choice - 1)
            save_data(data)
            print(f"Topic '{removed['name']}' deleted.")
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
    percentage = (completed / total) * 100

    print(f"\nProgress: {completed}/{total} completed")
    print(f"Completion Percentage: {percentage:.2f}%")


def main():
    data = load_data()

    while True:
        print("\n--- DevTrack Menu ---")
        print("1. View topics")
        print("2. Add topic")
        print("3. Mark topic as completed")
        print("4. Edit topic")
        print("5. Delete topic")
        print("6. View progress")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            show_topics(data)
        elif choice == "2":
            add_topic(data)
        elif choice == "3":
            mark_completed(data)
        elif choice == "4":
            edit_topic(data)
        elif choice == "5":
            delete_topic(data)
        elif choice == "6":
            show_progress(data)
        elif choice == "7":
            print("Goodbye! Keep learning 🚀")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
