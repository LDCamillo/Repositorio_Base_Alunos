import requests

def ping():
    response = requests.get("https://restful-booker.herokuapp.com/ping")
    return response.status_code == 201 


def autenticacao():
    corpo = {
        "username":"admin",
        "password":"password123"
    }

    response = requests.post("https://restful-booker.herokuapp.com/auth", json=corpo)
    return response.json()["token"]


def criar_booking(nome="Fulano",sobrenome="Ciclano",valor=0,
            pago = False, checkin = "2025-08-20", checkout="2025-08-20",
            adicionais="Café da Manhã"):
    corpo = {
            "firstname" : nome,
            "lastname" : sobrenome,
            "totalprice" : valor,
            "depositpaid" : pago,
            "bookingdates" : {
            "checkin" : checkin,
            "checkout" : checkout
            },
            "additionalneeds" : adicionais
            }
    response = requests.post("https://restful-booker.herokuapp.com/booking", json=corpo)
    return response.json()["bookingid"]

def busca_booking(bookingId):
    response = requests.get(f"https://restful-booker.herokuapp.com/booking/{bookingId}")
    print(response.json())
    return response.json()


def atualiza_todo_booking(bookingId,nome,sobrenome,valor,
                          pago,checkin,checkout,adicionais):
    cabecalho = {
        "Cookie":f"token={autenticacao()}"
    }


    corpo = {
            "firstname" : nome,
            "lastname" : sobrenome,
            "totalprice" : valor,
            "depositpaid" : pago,
            "bookingdates" : {
            "checkin" : checkin,
            "checkout" : checkout
            },
            "additionalneeds" : adicionais
            }
    
    response = requests.put(f"https://restful-booker.herokuapp.com/booking/{bookingId}", json=corpo, headers=cabecalho)
    print(response.text)

def atualiza_parcealmente_booking(booking, **kwargs):
    cabecalho= {"cookie" :f"token={autenticacao()}"}
    corpo= kwargs
    response = requests.patch(f"https://restful-booker.herokuapp.com/booking/{booking}", json=corpo, headers=cabecalho)
    print(response.text)
    return response.json()

def delete_booking(boolkingId): 

    cabecalho= {
        "Cookie" :f"token={autenticacao()}"
    }

    response = requests.delete(f"https://restful-booker.herokuapp.com/booking/{boolkingId}", headers=cabecalho)
    if response.status_code == 201:
        print("Deletado. ")
    else:
        print("Não foi possível deletar.")

### ÁREA DE TESTES
#atualiza_parcialmente_booking(5, additionalneeds= "Café")
#delete_booking(11)
print("-" * 35)
print("ATIVIDADE 1 - HEALTH CHECK")
print(ping())
print("-" * 35)

print("-" * 35)
print("ATIVIDADE 2")
print(autenticacao())

print("-" * 35)
print("ATIVIDADE 3")
bookingId = criar_booking(nome=" cleber",sobrenome="iano",valor=10)
print(bookingId)
print("-" * 35)

print("-" * 35)
print("ATIVIDADE 4")
print(busca_booking(bookingId))
print("-" * 35)

print("-" * 35)
print("ATIVIDADE 5")
print(atualiza_todo_booking(bookingId,nome="jhon",sobrenome="dow",valor=50,pago=True, checkin= "2025-08-20", checkout= "2025-08-20",adicionais= "Café da Manhã"))
print("-" * 35)

print("-" * 35)
print("ATIVIDADE 6")
print(atualiza_parcealmente_booking(bookingId, firstname = "James"))
print("-" * 35)

print("-" * 35)
print("ATIVIDADE 7")
print(delete_booking(bookingId))
print("-" * 35)