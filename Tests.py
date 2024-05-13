import sys
import unittest
from io import StringIO
from antlr4 import *
import json

from flask import jsonify

from antlr.AMMScriptLexer import AMMScriptLexer
from antlr.AMMScriptParser import AMMScriptParser
from AMMScript import interpret

class TestAMMScriptParser(unittest.TestCase):
    def setUp(self):
        self.lexer = AMMScriptLexer(input)
        self.stream = CommonTokenStream(self.lexer)
        self.parser = AMMScriptParser(self.stream)

    def getInterpretedCode(self, code):
        captured_output = StringIO()
        sys.stdout = captured_output
        interpret(code)

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()

        lines = output.split('\n')

        last_line = lines[-1]

        return last_line



    def getExecutedCode(self, code):
        result = interpret(code)
        return result


    def test_print(self):
        code = """
        print 3;
        print "Hello World!";
        print true;
        print false;
        """
        expected_output = [3, 'Hello World!', True, False]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_true(self):
        code = """
        print true;
        """
        expected_output1 = [True]
        expected_output2 = [False]
        self.assertEqual(self.getExecutedCode(code), expected_output1)
        self.assertNotEqual(self.getExecutedCode(code), expected_output2)

    def test_false(self):
        code = """
        print false;
        """
        expected_output1 = [False]
        expected_output2 = [True]
        self.assertEqual(self.getExecutedCode(code), expected_output1)
        self.assertNotEqual(self.getExecutedCode(code), expected_output2)

    def test_expr_plus_minus(self):
        code = """
        set x = 1;
        set y = -2;
        print x + 3 - y;
        print 10 - 2 + 3;
        """
        expected_output = [6, 11]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_expr_and_or(self):
        code = """
        print true and (false or true);
        print false and false;
        print false and true;
        print true and true;
        print true or false;
        print true or true;
        print false or false;
        """
        expected_output = [True, False, False, True, True, True, False]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_expr_mult_div_mod(self):
        code = """
        set x = 10;
        set y = 5;
        print x / 2;
        print y * 4;
        print y % 3;
        """

        expected_output = [5, 20, 2]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_variable_declaration(self):
        code = """
        set x = 10;
        set y = 20;
        print x;
        print y;
        """
        expected_output = [10, 20]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_expr_comparison(self):
        code = """
        set x = 5;
        set y = 6;
        print x < 10 and y >= 5;
        print x <= y;
        print y > 20;
        """
        expected_output = [True, True, False]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_variable_assignment(self):
        code = """
        set x = 10;
        x = 16;
        x = 20;
        x = 29;
        print x;
        """
        expected_output = [29]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_if(self):
        code = """"
        set x = 10;
        if (x > 5) { x = 9; } else { print x = 0; })
        print x;
        """
        expected_output = [9]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_switch(self):
        code = """
        set x = 2;
        switch (x) {
            case 1:
                x = 10;
                break;
            case 2:
                x = 20;
                break;
            default:
                x = 0;
        }
        print x;
        """
        expected_output = [20]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_while(self):
        code = """
        int i = 0;
        while (i < 5) {
            i = i + 1;
            print i;
        }
        """

        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_bubble_sort(self):
        code = """
        set a[5] = [4, 12, 5, 6, 2];
        set temp = -1;
        for set i=0;i<4;i=i+1 {
          for set j=0;j<4-i;j=j+1 {
            if a[j] > a[j + 1] {
              temp = a[j];
              a[j] = a[j + 1];
              a[j + 1] = temp;
            }
          }
        }
        
        for set k=0;k < 5;k = k + 1 {
        print a[k];
        }"""

        expected_output = [2, 4, 5, 6, 12]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_string(self):
        code = """
        print "Hello, people!";
        print "Nice to see you.";
        print "end";
        print "!";
        """
        expected_output = ["Hello, people!", "Nice to see you.", "end", "!"]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_expr_power(self):
        code = """
        print 2 ^ 3;
        print 3 ^ 2;
        print 3 ^ 1;
        print 11 ^ 0;
        print 2 ^ 0;
        print 4 ^ 4;
        print -2 ^ 0;
        print -2 ^ 2;
        print "napis" ^ 2;
        """
        expected_output = [8, 9, 3, 1, 1, 256, 1, 4, 'Nie można wykonać operacji potęgowania na napisach']
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_exp_parenthesis(self):
        code = """
        print (3 + 2) * 4;
        print 28 - (-3);
        print 3 ^ (2 + 1)
        """
        expected_output = [20, 31, 27]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_visit_array(self):
        code = """
        set a[4] = [1, 2, 3, -20];
        print a[0];
        print a[1];
        print a[2]; 
        print a[3]
        """
        expected_output = [1, 2, 3, -20]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_function_declaration(self):
        code = """
        func add(a, b) {
            return a + b;
        }
        print add(2,3);
        """
        expected_output = [5]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_if_in_loop(self):
        code = """
        set i = 0;
        while (i < 4) {
        print i;
            if (i % 2 == 0) {
                print "is even";
            } else {
                print "is odd";
            }
            i = i + 1;
        }
        """
        expected_output = [0, 'is even', 1, 'is odd', 2, 'is even', 3, 'is odd']
        self.assertEqual(self.getExecutedCode(code), expected_output)

if __name__ == '__main__':
    unittest.main()
