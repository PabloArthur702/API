# **Projeto de Gerenciamento de Tarefas**

Este é um projeto de gerenciamento de tarefas desenvolvido para máteria DCA3603 - ENGENHARIA DE SOFTWARE - T01 (2024.2), desenvolvida em Python, utilizando o framework Flask. A API implementa autenticação com JWT e está containerizada com Docker para facilitar a implantação.  

---

## **Links importantes**
- **Histórias de usuário:**  
  [Documentação no Google Docs](https://docs.google.com/document/d/1RviuKOJmK7BWzfPhResA2neH622yShreo7fcHMqRnhw/edit?usp=sharing)  

- **Diagrama UML do projeto:**  
  [Visualize no Google Drive](https://drive.google.com/file/d/1wX5p6B_cJklursa3Jh4o2clqm0vMm_Hz/view?usp=sharing)  

- **Caso de uso:**  
  [Visualize no Google Drive](https://drive.google.com/file/d/1egiMp8yv-c_JAHzoMbfY-Np2MV29TWfm/view?usp=sharing)  

---

## **Pré-requisitos**
Antes de iniciar, certifique-se de ter o seguinte instalado:
- **Python 3.10+**  
- **Docker** 

---

## **Funcionalidades principais**
1. **Cadastro de tarefas:** Crie tarefas informando título e descrição.  
2. **Listagem de tarefas:** Liste todas as tarefas cadastradas, filtrando por status (pendente/concluído).  
3. **Atualização de tarefas:** Atualize o status de uma tarefa para indicar progresso.  
4. **Autenticação JWT:** Proteja os endpoints, permitindo apenas o acesso de usuários autenticados.  
5. **Implantação com Docker:** Execute o projeto facilmente em um container.  

---

## **Como executar a API**
### **Passo 1: Clone o repositório**
Faça o download ou clone o repositório.

---

### **Passo 2: Construa a imagem Docker**
Dentro da pasta raiz do projeto, execute o seguinte comando para criar a imagem Docker:
```bash
docker build -t api-gerenciamento-tarefas .
```
### **Passo 3: Execute o container**
Inicie o container com o comando:
```bash
docker run -p 5000:5000 -it api-gerenciamento-tarefas
```

---

## **Autenticação com JWT**
A API utiliza JWT para proteger os endpoints. Siga os passos abaixo para autenticação:
---
### **Obter um token JWT:**
Faça uma requisição POST para o endpoint /login com as credenciais do usuário.
Exemplo (com curl):

```bash
curl -X POST http://localhost:5000/login \
-H "Content-Type: application/json" \
-d '{"username": "admin", "password": "123"}'
Resposta esperada:
{
    "access_token": "seu_token_aqui"
}
```

---

## **Usar o token JWT:**
Inclua o token no cabeçalho Authorization para acessar os endpoints protegidos.
Exemplo:
```bash	
curl -X GET http://localhost:5000/tasks \
-H "Authorization: Bearer seu_token_aqui"
```
