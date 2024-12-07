# Study Resource Recommender

## Introduction
This project, "Study Resource Recommender," is designed to help MIMS students access curated study materials based on their preferences for topics, content types, and, most importantly, agreement by TAs. Implemented in Python, the system utilizes structured JSON datasets to store resource metadata, enabling efficient retrieval and manipulation.
**Interface for TAs:** At the core of the solution is a tagging system that allows TAs to annotate resources independently. The reliability of their annotations is evaluated using Cohen's Kappa, ensuring that only highly agreed-upon resources are prioritized for recommendations. This fosters a robust and consensus-driven approach to resource selection.
**Interface for Students:** For students, the system offers a faceted navigation interface through an interactive CLI, allowing dynamic filtering of resources based on multiple attributes. Enhanced with autocomplete functionality, this interface ensures ease of use and efficiency. The recommendation engine further refines the experience by integrating student preferences with quality-assessed tags to deliver personalized and reliable study resource suggestions.
Each feature—tagging, navigation, and recommendation—functions as a modular component, collectively creating a comprehensive and reliable system for information discovery and resource recommendation.

## Key Features
1. **JSON Dataset**: 
   - Resources and tags are stored in separate JSON files.
   - The resources JSON file includes attributes like ID, title, topic, difficulty, and content type.
   - The tags JSON file records annotations provided by TAs, including agreement metrics for quality control.

2. **Cohen's Kappa**:
   - Used to evaluate inter-annotator agreement between two TAs tagging study resources.
   - Ensures that only resources with high agreement are prioritized for recommendations.

3. **Faceted Navigation with Ranking**:
   - Provides an interactive CLI for filtering resources based on topic, difficulty, and content type.
   - Autocomplete functionality enhances usability and reduces input errors.
   - Filters are combined with sorting by agreement, ensuring that highly agreed-upon resources are ranked higher in the results.

## How It Works
- **Resource Tagging**: TAs independently tag resources, and their agreement is evaluated using Cohen's Kappa.
- **Faceted Navigation**: Students filter resources interactively, with results ranked by agreement level to prioritize reliable suggestions.
- **JSON Data Management**: Resources and tags are modularly stored and retrieved, ensuring scalability and data integrity.

## Files and Functionality
- `database_setup.py`: Generates a JSON dataset of study resources.
- `resource_tagging.py`: Allows TAs to annotate resources and calculates Cohen's Kappa for agreement.
- `faceted_navigation.py`: Implements faceted navigation with filtering and ranking based on tagging agreement.

## Usage Instructions
1. **Set Up**:
   - Run `database_setup.py` to generate the resources JSON dataset.
   - Tag resources using `resource_tagging.py` to record annotations and calculate agreement.

2. **Faceted Navigation**:
   - Use `faceted_navigation.py` to filter and sort resources interactively.

3. **Example Commands**:
   - Generate dataset:
     ```bash
     python database_setup.py
     ```
   - Tag resources and calculate agreement:
     ```bash
     python resource_tagging.py
     ```
   - Explore resources using faceted navigation:
     ```bash
     python faceted_navigation.py
     ```

## Concepts Connected to INFO 202
- **JSON Dataset**: Demonstrates structured data storage and metadata principles for efficient retrieval.
- **Cohen's Kappa**: Reflects inter-annotator reliability, ensuring only high-quality resources are recommended.
- **Faceted Navigation**: Aligns with metadata-rich systems for efficient information retrieval and dynamic querying.

## Future Enhancements
- Add machine learning for collaborative filtering to enhance personalization.
- Develop a web-based interface for broader accessibility.
- Expand the dataset with more diverse resources and tagging attributes.

---
