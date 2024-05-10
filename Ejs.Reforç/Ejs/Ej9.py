import_ = int(input("Quin és l'import de la compra:"))

import_ = int((import_ - (import_ * 15 )/ 100))
print(import_)