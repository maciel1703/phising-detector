
from urllib.parse import urlsplit


# ==================================================
# 1. ENTRADA DE DADOS
# Recebe a URL que será analisada pelo programa.
# ==================================================

armazenar_url = input("Qual URL deseja analisar: ")
print(armazenar_url)


# ==================================================
# 2. VALIDAÇÃO DA ENTRADA
# Verifica se o usuário informou alguma URL.
# Retorna True caso a entrada esteja vazia.
# ==================================================

def validar_url(armazenar_url):

    if armazenar_url == "":
        return True
    else:
        return False


url_vazia = validar_url(armazenar_url)

# Interrompe a execução caso nenhuma URL seja informada.
if url_vazia:
    print("Nenhuma URL foi informada.")
    exit()


# ==================================================
# 3. SEPARAÇÃO DOS COMPONENTES DA URL
# Utiliza urlsplit() para separar protocolo,
# hostname, porta e outros componentes.
# ==================================================

apuracao_url = urlsplit(armazenar_url)


# ==================================================
# 4. ANÁLISE E VALIDAÇÃO DA URL
# Verifica o protocolo, hostname e porta.
# ==================================================

def analisar_url(apuracao_url):

    # Verifica se o protocolo é HTTP ou HTTPS.
    if apuracao_url.scheme in ("http", "https"):
        print("Protocolo permitido.")
    else:
        print("Protocolo não permitido.")
        return

    # Verifica se a URL possui um hostname.
    if apuracao_url.hostname is None:
        print("Hostname não foi encontrado.")
        return

    # Obtém a porta informada na URL.
    url_port = apuracao_url.port

    # Define a porta padrão conforme o protocolo,
    # caso nenhuma porta tenha sido especificada.
    if apuracao_url.port is None:
        if apuracao_url.scheme == "https":
            url_port = 443

        elif apuracao_url.scheme == "http":
            url_port = 80

    # Retorna os dados extraídos para a etapa final.
    return (
        url_port,
        apuracao_url.scheme,
        apuracao_url.hostname
    )


# ==================================================
# 5. TRATAMENTO DO RETORNO
# Verifica se a análise foi concluída corretamente
# antes de desempacotar os valores retornados.
# ==================================================

retorno_funcao = analisar_url(apuracao_url)

if retorno_funcao is None:
    print("Não foi possível analisar a URL.")

else:
    porta, protocolo, hostname = retorno_funcao

    # Apresenta o resultado da análise.
    resultado_url = (
        f"Análise da URL concluída: "
        f"{protocolo} {porta} {hostname}"
    )

    print(resultado_url)
