
formula = input()

formula=formula.split('-')

try: #만약 -부호가 없다면 int로 선언이 안될것이다.
    result=int(formula[0])
    for i in range(1,len(formula)):
        try:
            result-=int(formula[i])
        except:
            addformula=formula[i]
            # addformula=addformula.split('+')
            addformula=list(map(int,addformula.split('+')))
            print(addformula)
            result-=sum(addformula)

except:
    #위의 split으로 인해 지금 문자열이 아닌 list형태임
    formula=''.join(formula)
    result=sum(list(map(int,formula.split('+'))))


print(result)