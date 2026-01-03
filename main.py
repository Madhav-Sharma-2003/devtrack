import json
DATA_FILE = "data/progress.json"

def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)
    
def show_topics():
    data = load_data()
    topics = data["topics"]

    if not topics:
        print("No topics added yet.")
        return
    
    print("Your Learning Topics:")
    for idx, topic in enumerate(topics, start = 1):
        print(f"{idx}.{topic}")



def main():
    print("Welcome to DevTrack - Day 2")
    show_topics()

if __name__ == "__main__":
    main()