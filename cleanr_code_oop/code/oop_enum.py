from enum import Enum

class Krabby_patty_status(Enum):
    RAW = 1
    COOKED = 2
    ROT = 3
    
print(Krabby_patty_status.RAW)
# Krabby_patty_status.RAW

print(Krabby_patty_status.RAW.value == 1)
# True

for krabby_patty_statu  in Krabby_patty_status:
    print(krabby_patty_statu)
# Krabby_patty_status.RAW
# Krabby_patty_status.COOKED
# Krabby_patty_status.ROT
