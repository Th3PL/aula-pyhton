# dic = {
#     "montadora" : "ford",
#     "modelo" : "mustang",
#     "ano" : 1964,
#     "ano" : 1980

# }
# # print(dic) 
# # print(dic["modelo"])
# # print(dic.get("montadora"))
# # print(len(dic))
# # cliente = dict(nome = "Astrogildo", idade = 25, estado = "SP")
# # print(cliente)
# # print(cliente.keys())
# # print(cliente.values())

# dic["ano"] = 2000
# print(dic)
# dic.update({"montadora":"Fiat"})
# print(dic)
# dic["cor"] = "prata"
# print(dic)
# dic.update({"motor":1.0})
# print(dic)
# dic.pop("montadora")
# dic.popitem()
# print(dic)

# cliente = dict(nome = "Astrogildo", idade = 25, estado = "SP")
# print("Exibindo as chaves do dicionário:")
# for c in cliente.keys():
#     print(c)
# print("-"*40)
# print("Exibindo os valores do dicionário:")
# for c in cliente.values():
#     print(c)

clientes = {
    "cliente1" : {"nome" : "Astrogildo", "ano" : 2000},
    "cliente2" : {"nome" : "Berisvaldo", "ano" : 2003},
    "cliente3" : {"nome" : "Gumercindo", "ano" : 1998}
}

print(clientes)
print(clientes["cliente2"]["nome"])