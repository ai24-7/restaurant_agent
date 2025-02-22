# from concurrent.futures import ThreadPoolExecutor, as_completed
# from transformers import AutoTokenizer, AutoModel
# import pandas as pd
# import torch
# import json
# from pinecone import Pinecone, ServerlessSpec
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from utils.config import PINECONE_API_KEY, PINECONE_INDEX_NAME, EMBED_DIM, HF_EMBEDDING_MODEL
# import re

# # Initialize tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained(HF_EMBEDDING_MODEL)
# model = AutoModel.from_pretrained(HF_EMBEDDING_MODEL)
# pc = Pinecone(api_key=PINECONE_API_KEY)
# # Function to generate embeddings
# def generate_embedding(row):
#     content = (
#         f"Menu Category: {row['menu_category']}, Menu Item: {row['menu_item']}. "
#         f"Description: {row['menu_description']}, Ingredients: {row['ingredient_name']}. "
#         f"Categories: {row['categories']}, Confidence: {row['confidence']}, Price: {row['price']}. "
#         f"Rating: {row['rating']}"
#     )
#     inputs = tokenizer(content, return_tensors="pt", truncation=True)
#     with torch.no_grad():
#         outputs = model(**inputs)
#     return outputs.last_hidden_state.mean(dim=1).squeeze().tolist(), content  # Return content along with embedding

# # Load your dataframe 'df' with 50000 rows here
# CSV_FILE = "data/sample.csv"
# df = pd.read_csv(CSV_FILE)

# vectors = []

# # Using ThreadPoolExecutor to parallelize embedding generation
# with ThreadPoolExecutor() as executor:
#     embedding_futures = {executor.submit(generate_embedding, row): row for _, row in df.iterrows()}
#     for future in as_completed(embedding_futures):
#         row = embedding_futures[future]
#         try:
#             embedding, content = future.result()  # Retrieve both embedding and content
#             vectors.append({
#                 "id": str(row['item_id']),
#                 "values": embedding,
#                 "metadata": {
#                     "restaurant_name": row['restaurant_name'],
#                     "address": row['address1'],
#                     "city": row['city'],
#                     "state": row['state'],
#                     "country": row['country'],
#                     "zip_code": row['zip_code'],
#                     "rating": row['rating'],
#                     "menu_category": row['menu_category'],
#                     "text": content,
#                 }
#             })
#         except Exception as e:
#             print(f"Error processing row {row['item_id']}: {str(e)}")

# # Save vectors to a JSON file
# with open('vectors.json', 'w') as f:
#     json.dump(vectors, f)


# if PINECONE_INDEX_NAME not in pc.list_indexes().names():
#     pc.create_index(name=PINECONE_INDEX_NAME,
#                     dimension=EMBED_DIM,
#                     metric="cosine",
#                     spec=ServerlessSpec(
#                         cloud="aws",
#                         region="us-east-1"
#                     )
#     )

# # Connect to the index.
# index = pc.Index(PINECONE_INDEX_NAME)
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")



# input_file = 'vectors.json'
# output_file = 'vectors_fixed.json'

# with open(input_file, 'r') as f:
#     text = f.read()

# # Replace unquoted NaN (numeric token) with an empty string, ensuring it's a standalone word
# text = re.sub(r'(?<!["\w])NaN(?!["\w])', '0', text)

# # Replace quoted "NaN" with an empty string
# text = re.sub(r'"\bNaN\b"', '""', text)

# # Replace quoted 'NaN' with an empty string
# text = re.sub(r"'\bNaN\b'", '""', text)

# with open(output_file, 'w') as f:
#     f.write(text)


# with open('vectors_fixed.json', 'r') as f:
#     vectors = json.load(f)

# # store the vectors in the pinecone index
# upsert_response = index.upsert(vectors=vectors, batch_size=100,)
# print("Upsert response:", upsert_response)