


def caesarcipher(text, shift):
    """
    Receives a string a shift value and encrypts it,
    using Caesar Cipher method.
    """
    
    cipher = " "
    for letter in text:    
        if letter.isupper():
            index = UPPERTEXT.index(letter)
            result = (index + shift)%26
            cipher += UPPERTEXT[result]
        elif letter.islower():
            index = LOWERTEXT.index(letter)
            result = (index + shift)%26
            cipher += LOWERTEXT[result]
        elif letter == ",":
            cipher += ","
        elif letter == " ":
            cipher += " "
    return cipher


if __name__ == "__main__":
    
    import sys
        
    
    UPPERTEXT = ('A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z').split(",")
    LOWERTEXT = ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z').split(",")
        
    
    if len(sys.argv) > 2:
        print("Error: Just one argument must be given!!!")   
    elif int(sys.argv[1]) <= 0:
        print("Error: Argument value must be positive!!!")         
    else:
        text = input("plaintext:")    
        print("ciphertext:" + caesarcipher(text, int(sys.argv[1])))
        print()
