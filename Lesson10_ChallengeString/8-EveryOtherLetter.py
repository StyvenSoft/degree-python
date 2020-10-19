# Cree una función llamada every_other_letter que tome una cadena llamada palabra como parámetro. 
# La función debe devolver una cadena que contenga todas las demás letras de la palabra.

# Write your every_other_letter function here:
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

# Uncomment these function calls to test your tip function:
print(every_other_letter("Learning"))
# should print Lann
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 