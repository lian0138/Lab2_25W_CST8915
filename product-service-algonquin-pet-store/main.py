from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a FastAPI instance
app = FastAPI()

# Add CORS middleware to allow any origin with GET method
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Allow GET requests
)

# Define a product data model
class Product(BaseModel):
    id: int
    name: str
    price: float

# Define a route for products
@app.get("/products", response_model=list[Product])
async def get_products():
    products = [
        Product(id=1, name="Dog Food", price=19.99),
        Product(id=2, name="Cat Food", price=34.99),
        Product(id=3, name="Bird Seeds", price=10.99),
    ]
    return products

# Run the application with the specified port, default to 8000
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # Get port from .env
    uvicorn.run(app, host="0.0.0.0", port=port)