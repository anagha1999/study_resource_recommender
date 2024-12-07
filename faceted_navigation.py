import json

def load_database(file_name="resources.json"):
    """Load resources from JSON file."""
    with open(file_name, "r") as f:
        return json.load(f)

def load_tags(file_name="tags.json"):
    """Load tags from JSON file."""
    with open(file_name, "r") as f:
        return json.load(f)

def calculate_cohen_kappa(tags):
    """Calculate Cohen's Kappa for agreement."""
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

def sort_resources_by_agreement(resources, tags):
    """
    Sort resources based on agreement between TA annotations.
    Resources with high agreement are ranked higher.
    """
    resources_with_agreement = []
    for res in resources:
        res_id = res["id"]
        if res_id in tags and tags[res_id]["ta1"] == tags[res_id]["ta2"]:
            resources_with_agreement.append(res)

    return sorted(resources_with_agreement, key=lambda r: r["id"])

def filter_and_sort_resources(resources, tags, topic=None, difficulty=None, content_type=None):
    """
    Filter resources based on user input and sort them based on agreement.
    """
    filtered_resources = resources
    if topic:
        filtered_resources = [res for res in filtered_resources if topic.lower() in res["topic"].lower()]
    if difficulty:
        filtered_resources = [res for res in filtered_resources if difficulty.lower() in res["difficulty"].lower()]
    if content_type:
        filtered_resources = [res for res in filtered_resources if content_type.lower() in res["content_type"].lower()]

    # Sort by agreement
    return sort_resources_by_agreement(filtered_resources, tags)

def faceted_navigation():
    resources = load_database()
    tags = load_tags()

    print("\nFaceted Navigation:")
    print("Enter filtering criteria (or leave blank to skip):")
    topic = input("Preferred topic (e.g., Programming, Data Science): ").strip()
    difficulty = input("Preferred difficulty (e.g., Beginner, Intermediate): ").strip()
    content_type = input("Preferred content type (e.g., Video, Article): ").strip()

    # Filter and sort resources
    filtered_resources = filter_and_sort_resources(resources, tags, topic, difficulty, content_type)

    print("\nRecommended Resources (sorted by agreement):")
    if filtered_resources:
        for res in filtered_resources:
            print(f"- {res['title']} ({res['topic']}, {res['difficulty']}, {res['content_type']})")
    else:
        print("No resources found matching your criteria.")

if __name__ == "__main__":
    faceted_navigation()
