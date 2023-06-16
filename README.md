# Laook Recipe Finder

This is the backend service of Laook. Laook Recipe Finder is an innovative app that simplifies the process of finding recipes based on the ingredients you have on hand. With Laook, users can take a picture of the ingredients they have, leverage powerful image recognition technology, and receive a list of recognized ingredients.

## Features

- **Ingredient Recognition**: Take a picture of your ingredients using the app, and the image recognition model will identify the ingredients present in the image.
- **Ingredient Modification**: In case of any mismatches or inaccuracies, users have the flexibility to modify the list of recognized ingredients manually.
- **Recipe Recommendations**: After finalizing the list of ingredients, Laook provides users with a curated list of food menus and recipes that can be prepared using the given ingredients.
- **User-friendly Interface**: Laook offers an intuitive and user-friendly interface, making it easy for users to capture and modify ingredient images, view ingredient lists, and explore recipe suggestions.

## Staging Test
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/10569299-cdf150eb-466e-4a83-b17e-7fb33c136524?action=collection%2Ffork&collection-url=entityId%3D10569299-cdf150eb-466e-4a83-b17e-7fb33c136524%26entityType%3Dcollection%26workspaceId%3D7778e172-9e48-49c8-a63a-9853bec604fa)

## Getting Started

To run the Laook backend service locally, follow the steps below:

### Prerequisites

- Python 3.7 or higher
- Docker (optional)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Bangkit-Laook/backend.git
   cd laook
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   # For Unix-based system (Max/Linux)
   python3 -m venv venv
   source venv/bin/activate
   ```

   ```bash
   # For Windows system
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. Start the Laook server:

   ```bash
   uvicorn main:app --reload
   ```

2. Open your web browser and go to "http://localhost:8000" to access the Laook Recipe Finder app.

### Dockerizing the App

To run the app using Docker, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t laook .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 laook
   ```

3. Open your web browser and go to "http://localhost:8000" to access the Laook Recipe Finder app.

## Contributing

Contributions to Laook Recipe Finder are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
# 2laook-backend
# 2laook-backend
# laook-backend
