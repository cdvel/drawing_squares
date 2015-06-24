from nose.tools import *
from drawing import *

sq_four = "xxxx\nx  x\nx  x\nxxxx";
sq_seven = "xxxxxxx\nx     x\nx     x\nx     x\nx     x\nx     x\nxxxxxxx";

def test_zero():
    assert draw_square(0) == ""
 
def test_edge(): 
    assert draw_square(1) == "x\n"   
    
def test_draw_filled():
    assert draw_square(2) == "xx\nxx"   
    
def test_draw_unfilled():
    assert draw_square(4) == sq_four  

def test_combine():
    assert combine_strings(["x     x", "x  x"]) == "x  x  x";
    
def test_draw_two_top(): 
    assert draw_square(4) == sq_four 
    assert draw_square(7) == sq_seven
    assert draw_two([7,4]) == "xxxxxxx\nx  x  x\nx  x  x\nxxxx  x\nx     x\nx     x\nxxxxxxx"
    
def test_draw_n_top():     
    assert draw_n([7,4]) == "xxxxxxx\nx  x  x\nx  x  x\nxxxx  x\nx     x\nx     x\nxxxxxxx"
    assert draw_n([12,7,4]) == "xxxxxxxxxxxx\nx  x  x    x\nx  x  x    x\nxxxx  x    x\nx     x    x\nx     x    x\nxxxxxxx    x\nx          x\nx          x\nx          x\nx          x\nxxxxxxxxxxxx"