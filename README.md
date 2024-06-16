# Projeto Bancário em Python - Versão 1

Este repositório contém um projeto bancário simples implementado em Python. O objetivo é fornecer funcionalidades básicas de saque, depósito e extrato, divididas em módulos para facilitar a compreensão e manutenção do código. Nesta versão, o projeto trabalha com apenas um usuário, sem a necessidade de número de agência e conta bancária.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `banco_v1.py`: Código principal que utiliza as funcionalidades de saque, depósito e extrato.
- `depositar.py`: Módulo responsável pela funcionalidade de depósito.
- `sacar.py`: Módulo responsável pela funcionalidade de saque.
- `extrato.py`: Módulo responsável pela funcionalidade de extrato.

## Funcionalidades

- **Depósito**: Permite ao usuário realizar depósitos, que são armazenados em uma variável e exibidos na operação de extrato.
- **Saque**: Permite ao usuário realizar até 3 saques diários com limite máximo de R$500 por saque. O sistema verifica se há saldo suficiente antes de permitir o saque.
- **Extrato**: Lista todos os depósitos e saques realizados na conta e exibe o saldo atual. Os valores são mostrados no formato R$xxx.xx (ex: 1500.45 = R$1500.45).

## Regras de Negócio

- Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
- O sistema deve permitir realizar 3 saques diários com limite máximo de R$500 por saque.
- Caso o usuário não tenha saldo suficiente, o sistema exibirá uma mensagem de saldo insuficiente.
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
- O extrato deve listar todos os depósitos e saques realizados na conta e exibir o saldo atual.

## Pré-requisitos

- Python 3.x

## Instalação

Clone o repositório para a sua máquina local:

```bash
https://github.com/MentiDMarco/Desafio_Banco_DIO.git
