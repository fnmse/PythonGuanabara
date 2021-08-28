primeirotermo= int(input('Digite o primeiro termo: '))
razão=int(input('Digite a razão: '))
decimo=primeirotermo+(10-1)*razão
for c in range (primeirotermo,decimo+razão,razão):

    print(c,end=' ')