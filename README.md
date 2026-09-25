# System Monitor

Monitor de sistema em Python que exibe o uso de CPU, memória RAM e disco diretamente no terminal, com atualização contínua na mesma linha.

Projeto desenvolvido para praticar Python por meio de uma ferramenta útil para acompanhar os recursos da máquina.

## Funcionalidades

- Uso geral da CPU em porcentagem.
- Uso de memória RAM em porcentagem, com quantidade utilizada e total em GiB.
- Uso do sistema de arquivos que contém `/`, com porcentagem e espaço utilizado e total em GiB.
- Atualização aproximadamente a cada segundo.
- Encerramento com `Ctrl+C`.
- Alerta quando o uso de RAM atinge ou ultrapassa 80%.
- Histórico das leituras salvo automaticamente em CSV.
- Limpeza do restante da linha quando a mensagem de alerta desaparece.

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

O limite do alerta de RAM está na constante `RAM_ALERT_THRESHOLD`, em `monitor.py`. O padrão é `80` (porcentagem). O alerta é exibido enquanto o uso estiver igual ou acima desse limite.

## Histórico em CSV

A cada leitura, o programa acrescenta uma linha ao arquivo `history.csv`, criado na mesma pasta de `history.py`. As colunas são:

```text
timestamp,cpu_percent,ram_percent,disk_percent
2026-09-24T14:30:00,12.5,42.0,38.4
```

O exemplo é ilustrativo. A data e a hora são locais, com precisão de segundos; as métricas são percentuais. O cabeçalho é escrito somente quando o arquivo não existe ou está vazio. Ao reiniciar o monitor, as leituras anteriores são preservadas.

O histórico cresce enquanto o monitor está rodando; ainda não há rotação ou limite de tamanho. A pasta precisa permitir escrita. O CSV é um arquivo gerado localmente e está no `.gitignore`.

## Organização do código

- `monitor.py`: coleta CPU, RAM e disco, converte bytes para GiB, calcula o alerta e coordena a exibição e a gravação no laço principal. Trata o encerramento com `Ctrl+C`.
- `display.py`: contém `show_metrics()`, responsável pela formatação e exibição. Usa `\r` e a sequência ANSI `\033[K` para atualizar e limpar a linha em um terminal compatível.
- `history.py`: contém `save_metrics()`, responsável pelo caminho do CSV, cabeçalho e gravação das leituras.
- `requirements.txt`: declara `psutil==7.2.2`. Os módulos `csv`, `datetime` e `pathlib` fazem parte da biblioteca padrão do Python.

Os módulos usam funções; não há classes nesta versão.

## Aprendizados

- Consulta de informações do sistema com `psutil`.
- Organização do código em funções e módulos, com imports entre arquivos.
- Condições e constantes para definir alertas.
- Escrita de CSV em modo de acréscimo, usando `with`.
- Caminhos com `pathlib` e registro de data/hora com `datetime`.
- Laços de repetição e tratamento de `KeyboardInterrupt`.
- Formatação de números com f-strings.
- Atualização da saída do terminal com `\r`, `end` e `flush`.
- Uso de ambiente virtual e do ponto de entrada `if __name__ == "__main__"`.

