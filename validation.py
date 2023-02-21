#Modulo validacion

def main():
    valInt()
    valFloat()
    valList()
    valComplex()

def valInt(primero, segundo = ""):
    try:
        numero = int(primero)
        
        if segundo == "":
            return True
        
        if segundo != "":
            if len(segundo) != 2:
                raise ValueError
            if type(segundo) == list:
                if segundo[0] < segundo[-1]:
                    pass
                else:
                    raise ValueError
                if numero >= segundo[0] and numero <= segundo[-1] :
                    return True
                else:
                    return False
            
            if type(segundo) == tuple:
                if segundo[0] < segundo[-1]:
                    pass
                else:
                    raise ValueError
                if numero > segundo[0] and numero < segundo[-1]:
                    return True
                else:
                    return False
            
            elif type(segundo) == set or type(segundo) == dict:
                raise TypeError
                
            else:    
                if segundo.startswith("[") == True and segundo.endswith("]") ==True:
                        lista = list(segundo)
                        if int(lista[1]) < int(lista[-2]):
                            pass
                        else:
                            raise ValueError
                        if numero >= int(lista[1]) and numero <= int(lista[-2]) :
                            return True
                        else:
                            return False
                    
                elif segundo.startswith("(") == True and segundo.endswith(")") == True:
                    tupla = tuple(segundo)
                    if int(tupla[1]) < int(tupla[-2]):
                        pass
                    else:
                        raise ValueError
                    if numero > int(tupla[1]) and numero < int(tupla[-2]):
                        return True
                    else:
                        return False
                else:
                    raise TypeError
    except ValueError:
        return False
    except TypeError:
        return False

def valFloat(primero, segundo = ""):
    try:
        if type(primero) == int:
            return False
        try:
            if int(primero) == True:
                return False
        except ValueError:
            pass
        numero = float(primero)
  
        if segundo == "":
            return True
        
        if segundo != "":
            if len(segundo) != 2:
                raise ValueError
            if type(segundo) == list:
                if segundo[0] < segundo[-1]:
                    pass
                else:
                    raise ValueError
                if numero >= segundo[0] and numero <= segundo[-1] :
                    return True
                else:
                    return False
            
            if type(segundo) == tuple:
                if segundo[0] < segundo[-1]:
                    pass
                else:
                    raise ValueError
                if numero > segundo[0] and numero < segundo[-1]:
                    return True
                else:
                    return False
            
            elif type(segundo) == set or type(segundo) == dict:
                raise TypeError
            
            else:    
                if segundo.startswith("[") == True and segundo.endswith("]") ==True:
                        lista = list(segundo)
                        if float(lista[1]) < float(lista[-2]):
                            pass
                        else:
                            raise ValueError
                        if numero >= float(lista[1]) and numero <= float(lista[-2]) :
                            return True
                        else:
                            return False
                    
                elif segundo.startswith("(") == True and segundo.endswith(")") == True:
                    tupla = tuple(segundo)
                    if float(tupla[1]) < float(tupla[-2]):
                        pass
                    else:
                        raise ValueError
                    if numero > float(tupla[1]) and numero < float(tupla[-2]):
                        return True
                    else:
                        return False
                else:
                    raise TypeError
    except ValueError:
        return False
    except TypeError:
        return False

def valComplex(primero, segundo = ""):
    try:

        if type(primero) == complex:
            pass
        else:
            raise ValueError
        
        letra = str(primero)
        a = pow(int(letra[1]),2)
        b = pow(int(letra[3]),2)
        c = a + b
        numero = pow(c, 0.5)
    
        if segundo == "":
            return True
        if segundo != "":
            if len(segundo) != 2:
                raise ValueError
            if type(segundo) == list:
                if segundo[0] < segundo[-1]:
                    pass
                else:
                    raise ValueError
                if numero >= segundo[0] and numero <= segundo[-1] :
                    return True
                else:
                    return False
            
            if type(segundo) == tuple:
                if segundo[0] < segundo[-1]:
                    pass
                else:
                    raise ValueError
                if numero > segundo[0] and numero < segundo[-1]:
                    return True
                else:
                    return False
            
            elif type(segundo) == set or type(segundo) == dict:
                raise TypeError
              
            else:    
                if segundo.startswith("[") == True and segundo.endswith("]") ==True:
                        lista = list(segundo)
                        if int(lista[1]) < int(lista[-2]):
                            pass
                        else:
                            raise ValueError
                        if numero >= int(lista[1]) and numero <= int(lista[-2]) :
                            return True
                        else:
                            return False
                    
                elif segundo.startswith("(") == True and segundo.endswith(")") == True:
                    tupla = tuple(segundo)
                    if int(tupla[1]) < int(tupla[-2]):
                        pass
                    else:
                        raise ValueError
                    if numero > int(tupla[1]) and numero < int(tupla[-2]):
                        return True
                    else:
                        return False
                else:
                    raise TypeError
    except ValueError:
        return False
    except TypeError:
        return False
    except AttributeError:
        return False

def valList(primero, segundo = "", tercero = ""):
    try: 
        if type(primero) == list:
            pass
        else:
            return False
        if segundo == "" and tercero == "":
            return True
        elif segundo != "" and tercero == "":
            raise TypeError
        
        if type(segundo) == list or type(segundo) == int:
            pass
        else:    
            raise TypeError
            
        if tercero == "len" or tercero == "value":
            pass
        else:    
            raise ValueError 
        
        if tercero == "len" and type(segundo) == int:
            if len(primero) != int(segundo):
                return False
            return True
        if tercero == "value" and type(segundo) == list:
            if sorted(primero) == sorted(segundo):
                return True
            return False
        return False
    except ValueError:
        return False
    except TypeError:
        return False

if __name__== "__main__":
    main()