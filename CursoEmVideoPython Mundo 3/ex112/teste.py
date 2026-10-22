from ex112.utilidadescev import moeda
from ex112.utilidadescev import dados

p = dados.leiadin('Digite seu preço: R$')
moeda.resumo(p,20,8)