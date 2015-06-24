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
    
def draw_top(sizes):
    if len(sizes) == 0: return "";
    drawing = ""
    
    for i in range(0, len(sizes)):
        
        sq_bottom = draw_square(sizes[i])[len(drawing):]
        if drawing == "":
            drawing = draw_square(sizes[i])
        else:
            drawing = draw_square(sizes[i]) + drawing[len(drawing):]
        # if drawing >= sizes and i > 0: 
            # drawing = drawing[sizes[i]:]
    print drawing
    return drawing
