# System Monitor

Monitor de sistema em Python que exibe o uso de CPU, memória RAM e disco diretamente no terminal, com atualização contínua na mesma linha.

Projeto desenvolvido para praticar Python por meio de uma ferramenta útil para acompanhar os recursos da máquina.

## Funcionalidades

- Uso geral da CPU em porcentagem.
- Uso de memória RAM em porcentagem, com quantidade utilizada e total em GiB.
- Uso do sistema de arquivos que contém `/`, com porcentagem e espaço utilizado e total em GiB.
- Atualização aproximadamente a cada segundo.
- Encerramento com `Ctrl+C`.

## Exemplo de saída

```text
CPU:  12.5% | RAM:  42.0% (6.25/15.62) GiB | DISK:  38.4% (91.20/237.50 GiB)
```

Os valores são ilustrativos. Durante a execução, as métricas são atualizadas na mesma linha. GiB é uma unidade de tamanho equivalente a 1.073.741.824 bytes.

## Requisitos

- Python 3.12
- Biblioteca `psutil`.
- Terminal Linux como ambiente inicial de uso.


## Instalação

Após baixar ou clonar o repositório, abra um terminal na pasta que contém `monitor.py`.

Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências declaradas no `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Se já tiver um ambiente virtual criado, ative-o e execute o comando acima para instalar a versão especificada no projeto.

## Uso

Com o ambiente virtual ativado, execute:

```bash
python monitor.py
```

A primeira leitura aparece após aproximadamente um segundo. Para encerrar, pressione `Ctrl+C`:

```text
Monitor Stopped
```

O intervalo de medição está definido pela constante `UPDATE_INTERVAL`, no início de `monitor.py`. O valor padrão é `1`, em segundos; caso altere, mantenha um valor maior que zero.

## Organização do código

O programa está concentrado em `monitor.py`:

- `show_metrics()`: formata e exibe as métricas no terminal.
- `bytes_to_gib()`: converte valores em bytes para GiB.
- `main()`: coleta os dados continuamente e trata a interrupção pelo teclado.

## Aprendizados

- Consulta de informações do sistema com `psutil`.
- Organização do código em funções.
- Laços de repetição e tratamento de `KeyboardInterrupt`.
- Formatação de números com f-strings.
- Atualização da saída do terminal com `\r`, `end` e `flush`.
- Uso de ambiente virtual e do ponto de entrada `if __name__ == "__main__"`.

