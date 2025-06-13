🤖 Automação IR: Fim da Digitação Manual no Imposto de Renda!
O Automação IR é um projeto desenvolvido para revolucionar a rotina de escritórios de contabilidade, eliminando a tarefa manual, repetitiva e demorada de preencher os campos de receita na declaração de Imposto de Renda.

Criado para contadores e por quem entende suas dores, este script foi implementado e aprovado com sucesso por um escritório de contabilidade, validando sua eficácia e segurança no ambiente profissional. Diga adeus a horas de digitação e ao risco de erros humanos! ⚡️

A ferramenta lê os valores de receita (mensal ou anual) diretamente de uma planilha Excel e os insere de forma automática no programa da Receita Federal ou em qualquer outro sistema de declaração.

✨ Funcionalidades Principais
Foco Contábil: Projetado especificamente para o preenchimento de declarações de Imposto de Renda.
Leitura de Planilhas: Utiliza a biblioteca pandas para ler dados de faturamento de forma organizada a partir de arquivos .xlsx.
Automação de GUI: Controla o mouse e o teclado com pyautogui para navegar no programa da declaração, clicar em campos específicos e inserir os valores.
Configuração Flexível: Permite que o contador insira todas as configurações no início da execução: planilha, aba do mês, coordenadas dos campos e pausas customizadas.
Processamento em Lote: Processa múltiplas planilhas ou abas em sequência, ideal para lidar com a carteira de clientes de um escritório.
Feedback em Tempo Real: Exibe o status do processamento no terminal e notifica o usuário com um alerta visual ao final de cada declaração.
⚙️ Como Funciona
O fluxo de automação foi pensado para ser simples e seguro:

Configuração Inicial: O script solicita ao contador:

O caminho para a planilha Excel com os dados de receita.
A sigla da aba a ser processada (ex: Jan, Fev, Mar).
As coordenadas (x, y) na tela para os campos CPF e VALOR da Receita, e para o botão de salvar/enviar.
Os tempos de pausa (em segundos) entre cada lançamento e ao final de cada cliente/planilha.
Leitura dos Dados: A aba especificada da planilha é carregada, e os dados das colunas CPF e VALOR são extraídos.

Loop de Automação: Com o programa do Imposto de Renda aberto na tela correta, o script executa para cada linha da planilha:

O valor do CPF é copiado.
O mouse clica no campo CPF do programa e cola a informação (Ctrl + V).
O mesmo processo é repetido para o campo VALOR.
Para finalizar, o script clica no botão "Enviar" ou "Salvar".
Uma pequena pausa garante que o programa processe a informação antes de seguir para a próxima linha.
Conclusão e Próximo Cliente: Ao final de todos os lançamentos de uma planilha, uma caixa de alerta confirma a conclusão. O script então aguarda um tempo para que o contador possa preparar a declaração do próximo cliente.
