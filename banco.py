print(" "*30)
print("Banco Simulator LTDA.") 

limite = 500
numero_de_saque = 0
LIMITE_SAQUES = 3
transacoes = []
saldo = 0

while True:
      
      espacamento = 30
      print("\n" + "-"*30)
      print("Selecione uma opção:".center(espacamento))
      print("-"*30)
      print("1 - Depositar")
      print("2 - Sacar")
      print("3 - Consultar Extrato")
      print("4 - Sair")
      print("-"*30)

      opcao = input ("Selecione uma das opções:")
      
      if opcao == '1':       
           print("Depósito")

           deposito = float(input("Informe o valor de depósito: "))

           if deposito > 0:
                saldo += deposito
                transacoes.append(f"+ R$ { deposito}")
                print(f"Saldo atualizado: R$ {saldo:.2f}")

           else:
                print(f"Valor inválido, Tente novamente.")
  
      elif opcao == '2':
           print("Sacar")

           saque = float(input("Informe o valor de saque: "))

           if saque <= limite and saque > 0 and numero_de_saque < LIMITE_SAQUES and saldo >= saque:
                
                saldo -= saque
                numero_de_saque += 1
                transacoes.append(f"- R$ { saque }")

                print(f"Saldo atual de R$ { saldo:.2f}")

           else: 
          
                 status = (
                    "Saldo insuficiente" if saldo < saque else
                    "Limite de saque diário atingido (3)" if numero_de_saque >= LIMITE_SAQUES 
                     else "Valor de saque inválido")

                 print(f"{status}")

      elif opcao == '3':
           
           print("\n" + "Transações" + "\n")

           if transacoes:
                for transacao in transacoes:
                     print(transacao),
                print(f"Saldo: R$ {saldo:.2f}")
               
           else:
            print("Nenhuma transação registrada.")

      elif opcao == '4':
           print("Sessão encerrada.")
           break

      else:
           print("Opção Inválida")
