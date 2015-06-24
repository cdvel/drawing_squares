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
    
def test_draw_two_top():
    assert draw_square(4) == sq_four 
    assert draw_square(7) == sq_seven   
    assert draw_top([7,4]) == sq_four + sq_seven[len(sq_four):]   

    #assert draw_top([7,4]) == "xxxx\nx  x\nx  x\nxxxx  x\nx     x\nx     x\nx     x\nxxxxxxx"
