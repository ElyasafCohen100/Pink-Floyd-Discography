
phone_letters_dict = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def get_letter_combinations(digits): #23
   
    if not digits:
        print("No digits entered.") 
        return []
         
    combinations_list = [""]
    
    for digit in digits: #2, #3
        
        # ==== if the digit does not exist in the dictionary ==== #
        if digit not in phone_letters_dict:
            print("Invalid input. Digits 0 and 1 do not have corresponding letters.")
            return []
        
        letters_button_list = phone_letters_dict[digit]  #abc, #def
        new_combinations_list = []
        
        for combination in combinations_list:
            for letter in letters_button_list: # a, b, c,  =|=   #d, e, f,
                new_combinations_list.append(combination + letter) #[a, b, c] =|= [ad, ae, af, bd, be, bf, cd, ce, cf]
               
        combinations_list = new_combinations_list
                
    return combinations_list



# ========================================== # 
result = get_letter_combinations("456")
      
for i, combination in enumerate(result, 1):
    print(f"{combination:<6}", end="")
    if i % 5 == 0:
      print()
# ========================================== # 