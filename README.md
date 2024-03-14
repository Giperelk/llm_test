# LLM Test Project

Welcome to the LLM Test Project for the Python Developer with AI Experience position. This application allows users to upload documents (PDF only) and receive answers to questions based on the content of all uploaded documents.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the project, you need to have Docker installed on your system. You can download it from Docker's official website.

### Installing

To set up the project environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Giperelk/llm_test.git
   ```
2. Run the init-config script from the Makefile to initialize the configuration:
   ```bash
   make init-config
   ```
3. Modify the .env file created by the script with your COHERE_API_KEY. You can obtain an API key from Cohere’s website.

### Running the Project

To start the project, use the following command:

   ```bash
   make run
   ```

This command will build the Docker image and run the containers in detached mode.

### Stopping the Project
To stop the project and remove the containers, use the command:

   ```bash
   make stop
   ```

## Usage
After starting the project, you can access the application through [your web browser](http://127.0.0.1:8000) to upload PDF documents and ask questions based on them.

## License
This project is licensed under the MIT License.
