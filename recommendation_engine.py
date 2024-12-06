import json

def load_database(file_name="resources.json"):
    with open(file_name, "r") as f:
        return json.load(f)

def load_tags(file_name="tags.json"):
    with open(file_name, "r") as f:
        return json.load(f)

def recommend_resources():
    resources = load_database()
    tags = load_tags()

    # Filter resources based on agreement
    agreed_resources = [
        res for res in resources
        if res["id"] in tags and tags[res["id"]]["ta1"] == tags[res["id"]]["ta2"]
    ]

    print("\nEnter Your Preferences:")
    topic = input("Preferred topic (Programming, Data Science, AI/ML, HCI, Security): ").lower()
    difficulty = input("Preferred difficulty (Beginner, Intermediate, Advanced): ").lower()
    content_type = input("Preferred content type (Video, Article, Book): ").lower()

    recommendations = [
        res for res in agreed_resources
        if (topic in res["topic"].lower())
        and (difficulty in res["difficulty"].lower())
        and (content_type in res["content_type"].lower())
    ]

    print("\nRecommended Resources:")
    if recommendations:
        for res in recommendations:
            print(f"- {res['title']} ({res['topic']}, {res['difficulty']}, {res['content_type']})")
    else:
        print("No recommendations found.")

if __name__ == "__main__":
    recommend_resources()
