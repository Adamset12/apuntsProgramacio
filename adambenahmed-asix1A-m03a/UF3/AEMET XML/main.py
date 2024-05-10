import xml.etree.ElementTree as xml

fitxer = "localidad_17202.xml"
def leer_xml(nombre_archivo):
   tree = xml.parse(nombre_archivo)
   print(tree)
   root = tree.getroot()
   return root

root = leer_xml(fitxer)
print(root)