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

## Sample Queries

### 1. Ingredient-Based Discovery
- **Example 1:** “Which restaurants in Los Angeles offer dishes with Impossible Meat?”
- **Example 2:** “Find restaurants near me that serve gluten-free pizza.”

### 2. Trending Insights & Explanations
- **Example:** “Give me a summary of the latest trends around desserts in San Francisco.”

### 3. Historical or Cultural Context
- **Example:** “What is the history of sushi, and which restaurants in my area are known for it?”  

### 4. Comparative Analysis
- **Example:** “Compare the average menu price of vegan restaurants in San Francisco vs. Mexican restaurants.”  

### 5. Menu Innovation & Flavor Trend
- **Example:** “How has the use of saffron in desserts changed over the last year, according to restaurant menus or news articles?”  

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

1. **Setup Environment:**  
   - Ensure you have access to the internal dataset.
   - Configure API keys and endpoints for external data sources (e.g., Wikipedia).

2. **Install Dependencies:**  
   Use your `requirements.txt` or Conda environment setup to install necessary packages.

3. **Run the Chat Bot:**  
   Start the chat bot application using streamlit run main.py
