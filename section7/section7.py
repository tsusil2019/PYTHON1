""" 

# 42 Introduction to variables

numberofcats = 10
numberofcats =numberofcats * 2
print(numberofcats)
numberofcats = 99
print(numberofcats)
numberofcats = numberofcats -1
print(numberofcats)
friends = 0
print(friends)
friends = numberofcats
print(friends)
 """
#==========================================================================

""" cash = 19867324678987.99
print(cash/5)
cash = cash / 5
print(cash)
 """
#==========================================================================
"""     # 44 Variable Naming Restrictions and conventions

        # 1 . Variavbles must stat with a letter or underscore    
        ## ex : _cats , cats
        #2 . The rst of the name must consist of letters,numbers or Underscores
        ## cats is fine  but hey@you not fine 
        #3 Names are case-Sensitive
        ## CATS != Cats ,  Cats != cats

     Naming Conventions
        #CamelCase
        #shake_case
      Most python programmers prefer to use standard style conventions when naming 
        things :
      Most variables should be snake_case (Underscores between words )
     Most variables should be also be lowercase with some exceptions:
        #CAPTAL_SNAKE_CASE usually refers to contants (eg PI=3.14)
        #UpperCamelCase Usually Refers to a class 
     Variables that start and end with two underscores (called "Dunder for double underscore")
        are supposed to be private to be private or left alone

                _no_touchy_
    
 """


#==========================================================================

            #45  DATA TYPES OVERVIEW
"""     
    1> Pyhon DATAtypes includes :

        bool : true or false values
        int  : an integer (1,2,3)
        str  : string a sequence if unicode eg "Susil How are you"
        list : an orfered sequence of values of other data types ed [1,2,3]
        dict : a collection of key : values eg {"first_name":"susil","last_name":"kumar"}
    
  """

 #==========================================================================

                 # 46 WHAT tTHE HECK IS DYNAMIC TYPING 
""" 
NOTE
                   Python is highly flexible about reassigning variables to different 
                   types 
                  
                   EX : awesome = True;
                        print(awesome) # True
                        awesome = None # noting 
                        print(awesome) #None
                        awesome = "a dog"
                        print(awesome) # a gog
                  # We call above variable awesome as DYNAMIC TYPING since 
                  # variables can change type 
                    readily .

                    Other Language such as C++ are statically-typed and variables
                             are stuck with their
                       Originally-assigned type:

                    Ex : int not_awesome = 5;
                        not_awesome = "cool" # !ERROR
                      

 """
""" 
# EXAMPLES

print(None) # you need to define it first (the None value) . NONE is for NOTHING
child = None
print(child)
print(type(child))  # <class 'NoneType'>

 """

  #==========================================================================

                    # 48 DOUBLE VS SINGLE QUOTES 
        # 'T SUSIL KUMAR'
        #"T.SUSIL KUMAR'S"
  
  #==========================================================================

                    # 50 STRING ESCAPE SEQUENCES 
                        # \n leaves a line
                        # \t Leaves a space (Horigantal tab)
                        # \r carriage return
                        # \v Vertical tab

#==========================================================================

                  # 52 STRING CONCATENATION
""" 
      str_one = "Your"
      str_two = "face"
      str_three = str_one + " " + str_two # Your face
       
 """
#==========================================================================

                
                