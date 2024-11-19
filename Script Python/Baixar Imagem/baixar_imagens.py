import os
import requests
from urllib.parse import urlparse
import shutil

# Diretório onde as imagens serão salvas
DIRECTORY = "imagens"

#Precisamos de um User-agent para conectar e extrair informações da Wikipedia, sem sofrermos com bloqueios e ou banimento eventual  (Erro 403)
headers = {'User-Agent': 'SilasBot/0.1 (silas-rg@hotmail.com)'}

# Cria o diretório se não existir
if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)

# Dicionário com os códigos ICAO e URLs das imagens
icao_imagens = {
    "ABJ": "https://upload.wikimedia.org/wikipedia/commons/6/61/Abaete-Airlines-logo.jpg",
    "SAA": "https://upload.wikimedia.org/wikipedia/en/7/7c/SAA_logo_%282019%29.svg",
    "QTR": "https://upload.wikimedia.org/wikipedia/en/9/9b/Qatar_Airways_Logo.svg",
    "PAM": "https://upload.wikimedia.org/wikipedia/pt/f/f2/MAP_Linhas_A%C3%A9reas_logo.png",
    "PTB": "https://www.tribunaribeirao.com.br/wp-content/uploads/2017/09/Bannergradil-156x079-Passaredo-960x378.jpg",
    "NCR": "https://upload.wikimedia.org/wikipedia/commons/d/dd/National_Airlines_logo.svg",
    "MPH": "https://upload.wikimedia.org/wikipedia/commons/3/33/Martinair_logo.svg",
    "MAA": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Mas-air-cargo.png",
    "SRU": "https://en.wikipedia.org/wiki/Star_Per%C3%BA#/media/File:Star_Per%C3%BA_logo.png",
    "MWM": "https://modern.com.br/wp-content/uploads/2015/03/logo2.png",
    "DLH": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Lufthansa_Logo_2018.svg",
    "LPE": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Latam-logo_-v_%28Indigo%29.svg",
    "LAN": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Latam-logo_-v_%28Indigo%29.svg",
    "LCO": "https://upload.wikimedia.org/wikipedia/en/2/25/LATAM_Cargo_logo.svg",
    "TAM": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Latam-logo_-v_%28Indigo%29.svg",
    "KAL": "https://upload.wikimedia.org/wikipedia/commons/8/8f/KoreanAir_logo.svg",
    "CKS": "https://upload.wikimedia.org/wikipedia/en/0/02/Ka_logo_red.jpg",
    "GEC": "https://upload.wikimedia.org/wikipedia/en/8/86/Lufthansa_Cargo_logo.svg",
    "KLM": "https://upload.wikimedia.org/wikipedia/commons/c/c7/KLM_logo.svg",
    "RER": "https://upload.wikimedia.org/wikipedia/commons/7/78/Areoregional_Logo.png",
    "SKX": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Skyways_Express_AB_logo.png",
    "SID": "https://siderallinhasaereas.com.br/wp-content/uploads/2024/03/logo-sideral-branca.png",
    "OMI": "https://www.omnibrasil.com.br/assets/home/img/logo-branco-omni.png",
    "LTG": "https://upload.wikimedia.org/wikipedia/pt/4/4f/ABSA_logo.png",
    "LAE": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Latam-logo_-v_%28Indigo%29.svg",
    "ETR": "https://upload.wikimedia.org/wikipedia/commons/1/11/Logo_Aerolineas_Estelar.png",
    "UPS": "https://upload.wikimedia.org/wikipedia/commons/6/6b/United_Parcel_Service_logo_2014.svg",
    "UKL": "https://upload.wikimedia.org/wikipedia/en/5/5e/Ukraine_Air_Alliance_logo.png",
    "SKU": "https://upload.wikimedia.org/wikipedia/commons/6/65/Sky_Airline_Logo.svg",
    "UAL": "https://upload.wikimedia.org/wikipedia/en/e/e0/United_Airlines_Logo.svg",
    "TOT": "https://media.licdn.com/dms/image/v2/D4D0BAQFBd_uPQyCBTg/company-logo_200_200/company-logo_200_200/0/1718655325023/anivia_servios_areos_ltda_logo?e=1733961600&v=beta&t=Q4BRis2SCPylZ-AdR-Nv8Vj8PGfhgSWI0Fdvajbnqn4",
    "TTL": "https://upload.wikimedia.org/wikipedia/en/9/91/Total_Linhas_A%C3%A9reas_New_Logo.jpeg",
    "TVR": "https://terraavia.com/logo.png",
    "TAP": "https://upload.wikimedia.org/wikipedia/commons/f/fd/TAP-Portugal-Logo.svg",
    "TPA": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Logo-Avianca-Cargo-2023.svg",
    "DTA": "https://assets.planespotters.net/files/airlines/8/taag-linhas-aereas-de-angola-airlines_92bb61.svg",
    "SLM": "https://upload.wikimedia.org/wikipedia/en/8/8f/Surinam_Airways_Logo.svg",
    "THY": "https://upload.wikimedia.org/wikipedia/commons/0/00/Turkish_Airlines_logo_2019_compact.svg",
    "CQB": "https://upload.wikimedia.org/wikipedia/en/9/92/Apu%C3%AD_T%C3%A1xi_A%C3%A9reo_logo.png",
    "DWI": "https://images.prismic.io/arajet-ezycommerce/b93f72da-5043-4605-8682-9b60bfee38dd_Logo_web_Arajet.png",
    "BOV": "https://upload.wikimedia.org/wikipedia/commons/6/63/Logotipo_de_BoA.svg",
    "AZU": "https://upload.wikimedia.org/wikipedia/commons/5/52/Logo_da_Azul_Linhas_A%C3%A9reas_Brasileiras.svg",
    "AVA": "https://upload.wikimedia.org/wikipedia/commons/7/70/Avianca_Logo.svg",
    "ITY": "https://upload.wikimedia.org/wikipedia/commons/7/75/ITA_Airways_Logo.svg",
    "AAL": "https://upload.wikimedia.org/wikipedia/en/2/23/American_Airlines_logo_2013.svg",
    "QCL": "https://upload.wikimedia.org/wikipedia/pt/3/30/Air_Class_L%C3%ADneas_A%C3%A9reas_logo.JPG",
    "LNE": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Latam-logo_-v_%28Indigo%29.svg",
    "BAW": "https://upload.wikimedia.org/wikipedia/en/4/42/British_Airways_Logo.svg",
    "KRE": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Logo-aerosucre.png",
    "ACA": "https://upload.wikimedia.org/wikipedia/commons/2/24/Air_Canada_Logo.svg",
    "CCA": "https://upload.wikimedia.org/wikipedia/en/a/a4/Air_China_logo.svg",
    "ADB": "https://upload.wikimedia.org/wikipedia/en/9/93/AntonovAirlines_Logo.png",
    "ARG": "https://upload.wikimedia.org/wikipedia/commons/7/73/Aerol%C3%ADneas_Argentinas_Logo_2010.svg",
    "AJB": "https://americanjet.com.ar/wp-content/uploads/2020/04/logo.png",
    "ANS": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Marca_andes_final.png",
    "GTI": "https://upload.wikimedia.org/wikipedia/en/c/cc/Atlas_Air_logo.svg",
    "AMX": "https://upload.wikimedia.org/wikipedia/en/d/d4/Aerom%C3%A9xico_logo.svg",
    "AJT": "https://upload.wikimedia.org/wikipedia/en/f/f6/Amerijet_International_Logo.svg",
    "CLX": "https://upload.wikimedia.org/wikipedia/en/6/66/Cargolux_Logo.svg",
    "IBE": "https://upload.wikimedia.org/wikipedia/commons/2/23/Logotipo_de_Iberia.svg",
    "GXA": "https://upload.wikimedia.org/wikipedia/en/6/6d/Global_Crossing_Airlines_Logo%2C_August_2021.svg",
    "GLO": "https://upload.wikimedia.org/wikipedia/commons/6/6b/LogoGOL-Pref-FundoClaro-RGB.svg",
    "FBZ": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Flybondi_logo_simple.svg",
    "AEA": "https://upload.wikimedia.org/wikipedia/commons/5/59/Air_Europa_Logo_%282015%29.svg",
    "FDX": "https://upload.wikimedia.org/wikipedia/commons/9/9d/FedEx_Express.svg",
    "CJT": "https://upload.wikimedia.org/wikipedia/en/6/6c/Cargojet_Airways_Logo.svg",
    "ETH": "https://upload.wikimedia.org/wikipedia/commons/7/75/Ethiopian_Airlines_Logo.svg",
    "UAE": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Emirates_logo.svg",
    "ABD": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Air_Atlanta_Icelandic_Logo.svg",
    "DAL": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Delta_logo.svg",
    "CMP": "https://upload.wikimedia.org/wikipedia/en/5/5a/Copa_airlines_logo.svg",
    "VCV": "https://upload.wikimedia.org/wikipedia/en/d/d7/Conviasa_Logo.svg",
    "ACN": "https://upload.wikimedia.org/wikipedia/commons/5/52/Logo_da_Azul_Linhas_A%C3%A9reas_Brasileiras.svg",
    "AFR": "https://upload.wikimedia.org/wikipedia/commons/4/44/Air_France_Logo.svg",
    "JES": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Logo_JetSmart.svg",
    "SWR": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Swiss_International_Air_Lines_Logo_2011.svg",
    "AZP": "https://upload.wikimedia.org/wikipedia/en/2/2c/Paranair_logo.svg",
    "EVE": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Iberojetlogo.png",
    "LAP": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Latam-logo_-v_%28Indigo%29.svg",
    "EDR": "https://upload.wikimedia.org/wikipedia/commons/3/38/FAW-logo.png",
    "ARE": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Latam-logo_-v_%28Indigo%29.svg",
    "JAT": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Logo_JetSmart.svg",
    "EAL": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Eastern_Airlines_logo.svg"
}

def baixar_imagem(icao, url):
    try:
        resposta = requests.get(url, stream=True, timeout=10, headers=headers)
        resposta.raise_for_status()  # Verifica se houve erro na requisição

        # Tenta extrair a extensão do arquivo a partir da URL
        parsed_url = urlparse(url)
        caminho = parsed_url.path
        extensao = os.path.splitext(caminho)[1]

        # Caso não consiga extrair a extensão, tenta determinar pelo Content-Type
        if not extensao:
            content_type = resposta.headers.get('Content-Type')
            if content_type:
                if 'jpeg' in content_type:
                    extensao = '.jpg'
                elif 'png' in content_type:
                    extensao = '.png'
                elif 'svg' in content_type:
                    extensao = '.svg'
                elif 'gif' in content_type:
                    extensao = '.gif'
                else:
                    extensao = '.jpg'  # Padrão
            else:
                extensao = '.jpg'

        nome_arquivo = f"{icao}{extensao}"
        caminho_arquivo = os.path.join(DIRECTORY, nome_arquivo)

        # Salva a imagem no diretório especificado
        with open(caminho_arquivo, 'wb') as arquivo:
            resposta.raw.decode_content = True
            shutil.copyfileobj(resposta.raw, arquivo)

        print(f"Imagem salva como {nome_arquivo}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar {icao}: {e}")

def main():
    for icao, url in icao_imagens.items():
        print(f"Baixando imagem para {icao}...")
        baixar_imagem(icao, url)

if __name__ == "__main__":
    main()
