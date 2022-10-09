vaca = int(input("digite a quantidade de vacas adquiridas "))
cavalo = int(input("digite a quantidade de cavalos adquiridos "))
ovelha = int(input("digite a quantidade de ovelhas adquiridas "))
producao_de_leite_por_dia = 3.2*vaca
producao_de_leite_por_semana = 7*producao_de_leite_por_dia
producao_de_leite_por_meses = 30*producao_de_leite_por_dia
print("producao de leite por dia: ", producao_de_leite_por_dia)
print("producao de leite por semana: ", round(producao_de_leite_por_semana, 14))
print("producao de leite por mês: ", producao_de_leite_por_meses)
print()
volume_de_la_em_quilos_por_dia = 2.3*ovelha
volume_de_la_em_quilos_por_semana = 7*volume_de_la_em_quilos_por_dia
volume_de_la_em_quilos_por_mes= 30*volume_de_la_em_quilos_por_dia
print("volume de lã em quilos por dia: ", volume_de_la_em_quilos_por_dia)
print("volume de lã em quilos por semana: ", volume_de_la_em_quilos_por_semana)
print("volume de lã em quilos por mês: ", volume_de_la_em_quilos_por_mes)
print()
quantidade_de_ferraduras = 4*cavalo
print("quantidade de ferraduras para os cavalos: ", quantidade_de_ferraduras)
