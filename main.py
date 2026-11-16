import asyncio
import httpx
from pydantic import BaseModel,EmailStr

class User(BaseModel):
	id:int
	name:str
	phone:str
	email:str

async def fetch_users(url: str) -> list[User]:
	async with httpx.AsyncClient() as client:
		response = await client.get(url)
		response.raise_for_status()
		raw_data = response.json()
		return [User(**item) for item in raw_data]

async def main() -> None:
	api_url = "https://jsonplaceholder.typicode.com/users"
	users= await fetch_users(api_url)

	for user in users[:4]:
		print(f"Id: {user.id} | Name {user.name} | Phone number {user.phone} | Email {user.email}")

if __name__ == "__main__":
	asyncio.run(main())
