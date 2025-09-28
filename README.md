# Data Master - Kariman Gomes

<p align="center">
  <img src="assets/images/Data-Master-Logo.png" style="width:800px; height:250px;">
</p>

O repositório "DataMaster-DataEngineer-Kariman" apresenta a solução de Engenharia de Dados criada por [Kariman](https://www.linkedin.com/in/kariman-gomes/) como parte do programa Data Master, uma iniciativa da F1rst Santander. <p>

## 📑 Sumário

<details>
  <summary>📌 1. Objetivo do Projeto</summary>

  - [Início Rápido](#inicio-rapido)

</details>

<details>
  <summary>🏗️ 2. Arquitetura de Solução</summary>

  - [Visão Geral](#visao-geral)
  - [Diagrama da Arquitetura de Solução](#diagrama-da-arquitetura-de-solucao)
  - [Componentes Principais](#componentes-principais)
  - [Características Essenciais do Projeto](#caracteristicas-essenciais-do-projeto)

</details>

<details>
  <summary>⚙️ 3. Arquitetura Técnica</summary>

  - [Visão Geral Técnica](#visao-geral-tecnica)
  - [Descrição do Fluxo de Dados](#descricao-do-fluxo-de-dados)
  - [Modelagem e Estrutura do Data Lake](#modelagem-e-estrutura-do-data-lake)
  - [Tecnologias e Serviços Utilizados](#tecnologias-e-servicos-utilizados)
  - [Infraestrutura como Código](#infraestrutura-como-codigo)
  - [Orquestração de Pipelines](#orquestracao-de-pipelines)
  - [Extração e Ingestão de Dados](#extracao-e-ingestao-de-dados)
  - [Armazenamento de Dados](#armazenamento-de-dados)
  - [Processamento e Transformação dos Dados](#processamento-e-transformacao-dos-dados)
  - [Qualidade e Validação de Dados](#qualidade-e-validacao-de-dados)
  - [Mascaramento e Segurança dos Dados](#mascaramento-e-seguranca-dos-dados)
  - [Observabilidade e Monitoramento](#observabilidade-e-monitoramento)
  - [Escalabilidade e Desempenho](#escalabilidade-e-desempenho)

</details>

<details>
  <summary>🚀 4. Guia de Configuração e Execução</summary>

  - [Pré-requisitos](#pre-requisitos)
  - [Configuração da Infraestrutura](#configuracao-da-infraestrutura)
  - [Configuração de Credenciais e Acessos](#configuracao-de-credenciais-e-acessos)
  - [Execução dos Pipelines de Ingestão](#execucao-dos-pipelines-de-ingestao)
  - [Execução dos Pipelines de Transformação](#execucao-dos-pipelines-de-transformacao)
  - [Execução da Integração com o CRM](#execucao-da-integracao-com-o-crm)

</details>

<details>
  <summary>💡 5. Melhorias e Considerações Finais</summary>

  - [Melhorias Futuras](#melhorias-futuras)
  - [Considerações Finais](#consideracoes-finais)

</details>

<details>
  <summary>💰 6. Custos do Projeto</summary>
</details>

<details>
  <summary>📚 7. Referências</summary>
</details>

##  📌 1. Objetivo do Projeto

Este projeto busca integrar dados de clientes espalhados em diferentes fontes e formatos, que dificultam a integração, padronização e análise unificada em um único repositório estruturado, permitindo que os dados sejam processados, transformados e analisados de maneira consistente e confiável, seguindo boas práticas de engenharia de dados e de software.

### 1.1 Problema

Atualmente, os dados de clientes encontram-se distribuídos em diversas fontes, como bancos de dados, APIs e arquivos CSV. Essa fragmentação gera dificuldades como:  
- Redundância e inconsistência entre registros.  
- Dificuldade de padronização e integração dos dados.  
- Falta de rastreabilidade e governança.  
- Barreiras para análises unificadas e confiáveis.

### 1.2 Solução

A solução proposta é construir um pipeline de dados baseado na arquitetura medalhão (Raw → Bronze → Silver → Gold), que:  
- Faz a ingestão dados de múltiplas fontes por meio de microserviços.  
- Centraliza e organiza as informações em um Data Lake na Azure.
- Processa e transforma os dados utilizando Databricks e Delta Lake. 
- Aplica limpeza, padronização e mascaramento de dados sensíveis.  
- Disponibiliza camadas de dados confiáveis e prontas para consumo analítico.

##  🏗️ 2. Arquitetura de Solução

### 2.1 Visão Geral

A arquitetura do case foi projetada para integrar dados de diferentes fontes e garantir que eles estejam disponíveis de forma consistente e confiável para análise. Os dados são ingeridos de três origens distintas (banco de dados, API e arquivos CSV) por meio de microserviços, processados e transformados em camadas de dados estruturadas (Bronze → Silver → Gold) e armazenados em um Data Lake na Azure.

O fluxo de dados segue a arquitetura medalhão, garantindo que cada camada tenha dados com níveis crescentes de qualidade e consistência, desde a ingestão bruta até a camada pronta para análise.

### 2.2 Diagrama da Arquitetura de Solução

![Figura 1 — Arquitetura de Solução](assets/images/Arquitetura-Pipeline-de-Dados.png)

*Figura 1 — Arquitetura de solução em alto nível, mostrando ingestão, processamento e armazenamento das camadas do Data Lake.*

### 2.3 Componentes Principais

- **Microserviços de Ingestão**: Cada microserviço é responsável por extrair dados de uma fonte específica e gravá-los na camada raw do Data Lake. Eles podem ser detalhados posteriormente quanto à linguagem, endpoints e bibliotecas utilizadas.  
- **Data Lake (Azure Storage Account)**: Armazena os dados em diferentes camadas de processamento (Raw, Bronze, Silver e Gold), seguindo a arquitetura medalhão e permitindo rastreabilidade e governança.  
- **Databricks**: realiza o processamento e a transformação dos dados. A camada Bronze utiliza o Auto Loader para ingestão automatizada, a camada Silver aplica limpeza, padronização e mascaramento de dados, e a camada Gold gera tabelas prontas para análise.  
- **Infraestrutura como Código (Terraform)**: Provisiona todos os recursos necessários, incluindo AKS, Storage Account, Databricks e demais componentes da arquitetura.  
- **Automação (GitHub Actions)**: Gerencia a criação, o deploy dos microserviços e verificação de qualidade de código.

## ⚙️ 3. Arquitetura Técnica

### 3.1 Visão Geral Técnica

O projeto utiliza uma arquitetura em nuvem na Azure, combinando práticas de engenharia de dados e engenharia de software. A infraestrutura é provisionada via Terraform e composta por microserviços para ingestão, Data Lake para armazenamento estruturado, Databricks para processamento e pipelines automatizados com GitHub Actions. O objetivo técnico é permitir a ingestão, transformação e disponibilização de dados confiáveis e padronizados em um ambiente reproduzível e escalável.

### 3.2 Descrição do Fluxo de Dados

1. **Ingestão**: Os microserviços consomem dados das fontes (Banco de Dados, API, Arquivos) e gravam na camada raw do Data Lake. 
2. **Bronze**: Databricks lê os dados da raw e cria tabelas Delta, mantendo a integridade das informações.  
3. **Silver**: Aplica transformações de limpeza, padronização e mascaramento de dados sensíveis.  
4. **Gold**: Gera tabelas prontas para consumo por ferramentas de BI ou análises avançadas.  

### 3.3 Tecnologias e Serviços Utilizados

- **Resource Group**: Agrupa todos os recursos provisionados na Azure. 
- **Storage Account**: Armazenamento do Data Lake com camadas Raw, Bronze, Silver e Gold.
- **ACR (Azure Container Service)**: Repositório para armazenar e versionar as imagens Docker dos microserviços.  
- **AKS (Azure Kubernetes Service)**: Execução dos microserviços de ingestão.
- **Databricks**: Processamento e transformação dos dados.
- **Delta Lake**: Garantia de consistência, versionamento e ACID nas tabelas.
- **Auto Loader**: Responsável por ingestão contínua dos dados da camada Raw para a Bronze.
- **Terraform**: Provisionamento de toda a infraestrutura na Azure.
- **GitHub Actions**: Automação de criação de infraestrutura, deploy de microserviços e execução de jobs.

### 3.4 Infraestrutura como Código

![Figura 2 — Infraestrutura CI/CD](assets/images/Arquitetura-Infrastructure-CI-CD.png)  

*Figura 2 — Arquitetura de infraestrutura com Terraform e principais recursos provisionados na Azure.*

Toda a infraestrutura do projeto é criada com uso de **Terraform**, que também salva o estado das criações para permitir atualizações ou exclusão da infraestrutura.

### Validações (CI)
- **Check Github Token**: Antes da criação dos recursos, é verificado se o *Personal Access Token* do GitHub está criado e configurado com os acessos necessários.
- **Check Azure Role Assignments**: Valida se o *Service Principal* necessário para a criação dos recursos está configurado corretamente com as permissões adequadas.  

### Criação de Recursos (CD)
- **Resource Group**: Responsável por armazenar os recursos.  
- **Azure Container Registry (ACR)**: Armazena as imagens dos microserviços.  
- **Azure Kubernetes Service (AKS)**: Cluster responsável pela execução dos microserviços.  
- **Storage Account**: Armazenamento das tabelas de dados.  
- **Storage Containers**: Containers específicos para as camadas de dados Raw, Bronze, Silver e Gold.  
- **Databricks**: Utilizado para o processamento de dados, desde a camada Raw até a camada Gold.

### 3.5 GitHub Actions

O GitHub Actions é responsável por orquestrar e automatizar todas as etapas do projeto, incluindo:

- **Provisionamento de Infraestrutura**: executa o Terraform para criação e atualização de recursos na Azure.  
- **Deploy de Microserviços**: build e publicação de imagens Docker no ACR, seguido de deploy no AKS.  
- **Transformação de Dados**: integração com Databricks para execução dos pipelines de Bronze, Silver e Gold.  

#### Resumo de Execução (Summary)
Cada execução de workflow gera automaticamente um **summary** dentro do GitHub Actions, contendo:  
- Recursos criados/atualizados pelo Terraform.  
- Status de execução das etapas (Infra, Ingestão, Transformação).  
- Outputs importantes do Terraform.  
- Links para logs detalhados de cada job.  

**Colocar imagem aqui dos summaries depois**

Esse resumo facilita a **auditoria** e permite acompanhar rapidamente o resultado das execuções sem precisar navegar em todos os logs.

#### Fluxo dos Workflows
1. **Infraestrutura** → Provisionamento completo via Terraform.  
2. **Ingestão** → Deploy automático de microserviços no AKS.  
3. **Transformação** → Execução dos notebooks no Databricks.  
4. **Exclusão** → Workflow específico para destruição segura da infraestrutura.  

Todos os workflows podem ser acionados manualmente (`workflow_dispatch`) ou automaticamente via `push` na branch principal.

### 3.6 Orquestração de Pipelines

Orquestração ainda em desenvolvimento

### 3.7 Extração e Ingestão de Dados

![Figura 3 — Microserviços de Ingestão](assets/images/Arquitetura-Microservices-CI-CD.png)  

*Figura 3 — Arquitetura de CI/CD dos microserviços de ingestão: extração de dados, build, deploy no AKS.*

A ingestão dos dados é realizada por **microserviços** desenvolvidos para cada fonte de dados (Banco de Dados, API e Arquivos). Esses microserviços são empacotados em contêineres e executados em um **Azure Kubernetes Service (AKS)**.

O fluxo segue os seguintes passos:  
1. Cada microserviço se conecta à sua respectiva fonte.  
2. Os dados são extraídos no formato de origem (JSON ou CSV).  
3. Os microserviços gravam os dados diretamente na **camada Raw** do Data Lake, em pastas específicos.  

Características principais:
- **Independência**: Cada microserviço é responsável por uma fonte, facilitando manutenção e evolução.  
- **Padronização**: Apesar das diferentes origens, os dados seguem o mesmo schema.  
- **Escalabilidade**: O uso do AKS permite aumentar ou reduzir réplicas de ingestão conforme a demanda.  
- **Automação**: Pipelines no GitHub Actions garantem que os microserviços sejam validados, construídos e implantados automaticamente no cluster.

#### Estrutura
microservice_name/
├── helm/               # Helm chart para deploy no AKS
├── src/
│ ├── application/      # Regras de negócio da aplicação
│ │ ├── helpers/        # Funções utilitárias
│ │ ├── services/       # Serviços de orquestração da lógica
│ │ └── validators/     # Validações de entrada e regras específicas
│ ├── domain/           # Definições de domínio
│ │ ├── exceptions/     # Classes de exceções específicas
│ │ └── ports/          # Interfaces para comunicação entre camadas
│ ├── infrastructure/   # Implementações concretas
│ │ ├── authentication/ # Autenticação e segurança
│ │ ├── config/         # Configurações de ambiente
│ │ ├── logging/        # Logs e monitoramento
│ │ ├── ingestion/      # Conectores e ingestão de dados
│ │ └── storage/        # Interação com o Data Lake
│ └── interfaces/       # Pontos de entrada
│ └── main.py           # API/CLI principal do microserviço
├── tests/              # Testes unitários e de integração
├── Dockerfile          # Definição da imagem Docker
├── Makefile            # Definição da imagem Docker
├── requirements.txt    # Dependências do serviço
├── setup.py            # Definição da imagem Docker
└── VERSION             # Usado para versionamento do Microserviço

A organização segue princípios da Clean Architecture, garantindo separação de responsabilidades e facilidade de manutenção:
- **domain** → Regras de negócio puras, interfaces (ports) e exceções.
- **application** → Casos de uso, serviços, validadores e helpers.
- **infrastructure** → Autenticação, logging, ingestão e persistência.
- **interfaces** → Pontos de entrada do serviço (ex.: main.py).
- **tests** → Testes unitários e de integração.
- **helm** → Manifests para deploy no AKS.

Arquivos de Configuração:
- **.dockerignore** -> Exclui arquivos desnecessários no build Docker.  
- **.flake8** -> Regras de lint para garantir padrão de código. 
- **.gitignore** -> Define arquivos ignorados no versionamento.
- **.pre-commit-config.yaml** -> Hooks para validações automáticas antes do commit.
- **pytest.ini** -> Configurações para execução dos testes com Pytest.

### 3.8 Armazenamento de Dados

O armazenamento dos dados é realizado em uma **Azure Storage Account**, estruturada segundo a arquitetura medalhão.
Cada camada possui um **container dedicado**, garantindo organização e isolamento entre os estágios do pipeline:

- **Raw**: Camada onde os microserviços depositam os dados ingeridos, preservando-os no formato original.  
- **Bronze**: Camada onde o Databricks cria tabelas Delta a partir da Raw, garantindo rastreabilidade e histórico.  
- **Silver**: Camada que contém dados limpos, padronizados e com mascaramento de informações sensíveis.  
- **Gold**: Camada final com dados prontos para consumo em análises e dashboards. 

### 3.9 Processamento e Transformação dos Dados

![Figura 4 — Data Processing CI](assets/images/Arquitetura-Data-Processing-CI.png)

*Figura 4 — Arquitetura de processamento e transformação de dados em Databricks, seguindo a arquitetura medalhão.*

O processamento dos dados é realizado no **Databricks**, utilizando **Microserviços Python** organizados em tarefas dentro de um **Job**.
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

#### Estrutura
processing_job/  
├── src/  
│   ├── config/       # Configurações do pipeline (parâmetros, schemas, paths)  
│   ├── modules/      # Módulos principais de transformação (Bronze, Silver ou Gold)  
│   ├── utils/        # Funções utilitárias reutilizáveis  
│   └── main.py       # Script principal do job executado no Databricks  
├── tests/            # Testes unitários e de integração  
├── requirements.txt  # Dependências do job

Arquivos de Configuração
- **.flake8** → Regras de lint para garantir padrão de código.
- **.gitignore** -> Define arquivos ignorados no versionamento.
- **.pre-commit-config.yaml** → Hooks para validações automáticas antes do commit.  
- **pytest.ini** → Configurações para execução dos testes com Pytest.

### 3.10 Qualidade e Validação de Dados

A qualidade dos dados é garantida a partir da camada **Silver**, onde são aplicadas regras de validação e consistência antes de disponibilizar as informações para consumo.  
O processo combina verificações automatizadas e padronizações implementadas nos notebooks do Databricks.

Principais validações aplicadas:  
- **Integridade de schema**: checagem se os dados seguem o schema esperado.  
- **Valores obrigatórios**: verificação de colunas críticas que não podem estar nulas (ex.: `customer_id`, `cpf`).  
- **Formatos válidos**: conferência de padrões, como CPF válido ou formato correto de e-mail.  
- **Valores de domínio**: validação de atributos contra listas pré-definidas (ex.: localização de lojas).  

Ferramentas e práticas:  
- **Delta Lake** para versionamento e rollback em caso de ingestão incorreta.  
- **Microserviço Python no Databricks** com funções de validação.    

**Benefícios principais**:  
- Evita propagação de dados inconsistentes para as camadas analíticas.  
- Garante confiabilidade e consistência para relatórios e dashboards.  
- Facilita auditoria e rastreabilidade em caso de erros de ingestão ou transformação.

### 3.11 Mascaramento e Segurança dos Dados

O projeto adota práticas de **segurança e privacidade** para proteger informações sensíveis dos clientes durante o ciclo de vida dos dados.  
O foco principal está no **mascaramento de dados pessoais**, realizado na transição da camada **Bronze → Silver**.

#### Mascaramento de Dados
- **CPF**: substituição parcial dos dígitos, preservando apenas os últimos 3 para rastreabilidade.  
- **Número de cartão de crédito**: ocultação de todos os dígitos, exceto os 4 últimos.  
- **E-mail**: ofuscação parcial do endereço, mantendo o domínio visível.  

Essas transformações são aplicadas através dos **Microserviços Python**, garantindo que os dados sensíveis não avancem para a camada Gold.

#### Segurança de Armazenamento e Acesso
- **Azure Storage Account**: Controle de permissões via *role-based access control* (RBAC).  
- **Segregação por camadas**: Cada container (Raw, Bronze, Silver, Gold) possui políticas de acesso específicas.  
- **GitHub Actions**: Uso de *secrets* para armazenar credenciais de forma segura.  
- **Service Principals**: Autenticação entre serviços com permissões mínimas necessárias.  

**Benefícios principais**:  
- Proteção de informações sensíveis em conformidade com boas práticas de governança.  
- Redução de riscos em auditorias e conformidade regulatória (LGPD).  
- Garantia de que dados analíticos não exponham informações pessoais desnecessárias.  

### 3.12 Observabilidade e Monitoramento

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

### 3.13 Escalabilidade e Desempenho

O projeto foi estruturado para suportar aumento de volume de dados e crescimento no número de fontes, mantendo eficiência e confiabilidade no processamento.

#### Escalabilidade
- **Microserviços em AKS**: permitem escalar horizontalmente, aumentando ou reduzindo réplicas conforme a demanda de ingestão.  
- **Databricks**: suporte a clusters escaláveis sob demanda, otimizando custo e performance no processamento das camadas Bronze, Silver e Gold.  
- **Storage Account**: arquitetura baseada em containers independentes para cada camada de dados, possibilitando expansão sem necessidade de reestruturação.  

#### Desempenho
- **Delta Lake**: garante performance em consultas e manipulação de grandes volumes de dados por meio de otimizações internas (indexação, caching e compactação de arquivos).  
- **Auto Loader**: possibilita ingestão contínua e eficiente dos dados da Raw para a Bronze, reduzindo o tempo de latência.  
- **Transformações distribuídas no Databricks**: uso de processamento paralelo para melhorar a velocidade em operações de limpeza e padronização.

#### Otimização de Escrita no Delta Lake  

O cluster Databricks está configurado com parâmetros de otimização para melhorar a performance de escrita e leitura de dados em tabelas Delta:  

- `spark.databricks.delta.optimizeWrite.enabled = true` → Habilita **optimize write**, que reduz o número de pequenos arquivos gerados, consolidando-os automaticamente durante a escrita.  
- `spark.databricks.delta.autoCompact.enabled = true` → Ativa a **auto compactação**, que combina arquivos pequenos em arquivos maiores de forma contínua, melhorando a performance de leitura e queries analíticas.

**Benefícios principais**:  
- Capacidade de lidar com aumento no volume e variedade de dados.  
- Redução da latência entre ingestão e disponibilização dos dados analíticos.  
- Otimização de custos ao escalar recursos somente quando necessário.

### 3.14 Metodologia de Desenvolvimento

O ciclo de desenvolvimento do projeto segue a estratégia de **GitFlow** para organização e rastreabilidade do código.  

Principais práticas adotadas:
- **Branch main** → sempre estável, representa a versão de produção.  
- **Branch develop** → concentra as novas features e integrações em andamento.  
- **Feature branches** → criadas a partir de `develop` para desenvolvimento de funcionalidades específicas.  
- **Release branches** → usadas para preparar versões estáveis antes de ir para produção.  
- **Hotfix branches** → permitem correções rápidas diretamente na `main`.

**Adicionar imagens das Branchs**

##  🚀 4. Guia de Configuração e Execução

### 4.1 Pré-requisitos

Antes de configurar e executar o projeto, é necessário garantir que o ambiente possua os seguintes pré-requisitos:

#### Identidade, Permissões, Credenciais e Acessos
- **Service Principal (SPN)** criado previamente.  
- **Secret da SPN** configurado (*Secret Value*, não o *Secret ID*).  
- A **SPN** precisa ter permissões na assinatura da Azure:  
  - *Contributor*  
  - *User Access Administrator*

#### GitHub Actions
- **Personal Access Token (PAT)** do GitHub criado e salvo nas *Secrets* do repositório com permissões adequadas.  

#### Secrets obrigatórias no GitHub
As seguintes *secrets* devem estar configuradas no repositório antes da execução de qualquer fluxo de criação:  

- `DB_KEY` → Para conexão com o Database.  
- `API_KEY` → Para conexão com a API.  
- `AZURE_CREDENTIALS` → Credenciais para conexão na Azure, seguindo o seguinte modelo JSON:  
  
  ```json
  {
    "clientId": "", 
    "clientSecret": "", 
    "subscriptionId": "", 
    "tenantId": "" 
  }
  ```

- `GH_PAT_TOKEN` → Token criado no GitHub, com as seguintes permissões:

repo → Full control of private repositories
repo:status → Access commit status
repo_deployment → Access deployment status
public_repo → Access public repositories
repo:invite → Access repository invitations
security_events → Read and write security events
workflow → Update GitHub Action workflows
write:packages → Upload packages to GitHub Package Registry
read:packages → Download packages from GitHub Package Registry
admin:org → Full control of orgs and teams, read and write org projects
write:org → Read and write org and team membership, read and write org projects
read:org → Read org and team membership, read org projects
manage_runners:org → Manage org runners and runner groups

### 4.2 Configuração da Infraestrutura

1. **Criar repositório a partir do template**  
   - Clique no botão **"Use this template"** no repositório original.  
   - Crie seu próprio repositório a partir dele.  
   - Faça o clone do **seu repositório recém-criado**:  
     ```bash
     git clone https://github.com/<usuario>/<novo-repo>.git
     cd <novo-repo>
     ```
    **OBS**: Colocar aqui imagem dos recursos criados na Azure

2. **Configurar as *secrets* no GitHub**  
   - Defina todas as *secrets* obrigatórias listadas na seção **Pré-requisitos**.  
   - Certifique-se de que as **Workflow permissions** estejam configuradas como *Read and Write*.

   **OBS**: Colocar aqui imagem dos recursos criados na Azure

3. **Executar o workflow de criação da infraestrutura**  
   - O workflow do GitHub Actions responsável pela criação deve ser acionado manualmente (`workflow_dispatch`) ou via push no branch principal.  
   - Esse pipeline realiza:  
     - Validação de credenciais e permissões.  
     - Criação/atualização do **Resource Group**.  
     - Provisionamento do **Storage Account** com containers (Raw, Bronze, Silver, Gold).  
     - Criação do **Azure Container Registry (ACR)**.  
     - Deploy do **Azure Kubernetes Service (AKS)**.  
     - Configuração do **Azure Databricks**.

     **OBS**: Colocar aqui imagem dos recursos criados na Azure

4. **Validar a implantação**  
   - Confirme que todos os recursos foram criados no **Resource Group** especificado.  
   
   **OBS**: Colocar aqui imagem dos recursos criados na Azure

---

**Observações**  
- O **Terraform** utiliza *Remote State* armazenado nos *artifacts* do GitHub Actions, permitindo atualizações e destruição da infraestrutura de forma segura.
- Existe um workflow específico para exclusão completa da infraestrutura.
  
  **OBS**: Colocar aqui imagem dos recursos criados na Azure

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

5. Considerações
A arquitetura permite que novas fontes sejam adicionadas facilmente criando um novo microserviço e registrando sua imagem no ACR.

O pipeline garante que qualquer atualização de código nos microserviços resulte em uma nova versão sendo automaticamente publicada e executada no AKS.

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

##  💡 5. Melhorias e Considerações Finais

###  5.1 Melhorias Futuras

- **Segurança de Rede (VNet e Private Endpoints):** inclusão de Virtual Networks e Private Endpoints para isolar os recursos da Azure e garantir maior segurança no tráfego de dados. 
- **Fluxo de Ambientes (Dev / Pre / Prod):** implementação de múltiplos ambientes com pipelines de deploy independentes, possibilitando testes e validações antes de subir em produção.  
- **Governança de Dados:** integração com catálogos de dados (ex.: **Unity Catalog**, **Purview**) para melhor rastreabilidade, versionamento e gestão de acesso.  
- **Qualidade e Validação de Dados:** uso de ferramentas como **Great Expectations** para validar schemas, detectar anomalias e garantir consistência antes de promover dados para Silver/Gold.  
- **Orquestração Completa:** adotar um orquestrador dedicado (ex.: **Airflow**, **Prefect**, ou **Azure Data Factory**) para controlar tanto ingestão quanto processamento, permitindo maior automação e dependências entre pipelines.  
- **Observabilidade e Alertas:** centralizar métricas, logs e alertas em ferramentas como **Azure Monitor** ou **Grafana**, possibilitando detecção proativa de falhas.  
- **Testes Automatizados:** expandir o uso de testes unitários e de integração para notebooks e microserviços, garantindo maior confiabilidade nas mudanças de código.  
- **Custo e Performance:** analisar otimizações de custo (storage tiers, autoscaling de clusters no Databricks) e desempenho (particionamento e otimização de tabelas Delta).  

###  5.2 Considerações Finais

O projeto demonstrou como é possível integrar dados de múltiplas fontes e formatos, organizando-os em um pipeline escalável e confiável na Azure.  
A solução aplicou boas práticas de engenharia de dados (arquitetura medalhão, uso de Delta Lake, pipelines automatizados) em conjunto com boas práticas de engenharia de software (microserviços, CI/CD, IaC).  

Embora ainda existam pontos de evolução, a arquitetura atual já fornece uma base sólida para ingestão, transformação e disponibilização de dados prontos para análise, podendo ser expandida gradualmente conforme as necessidades de negócio e requisitos de governança cresçam.

##  📚 6. Referências