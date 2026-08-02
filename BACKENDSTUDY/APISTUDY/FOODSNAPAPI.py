from fastapi import FastAPI, HTTPException
#HTTPEXCEPTION HAS TO BE IMPORTED FROM fastapi
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI()

class Post(BaseModel):
    id: str
    food_name: str = Field(..., min_length=2)
    restaurant: str
    rating: int = Field(..., ge = 1, le = 5)
    caption: str = Field(max_length=200)
    likes: int = Field(..., ge = 0)
#look up pydantic validation, not sure if this is complete, discuss w/ yaya

all_posts = [
    {
        "id": "1",
        "food_name": "Mango Lassi Cheesecake",
        "restaurant": "Table42",
        "rating": 5,
        "caption": "Lovely owners, very personable. Good food.",
        "likes" : 0
    },
    {
        "id": "2",
        "food_name": "Ice Soup",
        "restaurant": "My House",
        "rating": 1,
        "caption": "Second week of my bi-weekly paycheck.",
        "likes" : 0
    },
    {
        "id": "3",
        "food_name": "Curry Udon",
        "restaurant": "Ryuo",
        "rating": 5,
        "caption": "Expensive. My girl loved it! Expensive. Will learn to make at home.",
        "likes" : 0
    }
]

@app.get("/")
def health_check():
    return {"message" : "FoodSnap API running"}

@app.get("/posts")
def get_all_posts(min_rating: int = 1):
    if min_rating == 1:
        return all_posts
    ge_min = []
    for post in all_posts:
        if post["rating"] >= min_rating:
            ge_min.append(post)
    if len(ge_min) > 0:
        return ge_min
    raise HTTPException(status_code=404, detail="No posts rated greater than 4")

@app.get("/posts/{post_id}")
def retrieve_one_post(post_id: str):
    for post in all_posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts", response_model=Post)
def create_post(post: Post):
    post_data = post.model_dump()
    post_data["id"] = str(len(all_posts) + 1)
    all_posts.append(post_data)
    return post_data

@app.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: str,edit_post: Post):
    post_data = edit_post.model_dump()
    for post in all_posts:
        if post["id"] == post_id:
            if post_data["food_name"] != None:
                post["food_name"] = post_data["food_name"]
            if post_data["restaurant"] != None:
                post["restaurant"] = post_data["restaurant"]
            if post_data["rating"] != None:
                post["rating"] = post_data["rating"]
            if post_data["caption"] != None:
                post["caption"] = post_data["caption"]
            if post_data["likes"] != None:
                post["likes"] = post_data["likes"]
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    for i, post in enumerate(all_posts):
        if post["id"] == post_id:
            all_posts.pop(i)
            return("post removed")
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts/{post_id}/like")
def like_post(post_id: str):
    for post in all_posts:
        if post["id"] == post_id:
            post["likes"] = post["likes"] + 1
            return post
    raise HTTPException(status_code=404, detail="Post not found")