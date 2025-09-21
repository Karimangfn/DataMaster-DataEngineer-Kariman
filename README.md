# Data Master - Kariman Gomes

&nbsp;

<p align="center">
  <img src="assets/images/Data-Master-Logo.png" width="300">
</p>
&nbsp;

O repositório "DataMaster-DataEngineer-Kariman" apresenta a solução de Engenharia de Dados criada por [Kariman](https://www.linkedin.com/in/kariman-gomes/) como parte do programa Data Master, uma iniciativa da F1rst Santander. <p>

&nbsp;
1. [Objetivo do Projeto]()
   - [Início Rápido]()

2. [Arquitetura de Solução]()
   - [Visão Geral]()
   - [Diagrama da Arquitetura de Solução]()
   - [Componentes Principais]()
   - [Características Essenciais do Projeto]()

3. [Arquitetura Técnica]()
   - [Visão Geral Técnica]()
   - [Descrição do Fluxo de Dados]()
   - [Modelagem e Estrutura do Data Lake]()
   - [Tecnologias e Serviços Utilizados]()
   - [Infraestrutura como Código]()
   - [Orquestração de Pipelines]()
   - [Extração e Ingestão de Dados]()
   - [Armazenamento de Dados]()
   - [Processamento e Transformação dos Dados]()
   - [Qualidade e Validação de Dados]()
   - [Mascaramento e Segurança dos Dados]()
   - [Observabilidade e Monitoramento]()
   - [Escalabilidade e Desempenho]()

4. [Guia de Configuração e Execução]()
   - [Pré-requisitos]()
   - [Configuração da Infraestrutura]()
   - [Configuração de Credenciais e Acessos]()
   - [Execução dos Pipelines de Ingestão]()
   - [Execução dos Pipelines de Transformação]()
   - [Execução da Integração com o CRM]()

5. [Melhorias e Considerações Finais]()
   - [Melhorias Futuras]()
   - [Considerações Finais]()

6. [Custos do Projeto]()

7. [Referências]()

&nbsp;

## 1. Objetivo do Projeto

Este projeto busca integrar dados de clientes espalhados em diferentes fontes e formatos, que dificultam a integração, padronização e análise unificada em um único repositório estruturado, permitindo que os dados sejam processados, transformados e analisados de maneira consistente e confiável, seguindo boas práticas de engenharia de dados e de software.

### 1.1 Problema

Atualmente, os dados de clientes encontram-se distribuídos em diversas fontes, como bancos de dados, APIs e arquivos CSV. Essa fragmentação gera dificuldades como:  
- Redundância e inconsistência entre registros.  
- Dificuldade de padronização e integração dos dados.  
- Falta de rastreabilidade e governança.  
- Barreiras para análises unificadas e confiáveis.

### 1.2 Solução

A solução proposta é construir um pipeline de dados baseado na arquitetura medalhão (Raw → Bronze → Silver → Gold), que:  
- Ingesta dados de múltiplas fontes por meio de microserviços em AKS.  
- Centraliza e organiza as informações em um Data Lake na Azure.  
- Processa e transforma os dados utilizando Databricks e Delta Lake.  
- Aplica limpeza, padronização e mascaramento de dados sensíveis.  
- Disponibiliza camadas de dados confiáveis e prontas para consumo analítico.

## 2. Arquitetura de Solução

### 2.1 Visão Geral

A arquitetura do case foi projetada para integrar dados de diferentes fontes e garantir que eles estejam disponíveis de forma consistente e confiável para análise. Os dados são ingeridos de três origens distintas (banco de dados, API e arquivos CSV) por meio de microserviços, processados e transformados em camadas de dados estruturadas (Bronze → Silver → Gold) e armazenados em um Data Lake na Azure.

O fluxo de dados segue a arquitetura medalhão, garantindo que cada camada tenha dados com níveis crescentes de qualidade e consistência, desde a ingestão bruta até a camada pronta para análise.

### 2.2 Diagrama da Arquitetura de Solução

A seguir, apresentamos a **visão geral da solução**, mostrando como os dados fluem desde a ingestão até a disponibilização das camadas analíticas (Bronze → Silver → Gold).

![Figura 1 — Arquitetura de Solução](assets/images/Arquitetura-Pipeline-de-Dados.png)
*Figura 1 — Arquitetura de solução em alto nível, mostrando ingestão, processamento e armazenamento das camadas do Data Lake.*

### 2.3 Componentes Principais

- **Microserviços de Ingestão (AKS)**: cada microserviço é responsável por extrair dados de uma fonte específica e gravá-los na camada raw do Data Lake. Eles podem ser detalhados posteriormente quanto à linguagem, endpoints e bibliotecas utilizadas.  
- **Data Lake (Azure Storage Account)**: armazena os dados em diferentes camadas de processamento (Raw, Bronze, Silver e Gold), seguindo a arquitetura medalhão e permitindo rastreabilidade e governança.  
- **Databricks**: realiza o processamento e a transformação dos dados. A camada Bronze utiliza o Auto Loader para ingestão automatizada, a camada Silver aplica limpeza, padronização e mascaramento de dados, e a camada Gold gera tabelas prontas para análise.  
- **Infraestrutura como Código (Terraform)**: provisiona todos os recursos necessários, incluindo AKS, Storage Account, Databricks e demais componentes da arquitetura, garantindo consistência e reprodutibilidade.  
- **Automação (GitHub Actions)**: gerencia a criação e atualização da infraestrutura, o deploy dos microserviços e a execução dos jobs no Databricks, garantindo integração contínua e pipelines reproduzíveis.

### 2.4 Características Essenciais do Projeto

## 3. Arquitetura Técnica

### 3.1 Visão Geral Técnica

O projeto utiliza uma arquitetura em nuvem na Azure, combinando práticas de engenharia de dados e engenharia de software. A infraestrutura é provisionada via Terraform e composta por microserviços para ingestão, Data Lake para armazenamento estruturado, Databricks para processamento e pipelines automatizados com GitHub Actions. O objetivo técnico é permitir a ingestão, transformação e disponibilização de dados confiáveis e padronizados em um ambiente reproduzível e escalável.

### 3.2 Descrição do Fluxo de Dados

1. **Ingestão**: os microserviços consomem dados das fontes (banco, API, CSV) e gravam na camada raw do Data Lake.  
2. **Bronze**: Databricks lê os dados da raw e cria tabelas Delta, registrando metadados importantes e mantendo a integridade das informações.  
3. **Silver**: aplica transformações de limpeza, padronização e mascaramento de dados sensíveis.  
4. **Gold**: gera tabelas analíticas prontas para consumo por ferramentas de BI ou análises avançadas.  

### 3.3 Tecnologias e Serviços Utilizados

Azure Storage Account: Armazenamento do Data Lake com camadas Raw, Bronze, Silver e Gold.
AKS (Azure Kubernetes Service): Execução dos microserviços de ingestão.
Databricks: Processamento e transformação dos dados.
Terraform: Provisionamento de toda a infraestrutura na Azure.
GitHub Actions: Automação de criação de infraestrutura, deploy de microserviços e execução de jobs.
Delta Lake: Garantia de consistência, versionamento e ACID nas tabelas.

### 3.4 Infraestrutura como Código

O diagrama abaixo mostra como a **infraestrutura do projeto** é provisionada via Terraform, detalhando os principais recursos criados na Azure.

![Figura 2 — Infraestrutura CI/CD](assets/images/Arquitetura-Infrastructure-CI-CD.png)  
*Figura 2 — Arquitetura de infraestrutura com Terraform e principais recursos provisionados na Azure.*

Toda a infraestrutura do projeto é criada com uso de **Terraform**, que também salva o estado das criações para permitir atualizações ou exclusão da infraestrutura.

### Validações
- **Check GH PAT**: antes da criação dos recursos, é verificado se o *Personal Access Token* do GitHub está criado e configurado com os acessos necessários.  
- **Check Azure Role Assignments**: valida se o *Service Principal* necessário para a criação dos recursos está configurado corretamente com as permissões adequadas.  

### Recursos
- **Resource Group**: responsável por armazenar os recursos.  
- **Azure Container Registry (ACR)**: armazena as imagens dos microserviços.  
- **Azure Kubernetes Service (AKS)**: cluster responsável pela execução dos microserviços.  
- **Storage Account**: armazenamento das tabelas de dados.  
- **Storage Containers**: containers específicos para as camadas de dados Raw, Bronze, Silver e Gold.  
- **Azure Databricks**: utilizado para o processamento de dados, desde a camada Raw até a camada Gold.  

### 3.5 Orquestração de Pipelines

Orquestração ainda em desenvolvimento

### 3.6 Extração e Ingestão de Dados

Este diagrama detalha a **arquitetura CI/CD dos microserviços de ingestão**, mostrando como cada serviço consome suas fontes de dados, gera containers e faz deploy no AKS.

![Figura 3 — Microserviços de Ingestão](assets/images/Arquitetura-Microservices-CI-CD.png)  
*Figura 3 — Arquitetura de CI/CD dos microserviços de ingestão: extração de dados, build, deploy no AKS.*

A ingestão dos dados é realizada por **microserviços** desenvolvidos para cada fonte de dados (banco de dados, API e arquivos CSV). Esses microserviços são empacotados em contêineres e executados em um **Azure Kubernetes Service (AKS)**, garantindo escalabilidade e isolamento de processos.  

O fluxo segue os seguintes passos:  
1. Cada microserviço se conecta à sua respectiva fonte.  
2. Os dados são extraídos no formato de origem (JSON ou CSV).  
3. Os microserviços gravam os dados diretamente na **camada Raw** do Data Lake, em containers específicos.  

Características principais:  
- **Independência**: cada microserviço é responsável por uma fonte, facilitando manutenção e evolução.  
- **Padronização**: apesar das diferentes origens, os dados seguem o mesmo schema.  
- **Escalabilidade**: o uso do AKS permite aumentar ou reduzir réplicas de ingestão conforme a demanda.  
- **Automação**: pipelines no GitHub Actions garantem que os microserviços sejam validados, construídos e implantados automaticamente no cluster.  

### 3.7 Armazenamento de Dados

O armazenamento dos dados é realizado em uma **Storage Account da Azure**, estruturada segundo a arquitetura medalhão.  
Cada camada possui um **container dedicado**, garantindo organização e isolamento entre os estágios do pipeline:

- **Raw**: camada onde os microserviços depositam os dados ingeridos, preservando-os no formato original.  
- **Bronze**: camada onde o Databricks cria tabelas Delta a partir da Raw, garantindo rastreabilidade e histórico.  
- **Silver**: camada que contém dados limpos, padronizados e com mascaramento de informações sensíveis.  
- **Gold**: camada final com dados prontos para consumo em análises e dashboards.  

### 3.8 Processamento e Transformação dos Dados

O diagrama a seguir representa a **arquitetura de processamento de dados**, detalhando o fluxo Bronze → Silver → Gold no Databricks.

![Figura 4 — Data Processing CI](assets/images/Arquitetura-Data-Processing-CI.png)
*Figura 4 — Arquitetura de processamento e transformação de dados em Databricks, seguindo a arquitetura medalhão.*

O processamento dos dados é realizado no **Azure Databricks**, utilizando **notebooks Python** organizados em tarefas dentro de um **Databricks Job**.  
Cada job é dividido em três etapas principais, alinhadas à arquitetura medalhão:

1. **Bronze**  
   - Leitura dos dados da camada Raw por meio do **Auto Loader** do Databricks.  
   - Criação de tabelas **Delta Lake**, preservando os dados ingeridos com histórico e versionamento.  
   - Registro de metadados iniciais para rastreabilidade.  

2. **Silver**  
   - Aplicação de regras de **limpeza e padronização** (ex.: normalização de formatos, remoção de inconsistências).  
   - **Mascaramento de informações sensíveis**, como CPF e número de cartão de crédito.  
   - Enriquecimento dos dados quando necessário.  

3. **Gold**  
   - Estruturação dos dados em modelos analíticos.  
   - Preparação das tabelas para consumo em ferramentas de BI e relatórios.  
   - Disponibilização de dados consistentes e confiáveis para análise.

### 3.9 Qualidade e Validação de Dados

A qualidade dos dados é garantida a partir da camada **Silver**, onde são aplicadas regras de validação e consistência antes de disponibilizar as informações para consumo.  
O processo combina verificações automatizadas e padronizações implementadas nos notebooks do Databricks.

Principais validações aplicadas:  
- **Integridade de schema**: checagem se os dados seguem o schema esperado.  
- **Valores obrigatórios**: verificação de colunas críticas que não podem estar nulas (ex.: `customer_id`, `cpf`).  
- **Formatos válidos**: conferência de padrões, como CPF válido ou formato correto de e-mail.  
- **Valores de domínio**: validação de atributos contra listas pré-definidas (ex.: localização de lojas).  

Ferramentas e práticas:  
- **Delta Lake** para versionamento e rollback em caso de ingestão incorreta.  
- **Notebooks Python no Databricks** com funções de validação.  
- Possibilidade futura de integração com frameworks como **Great Expectations** para validações mais complexas e documentação de regras de qualidade.  

**Benefícios principais**:  
- Evita propagação de dados inconsistentes para as camadas analíticas.  
- Garante confiabilidade e consistência para relatórios e dashboards.  
- Facilita auditoria e rastreabilidade em caso de erros de ingestão ou transformação.  

### 3.10 Mascaramento e Segurança dos Dados

O projeto adota práticas de **segurança e privacidade** para proteger informações sensíveis dos clientes durante o ciclo de vida dos dados.  
O foco principal está no **mascaramento de dados pessoais**, realizado na transição da camada **Bronze → Silver**.

#### Mascaramento de Dados
- **CPF**: substituição parcial dos dígitos, preservando apenas os últimos 3 para rastreabilidade.  
- **Número de cartão de crédito**: ocultação de todos os dígitos, exceto os 4 últimos.  
- **E-mail**: ofuscação parcial do endereço, mantendo o domínio visível.  

Essas transformações são aplicadas via **notebooks Python no Databricks**, garantindo que os dados sensíveis não avancem para a camada Gold.

#### Segurança de Armazenamento e Acesso
- **Azure Storage Account**: controle de permissões via *role-based access control* (RBAC).  
- **Segregação por camadas**: cada container (Raw, Bronze, Silver, Gold) possui políticas de acesso específicas.  
- **GitHub Actions**: uso de *secrets* para armazenar credenciais de forma segura.  
- **Service Principals**: autenticação entre serviços com permissões mínimas necessárias.  

**Benefícios principais**:  
- Proteção de informações sensíveis em conformidade com boas práticas de governança.  
- Redução de riscos em auditorias e conformidade regulatória (LGPD).  
- Garantia de que dados analíticos não exponham informações pessoais desnecessárias.  

### 3.11 Observabilidade e Monitoramento

O projeto prevê mecanismos de **observabilidade e monitoramento** para acompanhar a execução dos pipelines, identificar falhas rapidamente e garantir confiabilidade no fluxo de dados.

#### Logs e Métricas
- **Microserviços (AKS)**: geração de logs de execução e falhas, que podem ser integrados ao **Azure Monitor** ou **Application Insights**.  
- **Databricks Jobs**: registro automático de logs de execução, status de tarefas e métricas de processamento.  
- **GitHub Actions**: logs detalhados de cada etapa de CI/CD, permitindo auditoria das execuções.  

#### Alertas
- Configuração de alertas no **Azure Monitor** para falhas em microserviços ou indisponibilidade de recursos.  
- Alertas no **Databricks** para jobs que falharem ou ultrapassarem o tempo limite de execução.  

#### Observabilidade de Dados
- Métricas de volume de dados ingeridos em cada fonte.  
- Taxa de erros de ingestão ou registros inválidos.  
- Possibilidade futura de integração com ferramentas de **Data Lineage** para rastreabilidade ponta a ponta.  

**Benefícios principais**:  
- Redução do tempo de detecção e resposta a falhas.  
- Garantia de confiabilidade e disponibilidade dos pipelines.  
- Maior transparência sobre a saúde do ecossistema de dados.  

### 3.12 Escalabilidade e Desempenho

O projeto foi estruturado para suportar aumento de volume de dados e crescimento no número de fontes, mantendo eficiência e confiabilidade no processamento.

#### Escalabilidade
- **Microserviços em AKS**: permitem escalar horizontalmente, aumentando ou reduzindo réplicas conforme a demanda de ingestão.  
- **Databricks**: suporte a clusters escaláveis sob demanda, otimizando custo e performance no processamento das camadas Bronze, Silver e Gold.  
- **Storage Account**: arquitetura baseada em containers independentes para cada camada de dados, possibilitando expansão sem necessidade de reestruturação.  

#### Desempenho
- **Delta Lake**: garante performance em consultas e manipulação de grandes volumes de dados por meio de otimizações internas (indexação, caching e compactação de arquivos).  
- **Auto Loader**: possibilita ingestão contínua e eficiente dos dados da Raw para a Bronze, reduzindo o tempo de latência.  
- **Transformações distribuídas no Databricks**: uso de processamento paralelo para melhorar a velocidade em operações de limpeza e padronização.  

**Benefícios principais**:  
- Capacidade de lidar com aumento no volume e variedade de dados.  
- Redução da latência entre ingestão e disponibilização dos dados analíticos.  
- Otimização de custos ao escalar recursos somente quando necessário.

## 4. Guia de Configuração e Execução

### 4.1 Pré-requisitos

Antes de configurar e executar o projeto, é necessário garantir que o ambiente possua os seguintes pré-requisitos:

#### Identidade e Permissões
- **Service Principal (SPN)** criado previamente.  
- **Secret da SPN** configurado (Secret Value, não o Secret ID).  
- A **SPN** precisa ter permissões na assinatura da Azure:  
  - *Contributor*  
  - *User Access Administrator*  
- A **SPN** deve ter também a role **Storage Blob Data Contributor** associada.  

#### Configuração do AKS e ACR
- O nome do **ACR** deve ser informado **sem o sufixo** `.azurecr.io`.  
- O **AKS** é privado, logo os comandos devem ser executados via `az aks command invoke`.  
- O nó do AKS deve ser baseado em arquitetura **AMD** (ARM não é suportado).  

#### GitHub Actions
- **Workflow permissions** devem estar configuradas como **Read and Write**.  
- **Personal Access Token (PAT)** do GitHub criado e salvo nas *Secrets* do repositório com permissões adequadas.  

#### Configurações de Rede
- O recurso **Network Watcher NG** precisa estar desabilitado na região da implantação.  

#### Secrets obrigatórias no GitHub
As seguintes *secrets* devem estar configuradas no repositório:  
- `DB_KEY`  
- `API_KEY`  
- `ACR_NAME`  
- `AKS_NAME`  
- `STORAGE_ACCOUNT`  
- `AZURE_CREDENTIALS`  
- `RESOURCE_GROUP`  
- `GH_PAT_TOKEN`  

### 4.2 Configuração da Infraestrutura

A criação e configuração da infraestrutura do projeto é realizada de forma automatizada utilizando **Terraform** em conjunto com **GitHub Actions**.  
Esse processo garante reprodutibilidade, versionamento e consistência em todas as implantações.

#### Passos principais

1. **Clonar o repositório**
   ```bash
   git clone https://github.com/<usuario>/<repo>.git
   cd <repo>
Configurar as secrets no GitHub

Definir todas as secrets obrigatórias listadas na seção Pré-requisitos.

Garantir que o workflow permissions esteja configurado como Read and Write.

Executar o workflow de criação de infraestrutura

O workflow do GitHub Actions responsável pela criação da infraestrutura deve ser acionado manualmente (workflow_dispatch) ou via push para o branch principal.

Esse pipeline realiza:

Validação de credenciais e permissões.

Criação/atualização do Resource Group.

Provisionamento do Storage Account com containers (Raw, Bronze, Silver, Gold).

Criação do Azure Container Registry (ACR).

Deploy do Azure Kubernetes Service (AKS).

Configuração do Azure Databricks.

Validar a implantação

Confirmar que todos os recursos foram criados no Resource Group especificado.

Testar conectividade do AKS utilizando:

bash
Copiar código
az aks command invoke --name <aks-name> --resource-group <rg-name> --command "kubectl get pods -A"
Verificar se os containers do Storage estão organizados conforme a arquitetura medalhão.

Observações
O Terraform utiliza Remote State armazenado nos artifacts do GitHub Actions, permitindo atualizações e destruição da infraestrutura de forma segura.

Existe um workflow específico para exclusão completa da infraestrutura, que deve ser executado com cautela.

### 4.3 Configuração de Credenciais e Acessos

Para garantir que a infraestrutura e os pipelines de dados sejam provisionados e executados corretamente, é necessário configurar credenciais e permissões adequadas no **Azure** e no **GitHub**.

#### 1. Service Principal (SPN)
O projeto utiliza uma **Service Principal (SPN)** para autenticação e criação de recursos no Azure.

- Criação da SPN:
  ```bash
  az ad sp create-for-rbac \
    --name spn-datamaster \
    --role Contributor \
    --scopes /subscriptions/<SUBSCRIPTION_ID>
Permissões necessárias:

Contributor → criação e gerenciamento dos recursos.

User Access Administrator → atribuição de permissões a outros recursos/usuários.

Storage Blob Data Contributor → acesso ao Storage Account.

⚠️ Atenção: a SPN deve ter secret value salvo, não apenas o secret ID.

2. Secrets no GitHub
As seguintes secrets devem ser configuradas no repositório (Settings > Secrets and variables > Actions):

DB_KEY → chave de acesso para a fonte de dados do banco de dados.

API_KEY → chave de acesso para a API de clientes.

ACR_NAME → nome do Azure Container Registry (sem o sufixo .azurecr.io).

AKS_NAME → nome do cluster Kubernetes (AKS).

STORAGE_ACCOUNT → nome da Storage Account.

AZURE_CREDENTIALS → credenciais em formato JSON da SPN criada no Azure.

RESOURCE_GROUP → nome do Resource Group utilizado.

GH_PAT_TOKEN → token pessoal do GitHub, com permissões de leitura/escrita para automações.

3. Configurações adicionais
O cluster AKS é privado, portanto todos os comandos devem ser executados via:

bash
Copiar código
az aks command invoke
O node pool do AKS deve utilizar arquitetura AMD (não ARM).

Desabilitar o recurso Network Watcher NG na região do projeto para evitar conflitos de monitoramento.

4. Workflow Permissions
No repositório, configure os Workflow permissions em:
Settings > Actions > General > Workflow permissions

Selecione Read and Write permissions para permitir que os workflows criem e atualizem recursos no Azure.

### 4.4 Execução dos Pipelines de Ingestão

A ingestão de dados neste projeto é realizada por meio de **microserviços** executados em um cluster **AKS (Azure Kubernetes Service)**.  
Cada microserviço é responsável por extrair dados de uma fonte distinta (**Banco de Dados**, **API** e **Arquivos CSV**) e gravá-los na camada **Raw** do Data Lake.

#### 1. Deploy dos Microserviços
O deploy dos microserviços é feito via GitHub Actions.  
Ao realizar um **merge** na branch `main`, o pipeline responsável irá:

1. **Buildar as imagens** Docker dos microserviços.  
2. **Publicar as imagens** no **Azure Container Registry (ACR)**.  
3. **Deployar as imagens** no cluster **AKS**.

Esse processo é totalmente automatizado pela esteira de CI/CD configurada no repositório.

#### 2. Execução da Ingestão
Uma vez que os microserviços estejam em execução no **AKS**, cada um consome sua fonte de dados:

- **Banco de Dados** → extrai registros no formato `.json`.  
- **API** → coleta dados de clientes e normaliza no mesmo schema.  
- **Arquivos CSV** → lê e processa arquivos armazenados em diretórios de entrada.  

Todos os dados são enviados para a **camada Raw** do **Azure Storage Account**.

#### 3. Acesso ao Cluster Privado
Como o **AKS** é privado, os comandos de execução e troubleshooting devem ser feitos usando:

```bash
az aks command invoke \
  --resource-group <RESOURCE_GROUP> \
  --name <AKS_NAME> \
  --command "kubectl get pods -n <namespace>"
4. Observando a Ingestão
Para verificar se os microserviços estão rodando corretamente:

Validar os pods no cluster:

bash
Copiar código
kubectl get pods -n <namespace>
Conferir os logs:

bash
Copiar código
kubectl logs <pod_name> -n <namespace>
Validar que os arquivos foram gravados na camada Raw do Data Lake:

bash
Copiar código
az storage blob list \
  --account-name <STORAGE_ACCOUNT> \
  --container-name raw \
  --output table
5. Considerações
A arquitetura permite que novas fontes sejam adicionadas facilmente criando um novo microserviço e registrando sua imagem no ACR.

O pipeline garante que qualquer atualização de código nos microserviços resulte em uma nova versão sendo automaticamente publicada e executada no AKS.
```

### 4.5 Execução dos Pipelines de Transformação

Após a ingestão na camada **Raw**, os dados passam por pipelines de transformação no **Databricks**, organizados segundo a **arquitetura medalhão** (Bronze → Silver → Gold).  
Esses pipelines são implementados como **notebooks em Python** e orquestrados via **Databricks Jobs**.

#### 1. Estrutura do Job no Databricks
O Job é composto por **3 tasks sequenciais**:

1. **Bronze**  
   - Consome dados da camada Raw utilizando o **Auto Loader** do Databricks.  
   - Cria tabelas Delta na camada Bronze.  
   - Garante schema enforcement e versionamento dos dados.  

2. **Silver**  
   - Aplica transformações de limpeza e padronização.  
   - Realiza o **mascaramento de dados sensíveis** (ex.: CPF, cartão de crédito).  
   - Cria tabelas Delta refinadas e prontas para análises intermediárias.  

3. **Gold**  
   - Gera tabelas analíticas e métricas de negócio (ex.: total de compras, clientes por loja).  
   - Disponibiliza dados prontos para consumo por ferramentas de BI e relatórios.  

#### 2. Execução Manual do Job
Para executar manualmente os pipelines no Databricks:

1. Acesse o **Workspace do Databricks**.  
2. Vá até a seção **Jobs**.
3. Localize o Job configurado (ex.: `etl-customers`).
4. Clique em **Run Now** para disparar a execução.

#### 3. Execução Automatizada
A execução também pode ser disparada automaticamente via **GitHub Actions**:
- Ao atualizar os notebooks no repositório, a esteira de CI/CD valida o código.  
- Caso aprovado, o pipeline de deploy publica os notebooks no Databricks.  
- O **Databricks CLI** é então usado para disparar o Job de transformação.  

#### 4. Monitoramento
Durante a execução do Job, é possível acompanhar:
- **Logs de execução** diretamente no Databricks.  
- Status de cada task (Success / Failed / Running).  
- Histórico de execuções, permitindo auditoria e rastreabilidade.  

#### 5. Considerações
- O uso do **Delta Lake** garante versionamento e controle de qualidade.  
- A separação em camadas (Bronze, Silver, Gold) assegura evolução gradual na confiabilidade dos dados.  
- Novas transformações podem ser adicionadas facilmente criando tasks adicionais no Job.

## 5. Melhorias e Considerações Finais

### 5.1 Melhorias Futuras

Apesar de o projeto atender ao objetivo principal de centralizar dados de múltiplas fontes em um Data Lake estruturado e processado até a camada Gold, existem pontos de evolução que podem ser incorporados em versões futuras:

- **Segurança de Rede (VNet e Private Endpoints):** inclusão de Virtual Networks e Private Endpoints para isolar os recursos da Azure e garantir maior segurança no tráfego de dados.  
- **Fluxo de Ambientes (Dev / Pre / Prod):** implementação de múltiplos ambientes com pipelines de deploy independentes, possibilitando testes e validações antes de subir em produção.  
- **Governança de Dados:** integração com catálogos de dados (ex.: **Unity Catalog**, **Purview**) para melhor rastreabilidade, versionamento e gestão de acesso.  
- **Qualidade e Validação de Dados:** uso de ferramentas como **Great Expectations** para validar schemas, detectar anomalias e garantir consistência antes de promover dados para Silver/Gold.  
- **Orquestração Completa:** adotar um orquestrador dedicado (ex.: **Airflow**, **Prefect**, ou **Azure Data Factory**) para controlar tanto ingestão quanto processamento, permitindo maior automação e dependências entre pipelines.  
- **Observabilidade e Alertas:** centralizar métricas, logs e alertas em ferramentas como **Azure Monitor** ou **Grafana**, possibilitando detecção proativa de falhas.  
- **Testes Automatizados:** expandir o uso de testes unitários e de integração para notebooks e microserviços, garantindo maior confiabilidade nas mudanças de código.  
- **Custo e Performance:** analisar otimizações de custo (storage tiers, autoscaling de clusters no Databricks) e desempenho (particionamento e otimização de tabelas Delta).  

### 5.2 Considerações Finais

O projeto demonstrou como é possível integrar dados de múltiplas fontes e formatos, organizando-os em um pipeline escalável e confiável na Azure.  
A solução aplicou boas práticas de engenharia de dados (arquitetura medalhão, uso de Delta Lake, pipelines automatizados) em conjunto com boas práticas de engenharia de software (microserviços, CI/CD, IaC).  

Embora ainda existam pontos de evolução, a arquitetura atual já fornece uma base sólida para ingestão, transformação e disponibilização de dados prontos para análise, podendo ser expandida gradualmente conforme as necessidades de negócio e requisitos de governança cresçam.

## 6. Referências