# program to store id
Id={"gmail":{"kiera@hotmail.com":"123456kl","tom":"tom545454"},"blog":{"sam@wen":2345678,"not@jos":856457}}
#username="babul"
#pwd="7154"
while True:
    username=input("enter your username to unlock view setting")
    if username!="babul":
        continue
    print("thank you")
    pwd=input("enter pwd")
    if pwd=="7154":
        break
    print("thank you again")
while True:
    inputx=(input("what do you want to view gmail,blog"))
    if inputx!="gmail":
        continue
    print("gmail user name")
    view=input()
    if view!="kiera@hotmail.com":
        continue
    print(Id["gmail"]["kiera@hotmail.com"])
    
        