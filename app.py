import requests  # Biblioteca para fazer requisicoes HTTP

def ler_valor_arquivo(caminho_arquivo):
    """
    Lê o conteúdo de um arquivo de texto e retorna o valor.
    
    Parâmetros:
        caminho_arquivo (str): O caminho para o arquivo de texto.
    
    Retorno:
        str: O conteúdo do arquivo como uma string.
    """
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            valor = arquivo.read().strip()  # Remove espaços extras e quebras de linha
        return valor
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def enviar_post_api(url, dados):
    """
    Envia uma requisição POST para a API com os dados fornecidos.
    
    Parâmetros:
        url (str): A URL da API.
        dados (dict): Os dados a serem enviados no corpo da requisição POST.
    
    Retorno:
        response: O objeto de resposta da requisição.
    """
    try:
        response = requests.post(url, json=dados)  # Envia os dados como JSON
        response.raise_for_status()  # Levanta uma exceção se o status code for 4xx ou 5xx
        print("Requisição bem-sucedida!")
        print("Resposta da API:", response.json())  # Exibe a resposta da API
        return response
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar requisição POST: {e}")
        return None

def main():
    """
    Função principal do aplicativo.
    """
    caminho_arquivo = 'valor.txt'  # Caminho do arquivo de texto
    url_api = 'https://exemplo.com/api'  # URL da API (substitua pelo endpoint real)
    
    valor = ler_valor_arquivo(caminho_arquivo)
    if valor is not None:
        dados = {"valor": valor}  # Cria o dicionário com o valor lido do arquivo
        enviar_post_api(url_api, dados)

if __name__ == "__main__":
    main()
