letters = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: "g h i".split(),
    5: ("j k l").split(),
    6: ("m n o").split(),
    7: ("p q r s").split(),
    8: ("t u v").split(),
    9: ("w x y z").split(),
}

def main():
    digits = input()
    output = (t9([], digits))
    print(output)
    print(f"Length of the output is: {len(output)}")

def t9(outputs, numstring):

    if numstring == "":
        return outputs

    digit = int(numstring[0])
    newList = []
    options = letters[digit]
    if outputs == []:
        return t9(options, numstring[1:])
    for opt in options:
        
        t = list(outputs)
        for i in range(len(outputs)):
            t[i] = t[i] + opt

            # print([y += opt for y in outputs])
        newList.extend(t)
    return t9(newList, numstring[1:])




main()