'''
Adam Ben Ahmed
ASIXc1A
'''
from time import sleep
# region Declaració de Funcions ----------
def preparar_aigua():
    print("Escalfar aigua")
    sleep(1)
    print("Posar-hi sal")
    sleep(1)
def fregir_pastanagues():
    print("Preparar paella per fregir")
    sleep(1)
    print("Rossejar pastanagues")
    sleep(1)
    print("Netejar oli de paella")
    sleep(1)
def fregir_cebes():
    print("Preparar paella per fregir")
    sleep(1)
    print("Rossejar cebes")
    sleep(1)
    print("Netejar oli de paella")
    sleep(1)
def saltar_ingredients():
    print("Preparar paella per saltar")
    sleep(1)
    print("Cuinar remenant ingredients")
    sleep(1)
def recopilar_ingredients():
   print("Comprar al supermercat")
   sleep(1)
   print("Disposar-los sobre el marbre")
   sleep(1)
def cuinar_tallarines():
   preparar_aigua()
   print("Bullir tallarines")
   sleep(1)
   print("Escórrer tallarines")
   sleep(1)
   print("Deixar-les preparades")
   sleep(1)
def cuinar_pastanagues():
   print("Tallar pastanagues")
   sleep(1)
   fregir_pastanagues()
   print("Deixar pastanagues preparades")
   sleep(1)
def cuinar_cebes():
   print("Tallar cebes")
   sleep(1)
   fregir_cebes()
   print("Deixar cebes preparades")
   sleep(1)
def preparacio_final():
   print("Barrejar ingredients amb salsa teriyaki")
   sleep(1)
   saltar_ingredients()
   print("Deixar llest per servir")
   sleep(1)
def preparar_fieus_yakisoba_vegetals():
    recopilar_ingredients()
    cuinar_tallarines()
    cuinar_pastanagues()
    cuinar_cebes()
    preparacio_final()
# endregion
# region INICI: Preparar fideus Yakisoba
preparar_fieus_yakisoba_vegetals()
# endregion