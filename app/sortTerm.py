class sortTerm():

    def sortTerm(self,box):
        #sort term
        term = []
        one =[]
        two =[]
        for i in box:
            if i[0] == "1":
                one.append(i)
            elif i[0] == "2":
                two.append(i)
        one.sort()
        two.sort()
        print(one)
        print(two)
        o = ""
        t = ""
        while (one != [] or two != []):
            if o == "":
                if one != []:
                    o = one.pop()
            if t == "":
                if two != []:
                    t = two.pop()
            print(one)
            print(two)
            if t[2:] >= o[2:] :
                term.append(t)
                t = ""
            elif o[2:] > t[2:]:
                term.append(o)
                o = ""
            if one == [] and two == [] :
                if o != "" :
                    term.append(o)
                    o = ""
                elif t != "" :
                    term.append(t)
                    t = ""
        print(term)
        return term
