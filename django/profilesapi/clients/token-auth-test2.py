import requests

def client():
    data = {"username": "caleb",
            "email": "caleb@drakeweb.org",
            "password1": "changeme123",
            "password2": "changeme123"
            }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
                              data=data)
    print("Status Code:" , response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()