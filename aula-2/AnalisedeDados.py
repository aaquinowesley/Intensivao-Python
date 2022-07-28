import pandas as pd
import plotly.express as px 
# Criar o Passo a Passo

# Passo 1: Importar a Base de Dados
tabela = pd.read_csv('telecom_users.csv')
# Passo 2: Visualizar a Base de Dados

# Entender as informações que voçê tem disponível

# Descobrir as cagadas da Base de Dados

# Passo 3: Tratamento de Dados (Resolver as cagadas da base de Dados)


print(tabela)

# Excluir coluna unútil

# axis = 0 -> eixo da linha
# axis = 1 -> eixo da coluna


tabela = tabela.drop('Unnamed: 0', axis=1)
# Opções ignore, raise, coerce, default 'raise'
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")


# Tratar informações vazias

# Colunas que tem alguma informação vazia 
tabela.dropna(how="all", axis=1)

# Linhas que tem alguma informação vazia 
tabela.dropna(how="any", axis=0)

print(tabela.info())

# Passo 4: Análise Inicial dos Dados
# Como estão os Cancelamentos? 26%
print(tabela["Churn"].value_counts())
# Percentual
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

coluna = "Aposentado"

for coluna in tabela.columns:
    #Criando Graficos 

    # Etapa 1: Cria o gráfico
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    # Etapa 2: Exibe o gráfico
    grafico.show()