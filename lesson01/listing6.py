a = 2
b = 3
i = 1

while True:
    print(f'{i}-й день {a}')
    a = round(a + (a * 0.1), 2)
    i += 1
    if a >= b:
        print(f'{i}-й день {a}')
        break 
  
print(f'Ответ: на {i}-й день спортсмен достиг результата не менее {b} км.')
    
    
    
      
