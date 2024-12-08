# **Projeto de Gerenciamento de Tarefas**

Este é um projeto de gerenciamento de tarefas desenvolvido para máteria DCA3603 - ENGENHARIA DE SOFTWARE - T01 (2024.2). Desenvolvida em Python, utilizando o framework Flask. A API implementa autenticação com JWT e está containerizada com Docker.

### **Autores:**

[Mauricio](https://github.com/MauricioMatheus)

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

## **Funcionalidades principais**
1. **Cadastro de tarefas:** Crie tarefas informando título e descrição.  
2. **Listagem de tarefas:** Liste todas as tarefas cadastradas, filtrando por status (pendente/concluído).  
3. **Atualização de tarefas:** Atualize o status de uma tarefa para indicar progresso.  
4. **Autenticação JWT:** Proteja os endpoints, permitindo apenas o acesso de usuários autenticados.  
5. **Implantação com Docker:** Execute o projeto facilmente em um container.  

---

## **Como executar a API**
### **Passo 1: Clone o repositório**
Faça o download ou clone o repositório na sua máquina e abra no seu ambiente de programação.

### **Passo 2: Construa a imagem Docker**
No terminal, dentro da pasta raiz do projeto, execute o seguinte comando para criar a imagem Docker:
```bash
docker build -t api-gerenciamento-tarefas .
```

### **Passo 3: Execute o container**
Após o passo 2, inicie o container com o comando:
```bash
docker run -p 5000:5000 -it api-gerenciamento-tarefas
```

Após a execução do container, os endpoints da API estarão disponíveis no servidor **http://localhost:5000/**, permitindo a realização de operações utilizando os métodos **GET**, **POST** e **DELETE**. Esses métodos podem ser utilizados para interagir com os recursos da API, como cadastrar, listar, atualizar e excluir tarefas. Certifique-se de incluir o token JWT no cabeçalho das requisições para acessar os endpoints protegidos.

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

## **Usar o token JWT:**
Inclua o token no cabeçalho Authorization para acessar os endpoints protegidos.
Exemplo:
```bash	
curl -X GET http://localhost:5000/tasks \
-H "Authorization: Bearer seu_token_aqui"
```
