class Тварини:
    pass
   def bre(self):
       print('дихає')
   def mov(self):
     print('рухається')
   def eat(self):
     print('харчується їжею')
 class Ссавці(Тварини):
  def milk (self):
   print('годує дитинчат')
 class Жирафи(Ссавці):
  def їсти_листя_з_дерев(self):
   print('їсть листя')
  def ліву_ногу_вперед(self):
   print('ліва нога вперед')
  def праву_ногу_вперед(self):
   print('права нога вперед')
  def ліву_ногу_назад(self):
   print('ліва нога назад')
  def праву_ногу_назад(self):
   print('права нога назад')
  def танцювати(self):
    self.ліву_ногу_вперед()
    self.ліву_ногу_назад()
    self.праву_ногу_вперед()
    self.праву_ногу_назад()
    self.ліву_ногу_назад()
    self.праву_ногу_назад()
    self.праву_ногу_вперед()
    self.ліву_ногу_вперед()
реджинальд = Жирафи()
реджинальд.танцювати()