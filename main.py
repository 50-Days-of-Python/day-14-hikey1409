def flat_list(l):
    # input nested list is stored in l
    # Insert Code below
    sdl=[]
    for i in l:
        if type(i) == list:
            sdl.extend(flat_list(i))
        else:
            sdl.append(i)    
    # Insert Code Above
    # Return single-dimension list.
    return sdl
