import requests

def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")  # שליחת בקשת API
    data = response.json()  # המרת התגובה ל-JSON

    assert response.status_code == 200, "ה-API לא החזיר תשובה תקינה!"  # בדיקת סטטוס 200
    assert data["id"] == 1, "המשתמש שהתקבל אינו נכון!"  # בדיקת שהתקבל המשתמש הנכון

    print("✅ הבדיקה עברה בהצלחה!")

def test_create_user():
    url = "https://jsonplaceholder.typicode.com/users"
    new_user = {
        "name": "Guy QA",
        "username": "guyqa",
        "email": "guy.qa@example.com"
    }

    response = requests.post(url, json=new_user)  # שליחת בקשת POST
    data = response.json()  # המרת התגובה ל-JSON

    assert response.status_code == 201, "המשתמש לא נוצר בהצלחה!"  # בדיקת שהמשתמש נוצר
    assert data["name"] == "Guy QA", "שם המשתמש שגוי!"  # בדיקת שם המשתמש

    print("✅ המשתמש נוצר בהצלחה!")