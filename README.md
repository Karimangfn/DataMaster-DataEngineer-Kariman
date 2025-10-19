# Data Master - Kariman Gomes

<p align="center">
  <img src="assets/images/Data-Master-Logo.png" style="width:800px; height:250px;">
</p>

O repositório "DataMaster-DataEngineer-Kariman" apresenta a solução de Engenharia de Dados criada por [Kariman](https://www.linkedin.com/in/kariman-gomes/) como parte do programa Data Master, uma iniciativa da F1rst Santander. <p>

## 📑 Sumário

<details>
  <summary>📌 1. Visão Geral do Projeto</summary>

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
  <summary>📚 6. Referências</summary>
</details>

## 📌 1. Visão Geral do Projeto

Este projeto consiste em uma **plataforma de engenharia e experimentação de dados** desenvolvida para demonstrar, em um ambiente controlado e reproduzível, as principais práticas de **ingestão, processamento, governança e automação de dados em nuvem**.

A solução foi concebida como uma **infraestrutura completa**, que une conceitos de **engenharia de dados**, **engenharia de software** e **arquitetura em nuvem** para sustentar fluxos de dados **escaláveis, auditáveis e seguros**.

### 1.1 Propósito

A plataforma busca resolver um conjunto mais amplo de desafios enfrentados em ambientes de dados modernos, incluindo:

* Fragmentação de dados em múltiplas origens e formatos.
* Falta de padronização e governança no ciclo de vida dos dados.
* Dificuldade de reprodutibilidade e versionamento de ambientes.
* Baixa automação nos processos de ingestão, transformação e deploy.
* Necessidade de garantir segurança, qualidade e rastreabilidade ponta a ponta.

### 1.2 Abordagem

A solução foi projetada para atender a esses desafios de forma **modular e integrada**, combinando:

* **Arquitetura Medalhão (Raw → Bronze → Silver → Gold)** para organizar e evoluir os dados em camadas de qualidade.
* **Infraestrutura como Código (Terraform)** para provisionar automaticamente os recursos na Azure.
* **Microserviços de Ingestão** para integrar múltiplas fontes de dados de forma independente e escalável.
* **Databricks e Delta Lake** para processamento distribuído, versionamento e confiabilidade transacional.
* **Automação com GitHub Actions** para CI/CD de infraestrutura, código e pipelines.
* **Governança e Segurança** via RBAC, Service Principals e mascaramento de dados sensíveis.
* **Observabilidade e Monitoramento** para acompanhamento de execuções e detecção de falhas.
* **Boas práticas de Engenharia de Software**, como Clean Architecture, testes automatizados e validações de qualidade de código.

##  🏗️ 2. Arquitetura de Solução

### 2.1 Visão Geral

A arquitetura foi projetada para sustentar uma plataforma modular de engenharia de dados, capaz de integrar, processar e disponibilizar informações de forma escalável e governada na nuvem.

No centro da solução, encontra-se um pipeline de dados estruturado na arquitetura medalhão (Raw → Bronze → Silver → Gold), responsável por orquestrar o fluxo de dados desde a ingestão até a camada analítica. Esse pipeline é suportado por uma infraestrutura automatizada e reprodutível, provisionada via Terraform, e integrada a componentes de observabilidade, segurança e automação contínua.

Os dados são ingeridos de três origens distintas (banco de dados, API e arquivos) por meio de microserviços independentes, processados no Databricks e armazenados em um Data Lake na Azure.

### 2.2 Diagrama da Arquitetura de Solução

![Figura 1 — Arquitetura de Solução](assets/images/Arquitetura-Pipeline-de-Dados.png)

*Figura 1 — Arquitetura de solução em alto nível, mostrando ingestão, processamento e armazenamento das camadas do Data Lake.*

### 2.3 Componentes Principais

- **Microserviços de Ingestão**: Cada microserviço é responsável por extrair dados de uma fonte específica e gravá-los na camada raw do Data Lake.
- **Data Lake (Azure Storage Account)**: Armazena os dados em diferentes camadas de processamento (Raw, Bronze, Silver e Gold), seguindo a arquitetura medalhão e permitindo rastreabilidade.
- **Databricks**: realiza o processamento e a transformação dos dados. A camada Bronze utiliza o Auto Loader para ingestão automatizada, a camada Silver aplica limpeza, padronização e mascaramento de dados, e a camada Gold gera a tabela pronta para análise.
- **Infraestrutura como Código (Terraform)**: Provisiona todos os recursos necessários, incluindo ACR, AKS, Storage Account, Databricks e demais componentes da arquitetura.
- **Automação (GitHub Actions)**: Gerencia a criação, o deploy dos microserviços e verificação de qualidade de código.

## ⚙️ 3. Arquitetura Técnica

### 3.1 Descrição do Fluxo de Dados

1. **Ingestão**: Os microserviços consomem dados das fontes (Banco de Dados, API, Arquivos) e gravam na camada raw do Data Lake. 
2. **Bronze**: Databricks lê os dados da raw e cria a tabela Delta, mantendo a integridade das informações.
3. **Silver**: Aplica transformações de limpeza, padronização e mascaramento de dados sensíveis.  
4. **Gold**: Gera tabelas prontas para consumo ou análises.

### 3.2 Tecnologias e Serviços Utilizados

- **Resource Group**: Agrupa todos os recursos provisionados na Azure. 
- **ACR (Azure Container Service)**: Repositório para armazenar e versionar as imagens Docker dos microserviços.  
- **AKS (Azure Kubernetes Service)**: Execução dos microserviços de ingestão.
- **Storage Account**: Armazenamento do Data Lake com camadas Raw, Bronze, Silver e Gold.
- **Databricks**: Processamento e transformação dos dados.
- **Delta Lake**: Garantia de consistência, versionamento e ACID nas tabelas.
- **Terraform**: Provisionamento de toda a infraestrutura na Azure.
- **GitHub Actions**: Automação de criação de infraestrutura, deploy de microserviços e execução de jobs.

### 3.3 Infraestrutura como Código

![Figura 2 — Infraestrutura CI/CD](assets/images/Arquitetura-Infrastructure-CI-CD.png)  

*Figura 2 — Arquitetura de infraestrutura com Terraform e principais recursos provisionados na Azure.*

Toda a infraestrutura do projeto é criada com uso de **Terraform**, que também salva o estado das criações em artefatos para garantir a consistência do ambiente e a persistência do estado entre execuções, evitando perdas ou divergências durante atualizações.

### Validações (CI)
- **Check Github Token**: Antes da criação dos recursos, é verificado se o *Personal Access Token* do GitHub está criado e configurado com os acessos necessários.

- **Check Azure Role Assignments**: Valida se o *Service Principal* necessário para a criação dos recursos está configurado corretamente com as permissões adequadas para atribuir acesso a outro recursos.

- **check Azure Group Permissions**: Valida se o *Service Principal* necessário para a criação dos recursos está configurado corretamente com as permissões adequadas para criar grupos na Azure.

### Criação de Recursos (CD)
- **Resource Group**: Responsável por armazenar os recursos.  
- **Azure Container Registry (ACR)**: Armazena as imagens dos microserviços.  
- **Azure Kubernetes Service (AKS)**: Cluster responsável pela execução dos microserviços.
  - Criação de **role assignment** para permitir que o AKS faça pull das imagens.  
- **Storage Account**: Armazenamento das tabelas de dados.
  - Criação de **role assignment** do Service Principal com permissão de Storage Blob Data Contributor.
- **Storage Containers**: Containers específicos para as camadas de dados Raw, Bronze, Silver e Gold.  
- **Databricks**: Criação de recursos e configuração do workspace, incluindo:
  - Workspace Databricks
  - Conector de acesso (Access Connector)
  - Criação de External Locations (Bronze, Silver, Gold)
  - Criação de Schema
  - Criação de Job de processamento
  - Criação de Grupos de acesso na workspace
- **Access Groups**: Criação de grupos de acesso para governança na Azure.

#### Estrutura

```bash
infrastructure/
├── main.tf              # Chama os módulos e define os recursos principais
├── variables.tf         # Variáveis globais usadas pelos módulos
├── outputs.tf           # Saídas de recursos criados
├── providers.tf         # Providers (Azure, Databricks, etc.)
└── modules/             # Módulos reutilizáveis
    ├── access/          # Grupos e permissões (Azure AD / IAM)
    │   ├── main.tf
    │   ├── variables.tf
    ├── acr/             # Azure Container Registry
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    ├── aks/             # Azure Kubernetes Service
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    ├── databricks/      # Databricks workspace
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    │   └── providers.tf
    ├── resource_group/  # Resource Group
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    └── storage/         # Storage Account e containers
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
        └── providers.tf
```

### 3.4 GitHub Actions

O GitHub Actions é responsável por orquestrar e automatizar todas as etapas do projeto, incluindo:

- **Provisionamento de Infraestrutura**: executa o Terraform para criação e atualização de recursos na Azure.
- **Orquestração de Pipeline**: coordena a execução de todos os passos, incluindo o disparo dos microserviços de ingestão no AKS e dos jobs de transformação no Databricks.
- **Deploy de Microserviços**: build e publicação de imagens Docker no ACR, seguido de deploy no AKS.  
- **Transformação de Dados**: integração com Databricks para execução dos pipelines de Bronze, Silver e Gold. 

#### Resumo de Execução (Summary)
Cada execução de workflow gera automaticamente um **summary** dentro do GitHub Actions, contendo:  
- Recursos criados/atualizados pelo Terraform.
- Status de execução das etapas (Infra, Ingestão, Transformação).

**Colocar imagem aqui dos summaries depois**

#### Fluxo dos Workflows

**A. Workflows Principais**
1. **Infraestrutura** → Provisionamento completo via Terraform  
   1.1 - Deploy Cloud Infrastructure  
2. **Setup de Ingestão** → Setup de Microserviços no ACR e AKS  
   2.1 - Build and Push to ACR  
   2.2 - AKS Setup and Deploy  
3. **Orquestração** → Execução dos Microserviços e Job no Databricks  
   3.1 - Orchestrate Data Pipeline  

**B. Workflows de Qualidade (Pull Requests)**  
1. **Validação de Microserviço** → Executa lint, pré-commit hooks e testes para os microserviços.
  1.1 - Microservice Quality
2. **Validação de Data Processing** → Executa lint, pré-commit hooks e testes para o job de Data Processing.
  2.1 - Data Processing Quality

### 3.5 Orquestração de Pipelines

A orquestração dos pipelines é realizada por um **workflow do GitHub Actions**, que atua como coordenador central da execução de todo o processo de dados. O workflow realiza as seguintes funções:

- Detecta os microserviços que precisam ser executados, lendo arquivos de versão nos repositórios.
- Dispara os **jobs de ingestão no AKS**, validando previamente a existência das imagens no ACR.
- Dispara o **job de transformação no Databricks**, garantindo a execução dos pipelines Bronze, Silver e Gold.
- Coleta os resultados das execuções, tanto do AKS quanto do Databricks, e gera um resumo consolidado da execução.

- **Colocar Desenho?**

### 3.6 Extração e Ingestão de Dados

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

```bash
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
```

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

### 3.7 Armazenamento de Dados

O armazenamento dos dados é realizado em uma **Azure Storage Account**, estruturada segundo a arquitetura medalhão.
Cada camada possui um **container dedicado**, garantindo organização e isolamento entre os estágios do pipeline:

- **Raw**: Camada onde os microserviços depositam os dados ingeridos, preservando-os no formato original.  
- **Bronze**: Camada onde o Databricks cria tabelas Delta a partir da Raw, garantindo rastreabilidade e histórico.  
- **Silver**: Camada que contém dados limpos, padronizados e com mascaramento de informações sensíveis.  
- **Gold**: Camada final com dados prontos para consumo em análises e dashboards. 

### 3.8 Processamento e Transformação dos Dados

![Figura 4 — Data Processing CI](assets/images/Arquitetura-Data-Processing-CI.png)

*Figura 4 — Arquitetura de processamento e transformação de dados em Databricks, seguindo a arquitetura medalhão.*

O processamento dos dados é realizado no **Databricks**, utilizando **Microserviços Python** organizados em tarefas dentro de um **Job**.
Cada job é dividido em três etapas principais, alinhadas à arquitetura medalhão:

1. **Bronze**  
   - Leitura dos dados da camada Raw por meio do **Auto Loader** do Databricks.  
   - Criação de tabela **Delta**, preservando os dados ingeridos com histórico e versionamento.
   - Registro de metadados de rastreabilidade: source_file_name, ingestion_timestamp e raw_ingestion_id (UUID único por execução).
   - Aplicação de controle de acesso garantindo permissões adequadas a grupos de usuários.

  > 💡 O processamento incremental é realizado com o **Auto Loader**, que detecta novos arquivos na camada Raw e processa apenas dados novos.

2. **Silver**  
   - Aplicação de regras de **limpeza e padronização** (ex.: normalização de formatos, remoção de inconsistências).  
   - Deduplicação baseada em customer_id e purchase_date, preservando o registro mais recente.
   - Mascaramento de informações sensíveis:
      - cpf → SHA-256 → coluna cpf_masked
      - credit_card_number → SHA-256 → coluna credit_card_masked
      - email → ofuscação parcial mantendo domínio
   - Enriquecimento dos dados, como a coluna high_value_purchase (flag de compras de alto valor).
   - Preservação das colunas de metadados da Bronze (source_file_name, ingestion_timestamp, raw_ingestion_id).
   - Aplicação de controle de acesso garantindo permissões adequadas a grupos de usuários.

3. **Gold**  
   - Agregação dos dados Silver em tabelas analíticas, prontas para consumo em BI.
   - Criação da coluna derivada purchase_month (formato yyyy-MM) para análises mensais.
   - Cálculo de métricas agregadas por store_location e purchase_month:
      - total_purchases → número de compras
      - total_revenue → soma do valor total
      - average_purchase_value → valor médio de compra
      - high_value_purchases → contagem de compras de alto valor
   - Aplicação de controle de acesso garantindo permissões adequadas a grupos de usuários.

#### Estrutura

```bash
processing_job/  
├── src/  
│   ├── config/       # Configurações do pipeline (parâmetros, schemas, paths)  
│   ├── modules/      # Módulos principais de transformação (Bronze, Silver ou Gold)  
│   ├── utils/        # Funções utilitárias reutilizáveis  
│   └── main.py       # Script principal do job executado no Databricks  
├── tests/            # Testes unitários e de integração  
├── requirements.txt  # Dependências do job
```

Arquivos de Configuração
- **.flake8** → Regras de lint para garantir padrão de código.
- **.gitignore** → Define arquivos ignorados no versionamento.
- **.pre-commit-config.yaml** → Hooks para validações automáticas antes do commit.  
- **pytest.ini** → Configurações para execução dos testes com Pytest.

### 3.9 Qualidade e Validação de Dados

A qualidade dos dados é garantida a partir da camada **Silver**, onde são aplicadas regras de validação e consistência antes de disponibilizar as informações para consumo. O processo combina verificações automatizadas e padronizações implementadas nos microserviços do Databricks.

Principais validações aplicadas:  
- **Integridade de schema**: checagem se os dados seguem o schema esperado.  
- **Valores obrigatórios**: verificação de colunas críticas que não podem estar nulas (`customer_id`, `cpf`).
- **Conversão de tipos**: purchase_date → DateType, total_amount → DoubleType.
- **Formatos válidos**: conferência de padrões, como CPF válido ou formato correto de e-mail.
- **Deduplicação**: remoção de registros duplicados mantendo o mais recente por customer_id e purchase_date.
- **Validação de formatos**: emails válidos, datas consistentes, valores numéricos coerentes.
- **Valores de domínio**: conferência de atributos contra listas pré-definidas (ex.: store_location). 

Ferramentas e práticas:
- Delta Lake → versionamento, histórico, rollback e rastreabilidade.
- Microserviços Python no Databricks → implementam todas as validações, limpeza, deduplicação e mascaramento.   

**Benefícios principais**:  
- Evita propagação de dados inconsistentes para as camadas analíticas.  
- Garante confiabilidade e consistência para relatórios e dashboards.  
- Facilita auditoria e rastreabilidade em caso de erros de ingestão ou transformação.

### 3.10 Mascaramento e Segurança dos Dados

O projeto adota práticas de **segurança e privacidade** para proteger informações sensíveis dos clientes durante o ciclo de vida dos dados.  
O foco principal está no **mascaramento de dados pessoais**, realizado na transição da camada **Bronze → Silver**.

#### Mascaramento de Dados
- **CPF**: aplicação de hash criptográfico (SHA-256), preservando apenas parte para rastreabilidade.
- **Número de cartão de crédito**: aplicação de hash criptográfico (SHA-256), garantindo que os dados originais não sejam expostos. 

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

### 3.11 Governança

Nesse projeto, o tema de governança de dados é tratado para garantir que cada usuário tenha acesso apenas às informações necessárias, de acordo com sua função, promovendo segurança, rastreabilidade e compliance.

| Persona             | Nível de Acesso                   | Objetivo do Acesso                                              |
|---------------------|-----------------------------------|-----------------------------------------------------------------|
| Engenheiro de Dados | Leitura e Escrita na Raw e Bronze | Implementar e manter pipelines de ingestão e transformação.     |
| Cientista de Dados  | Leitura na Silver e Gold          | Realizar análises e modelagem preditiva sobre dados confiáveis. |
| Analista de Dados   | Leitura na Gold                   | Construir dashboards e relatórios para tomada de decisão.       |
| Administrador       | Controle Total                    | Gerenciar usuários, permissões e monitorar segurança.           |

- Todos os acessos são concedidos seguindo o princípio do **menor privilégio**.  
- O controle é feito via **RBAC** da Azure Storage Account e Service Principals.   

#### Azure Storage Account (RBAC)

- Engenheiros de dados recebem Storage Blob Data Contributor nos containers Raw e Bronze.
- Cientistas e analistas recebem Storage Blob Data Reader ou Reader parcial nos containers Silver e Gold.

#### Databricks

- Engenheiros de dados configuram e executam os jobs que processam os dados entre os layers (Raw → Bronze → Silver → Gold).
- Cientistas de dados podem acessar resultados processados nos jobs em Silver e Gold.
- Analistas de dados podem executar queries e montar dashboards apenas sobre os dados Gold gerados pelos jobs.
- Administradores têm controle total sobre a Storage Account e podem gerenciar jobs, permissões e auditoria no Databricks.

#### Unity Catalog

- O Unity Catalog gerencia tabelas, views, esquemas e funções, garantindo controle de acesso, incluindo permissões em nível de objeto, linha e coluna.
- **Rastreamento e auditoria**: permite registrar lineage completo, histórico de alterações e acessos aos dados.
- **Democratização de dados**: usuários podem descobrir e acessar dados de forma segura sem depender de pipelines específicos ou da intervenção de engenheiros de dados.
- **Compartilhamento seguro de dados**: tabelas e views podem ser compartilhadas entre diferentes equipes, unidades de negócio ou até parceiros externos, mantendo o controle sobre quem pode visualizar ou alterar os dados.
- **Padronização e organização**: centraliza metadados, schemas e nomenclaturas, garantindo consistência em todo o Data Lake e em múltiplas camadas de processamento.

### 3.12 Observabilidade e Monitoramento

O projeto adota logs como principal mecanismo de monitoramento para acompanhar a execução dos pipelines e detectar falhas, garantindo rastreabilidade e confiabilidade nos fluxos de dados.

#### Logs e Métricas
- **Microserviços (AKS)**: geração de logs de execução e falhas.
- **Databricks Jobs**: registro automático de logs de execução, status de tarefas e métricas de processamento.  
- **GitHub Actions**: logs de cada etapa de CI/CD, permitindo auditoria das execuções.

### 3.13 Escalabilidade e Desempenho

O projeto foi estruturado para suportar aumento de volume de dados e crescimento no número de fontes, mantendo eficiência e confiabilidade no processamento.

#### Escalabilidade
- **Microserviços em AKS**: permitem escalar horizontalmente, aumentando ou reduzindo réplicas conforme a demanda de ingestão.  
- **Databricks**: os jobs utilizam clusters com autoscale configurado, que realizam escalabilidade horizontal, adicionando ou removendo nós automaticamente conforme o volume de dados processado.
- **Storage Account**: arquitetura baseada em containers independentes para cada camada de dados, possibilitando expansão sem necessidade de reestruturação.

#### Desempenho
- **Delta Lake**: garante performance em consultas e manipulação de grandes volumes de dados por meio de otimizações internas (indexação, caching e compactação de arquivos).  
- **Auto Loader**: possibilita ingestão contínua e eficiente dos dados da Raw para a Bronze, reduzindo o tempo de latência.  
- **Transformações distribuídas no Databricks**: uso de processamento paralelo para melhorar a velocidade em operações de limpeza e padronização.

#### Parâmetros de Performance e Eficiência do Cluster Databricks 

O cluster Databricks está configurado com parâmetros de otimização para melhorar a performance de escrita e leitura de dados em tabelas Delta:  

- `spark.databricks.delta.optimizeWrite.enabled = true` → reduz o número de pequenos arquivos gerados, consolidando-os automaticamente durante a escrita.  
- `spark.databricks.delta.autoCompact.enabled = true` → combina arquivos pequenos em arquivos maiores de forma contínua, melhorando a performance de leitura e queries analíticas.
- `spark.databricks.delta.schema.autoMerge.enabled = true` → Permite que o Delta Lake atualize automaticamente o schema de uma tabela durante operações de merge, append ou overwrite, sem necessidade de recriação manual.
- `spark.sql.adaptive.enabled = true` → Ativa o Adaptive Query Execution, recurso do Spark que ajusta dinamicamente o plano de execução em tempo de execução (por exemplo, alterando o número de partições ou aplicando broadcast joins quando vantajoso), melhorando desempenho de forma automática.
- `spark.databricks.adaptive.autoOptimizeShuffle = true` → Faz parte do AQE e permite que o Databricks reajuste dinamicamente a estratégia de shuffle, otimizando a distribuição de dados entre os executores para evitar skew (desequilíbrio de carga entre partições).
- `spark.sql.adaptive.coalescePartitions.enabled = true` → Habilita o ajuste automático de partições após o shuffle, reduzindo o número de partições pequenas e otimizando o uso de recursos ao evitar a criação de tarefas muito pequenas (task overhead).
- `spark.databricks.io.cache.enabled = true` → Ativa o Databricks I/O Cache, que armazena dados frequentemente acessados em disco local SSD do cluster, reduzindo o tempo de leitura e o custo de reprocessamento em consultas repetitivas.

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

### **4.2 Criação do Repositório a partir do Template**

1. No repositório do projeto, acesse **“Use this template”**.
   
   ![Template - 01](assets/images/config-execution/template-01.png)

2. Selecione **“Create a new repository”**.
   
   ![Template - 02](assets/images/config-execution/template-02.png)

3. Mantenha marcada a opção para levar todas as *branches* do repositório, defina o nome em **Repository name**, adicione uma descrição, configure a visibilidade e clique em **Create repository**.
   
   ![Template - 03](assets/images/config-execution/template-03.png)

4. Aguarde alguns minutos enquanto o repositório é criado.
   
   ![Template - 04](assets/images/config-execution/template-04.png)

---

### **4.3 Configuração das Secrets e Variáveis de Ambiente**

5. Após o repositório ser criado, acesse **Settings**.
   
   ![Secrets - 01](assets/images/config-execution/secrets-01.png)

6. No menu à esquerda, clique em **Secrets and variables**.
   
   ![Secrets - 02](assets/images/config-execution/secrets-02.png)

7. Selecione a opção **Actions**.
   
   ![Secrets - 03](assets/images/config-execution/secrets-03.png)

8. Em **Actions secrets and variables**, clique em **New repository secret**.
   
   ![Secrets - 04](assets/images/config-execution/secrets-04.png)

9. A primeira *secret* a ser adicionada será **AZURE_CREDENTIALS**, seguindo o modelo JSON abaixo:
   
   ![Secrets - 05](assets/images/config-execution/secrets-05.png)

10. Em seguida, cadastre o token do GitHub com o nome **GH_PAT_TOKEN**.
   
   ![Secrets - 06](assets/images/config-execution/secrets-06.png)

11. Cadastre a chave para acessar a API, chamada **API_KEY**.
   
   ![Secrets - 07](assets/images/config-execution/secrets-07.png)

12. Cadastre a chave para acessar o banco de dados, chamada **DB_KEY**.
   
   ![Secrets - 08](assets/images/config-execution/secrets-08.png)

13. Ao finalizar, o painel de *secrets* deve se parecer com este:
   
   ![Secrets - 09](assets/images/config-execution/secrets-09.png)

---

### **4.4 Provisionamento da Infraestrutura na Azure**

14. Com tudo configurado, acesse a aba **Actions** no topo do repositório.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/infra-01.png)

15. No menu à esquerda, selecione o workflow **Deploy Cloud Infrastructure**.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/infra-02.png)

16. Clique em **Run workflow** e confirme.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/infra-03.png)

17. Após a execução completa, o workflow deve aparecer com todos os *steps* concluídos.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/infra-04.png)

18. Verifique na sua conta Azure os **Resource Groups** criados: um para os recursos principais, outro para os recursos base do AKS e outro para os recursos base do Databricks.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/infra-05.png)

19. O **Resource Group principal** conterá os recursos criados pelo workflow, incluindo **Databricks, AKS, ACR, Storage Account e Metastore Connector**.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/infra-06.png)

---

### **4.5 Build e Publicação das Imagens Docker**

20. Com a infraestrutura pronta, acesse os workflows e selecione **Build and Push to ACR**.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/acr-01.png)

21. No menu à direita, selecione as opções de **Run workflow**.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/acr-02.png)

22. Após a execução, verifique no **Azure Container Registry (ACR)** os containers e versões criadas dos microserviços.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/acr-03.png)

---

### **4.6 Deploy dos Microserviços no AKS**

23. Após o workflow do ACR, o workflow do **AKS** é disparado automaticamente.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/aks-01.png)

24. Acompanhe no **summary** as versões dos microserviços que estão sendo implantadas.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/aks-02.png)

25. Verifique no **AKS** se os microserviços estão em execução.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/aks-03.png)

---

### **4.7 Execução do Pipeline de Dados**

26. Com tudo instalado, execute o pipeline de ingestão e transformação de dados, selecionando o workflow **Orchestrate Data Pipeline**.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/pipe-01.png)

27. Clique em **Run workflow**.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/pipe-02.png)

28. Após a execução, verifique no **AKS** se os jobs foram concluídos com sucesso.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/pipe-03.png)

29. Por fim, confirme no **Databricks** a execução do job de transformação.
    
    ![Figura 4 — Data Processing CI](assets/images/config-execution/pipe-04.png)


##  💡 5. Melhorias e Considerações Finais

###  5.1 Melhorias Futuras

- **Segurança de Rede (VNet e Private Endpoints):** inclusão de Virtual Networks e Private Endpoints para isolar os recursos da Azure e garantir maior segurança no tráfego de dados. 
- **Fluxo de Ambientes (Dev / Pre / Prod):** implementação de múltiplos ambientes com pipelines de deploy independentes, possibilitando testes e validações antes de subir em produção.    
- **Observabilidade e Alertas:** centralizar métricas, logs e alertas em ferramentas como **Azure Monitor** ou **Grafana**, possibilitando detecção proativa de falhas. 
- **Infraestrutura como Código Dinâmica:** permitir que a própria GitHub Action altere a infraestrutura via Terraform ou equivalente, utilizando um backend para salvar estado.
- **Sincronização de Grupos AD e Databricks:** automatizar a sincronização de grupos do Azure AD com os grupos de Databricks, reduzindo etapas manuais de configuração de permissões e acesso.
- **Contratos de Dados:** adoção de contratos de dados para permitir ingestão de múltiplos tipos de schemas.
- **Pipelines Versionáveis e End-to-End:** possibilitar desenvolvimento de múltiplos pipelines versionáveis, desacoplados do Terraform fixo, integrados com os contratos de dados, permitindo criar novos fluxos de ingestão.
- **Expurgo da Camada Raw** : remover dados da camada Raw após a ingestão e validação, reduzindo custos de armazenamento.
- **Suporte a Streaming**: estender a arquitetura atual para incluir pipelines de ingestão e processamento streaming, tornando a plataforma híbrida (batch + streaming) e preparada para casos de uso em tempo real.
- **Abstração Multicloud**: reestruturar a camada de infraestrutura e os microserviços para desacoplar dependências específicas da Azure, viabilizando execução em múltiplos provedores de nuvem (AWS, GCP, Azure), com conectores e provisionamento agnósticos.
- **Evolução do fluxo de monitoramento**: aprimorar o monitoramento atual, baseado em logs de microserviços, Databricks Jobs e GitHub Actions, centralizando métricas, dashboards e alertas em ferramentas como Azure Monitor ou Grafana.

###  5.2 Considerações Finais

O projeto demonstrou como é possível integrar dados de múltiplas fontes e formatos, organizando-os em um pipeline escalável e confiável na Azure.  
A solução aplicou boas práticas de engenharia de dados (arquitetura medalhão, uso de Delta Lake, pipelines automatizados) em conjunto com boas práticas de engenharia de software (microserviços, CI/CD, IaC).  

Embora ainda existam pontos de evolução, a arquitetura atual já fornece uma base sólida para ingestão, transformação e disponibilização de dados prontos para análise, podendo ser expandida gradualmente conforme as necessidades de negócio e requisitos de governança cresçam.

##  📚 6. Referências
