# Agentic Chat Bot for Restaurant Insights

This project is an agentic chat bot designed to answer queries by integrating data from an internal proprietary dataset with information from external sources. The chatbot is built to provide comprehensive responses by combining structured restaurant data with up-to-date external information such as historical context, culinary trends, and analytical insights.

## Features

- **Ingredient-Based Discovery:**  
  Identify restaurants based on specific ingredients or dietary requirements.
  
- **Trending Insights & Explanations:**  
  Summarize current culinary trends, such as popular dessert innovations.
  
- **Historical or Cultural Context:**  
  Deliver background information (e.g., the history of sushi) along with local restaurant recommendations.
  
- **Comparative Analysis:**  
  Compare metrics such as average menu prices across different restaurant categories.
  
- **Menu Innovation & Flavor Trend:**  
  Analyze changes over time in ingredients and menu offerings, supported by both internal data and external news sources.


## Integration Details

- **Internal Proprietary Dataset:**  
  Contains detailed information on restaurants including menu items, pricing, ratings, and more.

- **External Sources:**  
  Incorporates data from external APIs (such as Wikipedia for historical info and news sources for current trends) to enhance the chatbot's responses with broader context.

## How It Works

1. **Query Processing:**  
   The chat bot receives a natural language query from the user.

2. **Data Retrieval:**  
   It determines which parts of the query require internal data, external data, or both, and fetches the relevant information accordingly.

3. **Data Integration and Analysis:**  
   The chatbot combines and analyzes the internal dataset and external sources to create a unified, comprehensive answer.

4. **Response Generation:**  
   The final answer is generated and returned to the user, ensuring clarity and contextual relevance.

## Getting Started

Follow these instructions to set up and run the project in your preferred development environment.

### Option 1: Local Development Environment

1. **Setup Environment:**
   - Ensure you have access to the internal dataset.
   - Configure API keys and endpoints for external data sources (e.g., Wikipedia).

2. **Create and Activate Conda Environment:**
   - Create a new Conda environment with Python 3.12:
     ```bash
     conda create --name chatbotenv python=3.12
     ```
   - Activate the environment:
     ```bash
     conda activate chatbotenv
     ```

3. **Install Dependencies:**
   Install the required packages using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
4. **Data Preprocessing, Setup Pinecone, and Upsert to Vector Database
   ```bash
   python preprocessing.py
   ```
5. **Run Program:**
  ```bash
  streamlit run main.py
  ```
### Option 2: Use Docker
1. **Build Docker Image:**
  ```bash
  docker build -t chatbotapi .
  ```
2. **Run Container:**
  ```bash
  docker run -d -p 8000:8000 --name backend chatbotapi
  ```
3. **Run UI:**
  In a new terminal run :
  ```bash
  streamlit run app.py --server.port 8501
  ```

### Option 3: Production
1. **Procedure**
  - dockerfile for backend, frontend and data
  - use copilot init to initialize the infrastructure
  - use copilot addons to add data
  - use copilot run to run the microservice