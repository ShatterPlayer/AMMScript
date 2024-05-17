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
        print x;
        """
        expected_output = [3, 'Hello World!', True, False, "Próba wypisania niezadeklarowanej wartości."]
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
        print false && false;
        print false && true;
        print true && true;
        print true || false;
        print true || true;
        print false || false;
        print "napis" && true;
        """
        expected_output = [False, False, True, True, True, False, "Operacje logiczne mogą być wykonywane tylko na typach bool"]
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
        print x <= y;
        print y > 20;
        print 3 > true;
        """
        expected_output = [True, False, "Nie można porównać wartości różnych typów"]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_variable_assignment(self):
        code = """
        set x = 10;
        x = 16;
        x = 20;
        x = 29;
        print x;
        print z;
        """
        expected_output = [29, "Próba wypisania niezadeklarowanej wartości."]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_if(self):
        code = """"
        set x = 10;
        if (x > 5) {
            x = 9;
        } else {
            x = 0;
        }
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

    def test_for(self):
        code = """
        for set i = 0; i < 21; i = i + 1 {
            print i;
        }
        """
        expected_output = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_while(self):
        code = """
        set i = 0;
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

    def test_visit_array(self):
        code = """
        set my_array[4] = [1, 2, 3, -20];
        print my_array[0];
        
        set my_other_array[5] = [0,1,2,3,4];
        for set i = 0; i < 5; i = i + 1{
        print my_other_array[i];
        }        
        
        """
        expected_output = [1, 0, 1, 2, 3, 4]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_function(self):
        code = """
        func add(a, b) {
            return a + b;
        }
        print add(2,3);
        print add(2,3,4);
            
        """
        expected_output = [5, f'Niewłaściwa liczba przekazanych parametrów do funkcji add.']
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

    def test_variable_in_for(self):
        code = """
        func fun() {
            for set i = 0; i < 2; i = i + 1 {
            set x = 5;
            return i + 1; 
            }
        } 
        
        print x;
        """
        expected_output = ["Próba wypisania niezadeklarowanej wartości."]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_loop_in_function(self):
        code = """
        func subtract_every_other(number) {
            set result = 0;
            for set i = 1; i < number + 1; i = i + 1 {
                for set j = 1; j < i + 1; j = j + 1 {
                    result = result - 1;
                }
            }
            return result;
        }
        
        print subtract_every_other(5);
        
        func substract_every_third(number) {
                set result = 0;
                set i = 1;
                while (i <= number) {
                    set j = 1;
                    while (j <= i && i % 3 == 0) {
                        result = result - 1; 
                        j = j + 1;
                    }
                    i = i + 1;
                }
                return result;
            }
        
        
        print substract_every_third(10);
        """
        expected_output = [-15, -18]
        self.assertEqual(self.getExecutedCode(code), expected_output)


    def test_switch_in_function(self):
        code = """
        func fun(x) {
            switch (x) {
                case 1:
                    set x = 10;
                    return x;
                    break;
                case 2:
                    set x = 15;
                    return x;
                    break;
                default:
                    set x = 0;
                    return x;
            }
        }
        
        print fun(2);
        """
        expected_output = [15]
        self.assertEqual(self.getExecutedCode(code), expected_output)

        def test_default_arguments_in_function(self):
            code = """
            func fun(x) {
                switch (x) {
                    case 1:
                        set x = 10;
                        return x;
                        break;
                    case 2:
                        set x = 15;
                        return x;
                        break;
                    default:
                        set x = 0;
                        return x;
                }
            }

            print fun(2);
            print fun();
            """
            expected_output = [15, 0]
            self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_recursion_in_function(self):
        code = """
        func factorial(n) {
            if (n == 0) {
                return 1; 
            } else {
                return n * factorial(n - 1); 
            }
        }

        print factorial(5); 
        """
        expected_output = [120]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_scoping(self):
        code = """
        func test(a, b = 1) {
            a = a + 1;
            print a;
            set c = 3;
            return a + b;
        }
        
        print c;
        """
        expected_output = ["Próba wypisania niezadeklarowanej wartości."]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_local_variable_in_function(self):
        code = """
        func myFunc() {
            set y = 20;
            return y;
        }    
        print myFunc();
        print y;
        """
        expected_output = [20, "Próba wypisania niezadeklarowanej wartości."]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_global_variable_in_function(self):
        code = """
        set x = 10;
        func myFunc() {
            return x;
        }    
        print myFunc();
        """
        expected_output = [10]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_local_and_global_variable(self):
        code = """
        set x = 10;
        func myFunc() {
            set x = 20;
            return x;
        }    
        print myFunc();
        print x;
        """
        expected_output = [20, 10]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_function_scope(self):
        code = """
        func innerFunc() {
            set x = 20;
            return x;
        }       
        
        func outerFunc() {
            set x = 30;
            print innerFunc();
            return x;
        }    
        
        print outerFunc();
        """
        expected_output = [20, 30]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_function_scope2(self):
        code = """
        func innerFunc() {
            set x = 50;
            return x;
        }         
            
        func outerFunc() {
            set x = 40; 
            print innerFunc();
            return x;
        }
        
        print outerFunc();
        print x;
        """
        expected_output = [50, 40, "Próba wypisania niezadeklarowanej wartości."]
        self.assertEqual(self.getExecutedCode(code), expected_output)

    def test_function_with_default_parameters(self):
        code = """
        func myFunc(a, b=5) {
            return a + b;
        }
        print myFunc(10);
        """
        expected_output = [15]
        self.assertEqual(self.getExecutedCode(code), expected_output)

if __name__ == '__main__':
    unittest.main()
