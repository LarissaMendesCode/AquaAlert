print("-"*50)
print("-"*50)
print (" Bem-vindo à Calculdora Sustentável!")
print("-"*50)
desperdicio_total_m3=0
def cadastrar():
  global desperdicio_total_m3
  print("-"*50)
  usuarios = str(input("Informe o seu nome: "))
  print("-"*50)
  #chuveiro
  print ("Atenção- Tempo médio de chuveiro aberto.Se possível, use o cronômetro.")
  print("-"*50)
  tempobanho= float(input("Informe o tempo médio de banho (min): "))
  qtdebanho= int(input("Informe o número de banhos/dia: "))
  chuveiro_consumo= qtdebanho* tempobanho*0.2*60
  print("-"*50)
  
  #torneira pia
  print("-"*50)
  print ("Atenção- Tempo médio de torneira aberta.Se possível, use o cronômetro.")
  print("-"*50)
  #lavar as mãos
  tempo_torneira_maos= float (input("Informe o tempo médio que você utiliza para lavar as mãos (min): "))
  qtdeusotorneiramaos= int(input("Informe a frequência ´para lavar as mãos/dia: "))
  #lavar a escovar os dentes
  tempo_torneira_escovardentes= float (input("Informe o tempo médio que você utiliza para escovar os dentes (min): "))
  qtdeusotorneiradentes= int(input("Informe a frequência para escovar os dentes: "))
  #lavar a louça
  tempo_torneira_lavarlouça= float (input("Informe o tempo médio que você utiliza para lavar louça (min): "))
  qtdeusotorneiralouça= int(input("Informe a frequência para lavar a louça: "))
  #total
  tempo_torneira= tempo_torneira_maos*qtdeusotorneiramaos+tempo_torneira_escovardentes*qtdeusotorneiradentes+tempo_torneira_lavarlouça*qtdeusotorneiralouça
  print (tempo_torneira)
  qtdeusotorneira= qtdeusotorneiramaos+qtdeusotorneiradentes+qtdeusotorneiralouça
  #torneira com arejador
  print ("Arejador é um acessório para regular a vazão da torneira!")
  arejador= int (input("Digite:\n1.torneira com arejador\n2.torneira sem arejador\n"))
  print("-"*50)
  if arejador==1:
    torneira_consumolavarmaos=tempo_torneira_maos*qtdeusotorneiramaos*0.15*60
    #print ("lavar as mãos",torneira_consumolavarmaos)
    torneira_consumodentes=tempo_torneira_escovardentes*qtdeusotorneiradentes*0.15*60
    #print ("escovar os dentes",torneira_consumodentes)
    torneira_consumolouca=tempo_torneira_lavarlouça*qtdeusotorneiralouça*0.15*60
    #print ("lavar louça",torneira_consumolouca)
    torneira_consumo= torneira_consumolavarmaos+torneira_consumodentes+torneira_consumolouca
    #print (torneira_consumo)
  if arejador==2: 
    torneira_consumolavarmaos=tempo_torneira_maos*qtdeusotorneiramaos*0.30*60
    #print ("lavar as mãos",torneira_consumolavarmaos)
    torneira_consumodentes=tempo_torneira_escovardentes*qtdeusotorneiradentes*0.30*60
    #print ("escovar os dentes",torneira_consumodentes)
    torneira_consumolouca=tempo_torneira_lavarlouça*qtdeusotorneiralouça*0.30*60
    #print ("lavar louça",torneira_consumolouca)
    torneira_consumo= torneira_consumolavarmaos+torneira_consumodentes+torneira_consumolouca
    #print (torneira_consumo)
  else:
    print ("escolha uma opçao válida.") 
    
  #descarga sanitário
  print("-"*50)
  qtdedescarga= int(input("Informe o número de descargas/dia: "))
  consumodescarga= 6*qtdedescarga
  print("-"*50)
  
  # Chuveiro Ideal: 36 litros/ banho 3 min / 2x ao dia/ 0,20L/S
  # A ONU (Organização das Nações Unidas) diz que 110 L/dia são suficientes total
  # para atender as necessidades 
  # básicas de consumo e higiene de uma pessoa. 
  
  #Cálculo chuveiro
  if chuveiro_consumo>48:
    desperdicio= chuveiro_consumo-48
    print ("Desperdício (L) Chuveiro: ",desperdicio)
    tempodesperdicio=tempobanho*2 - 4
    qtdebanhodesperdicio= qtdebanho -2
    print ("Recomendação eliminar o tempo de banho (min): ", tempodesperdicio)
    if qtdebanho>2:
      print ("Recomendação eliminar banhos por dia: ", qtdebanhodesperdicio)
    if qtdebanho==2:
      print ("Parabéns! Quantidade de banho dentro do recomendado: 2 banhos/dia ")
    
  else:
    economia = 72-chuveiro_consumo
    print ("Economia (L) Chuveiro: ", economia)
   
   #cálculo torneira 
  if  torneira_consumo> 27:
    desperdiciotorneira= torneira_consumo-27
    print ("Desperdício (L) Torneira: ",desperdiciotorneira)
    qtdeusotorneiradesperdício = qtdeusotorneira-6
    tempodesperdiciotorneira=tempo_torneira - 3.0
    print ("Recomendação eliminar o tempo de torneira em (min): ",tempodesperdiciotorneira)
    print ("Recomendação eliminar a frequência de torneira: ",qtdeusotorneiradesperdício )
  else:
    economiatorneira = 27-torneira_consumo
    print ("Economia (L) Torneira: ", economiatorneira)
    
  if consumodescarga>30:
    desperdiciodescarga= consumodescarga-30
    print ("Desperdício (L) Descarga:" ,desperdiciodescarga)
  else:
    economiadescarga= 30 - consumodescarga
    print ("Economia (L) Descarga: ", economiadescarga)
  
  print("-"*50) 
  desperdiciototal= desperdicio+ desperdiciotorneira+desperdiciodescarga
  desperdicio_total_m3= (desperdiciototal/1000)*30
  print("Desperdício total individual mensal (m³)", desperdicio_total_m3)
  print("-"*50)
  
# Torneira com arejador 0,15 L/s e sem arejador é 0,3 L/s.
# Torneiras com sensores que controlam a saída de água de acordo com a 
# aproximação das mãos reduzem o consumo entre 35% e 80%, na comparação 
# com as convencionais.
# descarga a vácuo 1 L/descarga descarga convencional de 6 a 12 L.
cadastrar ()
opcao= int(input("Quer saber do resultado?Selecione o número:\n1.Sair\n2.Resultado\n"))
if opcao==1:
   print("Até logo!")  
else:
  volumeatual= float (input("Informe o volume m³ da sua fatura atual: "))
  reais_atual= float (input("Informe o valor da sua conta atual:  "))
  volume = float (volumeatual - desperdicio_total_m3)
  print ("1.Residencial Social")
  print ("2.Residencial Popular")
  print ("3.Residencial Normal")
  esgoto = round(volume*0.8)
  categoria = int( input ("Informe a categoria: "))
  print ("Com o consumo racional de água, estima-se uma nova fatura (m³):", volume)
#Cálculo faturamento em reais
faixa_0_valor = 2.12
faixa_1_valor= 4.34
faixa_2_valor= 7.38
faixa_3_valor= 8.00
faixa_4_valor= 13.77
faixa_5_valor= 24.54
faixa_6_valor = 6.17
faixa_7_valor= 8.00
faixa_8_valor= 8.65
faixa_9_valor= 14.85
faixa_10_valor= 26.22
if categoria == 1:
    consumo_RS= volume*faixa_0_valor
  
if categoria==2:
      if volume <= 10:
          consumo_RS= volume*faixa_1_valor
          
      if volume > 10:
          volume2= volume-10
          
          consumo_RS= 10*faixa_1_valor + volume2*faixa_2_valor
          
      if volume > 15 and volume <= 20:
          volume3= volume-15
          
          consumo_RS= 10*faixa_1_valor + 5*faixa_2_valor + volume3*faixa_3_valor
          
      if volume >= 21 and volume <= 50:
          volume4= volume-20
          
          consumo_RS= 10*faixa_1_valor + 5*faixa_2_valor + 5*faixa_3_valor+ volume4*faixa_4_valor
          
      if volume > 50:
          volume5= volume-30
        
          consumo_RS= 10*faixa_1_valor + 5*faixa_2_valor + 5*faixa_3_valor+ 5*faixa_4_valor+ volume5*faixa_5_valor
      
      if categoria==2:
       if esgoto <= 10:
          
          esgoto_RS= esgoto*faixa_1_valor
       if esgoto > 10:
          
          esgoto2=esgoto - 10
          
          esgoto_RS= 10*esgoto*faixa_1_valor + esgoto2*faixa_2_valor
       if esgoto > 15 and esgoto <= 20:
          
          esgoto3= esgoto - 15
          
          esgoto_RS= 10*faixa_1_valor + 5*faixa_2_valor + esgoto3*faixa_3_valor
       if esgoto >= 21 and esgoto <= 50:
          
          esgoto4= volume-20
          
          esgoto_RS= 10*faixa_1_valor + 5*faixa_2_valor + 5*faixa_3_valor+ esgoto4*faixa_4_valor
       if esgoto > 50:
        
          esgoto5= volume-30
          
          esgoto_RS= 10*faixa_1_valor + 5*faixa_2_valor + 5*faixa_3_valor+ 5*faixa_4_valor+ esgoto5*faixa_5_valor
else:  
      print("Escolha uma opção válida")
      
if categoria==3:
      if volume <= 10:
          consumo_RS= volume*faixa_6_valor
          
      if volume > 10:
          volume2= volume-10
          
          consumo_RS= 10*faixa_6_valor + volume2*faixa_7_valor
          
      if volume > 15 and volume <= 20:
          volume3= volume-15
          
          consumo_RS= 10*faixa_6_valor + 5*faixa_7_valor + volume3*faixa_8_valor
          
      if volume >= 21 and volume <= 50:
          volume4= volume-20
          
          consumo_RS= 10*faixa_6_valor + 5*faixa_7_valor + 5*faixa_8_valor+ volume4*faixa_9_valor
          
      if volume > 50:
          volume5= volume-30
        
          consumo_RS= 10*faixa_6_valor + 5*faixa_7_valor + 5*faixa_8_valor+ 5*faixa_9_valor+ volume5*faixa_10_valor
      
      if categoria==3:
       if esgoto <= 10:
          
          esgoto_RS= esgoto*faixa_6_valor
       if esgoto > 10:
          
          esgoto2=esgoto - 10
          
          esgoto_RS= 10*esgoto*faixa_6_valor + esgoto2*faixa_7_valor
       if esgoto > 15 and esgoto <= 20:
          
          esgoto3= esgoto - 15
          
          esgoto_RS= 10*faixa_6_valor + 5*faixa_7_valor + esgoto3*faixa_8_valor
       if esgoto >= 21 and esgoto <= 50:
          
          esgoto4= volume-20
          
          esgoto_RS= 10*faixa_6_valor + 5*faixa_7_valor + 5*faixa_8_valor+ esgoto4*faixa_9_valor
       if esgoto > 50:
        
          esgoto5= volume-30
          
          esgoto_RS= 10*faixa_6_valor + 5*faixa_7_valor + 5*faixa_8_valor+ 5*faixa_9_valor+ esgoto5*faixa_10_valor
else:  
      print("Escolha uma opção válida")
      
print ("Total da fatura água (R$):", round(consumo_RS,2))
print ("Total da fatura de esgoto (R$):", round(esgoto_RS,2))
total_RS= consumo_RS+esgoto_RS
print ("Total da fatura (água e esgoto) (R$):", round(total_RS,2))
valoreconomia = reais_atual - total_RS
print ("Total economia (R$):", round(valoreconomia,2))
