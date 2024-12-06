import json
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def load_database(file_name="resources.json"):
    with open(file_name, "r") as f:
        return json.load(f)

def filter_resources(topic=None, difficulty=None, content_type=None):
    resources = load_database()

    # Apply filters
    filtered_resources = resources
    if topic:
        filtered_resources = [res for res in filtered_resources if topic.lower() in res["topic"].lower()]
    if difficulty:
        filtered_resources = [res for res in filtered_resources if difficulty.lower() in res["difficulty"].lower()]
    if content_type:
        filtered_resources = [res for res in filtered_resources if content_type.lower() in res["content_type"].lower()]
    
    return filtered_resources

def faceted_navigation():
    resources = load_database()

    # Autocomplete lists
    topics = list(set(res["topic"] for res in resources))
    difficulties = list(set(res["difficulty"] for res in resources))
    content_types = list(set(res["content_type"] for res in resources))

    topic_completer = WordCompleter(topics, ignore_case=True)
    difficulty_completer = WordCompleter(difficulties, ignore_case=True)
    content_type_completer = WordCompleter(content_types, ignore_case=True)

    print("Faceted Navigation:")
    
    # Interactive prompts with auto-completion
    topic = prompt("Enter topic (autocomplete available): ", completer=topic_completer)
    difficulty = prompt("Enter difficulty (autocomplete available): ", completer=difficulty_completer)
    content_type = prompt("Enter content type (autocomplete available): ", completer=content_type_completer)

    # Filter resources
    filtered = filter_resources(topic=topic, difficulty=difficulty, content_type=content_type)

    # Display results
    print("\nFiltered Resources:")
    if filtered:
        for res in filtered:
            print(f"- {res['title']} ({res['topic']}, {res['difficulty']}, {res['content_type']})")
    else:
        print("No resources found matching your criteria.")

if __name__ == "__main__":
    faceted_navigation()
