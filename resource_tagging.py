import json

def load_database(file_name="resources.json"):
    with open(file_name, "r") as f:
        return json.load(f)

def save_tags(resource_tags, file_name="tags.json"):
    """
    Save tags along with resource IDs.
    Format: {"resource_id": {"ta1": tag1, "ta2": tag2}}
    """
    with open(file_name, "w") as f:
        json.dump(resource_tags, f, indent=4)
    print(f"Tags saved in {file_name}")

def calculate_cohen_kappa(tags):
    """
    Calculate Cohen's Kappa based on saved tags.
    """
    ta1_tags = [tags[res_id]["ta1"] for res_id in tags]
    ta2_tags = [tags[res_id]["ta2"] for res_id in tags]

    n = len(ta1_tags)
    agreements = sum(1 for i in range(n) if ta1_tags[i] == ta2_tags[i])
    po = agreements / n

    category_counts_ta1 = {tag: ta1_tags.count(tag) for tag in set(ta1_tags)}
    category_counts_ta2 = {tag: ta2_tags.count(tag) for tag in set(ta2_tags)}

    pe = sum(
        (category_counts_ta1.get(cat, 0) / n) * (category_counts_ta2.get(cat, 0) / n)
        for cat in set(ta1_tags + ta2_tags)
    )

    kappa = (po - pe) / (1 - pe) if (1 - pe) != 0 else 0
    return kappa

def tag_resources():
    resources = load_database()
    resource_tags = {}

    print("Available Resources:")
    for resource in resources:
        print(f"{resource['id']}: {resource['title']} ({resource['topic']}, {resource['difficulty']}, {resource['content_type']})")

    print("\nSelect resource IDs to tag. Type 'done' to finish.")
    while True:
        resource_id = input("Enter resource ID to tag or 'done': ")
        if resource_id.lower() == 'done':
            break
        resource_id = int(resource_id)
        selected_resource = next((res for res in resources if res["id"] == resource_id), None)

        if selected_resource:
            print(f"Selected Resource: {selected_resource['title']}")
            tag1 = input("TA1: Enter topic tag (1-Programming, 2-Data Science, 3-AI/ML, 4-HCI, 5-Security): ")
            tag2 = input("TA2: Enter topic tag (1-Programming, 2-Data Science, 3-AI/ML, 4-HCI, 5-Security): ")
            resource_tags[resource_id] = {"ta1": int(tag1), "ta2": int(tag2)}
        else:
            print("Invalid resource ID.")

    kappa_score = calculate_cohen_kappa(resource_tags)
    print(f"\nCohen's Kappa Score for Inter-Annotator Agreement: {kappa_score}")

    save_tags(resource_tags)

if __name__ == "__main__":
    tag_resources()
