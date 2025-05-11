import requests

def converter_moeda(valor, de, para):
    url = f"https://api.exchangerate.host/convert?from={de}&to={para}&amount={valor}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        convertido = dados['result']
        print(f"\n💱 {valor:.2f} {de} = {convertido:.2f} {para}")
    else:
        print("❌ Erro ao acessar a API.")

def main():
    print("=== Conversor de Moedas ===")
    valor = float(input("Digite o valor: "))
    de = input("De (ex: BRL, USD, EUR): ").upper()
    para = input("Para (ex: USD, EUR, JPY): ").upper()
    
    converter_moeda(valor, de, para)

if _name_ == "_main_":
    main()