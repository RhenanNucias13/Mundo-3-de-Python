def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO DEVE VOTAR!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: NÃO É OBRIGATORIO VOTAR!'
    else:
        return f'Com {idade} anos: DEVE VOTAR!'

nasc = int(input('Em que ano você nasceu?: '))
print(voto(nasc))