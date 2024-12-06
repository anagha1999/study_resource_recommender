
# Study Resource Recommender

## Introduction
This project aims to build a system that helps MIMS students access curated study resources based on topics, difficulty levels, and content types. The system leverages JSON datasets, Cohen's Kappa for inter-annotator agreement, and faceted navigation to provide reliable and flexible recommendations. The project's functionality is modular, allowing tagging, navigation, and recommendation tasks to be performed independently or in conjunction.

## Key Features
1. **JSON Dataset**: 
   - Resources are stored in a lightweight, structured JSON format. 
   - The dataset includes metadata like ID, title, topic, difficulty, and content type, ensuring efficient retrieval and manipulation.
   - Supports dynamic querying for navigation and recommendation tasks.

2. **Cohen's Kappa**:
   - Used to evaluate inter-annotator agreement between two TAs tagging study resources.
   - Ensures that resources with high annotation agreement are prioritized for recommendations.
   - Provides a robust measure of tagging reliability by accounting for chance agreements.

3. **Faceted Navigation**:
   - Allows users to filter resources based on multiple attributes, including topic, difficulty, and content type.
   - Features autocomplete functionality to enhance user experience and reduce input errors.
   - Enables flexible exploration and refinement of search queries.

## How It Works
- **Resource Tagging**: The interface allows 2 TAs to independently tag resources, and the system calculates Cohen's Kappa to determine agreement levels.
- **Faceted Navigation**: Users can filter resources dynamically using various facets to meet specific needs.
- **Recommendation Engine**: Students receive recommendations based on their preferences and the reliability of the tagged resources.

## Files and Functionality
- `database_setup.py`: Creates a JSON dataset of study resources.
- `resource_tagging.py`: Enables TAs to tag resources and calculates Cohen's Kappa.
- `faceted_navigation.py`: Implements faceted search with autocomplete for efficient resource discovery.
- `recommendation_engine.py`: Provides tailored recommendations based on student preferences and tagging agreement.

## Usage Instructions
1. **Set Up**:
   - Run `pip install prompt_toolkit`
   - Run `database_setup.py` to generate the JSON dataset.
   - Tag resources using `resource_tagging.py` to build a reliable foundation.

2. **Navigate Resources**:
   - Use `faceted_navigation.py` to explore the dataset interactively.

3. **Get Recommendations**:
   - Use `recommendation_engine.py` to receive personalized study resource suggestions.

## Concepts Connected to INFO 202
- **JSON Dataset**: Demonstrates structured data storage and metadata principles.
- **Cohen's Kappa**: Reflects inter-annotator reliability, ensuring high-quality tagging.
- **Faceted Navigation**: Aligns with faceted metadata systems for efficient information retrieval.

## Future Enhancements
- Integration of machine learning for collaborative filtering.
- Development of a web-based interface for broader accessibility.
- Addition of more resource categories and metadata attributes.
