import random
import certifi
import pymongo
from pymongo import MongoClient

def get_random_word():
    cluster = MongoClient("mongodb+srv://efar716:12345@cluster0.sd3azp3.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
    db = cluster["Hangman"]
    collection = db["Hangman"]
    number_of_words = collection.count_documents({})
    random_id = random.randint(0,number_of_words - 1)
    word = collection.find_one({"_id":random_id})
    return word["word"]
def fill_database(file_name):
    cluster = MongoClient("mongodb+srv://efar716:12345@cluster0.sd3azp3.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
    db = cluster["Hangman"]
    collection = db["Hangman"]
    
    with open(file_name, 'r') as f:
        counter = collection.count_documents({})
        for word in f:
            word = word.strip("\n")
            word_length = len(word)
            post = {"_id":counter,"word":word,"length":word_length}
            if collection.count_documents({"word":word}) != 0:
                continue
            collection.insert_one(post,bypass_document_validation=False)
            counter += 1
            
def clear_database(file_name):
    cluster = MongoClient("mongodb+srv://efar716:12345@cluster0.sd3azp3.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
    db = cluster["Hangman"]
    collection = db["Hangman"]
    collection.delete_many({})
    
    
