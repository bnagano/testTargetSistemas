sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = 0

total = sp+rj+mg+es+outros

texto = f"""FATURAMENTO MENSAL
Faturamento total: R${total:,.2f}
Faturamento em SP: R$ {sp:,.2f} ({(sp*100)/total:,.2f}%)
Faturamento em RJ: R${rj:,.2f} ({(rj*100)/total:,.2f}%)
Faturamento em MG: R${mg:,.2f} ({(mg*100)/total:,.2f}%)
Faturamento em ES: R${es:,.2f} ({(es*100)/total:,.2f}%)
Faturamento em Outros: R${outros:,.2f} ({(outros*100)/total:,.2f}%)
"""

print(texto)

