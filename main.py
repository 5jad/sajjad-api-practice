import httpx
from pydantic import BaseModel,EmailStr

class User(BaseModel):
	id:int
	name:str
	phone:str
	email:str

def fetch_users(url:str) -> list[User]:
	response = httpx.get(url)
	response.raise_for_status()

	raw_data = response.json()
	return [User(**item) for item in raw_data]

if __name__ == "__main__":
	api_url = "https://jsonplaceholder.typicode.com/users"
	users= fetch_users(api_url)

	for user in users[:4]:
		print(f"Id: {user.id} | Name {user.name} | Phone number {user.phone} | Email {user.email}")
