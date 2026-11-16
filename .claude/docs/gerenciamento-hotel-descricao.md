**Sistema de Gerenciamento de Hotel**

**Objetivo:**  
 	Desenvolver um sistema para a gestão de reservas, check-in e check-out de clientes, e controle de disponibilidade de quartos. O sistema será utilizado somente por funcionários do hotel. O sistema deve fornecer funcionalidades para gerenciar Funcionários, Quartos, Clientes e Reservas. Não será necessário o desenvolvimento de funcionalidades de gerenciamento de pagamento.

**Casos de Uso:**

### **1\. Gerenciar Quartos**

 Ator: Administrador  
 Descrição: O administrador pode adicionar, editar e remover quartos do hotel, definindo suas características e disponibilidade.  
 Fluxo principal:

1. O administrador acessa a opção "Gerenciar Quartos".  
2. Ele pode visualizar a lista de quartos cadastrados.  
3. Ele pode adicionar um novo quarto, informando número, tipo (simples, duplo, suíte), capacidade e status.  
4. Ele pode editar informações de um quarto existente.  
5. Ele pode remover um quarto caso não esteja ocupado.  
   

### **2\. Gerenciar Clientes**

 Ator: Funcionário  
 Descrição: O funcionário pode cadastrar, editar e visualizar informações dos clientes.  
 Fluxo principal:

1. O funcionário acessa a opção "Gerenciar Clientes".  
2. Ele pode visualizar a lista de clientes cadastrados.  
3. Ele pode adicionar um novo cliente com nome, CPF, telefone e endereço, etc.  
4. Ele pode editar as informações de um cliente.  
   

   ## 

   ## 

## **3\. Gerenciar Funcionários**

 Ator: Administrador  
 Descrição: O administrador pode cadastrar, editar ou remover funcionários do sistema.  
 Fluxo principal:

1. O administrador acessa a opção "Gerenciar Funcionários".  
2. Ele pode visualizar a lista de funcionários cadastrados.  
3. Ele pode adicionar um novo funcionário, informando nome, cargo e credenciais de acesso.  
4. Ele pode editar ou desativar um funcionário.

### 

### **4\. Criar Reserva de Quarto**

 Ator: Funcionário  
 Descrição: O funcionário pode realizar reservas para clientes, escolhendo um quarto disponível.  
 Fluxo principal:

1. O funcionário acessa a opção "Criar Reserva".  
2. Ele busca um cliente existente ou cadastra um novo.  
3. Ele escolhe um quarto disponível.  
4. Ele define as datas de entrada e saída.  
5. Ele confirma a reserva.

### **5\. Realizar Check-in**

Ator: Funcionário  
 Descrição: O funcionário registra a entrada do cliente no hotel.  
 Fluxo principal:

1. O funcionário acessa a opção "Check-in".  
2. Ele busca a reserva do cliente.  
3. Ele confirma os dados e entrega a chave do quarto.  
4. O sistema atualiza o status da reserva para "Em andamento".

### **6\. Realizar Check-out**

 Ator: Funcionário  
 Descrição: O funcionário registra a saída do cliente e libera o quarto.  
 Fluxo principal:

1. O funcionário acessa a opção "Check-out".  
2. Ele busca a reserva do cliente.  
3. Ele verifica o estado do quarto.  
4. O sistema atualiza a reserva como "Finalizada" e libera o quarto para novas reservas.

### **7\. Cancelar Reserva**

 Ator: Funcionário  
 Descrição: O funcionário pode cancelar uma reserva antes da data de check-in, liberando o quarto.  
 Fluxo principal:

1. O funcionário acessa a opção "Gerenciar Reservas".  
2. Ele localiza a reserva do cliente.  
3. Ele seleciona a opção "Cancelar Reserva".  
4. O sistema atualiza o status da reserva para "Cancelada" e libera o quarto.

### **8\. Bloquear/Desbloquear Quartos**

 Ator: Administrador  
 Descrição: O administrador pode bloquear temporariamente um quarto para manutenção ou  outro motivo, impedindo reservas.  
 Fluxo principal:

1. O administrador acessa a opção "Gerenciar Quartos".  
2. Ele seleciona um quarto e marca como "Indisponível".  
3. O sistema impede novas reservas para este quarto.  
4. Quando o problema for resolvido, o administrador pode desbloquear o quarto.

### **9\. Gerar Relatórios de Reservas**

Ator: Administrador  
 Descrição: O administrador pode gerar relatórios sobre as reservas do hotel.  
 Fluxo principal:

1. O administrador acessa a opção "Gerar Relatórios".  
2. Ele escolhe filtros como período, cliente, status da reserva ou tipo de quarto.  
3. O sistema gera um relatório detalhado.

### **10\. Registrar Ocorrências em Quartos**

Ator: Funcionário  
 Descrição: O funcionário pode registrar problemas identificados nos quartos, como manutenção necessária ou objetos quebrados.  
 Fluxo principal:

1. O funcionário acessa a opção "Registrar Ocorrências".  
2. Ele escolhe o quarto e descreve o problema.  
3. O sistema registra a ocorrência e notifica a equipe de manutenção.  
   

## **11\. Configurar Tipos de Quartos e Tarifas**

Ator: Administrador  
 Descrição: O administrador pode definir e ajustar as tarifas dos quartos com base no tipo e período.  
 Fluxo principal:

1. O administrador acessa a opção "Configurar Tarifas".  
2. Ele pode visualizar a tabela de preços atual.  
3. Ele pode modificar os valores por tipo de quarto, período ou temporada.  
4. O sistema salva as novas tarifas.  
 


