# 🛫 Análise de Voo no Brasil - Junho

Este projeto foi desenvolvido com o objetivo de analisar a pontualidade dos voos realizados em solo brasileiro, comparando os meses de junho de 2023 e junho de 2024. A análise foi construída utilizando o Power BI, com dados públicos da ANAC, fornecendo insights robustos sobre atrasos, adiantamentos e pontualidade, além de variações ano a ano (YoY).

**Relatório**: [Análise de Voo - Junho](https://app.powerbi.com/view?r=eyJrIjoiZjgwMWY2YTMtMjc2MS00MWY5LWIzNDMtYmNjOGIwMmM4Yzk4IiwidCI6IjY3ZTdjOGU3LWUwOWUtNDk1Yi05YzRlLWQwMDhmZjVhNzJmZSJ9)

---

## 📖 Tabela de Conteúdos

1. [Visão Geral](#-visão-geral)
2. [Prospecção de Dados](#-prospecção-de-dados)
3. [ETL: Extração, Transformação e Carga](#-etl-extração-transformação-e-carga)
4. [Tabelas de Dimensão](#-tabelas-de-dimensão)
5. [Modelagem e Relacionamentos](#-modelagem-e-relacionamentos)
6. [Coluna Calculada](#-coluna-calculada)
7. [Cálculos e Medidas DAX](#%EF%B8%8F-c%C3%A1lculos-e-medidas-dax)
8. [Visualizações do Relatório](#-visualizações-do-relatório)
9. [Design e Ferramentas Utilizadas](#-design-e-ferramentas-utilizadas)
10. [Formatação condicional](#%EF%B8%8F-formata%C3%A7%C3%A3o-condicional)
11. [Tooltip e Popup de Ajuda](#%EF%B8%8F-tooltip-e-popup-de-ajuda) 
12. [Conclusão e Próximos Passos](#-conclusão-e-próximos-passos)
13. [Demonstração do Dashboard](#-demonstração-do-dashboard)

---

## 🌟 Visão Geral

O projeto aborda os seguintes tópicos:
- **Análise de Pontualidade (On-Time Performance - OTP)**: Percentual de voos pontuais.
- **Atrasos por Categoria**: Identificação de atrasos críticos, voos adiantados e inconsistências.
- **Variação Anual (YoY)**: Comparação do volume de voos realizados em junho de 2023 e 2024.
- **Insights Geográficos**: Rotas, atrasos por aeroporto e desempenho das empresas aéreas.

---

## 🔍 Prospecção de Dados

A base de dados foi extraída do site da ANAC, focando nos meses de junho de 2023 e 2024 para permitir uma análise de variação ano a ano (YoY). O formato inicial dos dados era CSV, o que facilitou a importação para o Power BI.

- [Base de dados ANAC - VRA](https://sas.anac.gov.br/sas/bav/view/frmConsultaVRALogado)
- **Volume de Dados**: Mais de 154.000 registros, abrangendo 297 aeroportos nacionais e internacionais, além de 83 empresas aéreas.

## **Site ANAC**
<img src="https://i.imgur.com/wzIkWwT.gif" alt="Site da ANAC" width="700" />

---

## 🛠 ETL: Extração, Transformação e Carga

O processo de ETL foi realizado no Power Query. Etapas principais:
1. **Unificação das Bases**: Mesclagem dos arquivos CSV de 2023 e 2024 em uma única tabela fato.
2. **Remoção de Colunas Irrelevantes**: Excluímos dados redundantes.
3. **Tratamento de Formatos**: Padronizamos datas e ajustamos valores nulos.

---

## 📋 Tabelas de Dimensão

### **1. dEmpresaAerea**
- **Objetivo**: Fornecer informações detalhadas sobre as empresas aéreas.
- **Campos**:
  - Nome, Sigla ICAO, País de Origem, Total de Voos e Rotas, Logomarca.
- **Métodos**:
  - Dados extraídos da [Wikipedia - Lista de Códigos de Empresas Aéreas](https://en.wikipedia.org/wiki/List_of_airline_codes).
  - **País de Origem**: Através da sigla foi possivel identificar o país de origem ao conectar o Wikipedia com o PowerBI.
  - **Automação**: Script em Python para download e tratamento de logomarcas.
  - **Tratamento**: As logomarcas foram ajustadas no Photoshop e hospedadas no Imgur para integração no Power BI.
<img src="https://i.imgur.com/D6I9GCM.png" alt="Tabela Empresas" width="700" />
<br>

**Imagens Localizadas**<br>
<img src="https://i.imgur.com/cLoLx9n.gif" alt="Imagens Localizadas" width="600" />


**Imagens Baixadas**<br>
<img src="https://i.imgur.com/pyECsQ8.gif" alt="Imagens Baixadas" width="600" />


 **Imagens Editadas**<br>
<img src="https://i.imgur.com/ox2ZfGs.gif" alt="Imagens Editadas" width="600" />


**Imagens Upadas**<br>
<img src="https://i.imgur.com/T5O1l41.png" alt="Imagens Upadas" width="600" />
 


### **2. dAeroportos**
- **Objetivo**: Detalhar informações geográficas e operacionais dos aeroportos.
- **Campos**:
  - Nome, Cidade, Estado, País, Coordenadas, Bandeiras dos Países.
- **Métodos**:
  - Uso de fontes abertas (ChatGPT, Google Maps) para preenchimento de coordenadas e tabela de bandeiras para compor a imagem do país.

<img src="https://i.imgur.com/ozCSHfb.gif" alt="Tabela Aeroporto" width="575" />

---

## 🔗 Modelagem e Relacionamentos

Foi utilizado o **Star Schema** para organizar as tabelas:
- **Fato**: Registros dos voos.
- **Dimensões**: Empresas aéreas, aeroportos de origem/destino, e datas.
- A duplicação da tabela de aeroportos permitiu dois relacionamentos ativos (origem e destino).

<img src="https://i.imgur.com/WPz9XCT.gif" alt="Star Schema" width="575" />

---

## 🧮 Coluna Calculada
As colunas calculadas foram criadas para facilitar o desenvolvimento de gráficos e análises mais detalhadas no relatório. Um exemplo é a coluna de Desempenho de Pontualidade, que classifica os voos como **Pontual**, **Adiantado**, **Atrasado** ou **Inconsistente**.
Com essas regras, foi possível categorizar os voos de forma precisa e garantir que os gráficos representassem insights claros e confiáveis.

## **Colunas da tabela fato (BaseDados)**
<img src="https://i.imgur.com/rKzTwYn.gif" alt="Coluna Calculada" width="550" />


---

## ✍️ Cálculos e Medidas DAX

### **1. Situação de Chegada**
Define o status do voo considerando atrasos e adiantamentos:
```DAX
Situação Chegada = 
VAR ChegadaReal = fBaseDados[Chegada Real]
VAR ChegadaPrevista = fBaseDados[Chegada Prevista]
VAR PartidaReal = fBaseDados[Partida Real]
VAR PartidaPrevista = fBaseDados[Partida Prevista]
VAR StatusPartida = fBaseDados[Situação Partida]
VAR SituacaoVoo = fBaseDados[Situação Voo]
VAR VooDomestico = RELATED(dAeroportosOrigem[País]) = "Brasil" && RELATED(dAeroportosDestino[País]) = "Brasil"
VAR AtrasoPartida = IF(StatusPartida = "+", PartidaReal - PartidaPrevista, 0)
VAR ChegadaAjustada = ChegadaPrevista + AtrasoPartida
VAR DiferencaMinutos = (ChegadaReal - ChegadaAjustada) * 1440
VAR LimitePontualidade = IF(VooDomestico, 30, 60)
RETURN
IF(
    SituacaoVoo = "CANCELADO", 
    BLANK(), 
    IF(
        ISBLANK(ChegadaReal) || ISBLANK(ChegadaPrevista) || ISBLANK(PartidaReal) || ISBLANK(PartidaPrevista), 
        "Inconsistente", 
        IF(
            DiferencaMinutos > LimitePontualidade, 
            "+" & FORMAT(INT(DiferencaMinutos / 60), "00") & "h" & FORMAT(MOD(DiferencaMinutos, 60), "00") & "min", 
            IF(
                DiferencaMinutos < 0, 
                "-" & FORMAT(INT(ABS(DiferencaMinutos) / 60), "00") & "h" & FORMAT(MOD(ABS(DiferencaMinutos), 60), "00") & "min", 
                "Pontual"
            )
        )
    )
)
```

### **2. Pontualidade Ponderada**
Calcula a pontualidade ajustada ao volume de voos:
```DAX
Pontualidade Ponderada = 
DIVIDE(VoosPontuais, TotalVoos, 0) * IF(TotalVoos < 10, TotalVoos / 10, 1)
```

### **3. Percentual OTP**
Calcula a porcentagem de cada categoria:
```DAX
Percentual OTP = 
VAR TotalGeral = CALCULATE(COUNTROWS(fBaseDados), ALL(fBaseDados[OTD]))
VAR TotalCategoria = COUNTROWS(fBaseDados)
RETURN DIVIDE(TotalCategoria, TotalGeral)
```

### **4. On-Time Performance**
Calcula o desempenho de pontualidade com base na coluna:
```DAX
OTP = IF(fBaseDados[Situação Chegada] = "Inconsistente", "Inconsistente",
    IF(fBaseDados[Situação Chegada] = "Pontual", "Pontual",
        IF(FIND("-",fBaseDados[Situação Chegada],1,0) = 0, "Atrasado",
            IF(FIND("-",fBaseDados[Situação Chegada],1,0) > 0, "Adiantado"))))
```

### **5. Horas de Voo**
Calcula o tempo total de voo:
```DAX
Horas de Voo =
VAR Horas = HOUR(fBaseDados[Chegada Real] - fBaseDados[Partida Real])
VAR Minutos = MINUTE(fBaseDados[Chegada Real] - fBaseDados[Partida Real])
RETURN
FORMAT(Horas, "0") & "h" & FORMAT(Minutos, "00") & "min"
```

### **6. Atraso em minutos**
Calcula quantos minutos de atraso ocorreu desde o momento da partida até o pouso no destino:
```DAX
Atraso em Minutos =
VAR ChegadaReal = fBaseDados[Chegada Real]
VAR ChegadaPrevista = fBaseDados[Chegada Prevista]
VAR PartidaReal = fBaseDados[Partida Real]
VAR PartidaPrevista = fBaseDados[Partida Prevista]
VAR StatusPartida = fBaseDados[Situação Partida]
VAR SituacaoVoo = fBaseDados[Situação Voo]
VAR AtrasoPartida = IF(StatusPartida = "+", PartidaReal - PartidaPrevista, 0)
VAR ChegadaAjustada = ChegadaPrevista + AtrasoPartida
VAR DiferencaMinutos = (ChegadaReal - ChegadaAjustada) * 1440
RETURN
IF(
    SituacaoVoo = "CANCELADO" || ISBLANK(ChegadaReal) || ISBLANK(ChegadaPrevista) || ISBLANK(PartidaReal) || ISBLANK(PartidaPrevista),
    BLANK(),
    DiferencaMinutos
)
```
### **7. Atraso em Solo**
Calcula o total de atraso em solo com base na previsão/chegada de partida e partida/chegada real:
```DAX
2024 Atraso em solo = 
CALCULATE(
    SUMX(
        FILTER(
            fBaseDados,
            fBaseDados[Ano] = 2024 &&
            fBaseDados[Situação Voo] = "REALIZADO"
        ),
        MAX(0, DATEDIFF(fBaseDados[Partida Prevista], fBaseDados[Partida Real], HOUR))
    )
)
```

### **8. Voos realizados 2023/2024**
Soma o total de voos realizados com base em algumas condições:
```DAX
2024 Realizados = IF(ISBLANK(CALCULATE(
    COUNTROWS(fBaseDados),
    fBaseDados[Ano] = 2024, fBaseDados[Situação Voo] = "REALIZADO" || fBaseDados[Situação Voo] = "NÃO INFORMADO"
)),"-",CALCULATE(
    COUNTROWS(fBaseDados),
    fBaseDados[Ano] = 2024, fBaseDados[Situação Voo] = "REALIZADO" || fBaseDados[Situação Voo] = "NÃO INFORMADO"
))
```
```DAX
2023 Realizados = IF(ISBLANK(CALCULATE(
    COUNTROWS(fBaseDados),
    fBaseDados[Ano] = 2023, fBaseDados[Situação Voo] = "REALIZADO" || fBaseDados[Situação Voo] = "NÃO INFORMADO"
)),"-",CALCULATE(
    COUNTROWS(fBaseDados),
    fBaseDados[Ano] = 2023, fBaseDados[Situação Voo] = "REALIZADO" || fBaseDados[Situação Voo] = "NÃO INFORMADO"
))
```

### **9. YoY Realizados (Variação)**
Calcula o tempo total de voo:
```DAX
YoY Realizados =
VAR Voos2023 = VALUE([2023])
VAR Voos2024 = VALUE([2024])
VAR YoY = DIVIDE(Voos2024 - Voos2023, Voos2023)


RETURN
IF(
    ISBLANK(Voos2024) || ISBLANK(Voos2023),
    "-",
    IF(
        YoY >= 0,
        "▲ " & FORMAT(YoY, "0.00%"),
        "▼ " & FORMAT(YoY, "0.00%")
    )
)
```

---

## 📊 Visualizações do Relatório

### **1. Map Flow**
- **Descrição**: Mostra rotas de voo com base em coordenadas.
- **Configuração**: Coordenadas ajustadas no Power Query.
<img src="https://i.imgur.com/DxAO8J2.png" alt="Dashboard Mapa" width="400" />

### **2. Cartões KPI**
- **Métricas**: Total de voos, variações YoY.
- **Formatos**: Cores condicionais (verde/vermelho) para destacar crescimento ou queda.
<img src="https://i.imgur.com/8skuWrU.gif" alt="Cartões com variação" width="400" />

### **3. Gráfico de Rosca - OTD**
- Exibe as categorias: Pontual, Adiantado, Atrasado, Inconsistente.

### **4. Gráfico de Pizza - Empresas Aéreas**
- Destaca as 5 empresas mais pontuais.

### **5. Gráfico de linha - Pico de cancelamento diário**
- Destaca os cancelamentos diarios.

### **6. Simple Image - Bandeira e logo tipo da empresa**
- Plugin que permite criar imagens dinamicas a partir de link anexado na tebela.
<img src="https://i.imgur.com/KN5eYxo.png" alt="Simple Image" width="400" />

### **7. Gráfico de linha e coluna - Comparação de voos realizado**
- Destaca os dias com voos superiores se comparado com 2023, para tal foi usado a formula DAX:
```DAX
YoY Cor =
IF(
    ISBLANK([2024]),
    "2",
    IF(
        ISBLANK([2023]),
        "3",
        IF(
            [2024] = [2023],
            "4",
            IF(
                [2024] > [2023],
                "1",
                "0"
            )
        )
    )
)
```
<img src="https://i.imgur.com/wBj47Lx.gif" alt="Gráfico com linhas" width="500" />

---

## 🎨 Design e Ferramentas Utilizadas

<img src="https://i.imgur.com/cQ6DTmp.png" alt="Informações das ferramentas" width="800" />


---

## 🖼️ Formatação Condicional 

Utilizada para mudar algumas tonalidades de forma dinamica, como por exemplo a tonalidade das variações (YoY) que a depender da condição apresenta cor diferente.

### **1. Variação**
- Destaca a cor com base na variação do valor.
```DAX
YoY Realizados =
VAR Voos2023 = VALUE([2023])
VAR Voos2024 = VALUE([2024])
VAR YoY = DIVIDE(Voos2024 - Voos2023, Voos2023)


RETURN
IF(
    ISBLANK(Voos2024) || ISBLANK(Voos2023),
    "-",
    IF(
        YoY >= 0,
        "▲ " & FORMAT(YoY, "0.00%"),
        "▼ " & FORMAT(YoY, "0.00%")
    )
)
```
<img src="https://i.imgur.com/VvdbB8D.gif" alt="Cores da variação" width="650" />

---

## 🕵️ Tooltip e Popup de Ajuda

Tanto o **Tooltip** quanto o **Popup de ajuda** foram desenvolvidos com a inteção de facilitar o entendimento de cada grafico, para tal utilizei da ferramenta bookmarker.

**Tooltip**<br>
<img src="https://i.imgur.com/UMhTcx3.gif" alt="Mapa" width="400" /> 

<img src="https://i.imgur.com/MSaEOhf.gif" alt="OTP" width="500" /> 

<img src="https://i.imgur.com/sDwIUTC.gif" alt="Tabela" width="500" />

**Popup de ajuda - Empresas Aéreas**<br>
<img src="https://i.imgur.com/4txmFzT.gif" alt="Popup de Ajuda" width="700" />

---

## 💻 Montagem visual do dashboard 

O **Figma** foi usado para prototipar o layout do dashboard, testando diferentes disposições, cores e gráficos. Ele garantiu um design intuitivo e colaborativo, permitindo ajustes rápidos antes da implementação no Power BI.
<img src="https://i.imgur.com/1B3L4uM.gif" alt="Figma" width="700" />

---

## 🤌 Demonstração do Dashboard
[![Video demonstrativo](https://markdown-videos-api.jorgenkh.no/url?url=https%3A%2F%2Fyoutu.be%2FVQc0VgjM18I)](https://youtu.be/VQc0VgjM18I)

<iframe width="560" height="315" src="https://www.youtube.com/embed/VQc0VgjM18I?si=TM-SQNQ1kcMuHBF5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 🚀 Conclusão e Próximos Passos

Este relatório analisa de forma abrangente o desempenho do setor aéreo no Brasil, fornecendo insights relevantes para empresas e gestores.

Meu Linkedin: [Silasrdgs](https://www.linkedin.com/in/silasrdgs)

---
