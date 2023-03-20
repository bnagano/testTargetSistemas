def reversa(palavra):
    reversa = ""
    for i in palavra:
        reversa = i + reversa
    return reversa

palavra = "TargetSistemas"

print(reversa(palavra))