s=float(input('Digite o salário: '))
r=s+ (s*0.10) if s>1250 else s+(s*0.15)
print(r)