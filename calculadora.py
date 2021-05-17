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