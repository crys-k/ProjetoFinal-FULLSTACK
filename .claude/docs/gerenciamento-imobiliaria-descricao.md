### **Sistema de Aluguel de Imóveis (Imobiliária)**

**Objetivo:** Gerenciar o aluguel de imóveis (apartamentos, casas, salas comerciais). O sistema deve permitir o cadastro de imóveis, controle de clientes e de locações. O sistema será utilizado somente por funcionários da Imobiliária. O sistema deve fornecer funcionalidades para gerenciar Funcionários, Quartos, Clientes e Reservas. Não será necessário o desenvolvimento de funcionalidades de gerenciamento de pagamento.

**Casos de Uso:**

## **1\. Gerir Funcionários**

 Ator: Administrador  
 Descrição: O administrador pode cadastrar, editar ou remover funcionários do sistema.  
 Fluxo principal:

1. O administrador acessa a opção "Gerenciar Funcionários".  
2. Ele pode adicionar novos funcionários, editar ou excluir contas.

## **2\. Cadastrar Imóvel**

 Ator: Funcionário  
 Descrição: O funcionário pode adicionar novos imóveis ao sistema.  
 Fluxo principal:

1. O funcionário acessa a opção "Cadastrar Imóvel".  
2. Ele preenche informações como endereço, tipo (apartamento, casa, sala comercial), número de quartos, metragem e valor do aluguel.  
3. Ele pode anexar fotos do imóvel.  
4. O sistema salva o cadastro e marca o imóvel como "Disponível".

## **3\. Editar/Remover Imóvel**

 Ator: Funcionário  
 Descrição: O funcionário pode editar ou remover imóveis cadastrados.  
 Fluxo principal:

1. O funcionário acessa a opção "Gerenciar Imóveis".  
2. Ele busca o imóvel desejado.  
3. Ele pode editar os detalhes do imóvel.  
4. Caso o imóvel não tenha locações ativas, ele pode removê-lo do sistema.

## **4\. Gerenciar Clientes**

 Ator: Funcionário  
 Descrição: O funcionário pode cadastrar, editar e visualizar informações de clientes.  
 Fluxo principal:

1. O funcionário acessa a opção "Gerenciar Clientes".  
2. Ele pode visualizar a lista de clientes cadastrados.  
3. Ele pode adicionar um novo cliente, informando nome, CPF/CNPJ, telefone e endereço.  
4. Ele pode editar as informações de um cliente.

## **5\. Criar Locação**

 Ator: Funcionário  
 Descrição: O funcionário pode alugar um imóvel para um cliente.  
 Fluxo principal:

1. O funcionário acessa a opção "Criar Locação".  
2. Ele seleciona um cliente e um imóvel disponível.  
3. Ele define a duração do contrato.  
4. Ele confirma a locação.  
5. O sistema atualiza o status do imóvel para "Alugado".

## **6\. Finalizar Locação**

 Ator: Funcionário  
 Descrição: O funcionário pode encerrar um contrato de aluguel e liberar o imóvel para novas locações.  
 Fluxo principal:

1. O funcionário acessa a opção "Gerenciar Locações".  
2. Ele busca a locação ativa.  
3. Ele encerra o contrato e confirma a devolução do imóvel.  
4. O sistema atualiza o status do imóvel para "Disponível".

## **7\. Cancelar Locação Antes da Entrada**

 Ator: Funcionário  
 Descrição: O funcionário pode cancelar uma locação antes do cliente ocupar o imóvel.  
 Fluxo principal:

1. O funcionário acessa a opção "Gerenciar Locações".  
2. Ele encontra a locação pendente e seleciona "Cancelar Locação".  
3. O sistema libera o imóvel para novas locações.

## **8\. Gerar Relatórios de Locações**

 Ator: Administrador  
 Descrição: O administrador pode gerar relatórios detalhados sobre as locações.  
 Fluxo principal:

1. O administrador acessa a opção "Gerar Relatórios".  
2. Ele seleciona filtros como período, tipo de imóvel ou status da locação.  
3. O sistema exibe os dados em formato de relatório.

## **9\. Bloquear/Desbloquear Imóvel**

 Ator: Administrador  
 Descrição: O administrador pode bloquear um imóvel para manutenção ou outras razões.  
 Fluxo principal:

1. O administrador acessa a opção "Gerenciar Imóveis".  
2. Ele seleciona um imóvel e marca como "Indisponível".  
3. O imóvel não pode mais ser alugado até ser desbloqueado.

## **10\. Registrar Ocorrências no Imóvel**

 Ator: Funcionário  
 Descrição: O funcionário pode registrar problemas no imóvel, como necessidade de manutenção.  
 Fluxo principal:

1. O funcionário acessa a opção "Registrar Ocorrência".  
2. Ele seleciona um imóvel e descreve o problema.  
3. O sistema registra a ocorrência e notifica a equipe responsável.  
   

## **11\. Pesquisar Imóveis Disponíveis**

 Ator: Funcionário  
 Descrição: O funcionário pode buscar imóveis disponíveis para locação de acordo com critérios específicos.  
 Fluxo principal:

1. O funcionário acessa a opção "Pesquisar Imóveis".  
2. Ele insere critérios de busca como localização, tipo de imóvel, número de quartos, valor do aluguel, etc.  
3. O sistema exibe uma lista de imóveis que correspondem aos critérios.  
4. O funcionário pode visualizar os detalhes de um imóvel específico.  
   

