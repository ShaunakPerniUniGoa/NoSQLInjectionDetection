import json
import pymongo
import os

print(os.path)
print(os.listdir())

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test_database"]
collection = db["test_collection"]

with open("No-SQL_Gen/No-SqlDataset.json", "r") as queryFile:
    data = json.load(queryFile)
    text_list = [obj["text"] for obj in data]

# Create a file to log the query results
with open("./Dataset/query_results.txt", "w") as result_file:
    for query_text in text_list:
        try:
            # Parse the query string into a valid MongoDB query object
            query = eval(query_text)
            result = collection.find(query)
            # Log the query and the result
            print(f"Query: {query_text}")
            print(f"Result: {list(result)}")
            # Log success in the file
            result_file.write(f"Success,\n")
        except Exception as e:
            # Log any errors
            print(f"Error executing query '{query_text}': {e}")
            # Log failure in the file
            result_file.write(f"Failed,\n")

# Close the MongoDB connection
client.close()