>>> def вага_на_місяці(вага, приріст, роки):
 роки = роки + 1
 for рік in range(1, роки):
 вага = вага + приріст
 вага_на_місяці = вага * 0.165
 print(‡Рік %s твоя вага %s‡ % (рік, вага_на_місяці))
>>> вага_на_місяці(35, 0.3, 5)