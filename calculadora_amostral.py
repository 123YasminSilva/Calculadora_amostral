#Calculadora_amostral
população=int(input("Digite a população:"))
margem_erro=int(input('Escolha margem de erro:'))
margem_erro=margem_erro/100
amostra_inicial=1/margem_erro**2
amostra=(população*amostra_inicial)/(população+amostra_inicial)
print('é necessário entrevistar {:.0f} pessoas para uma população de {}, a margem de erro é de {:.0%}'.format(amostra,população,margem_erro))