from datetime import date as data
 
#------------------------------------//------------------------------------//------------------------------------//------------------------------------//
 
def calculadora(valor):
    """
    Calculadora com objetivo de calcular máximo de pessoas que irão visualizar o anúncio.
    :param valor: Reais investidos no anúncio.
    :return: Retorna o máximo de pessoas que vão ver o anúncio, bem como clicks e afins, conforme problema proposto.
    """
 
    visualizacoes = 0
 
    try:
        visualizacoes += int(valor) * 30
    except (TypeError, ValueError):
        return 'Valor incorreto ou tipo de entrada divergente, tente novamente.'
 
    clicks = round((visualizacoes / 100) * 12, 0)
    compartilhamentos = round((clicks / 20) * 3, 0)
    visualizacoes += 160 * compartilhamentos
 
    return [clicks, compartilhamentos, visualizacoes]
 
#------------------------------------//------------------------------------//------------------------------------//------------------------------------//
 
cadastros = [] # Lista para salvar cadastros e gerar o relatório final.
continuar = "s" # Para fechar o loop de cadastro.
 
#------------------------------------//------------------------------------//------------------------------------//------------------------------------//
 
while continuar == 's':
 
    try: # Verifica as entradas, se caso acontecer algum erro, retorna um print e começa o loop novamente.
        nome = input("Digite o nome do anúncio: ")
        cliente = input("Digite o nome do cliente: ")
        datainicio = input("Digite a data de inicio 'dia/mes/ano': ").split("/")
        datafinal = input("Digite a data de término 'dia/mes/ano': ").split("/")
        investimentodia = int(input("Digite o investimento por dia (sem R$): ").replace(",", "."))
        difdatas = data(int(datafinal[2]), int(datafinal[1]), int(datafinal[0])) - data(int(datainicio[2]), int(datainicio[1]), int(datainicio[0]))
    except:
        print("Aconteceu algum erro, tente novamente!")
 
    cadastros.append({
        "nome": nome,
        "cliente": cliente,
        "datainicio": "/".join(datainicio),
        "datafinal": "/".join(datafinal),
        "quantidadedias": difdatas.days,
        "investimentodia": 'R$'+ str(investimentodia).replace(".", ","),
        "valortotal": "R$" + str(investimentodia * difdatas.days).replace(".", ","),
        "visualizacoesmax": f"{calculadora(investimentodia * difdatas.days)[2]} visualizações.",
        "clicksmax": f"{calculadora(investimentodia * difdatas.days)[0]} clicks.",
        "compartilhamentosmax": f"{calculadora(investimentodia * difdatas.days)[1]} compartilhamentos."
    })
 
    continuar = input("Para continuar cadastrando, inserir 's', para gerar relatório deixar vazio: ")
 
#------------------------------------//------------------------------------//------------------------------------//------------------------------------//
 
tipo = input("Modo de pesquisa, 'cliente, data, todos': ")
 
if tipo == 'todos':
    for cadastro in cadastros:
        print("\n")
        print("---------------------------------------------------------")
        print(f"Nome do anúncio: {cadastro['nome']}\n"
              f"Nome do cliente: {cadastro['cliente']}\n"
              f"Data de início: {cadastro['datainicio']}\n"
              f"Data de término: {cadastro['datafinal']}\n"
              f"Dias contados: {cadastro['quantidadedias']}\n"
              f"Ivestimento por dia: {cadastro['investimentodia']}\n"
              f"Valor total investido: {cadastro['valortotal']}\n"
              f"Visualizações máximas: {cadastro['visualizacoesmax']}\n"
              f"Clicks máximos: {cadastro['clicksmax']}\n"
              f"Compartilhamentos máximos: {cadastro['compartilhamentosmax']}"
              )
        print("---------------------------------------------------------")
 
elif tipo == 'cliente':
    nomedocliente = input("Digite o nome do cliente: ")
    for cadastro in list(filter(lambda x: x['cliente'] == nomedocliente, cadastros)):
        print("\n")
        print("---------------------------------------------------------")
        print(f"Nome do anúncio: {cadastro['nome']}\n"
              f"Nome do cliente: {cadastro['cliente']}\n"
              f"Data de início: {cadastro['datainicio']}\n"
              f"Data de término: {cadastro['datafinal']}\n"
              f"Dias contados: {cadastro['quantidadedias']}\n"
              f"Ivestimento por dia: {cadastro['investimentodia']}\n"
              f"Valor total investido: {cadastro['valortotal']}\n"
              f"Visualizações máximas: {cadastro['visualizacoesmax']}\n"
              f"Clicks máximos: {cadastro['clicksmax']}\n"
              f"Compartilhamentos máximos: {cadastro['compartilhamentosmax']}"
              )
        print("---------------------------------------------------------")
 
#------------------------------------//------------------------------------//------------------------------------//------------------------------------//