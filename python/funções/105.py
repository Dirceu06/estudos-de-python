def notas(*num,sit=False):
    """tira a media, situação, total, maior e menor nota

    Args:
        sit (bool, optional): define se a situação da media da turma vai ser exibida. Defaults to False.
        *num (int): notas que serão usadas para determinar as infos
    Returns:
        dict: um dicionario guardando totas a informações 
    """
    relatorio = dict()
    relatorio['total'] = len(num)
    relatorio['menor'] = relatorio['maior'] = num[0]
    soma = 0
    for n in num:
        soma+=n
        if n >= relatorio['maior']: relatorio['maior'] = n
        if n<= relatorio['menor']: relatorio['menor'] = n
    media = soma/relatorio['total']
    relatorio['media'] = media

    if sit:
        if relatorio['media'] >= 7: relatorio['situacao'] = 'boa'
        if relatorio['media'] < 7 and relatorio['media'] > 6: relatorio['situacao'] = 'razoavél'
        if relatorio['media'] < 6: relatorio['situacao'] = 'ruim'
    return relatorio

resp=notas(7,4,2,9,3,2,sit=True)
print(resp)