
#identificar a categoria
volume= float (input("Informe o volume m³ da sua fatura: "))
esgoto = round(volume*0.8)

print ("1.Residencial Social")
print ("2.Residencial Popular")
print ("3.Residencial Normal")
categoria = int( input ("Informe a categoria: "))

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