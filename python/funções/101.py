def soma(*num,sub=False):
    """_summary_

    Args:
        sub (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    resultado = 0
    for n in num:
        if sub: resultado-=n
        else: resultado+=n
    return resultado

print(soma(3,2,5,3,2,1,3,sub=True))