def draw_square(size):
    size = 0 if size < 0 else size
    sq = ""
    for i in range(0, size):
        if i == 0 or i == size-1:
            sq += "x"*size
            if i == 0:
                sq += "\n"
        else:
            # remove 2 used for edges
            sq+= "x"+" "*(size-2)+"x\n"
    #print sq
    return sq

def combine_strings(ss):
    s1, s2 = ss
    res = list(s1);
    
    for i in range(0, len(s2)):
        if (s1[i] == 'x' or s2[i] == 'x'):
            res[i] = 'x'
        else:        
            res[i] =' '
    
    return "".join(res)


def draw_two(sizes):
    # assume first element is larger
    s1, s2 = sizes
    sq1 = draw_square(s1).split("\n")
    sq2 = draw_square(s2).split("\n")
    res = sq1;
    
    for i in range(0, len(sq2)):
        res[i] = combine_strings([sq1[i],sq2[i]])
    
    sqs = "";
    for line in res:
        sqs += line + "\n"
    
    print sqs[0:len(sqs)];
    return sqs[0:len(sqs)-1];

def draw_on_top(drawing, newSize):
    s1 = drawing 
    s2 = newSize

    sq1 = drawing.split("\n") 
    sq2 = draw_square(s2).split("\n")
    res = sq1;
    
    for i in range(0, len(sq2)):
        res[i] = combine_strings([sq1[i],sq2[i]])
    
    sqs = "";
    for line in res:
        sqs += line + "\n"
    
    print sqs[0:len(sqs)];
    return sqs[0:len(sqs)-1];
    
def draw_n(sizes):
    if  len(sizes) == 0: 
        return ""
    if len(sizes) == 1:
        return draw_square(sizes[0]);
    
    szs = sorted(sizes, reverse=True);
    drawing = draw_square(szs[0]);
    
    for i in range(1, len(szs)):
        print drawing
        drawing = draw_on_top(drawing, szs[i]) 
        
    print drawing;
    return drawing;