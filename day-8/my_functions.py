alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')        # it is more simple than write each letter into list

def caeser(text, shift, direction):
    end_text = ''
    for char in text.lower():
        if char in alphabet:                        # if there are symbols or numbers
            index_ = alphabet.index(char)           # h - 7, ...
        
            if direction.lower() == "encode":
                new_index = index_ + shift              # h - 7 => 7 + shift
            elif direction.lower() == "decode":
                new_index = index_ - shift              # h - 7 => 7 - shift => ...
            end_text += alphabet[new_index]

        else:
            end_text += char


    print(f'{direction}d version: {end_text}')