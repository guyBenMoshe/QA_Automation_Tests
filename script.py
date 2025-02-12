# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/users/1") 
# data = response.json() 

# assert response.status_code == 200
# assert data["id"] == 1

# print(data)

# ------------------------- 

# import requests

# url = "https://jsonplaceholder.typicode.com/users"
# new_user = {
#     "name": "Guy QA",
#     "username": "guyqa",
#     "email": "guy.qa@example.com"
# }

# response = requests.post(url, json=new_user)
# data = response.json()

# assert response.status_code == 201
# assert data["name"] == "Guy QA"

# print("✅ המשתמש נוצר בהצלחה!")

# ------------------------- 

def add(x, y):
    return x + y  # פונקציה שמחברת שני מספרים

def test_add():
    assert add(2, 3) == 5  # בדיקה שהפונקציה מחזירה 5
    assert add(-1, 1) == 0  # בדיקה שהחיבור נכון גם למספרים שליליים



