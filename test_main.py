import pytest
from main import User, fetch_users

def test_user_model_valid():
	data={
		"id":1,
		"name":"Sajjad",
		"phone":"07700000000",
		"email":"sajjad@exmaple.com"
}

	user=User(**data)
	assert user.id == 1
	assert user.name == "Sajjad"

@pytest.mark.asyncio
async def test_fetch_users():
	url = "https://jsonplaceholder.typicode.com/users"
	users= await fetch_users(url)

	assert len(users)==10
	assert isinstance(users[0], User)
