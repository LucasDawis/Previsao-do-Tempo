import requests
import os
from dotenv import load_dotenv

load_dotenv()

def consulta_previsao_tempo(cidade, API_KEY):
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt-br"
    requisicao = requests.get(link)
    dados = requisicao.json()
    return dados

def kelvin_para_celsius(temp_kelvin):
    return round(temp_kelvin - 273.15, 2)


def obter_cidade():
    while True:
        cidade = input("Digite o nome da cidade para obter a previsão do tempo (ou 'sair' para encerrar): ").strip()
        if cidade.lower() == 'sair':
            return None
        elif cidade:
            return cidade
        else:
            print("Por favor, insira o nome da cidade.")

def exibir_previsao_tempo(dados_previsao):
    if dados_previsao["cod"] == 200:
        print("\nPrevisão do tempo para", dados_previsao["name"] + ", " + dados_previsao["sys"]["country"])
        temperatura_celsius = kelvin_para_celsius(dados_previsao["main"]["temp"])
        print("Temperatura:", "{:.2f}".format(temperatura_celsius), "°C")
        print("Condição:", dados_previsao["weather"][0]["description"])
    else:
        print("\nErro ao obter previsão do tempo:", dados_previsao.get("message", "Erro desconhecido."))
    
    
def main():
    API_KEY = str(os.getenv("API_KEY"))
    
    print("Bem vindo ao serviço de previsão do tempo!")
    
    while True:
        cidade = obter_cidade()
        if not cidade:
            print("Encerrando o programa, até a proxima! ")
            
        dados_previsao = consulta_previsao_tempo(cidade, API_KEY)
        exibir_previsao_tempo(dados_previsao)

if __name__ == "__main__":
    main()
