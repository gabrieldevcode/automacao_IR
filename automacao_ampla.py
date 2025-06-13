import pandas as pd
import pyautogui
import pyperclip
import time

# Configurações iniciais
def get_user_inputs():
    # Solicita ao usuário a sigla da planilha (3 primeiras letras do mês)
    sheet = input("Digite a sigla do mês (ex: Jan, Feb, Mar). Enter sem valor para sair: ").strip()
    if not sheet:
        return None
    # Coordenadas para as ações (x, y)
    cpf_coord = tuple(map(int, input("Coordenadas para CPF (x,y): ").split(',')))
    valor_coord = tuple(map(int, input("Coordenadas para VALOR (x,y): ").split(',')))
    send_coord = tuple(map(int, input("Coordenadas para botão Enviar (x,y): ").split(',')))
    # Pausas
    pause_between_rows = float(input("Tempo de pausa entre linhas (segundos, ex: 0.5): "))
    pause_after_sheet = float(input("Tempo de pausa após terminar a planilha (segundos, ex: 60): "))
    return {
        'sheet': sheet,
        'cpf_coord': cpf_coord,
        'valor_coord': valor_coord,
        'send_coord': send_coord,
        'pause_rows': pause_between_rows,
        'pause_sheet': pause_after_sheet
    }


def process_sheet(workbook_path, config):
    sheet_name = config['sheet']
    print(f"Processando planilha: {sheet_name}")

    # Carrega a planilha específica
    df = pd.read_excel(workbook_path, sheet_name=sheet_name, usecols=['CPF', 'VALOR'])

    for idx, row in df.iterrows():
        cpf = str(row['CPF'])
        valor = str(row['VALOR'])

        # Preenche CPF
        pyperclip.copy(cpf)
        pyautogui.click(*config['cpf_coord'])
        pyautogui.hotkey('ctrl', 'v')

        # Preenche VALOR
        pyperclip.copy(valor)
        pyautogui.click(*config['valor_coord'])
        pyautogui.hotkey('ctrl', 'v')

        # Clica enviar
        pyautogui.click(*config['send_coord'])

        time.sleep(config['pause_rows'])

    # Mensagem de conclusão
    pyautogui.alert(text=f"Concluído: planilha {sheet_name}", title='Processamento Concluído')
    print(f"Finalizado {sheet_name}. Pausando por {config['pause_sheet']}s...")
    time.sleep(config['pause_sheet'])


def main():
    workbook = input("Caminho do arquivo Excel: ").strip()
    print("--- Iniciando automação ---")

    while True:
        cfg = get_user_inputs()
        if cfg is None:
            print("Saindo...")
            break
        try:
            process_sheet(workbook, cfg)
        except Exception as e:
            print(f"Erro ao processar planilha {cfg['sheet']}: {e}")
            break

    print("Automação finalizada.")


if __name__ == '__main__':
    main()
