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

Colocar desenho de arquitetura

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
### 3.5 Orquestração de Pipelines
### 3.6 Extração e Ingestão de Dados
### 3.7 Armazenamento de Dados
### 3.8 Processamento e Transformação dos Dados
### 3.9 Qualidade e Validação de Dados
### 3.10 Mascaramento e Segurança dos Dados
### 3.11 Observabilidade e Monitoramento
### 3.12 Escalabilidade e Desempenho

## 4. Guia de Configuração e Execução

### 4.1 Pré-requisitos
### 4.2 Configuração da Infraestrutura
### 4.3 Configuração de Credenciais e Acessos
### 4.4 Execução dos Pipelines de Ingestão
### 4.5 Execução dos Pipelines de Transformação

## 5. Melhorias e Considerações Finais

### 5.1 Melhorias Futuras
### 5.2 Considerações Finais

## 7. Referências