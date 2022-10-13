# Bestand in read-only (r) mode openen (wel zo veilig, we gaan niets overschrijven)
bestand = open("test.txt", "r")

# Een tekst naar het bestand schrijven
regel1 = bestand.readline()
print(regel1)

regel2 = bestand.readline()
print(regel2)

regel3 = bestand.readline()
print(regel3)