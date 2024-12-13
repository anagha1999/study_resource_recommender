import json

def create_database(file_name="resources.json"):
    resources = [
        # Programming
        {"id": 1, "title": "Automate the Boring Stuff with Python", "topic": "Programming", "difficulty": "Beginner", "content_type": "Book"},
        {"id": 2, "title": "CS50's Introduction to Computer Science", "topic": "Programming", "difficulty": "Beginner", "content_type": "Video"},
        {"id": 3, "title": "Cracking the Coding Interview", "topic": "Programming", "difficulty": "Intermediate", "content_type": "Book"},
        {"id": 4, "title": "Advanced Python Programming", "topic": "Programming", "difficulty": "Advanced", "content_type": "Book"},
        
        # Data Science
        {"id": 5, "title": "Data Science from Scratch", "topic": "Data Science", "difficulty": "Beginner", "content_type": "Book"},
        {"id": 6, "title": "Introduction to Data Science by Coursera", "topic": "Data Science", "difficulty": "Beginner", "content_type": "Video"},
        {"id": 7, "title": "Practical Statistics for Data Scientists", "topic": "Data Science", "difficulty": "Intermediate", "content_type": "Book"},
        {"id": 8, "title": "Python for Data Analysis", "topic": "Data Science", "difficulty": "Intermediate", "content_type": "Book"},
        
        # AI/ML
        {"id": 9, "title": "Deep Learning Specialization by Andrew Ng", "topic": "AI/ML", "difficulty": "Beginner", "content_type": "Video"},
        {"id": 10, "title": "Hands-On Machine Learning with Scikit-Learn and TensorFlow", "topic": "AI/ML", "difficulty": "Intermediate", "content_type": "Book"},
        {"id": 11, "title": "Reinforcement Learning: An Introduction", "topic": "AI/ML", "difficulty": "Advanced", "content_type": "Book"},
        {"id": 12, "title": "AI for Everyone by Andrew Ng", "topic": "AI/ML", "difficulty": "Beginner", "content_type": "Video"},
        
        # HCI
        {"id": 13, "title": "The Design of Everyday Things", "topic": "HCI", "difficulty": "Beginner", "content_type": "Book"},
        {"id": 14, "title": "Don't Make Me Think: A Common Sense Approach to Web Usability", "topic": "HCI", "difficulty": "Intermediate", "content_type": "Book"},
        {"id": 15, "title": "Human-Computer Interaction", "topic": "HCI", "difficulty": "Advanced", "content_type": "Book"},
        {"id": 16, "title": "Interaction Design Foundation Courses", "topic": "HCI", "difficulty": "Beginner", "content_type": "Video"},
        
        # Security
        {"id": 17, "title": "Cybersecurity for Beginners", "topic": "Security", "difficulty": "Beginner", "content_type": "Book"},
        {"id": 18, "title": "The Web Application Hacker's Handbook", "topic": "Security", "difficulty": "Intermediate", "content_type": "Book"},
        {"id": 19, "title": "Practical Malware Analysis", "topic": "Security", "difficulty": "Advanced", "content_type": "Book"},
        {"id": 20, "title": "Introduction to Cybersecurity by IBM", "topic": "Security", "difficulty": "Beginner", "content_type": "Video"}
    ]

    with open(file_name, "w") as f:
        json.dump(resources, f, indent=4)
    print(f"Database created in {file_name}")

if __name__ == "__main__":
    create_database()
