import requests

def client():
    token_h = 'Token d4cc48448985ef869145b8115887e442b4e0d917'
    # credentials = {"username": "shannon", "password": "aikman08"}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                          data=credentials)
    headers = {'Authorization': token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)
    print("Status Code:" , response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()