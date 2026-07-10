# Jornada Python — Hashtag Programação

Repositório com os projetos práticos desenvolvidos durante a Jornada de Python da Hashtag Programação, uma semana intensiva (segunda a quinta) cobrindo automação, análise de dados, machine learning e integração com IA generativa.

## → Projetos

### 01 · Automação de Cadastro de Produtos (RPA)
`/AULA 1`

Robô de automação (RPA) que faz login em um sistema web e cadastra produtos automaticamente a partir de uma planilha, eliminando o trabalho manual e repetitivo de digitação.

- Leitura de base de dados em CSV com **Pandas**
- Automação de mouse e teclado com **PyAutoGUI**
- Preenchimento automático de formulários web linha a linha

**Stack:** `Python` `PyAutoGUI` `Pandas`

---

### 02 · Análise de Cancelamento de Clientes (Data Insights)
`/AULA 2`

Case de análise exploratória de dados para uma empresa com mais de 800 mil clientes, com o objetivo de identificar os principais fatores que levam ao cancelamento do serviço e propor ações de retenção.

- Limpeza e tratamento de dados (remoção de nulos e colunas irrelevantes)
- Análise estatística da taxa de cancelamento
- Visualização de dados com **Plotly** para cruzar cada variável com o cancelamento
- Identificação de padrões: tipo de contrato, número de ligações ao call center e atraso de pagamento

**Stack:** `Python` `Pandas` `Plotly` `Jupyter Notebook`

---

### 03 · Previsão de Score de Crédito (Machine Learning)
`/AULA 3`

Modelo de inteligência artificial para classificar automaticamente o score de crédito de clientes de um banco em Ruim, OK ou Bom, a partir do histórico e perfil de cada cliente.

- Pré-processamento com **LabelEncoder** para variáveis categóricas
- Treinamento e comparação de dois modelos: **Random Forest** e **KNN**
- Avaliação de acurácia dos modelos
- Aplicação do modelo treinado para prever o score de novos clientes

**Stack:** `Python` `Pandas` `Scikit-learn`

---

### 04 · Chatbot com IA
`/AULA 4`

Aplicação web de chat interativo que envia as mensagens do usuário para um modelo de linguagem e exibe as respostas em tempo real, mantendo o histórico da conversa.

- Interface construída com **Streamlit**
- Integração com a API da **OpenAI** (GPT-4o)
- Gerenciamento de histórico de conversa via `session_state`

**Stack:** `Python` `Streamlit` `OpenAI API`

## → Tecnologias gerais

`Python` · `Pandas` · `Scikit-learn` · `Plotly` · `PyAutoGUI` · `Streamlit` · `OpenAI API` · `Jupyter Notebook`

## → Sobre

Projetos desenvolvidos como parte da Jornada de Python da Hashtag Programação, com foco em aplicar Python em cenários práticos de mercado: automação de processos, análise de dados e inteligência artificial.