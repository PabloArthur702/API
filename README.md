# **Projeto de Gerenciamento de Tarefas**

Este é um projeto de gerenciamento de tarefas desenvolvido para máteria DCA3603 - ENGENHARIA DE SOFTWARE - T01 (2024.2). Desenvolvida em Python, utilizando o framework Flask. A API implementa autenticação com JWT e está containerizada com Docker.

### **Autores:**

[Maurício Matheus](https://github.com/MauricioMatheus)

[Pablo Arthur](https://github.com/PabloArthur702)

[Yuri Borges](https://github.com/YuriFBorges)

---

- **Histórias de usuário:**  
  [Clique aqui para Histórias de usuário](https://drive.google.com/drive/folders/141v8i4cvNGrrzBccZesZNT_eU48w4BHv?usp=sharing)  

- **Diagrama UML do projeto:**  
  [Clique aqui para Diagrama UML do projeto](https://drive.google.com/drive/folders/1sM3cB320fvlwXP4lYR8_cxHk7plEDnPT?usp=sharing)  

- **Caso de uso:**  
  [Clique aqui para Caso de uso](https://drive.google.com/drive/folders/1zfTk6-IrFdoyXAVV9pJAegro8bxOK0Jq?usp=sharing)
  
---

## **Execute a API usando os seguintes comandos em um terminal compatível:**

### **1. Clone o repositório**
```bash
git clone https://github.com/PabloArthur702/API_tasks.git
```
### **2. Entre no diretório do repositório clonado**
```bash
cd API_tasks
```

### **3. Crie a imagem Docker**
```bash
docker build -t api-gerenciamento-tarefas .
```

### **4. Inicie o container**
```bash
docker run -p 5000:5000 -it api-gerenciamento-tarefas
```

### **5. Uso da API**
Após a execução do container, os endpoints da API estarão disponíveis no servidor **http://localhost:5000/**, permitindo a realização de operações utilizando os métodos para o CRUD. Esses métodos podem ser utilizados para interagir com os recursos da API, como cadastrar, listar, atualizar e excluir tarefas.

---

## **Comandos de autenticação:**

### **1. Registro de Usuário**
Abrindo o postman, cole a URL fornecida e atribua no final o endpoint /register, selecione o método "POST". Mude para "Body", selecione "raw" e depois modifique "Text" para "JSON". Adicione dentro do campo a seguinte requisição:
```bash
{
    "name": "João",
    "password": "1234"
}
```
Depois clique em "Send".  
Respostas:

201: Usuário cadastrado com sucesso.

400: Usuário já existe.

### **2. Login**
Endpoint: /login
Método: POST
Descrição: Retorna um token JWT para autenticação.
Requisição:
```bash
{
    "name": "João",
    "password": "1234"
}
```
Respostas:

200: Retorna o token de acesso.

401: Credenciais inválidas.  

Selecione e cole o token gerado. No postman mude para "Authorization". Em "Auth type" selecione "Bearer Token" e cole o token gerado.

---

## **Comandos de implantação:**

### **1. Adicionar Tarefa**
Endpoint: /tasks
Método: POST
Autenticação: Requer JWT.
Descrição: Adiciona uma nova tarefa.
Requisição:
```bash
{
    "title": "Estudar para prova",
    "description": "Revisar matemática",
    "deadline": "2024-12-10 12:00:00"
}
```
Respostas:

201: Tarefa adicionada com sucesso.

401: Token inválido ou ausente.

### **2. Consultar Todas as Tarefas**
Endpoint: /tasks
Método: GET
Autenticação: Requer JWT.
Descrição: Retorna todas as tarefas do usuário autenticado.  
Respostas:

200: Lista de tarefas do usuário.

### **3. Consultar Tarefa por ID**
Endpoint: /tasks/<id>
Método: GET
Autenticação: Requer JWT.
Descrição: Retorna os detalhes de uma tarefa específica.  
O "id" das tarefas se parecem com "cd5d7d2a-bdb4-411f-8471-4e88d33a44f8".  
Respostas:

200: Detalhes da tarefa.

404: Tarefa não encontrada.

### **4. Editar Tarefa**
Endpoint: /tasks/<id>
Método: PUT
Autenticação: Requer JWT.
Descrição: Atualiza os detalhes de uma tarefa específica.
Requisição:
```bash
{
    "title": "Estudar para prova",
    "description": "Estrutura de Dados I, Banco de Dados e Engenharia de Software",
    "deadline": "08/12/2024 08:50:00"
}
```
Respostas:

200: Tarefa atualizada com sucesso.

404: Tarefa não encontrada.

### **5. Marcar Tarefa como Concluída**
Endpoint: /tasks/<id>/done
Método: PUT
Autenticação: Requer JWT.
Descrição: Marca uma tarefa como concluída.
Respostas:

200: Tarefa marcada como feita.

404: Tarefa não encontrada.

### **6. Excluir Tarefa**
Endpoint: /tasks/<id>
Método: DELETE
Autenticação: Requer JWT.
Descrição: Exclui uma tarefa específica.
Respostas:

200: Tarefa deletada com sucesso.

404: Tarefa não encontrada.
