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

## **Execute a API usando os seguintes comandos em um terminal compatível:**

### **Passo 1: Clone o repositório**
```bash
git clone https://github.com/PabloArthur702/API_tasks.git
```
### **Passo 2: Entre no diretório do repositório clonado**
```bash
cd API_tasks
```

### **Passo 3: Crie a imagem Docker**
```bash
docker build -t api-gerenciamento-tarefas .
```

### **Passo 4: Inicie o container**
```bash
docker run -p 5000:5000 -it api-gerenciamento-tarefas
```

### **Passo 5: Uso da API**
Após a execução do container, os endpoints da API estarão disponíveis no servidor **http://localhost:5000/**, permitindo a realização de operações utilizando os métodos para o CRUD. Esses métodos podem ser utilizados para interagir com os recursos da API, como cadastrar, listar, atualizar e excluir tarefas. Certifique-se de incluir o token JWT no cabeçalho das requisições para acessar os endpoints protegidos.

