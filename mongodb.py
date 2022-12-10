from pymongo import MongoClient

# Create a new MongoClient instance
client = MongoClient("mongodb://localhost:27017")

# Access the "my_database" database
db = client.db1

# Create a new document to insert
my_document = {
    "name": "Dinda",
    "age": 25,
    "city": "Surabaya"
}

# db.ctest.insert_one(my_document)

# Query the collection for documents with the "name" field set to "John Doe"
cursor = db.ctest.find({"name": "John Doe"})

# Iterate over the cursor and print the documents
for document in cursor:
    print(document)

# Update the document by setting the "age" field to 36
db.ctest.update_one({"name": "John Doe"}, {"$set": {"age": 36}})

# Delete the document from the collection
db.ctest.delete_one({"name": "John Doe"})
