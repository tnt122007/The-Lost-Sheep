ehp = 200 
buff = 0
buffmulti = 0
mbuff = 0
mbuffmulti = 0
shield = 0
mshield = 0
chp = 0
cdef = 0
cmdef = 0
catk = 0
cmatk = 0
turn = 3
b = 0  
while b == 0 :
     print ("Choose your character")
     print ("1-Divine tnt")
     a = float(input("Type number to choose character"))    
     if a == 1:
         b = 2
         print ("That is a right answer you now have 4 skill and here its your stat")
         chp = 120
         print ("Hp: 120")
         catk = 25
         print ("Attack: 25")
         cmatk = 25
         print ("Magic attack: 25")
         print ("Skill 1: Explosion - Attack - Explosion by your self and deal dmg")
 
         print ("Skill 2: Magic explosion - Magic attack - Explosion by your self and deal dmg")
         print ("Skill 3: Shield - Support - Create a shield that protect you from 999 dmg")
         print ("Skill 4: Magic shield - Support - Create a magic shield that protect you from 999 magic dmg")
         while ehp > 0:
          print ("Choose skill that you want to  use")
          print ("1-Magic explosion")
          print ("2-Magic explosion")
          print ("3-Shield")
          print ("4-Magic shield")
          s = int(input("Type number to use skill"))
          if s == 1:
            ehp = ehp - (catk*1.5 + buff + buff*buffmulti )
            print("You swing your own sword to slash enemy, enemy HP is now only:", ehp)
          elif s == 2:
            ehp = ehp - 10 - buff
            print("You focus all your mind and cast a magic spell that shot a fire ball, enemy HP is now only:", ehp)
          elif s == 3:
            buff = buff + 3
            print("You focus all your muscle and you become buff")
          elif s == 4: 
            mbuff = mbuff + 2
            print("You focus all your mind and you become smarter")     
          else:
           print("Please type a number that stand for a skill")
     else:
         print("Choose a number for character")
        

 

 



 