import pymongo
from datetime import datetime

connection_url = 'mongodb+srv://djangochocolateschallenge:djangochocolateschallenge17@cluster0.di5foqj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = pymongo.MongoClient(connection_url)

database = client['chocolates']
collection = database['chocolates_challenge']

current_time = datetime.now().time().strftime('%H:%M:%S')
image_url = "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=60"

chocolates_data = [
    {
        "name": "Dark Delight",
        "image": image_url,
        "price": 2.99,
        "rating": 4.5,
        "time": current_time
    },
    {
        "name": "Caramel Crunch",
        "image": image_url,
        "price": 3.49,
        "rating": 4.7,
        "time": current_time
    },
    {
        "name": "Hazelnut Heaven",
        "image": image_url,
        "price": 3.99,
        "rating": 4.6,
        "time": current_time
    },
    {
        "name": "White Wonder",
        "image": image_url,
        "price": 2.79,
        "rating": 4.3,
        "time": current_time
    },
    {
        "name": "Mint Magic",
        "image": image_url,
        "price": 3.29,
        "rating": 4.4,
        "time": current_time
    },
    {
        "name": "Berry Bliss",
        "image": image_url,
        "price": 3.59,
        "rating": 4.2,
        "time": current_time
    },
    {
        "name": "Nutty Nirvana",
        "image": image_url,
        "price": 3.99,
        "rating": 4.8,
        "time": current_time
    },
    {
        "name": "Mocha Melt",
        "image": image_url,
        "price": 2.49,
        "rating": 4.1,
        "time": current_time
    },
    {
        "name": "Orange Zest",
        "image": image_url,
        "price": 3.29,
        "rating": 4.0,
        "time": current_time
    },
    {
        "name": "Coconut Craze",
        "image": image_url,
        "price": 3.19,
        "rating": 4.3,
        "time": current_time
    },
    {
        "name": "Almond Amour",
        "image": image_url,
        "price": 2.89,
        "rating": 4.7,
        "time": current_time
    },
    {
        "name": "Cherry Charm",
        "image": image_url,
        "price": 3.49,
        "rating": 4.2,
        "time": current_time
    },
    {
        "name": "Salted Caramel",
        "image": image_url,
        "price": 3.79,
        "rating": 4.6,
        "time": current_time
    },
    {
        "name": "Peanut Butter Pop",
        "image": image_url,
        "price": 2.99,
        "rating": 4.5,
        "time": current_time
    },
    {
        "name": "Espresso Edge",
        "image": image_url,
        "price": 3.69,
        "rating": 4.7,
        "time": current_time
    },
    {
        "name": "Cookie Crunch",
        "image": image_url,
        "price": 2.79,
        "rating": 4.3,
        "time": current_time
    },
    {
        "name": "Cocoa Classic",
        "image": image_url,
        "price": 3.19,
        "rating": 4.4,
        "time": current_time
    },
    {
        "name": "Fudge Fantasy",
        "image": image_url,
        "price": 3.99,
        "rating": 4.9,
        "time": current_time
    },
    {
        "name": "Strawberry Silk",
        "image": image_url,
        "price": 2.99,
        "rating": 4.1,
        "time": current_time
    },
    {
        "name": "Vanilla Velvet",
        "image": image_url,
        "price": 3.29,
        "rating": 4.0,
        "time": current_time
    }
]



