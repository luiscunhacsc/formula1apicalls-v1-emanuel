# 🏎️ Consulta Interativa de Corridas de Fórmula 1 com Streamlit

Este projeto apresenta uma aplicação web simples e interativa desenvolvida com [Streamlit](https://streamlit.io), que permite aos utilizadores explorarem os resultados de corridas de Fórmula 1 em diferentes temporadas, utilizando a [Ergast API](https://ergast.com/mrd/).

## 📚 Objetivo Educacional

Este projeto foi desenvolvido no contexto da unidade curricular **Análise de Sistemas**, com o propósito de demonstrar a integração entre frontends interativos e fontes de dados externas (REST APIs), promovendo uma compreensão prática sobre:

- Recolha e consumo de dados externos via HTTP.
- Estruturação de dados em JSON.
- Conceitos de interface homem-máquina (IHM) e interatividade.
- Uso de bibliotecas Python modernas para prototipagem rápida.

## 🚀 Funcionalidades

✅ Consulta de todas as temporadas de F1 desde 1950.  
✅ Seleção de corridas por temporada.  
✅ Visualização detalhada dos resultados de cada piloto.  
✅ Informação sobre equipa, nacionalidade, posição, número de voltas e muito mais.  
✅ Interface leve, intuitiva e sem necessidade de instalação de servidores complexos.

## 🧪 Tecnologias Usadas

- **Python 3.7+**
- **Streamlit** – Para criar a interface gráfica web.
- **Requests** – Para consumo da API RESTful.
- **Pandas** – Para manipulação leve de dados (opcional, mas incluído).

## 🛠️ Como Executar

1. **Clona o repositório:**

```bash
git clone https://github.com/teu-utilizador/consulta-f1.git
cd consulta-f1
````

2. **Cria um ambiente virtual (opcional mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
```

3. **Instala as dependências:**

```bash
pip install -r requirements.txt
```

4. **Executa a aplicação:**

```bash
streamlit run app.py
```

5. A aplicação abrirá automaticamente no browser. Se não abrir, visita [http://localhost:8501](http://localhost:8501).

## 🌐 API Utilizada

Os dados são obtidos diretamente da **Ergast Developer API**, um serviço gratuito e aberto com informações detalhadas sobre corridas de Fórmula 1 desde 1950.

* Documentação da API: [https://ergast.com/mrd/](https://ergast.com/mrd/)

## 🧠 Exemplos de Uso Educacional

* Avaliação de interações com APIs REST.
* Introdução ao consumo de dados JSON em aplicações reais.
* Desenvolvimento de protótipos rápidos de interfaces com Python.
* Análise de requisitos para sistemas de informação orientados a dados.

## 📸 Captura de Ecrã

> *(Podes aqui incluir uma imagem tipo screenshot do app.py em execução com resultados)*

## 📄 Licença

Este projeto é de uso educacional e está licenciado sob a **MIT License**. Consulta o ficheiro `LICENSE` para mais informações.

---

🧑‍🏫 Desenvolvido com fins pedagógicos por \[Luís Cunha e Emanuel Junqueira / ISMT].



