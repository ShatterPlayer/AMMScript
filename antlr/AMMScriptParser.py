# Generated from ./AMMScriptParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,553,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,5,0,50,8,0,10,0,12,0,53,9,
        0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,76,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,98,8,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,122,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,147,
        8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,161,8,5,
        10,5,12,5,164,9,5,3,5,166,8,5,1,5,3,5,169,8,5,1,6,1,6,1,6,1,6,3,
        6,175,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,187,8,8,10,
        8,12,8,190,9,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,198,8,8,10,8,12,8,201,
        9,8,1,8,1,8,5,8,205,8,8,10,8,12,8,208,9,8,1,8,1,8,1,8,5,8,213,8,
        8,10,8,12,8,216,9,8,1,8,3,8,219,8,8,1,9,1,9,1,9,1,9,5,9,225,8,9,
        10,9,12,9,228,9,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,236,8,9,10,9,12,9,
        239,9,9,1,9,1,9,5,9,243,8,9,10,9,12,9,246,9,9,1,9,1,9,1,9,5,9,251,
        8,9,10,9,12,9,254,9,9,1,9,3,9,257,8,9,1,10,1,10,1,10,1,10,5,10,263,
        8,10,10,10,12,10,266,9,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,274,
        8,10,10,10,12,10,277,9,10,1,10,1,10,5,10,281,8,10,10,10,12,10,284,
        9,10,1,10,1,10,1,10,5,10,289,8,10,10,10,12,10,292,9,10,1,10,3,10,
        295,8,10,1,11,1,11,1,11,1,11,5,11,301,8,11,10,11,12,11,304,9,11,
        1,11,1,11,1,11,1,11,1,11,1,11,5,11,312,8,11,10,11,12,11,315,9,11,
        1,11,1,11,5,11,319,8,11,10,11,12,11,322,9,11,1,11,1,11,1,11,5,11,
        327,8,11,10,11,12,11,330,9,11,1,11,3,11,333,8,11,1,12,1,12,3,12,
        337,8,12,1,13,1,13,3,13,341,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,5,14,351,8,14,10,14,12,14,354,9,14,1,14,1,14,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,5,15,366,8,15,10,15,12,15,369,9,15,1,
        15,1,15,1,16,1,16,1,16,1,16,5,16,377,8,16,10,16,12,16,380,9,16,1,
        16,1,16,1,17,1,17,1,17,1,17,5,17,388,8,17,10,17,12,17,391,9,17,1,
        17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,402,8,18,10,18,12,
        18,405,9,18,1,18,1,18,3,18,409,8,18,5,18,411,8,18,10,18,12,18,414,
        9,18,1,18,1,18,1,18,5,18,419,8,18,10,18,12,18,422,9,18,1,18,1,18,
        3,18,426,8,18,3,18,428,8,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,5,19,439,8,19,10,19,12,19,442,9,19,1,19,1,19,3,19,446,8,
        19,5,19,448,8,19,10,19,12,19,451,9,19,1,19,1,19,1,19,5,19,456,8,
        19,10,19,12,19,459,9,19,1,19,1,19,3,19,463,8,19,3,19,465,8,19,1,
        19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,3,20,475,8,20,1,20,1,20,1,
        20,1,20,3,20,481,8,20,5,20,483,8,20,10,20,12,20,486,9,20,3,20,488,
        8,20,1,20,1,20,1,20,5,20,493,8,20,10,20,12,20,496,9,20,1,20,1,20,
        1,21,1,21,1,21,1,21,1,21,5,21,505,8,21,10,21,12,21,508,9,21,3,21,
        510,8,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,531,8,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        5,23,548,8,23,10,23,12,23,551,9,23,1,23,0,1,46,24,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,5,1,0,21,25,
        2,0,28,29,31,31,1,0,26,27,1,0,15,20,1,0,42,43,624,0,51,1,0,0,0,2,
        75,1,0,0,0,4,97,1,0,0,0,6,121,1,0,0,0,8,146,1,0,0,0,10,148,1,0,0,
        0,12,170,1,0,0,0,14,179,1,0,0,0,16,182,1,0,0,0,18,220,1,0,0,0,20,
        258,1,0,0,0,22,296,1,0,0,0,24,336,1,0,0,0,26,340,1,0,0,0,28,342,
        1,0,0,0,30,357,1,0,0,0,32,372,1,0,0,0,34,383,1,0,0,0,36,394,1,0,
        0,0,38,431,1,0,0,0,40,468,1,0,0,0,42,499,1,0,0,0,44,513,1,0,0,0,
        46,530,1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,
        0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,1,55,
        1,1,0,0,0,56,57,3,10,5,0,57,58,5,47,0,0,58,76,1,0,0,0,59,60,3,12,
        6,0,60,61,5,47,0,0,61,76,1,0,0,0,62,63,3,14,7,0,63,64,5,47,0,0,64,
        76,1,0,0,0,65,66,3,42,21,0,66,67,5,47,0,0,67,76,1,0,0,0,68,69,3,
        46,23,0,69,70,5,47,0,0,70,76,1,0,0,0,71,76,3,16,8,0,72,76,3,24,12,
        0,73,76,3,40,20,0,74,76,3,36,18,0,75,56,1,0,0,0,75,59,1,0,0,0,75,
        62,1,0,0,0,75,65,1,0,0,0,75,68,1,0,0,0,75,71,1,0,0,0,75,72,1,0,0,
        0,75,73,1,0,0,0,75,74,1,0,0,0,76,3,1,0,0,0,77,78,3,10,5,0,78,79,
        5,47,0,0,79,98,1,0,0,0,80,81,3,12,6,0,81,82,5,47,0,0,82,98,1,0,0,
        0,83,84,3,14,7,0,84,85,5,47,0,0,85,98,1,0,0,0,86,87,3,42,21,0,87,
        88,5,47,0,0,88,98,1,0,0,0,89,90,3,46,23,0,90,91,5,47,0,0,91,98,1,
        0,0,0,92,98,3,18,9,0,93,98,3,24,12,0,94,98,5,10,0,0,95,98,5,11,0,
        0,96,98,3,36,18,0,97,77,1,0,0,0,97,80,1,0,0,0,97,83,1,0,0,0,97,86,
        1,0,0,0,97,89,1,0,0,0,97,92,1,0,0,0,97,93,1,0,0,0,97,94,1,0,0,0,
        97,95,1,0,0,0,97,96,1,0,0,0,98,5,1,0,0,0,99,100,3,10,5,0,100,101,
        5,47,0,0,101,122,1,0,0,0,102,103,3,12,6,0,103,104,5,47,0,0,104,122,
        1,0,0,0,105,106,3,14,7,0,106,107,5,47,0,0,107,122,1,0,0,0,108,109,
        3,42,21,0,109,110,5,47,0,0,110,122,1,0,0,0,111,112,3,46,23,0,112,
        113,5,47,0,0,113,122,1,0,0,0,114,122,3,20,10,0,115,122,3,26,13,0,
        116,117,5,9,0,0,117,118,3,46,23,0,118,119,5,47,0,0,119,122,1,0,0,
        0,120,122,3,38,19,0,121,99,1,0,0,0,121,102,1,0,0,0,121,105,1,0,0,
        0,121,108,1,0,0,0,121,111,1,0,0,0,121,114,1,0,0,0,121,115,1,0,0,
        0,121,116,1,0,0,0,121,120,1,0,0,0,122,7,1,0,0,0,123,124,3,10,5,0,
        124,125,5,47,0,0,125,147,1,0,0,0,126,127,3,12,6,0,127,128,5,47,0,
        0,128,147,1,0,0,0,129,130,3,14,7,0,130,131,5,47,0,0,131,147,1,0,
        0,0,132,133,3,42,21,0,133,134,5,47,0,0,134,147,1,0,0,0,135,136,3,
        46,23,0,136,137,5,47,0,0,137,147,1,0,0,0,138,147,3,22,11,0,139,147,
        3,26,13,0,140,147,5,10,0,0,141,147,5,11,0,0,142,143,5,9,0,0,143,
        144,3,46,23,0,144,145,5,47,0,0,145,147,1,0,0,0,146,123,1,0,0,0,146,
        126,1,0,0,0,146,129,1,0,0,0,146,132,1,0,0,0,146,135,1,0,0,0,146,
        138,1,0,0,0,146,139,1,0,0,0,146,140,1,0,0,0,146,141,1,0,0,0,146,
        142,1,0,0,0,147,9,1,0,0,0,148,149,5,2,0,0,149,168,5,49,0,0,150,151,
        5,21,0,0,151,169,3,46,23,0,152,153,5,36,0,0,153,154,5,38,0,0,154,
        155,5,37,0,0,155,156,5,21,0,0,156,165,5,36,0,0,157,162,3,46,23,0,
        158,159,5,46,0,0,159,161,3,46,23,0,160,158,1,0,0,0,161,164,1,0,0,
        0,162,160,1,0,0,0,162,163,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,
        0,165,157,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,169,5,37,0,
        0,168,150,1,0,0,0,168,152,1,0,0,0,169,11,1,0,0,0,170,174,5,49,0,
        0,171,172,5,36,0,0,172,173,5,38,0,0,173,175,5,37,0,0,174,171,1,0,
        0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,7,0,0,0,177,178,3,46,
        23,0,178,13,1,0,0,0,179,180,5,3,0,0,180,181,3,46,23,0,181,15,1,0,
        0,0,182,183,5,4,0,0,183,184,3,46,23,0,184,188,5,34,0,0,185,187,3,
        2,1,0,186,185,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,1,
        0,0,0,189,191,1,0,0,0,190,188,1,0,0,0,191,206,5,35,0,0,192,193,5,
        5,0,0,193,194,5,4,0,0,194,195,3,46,23,0,195,199,5,34,0,0,196,198,
        3,2,1,0,197,196,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,
        1,0,0,0,200,202,1,0,0,0,201,199,1,0,0,0,202,203,5,35,0,0,203,205,
        1,0,0,0,204,192,1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,206,207,
        1,0,0,0,207,218,1,0,0,0,208,206,1,0,0,0,209,210,5,5,0,0,210,214,
        5,34,0,0,211,213,3,2,1,0,212,211,1,0,0,0,213,216,1,0,0,0,214,212,
        1,0,0,0,214,215,1,0,0,0,215,217,1,0,0,0,216,214,1,0,0,0,217,219,
        5,35,0,0,218,209,1,0,0,0,218,219,1,0,0,0,219,17,1,0,0,0,220,221,
        5,4,0,0,221,222,3,46,23,0,222,226,5,34,0,0,223,225,3,4,2,0,224,223,
        1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,227,229,
        1,0,0,0,228,226,1,0,0,0,229,244,5,35,0,0,230,231,5,5,0,0,231,232,
        5,4,0,0,232,233,3,46,23,0,233,237,5,34,0,0,234,236,3,4,2,0,235,234,
        1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,240,
        1,0,0,0,239,237,1,0,0,0,240,241,5,35,0,0,241,243,1,0,0,0,242,230,
        1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,256,
        1,0,0,0,246,244,1,0,0,0,247,248,5,5,0,0,248,252,5,34,0,0,249,251,
        3,4,2,0,250,249,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,253,
        1,0,0,0,253,255,1,0,0,0,254,252,1,0,0,0,255,257,5,35,0,0,256,247,
        1,0,0,0,256,257,1,0,0,0,257,19,1,0,0,0,258,259,5,4,0,0,259,260,3,
        46,23,0,260,264,5,34,0,0,261,263,3,6,3,0,262,261,1,0,0,0,263,266,
        1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,267,1,0,0,0,266,264,
        1,0,0,0,267,282,5,35,0,0,268,269,5,5,0,0,269,270,5,4,0,0,270,271,
        3,46,23,0,271,275,5,34,0,0,272,274,3,6,3,0,273,272,1,0,0,0,274,277,
        1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,278,1,0,0,0,277,275,
        1,0,0,0,278,279,5,35,0,0,279,281,1,0,0,0,280,268,1,0,0,0,281,284,
        1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,283,294,1,0,0,0,284,282,
        1,0,0,0,285,286,5,5,0,0,286,290,5,34,0,0,287,289,3,6,3,0,288,287,
        1,0,0,0,289,292,1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,0,291,293,
        1,0,0,0,292,290,1,0,0,0,293,295,5,35,0,0,294,285,1,0,0,0,294,295,
        1,0,0,0,295,21,1,0,0,0,296,297,5,4,0,0,297,298,3,46,23,0,298,302,
        5,34,0,0,299,301,3,8,4,0,300,299,1,0,0,0,301,304,1,0,0,0,302,300,
        1,0,0,0,302,303,1,0,0,0,303,305,1,0,0,0,304,302,1,0,0,0,305,320,
        5,35,0,0,306,307,5,5,0,0,307,308,5,4,0,0,308,309,3,46,23,0,309,313,
        5,34,0,0,310,312,3,8,4,0,311,310,1,0,0,0,312,315,1,0,0,0,313,311,
        1,0,0,0,313,314,1,0,0,0,314,316,1,0,0,0,315,313,1,0,0,0,316,317,
        5,35,0,0,317,319,1,0,0,0,318,306,1,0,0,0,319,322,1,0,0,0,320,318,
        1,0,0,0,320,321,1,0,0,0,321,332,1,0,0,0,322,320,1,0,0,0,323,324,
        5,5,0,0,324,328,5,34,0,0,325,327,3,8,4,0,326,325,1,0,0,0,327,330,
        1,0,0,0,328,326,1,0,0,0,328,329,1,0,0,0,329,331,1,0,0,0,330,328,
        1,0,0,0,331,333,5,35,0,0,332,323,1,0,0,0,332,333,1,0,0,0,333,23,
        1,0,0,0,334,337,3,28,14,0,335,337,3,32,16,0,336,334,1,0,0,0,336,
        335,1,0,0,0,337,25,1,0,0,0,338,341,3,30,15,0,339,341,3,34,17,0,340,
        338,1,0,0,0,340,339,1,0,0,0,341,27,1,0,0,0,342,343,5,6,0,0,343,344,
        3,10,5,0,344,345,5,47,0,0,345,346,3,46,23,0,346,347,5,47,0,0,347,
        348,3,12,6,0,348,352,5,34,0,0,349,351,3,4,2,0,350,349,1,0,0,0,351,
        354,1,0,0,0,352,350,1,0,0,0,352,353,1,0,0,0,353,355,1,0,0,0,354,
        352,1,0,0,0,355,356,5,35,0,0,356,29,1,0,0,0,357,358,5,6,0,0,358,
        359,3,10,5,0,359,360,5,47,0,0,360,361,3,46,23,0,361,362,5,47,0,0,
        362,363,3,12,6,0,363,367,5,34,0,0,364,366,3,8,4,0,365,364,1,0,0,
        0,366,369,1,0,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,370,1,0,0,
        0,369,367,1,0,0,0,370,371,5,35,0,0,371,31,1,0,0,0,372,373,5,7,0,
        0,373,374,3,46,23,0,374,378,5,34,0,0,375,377,3,4,2,0,376,375,1,0,
        0,0,377,380,1,0,0,0,378,376,1,0,0,0,378,379,1,0,0,0,379,381,1,0,
        0,0,380,378,1,0,0,0,381,382,5,35,0,0,382,33,1,0,0,0,383,384,5,7,
        0,0,384,385,3,46,23,0,385,389,5,34,0,0,386,388,3,8,4,0,387,386,1,
        0,0,0,388,391,1,0,0,0,389,387,1,0,0,0,389,390,1,0,0,0,390,392,1,
        0,0,0,391,389,1,0,0,0,392,393,5,35,0,0,393,35,1,0,0,0,394,395,5,
        12,0,0,395,396,3,46,23,0,396,412,5,34,0,0,397,398,5,13,0,0,398,399,
        3,46,23,0,399,403,5,48,0,0,400,402,3,2,1,0,401,400,1,0,0,0,402,405,
        1,0,0,0,403,401,1,0,0,0,403,404,1,0,0,0,404,408,1,0,0,0,405,403,
        1,0,0,0,406,407,5,10,0,0,407,409,5,47,0,0,408,406,1,0,0,0,408,409,
        1,0,0,0,409,411,1,0,0,0,410,397,1,0,0,0,411,414,1,0,0,0,412,410,
        1,0,0,0,412,413,1,0,0,0,413,427,1,0,0,0,414,412,1,0,0,0,415,416,
        5,14,0,0,416,420,5,48,0,0,417,419,3,2,1,0,418,417,1,0,0,0,419,422,
        1,0,0,0,420,418,1,0,0,0,420,421,1,0,0,0,421,425,1,0,0,0,422,420,
        1,0,0,0,423,424,5,10,0,0,424,426,5,47,0,0,425,423,1,0,0,0,425,426,
        1,0,0,0,426,428,1,0,0,0,427,415,1,0,0,0,427,428,1,0,0,0,428,429,
        1,0,0,0,429,430,5,35,0,0,430,37,1,0,0,0,431,432,5,12,0,0,432,433,
        3,46,23,0,433,449,5,34,0,0,434,435,5,13,0,0,435,436,3,46,23,0,436,
        440,5,48,0,0,437,439,3,6,3,0,438,437,1,0,0,0,439,442,1,0,0,0,440,
        438,1,0,0,0,440,441,1,0,0,0,441,445,1,0,0,0,442,440,1,0,0,0,443,
        444,5,10,0,0,444,446,5,47,0,0,445,443,1,0,0,0,445,446,1,0,0,0,446,
        448,1,0,0,0,447,434,1,0,0,0,448,451,1,0,0,0,449,447,1,0,0,0,449,
        450,1,0,0,0,450,464,1,0,0,0,451,449,1,0,0,0,452,453,5,14,0,0,453,
        457,5,48,0,0,454,456,3,6,3,0,455,454,1,0,0,0,456,459,1,0,0,0,457,
        455,1,0,0,0,457,458,1,0,0,0,458,462,1,0,0,0,459,457,1,0,0,0,460,
        461,5,10,0,0,461,463,5,47,0,0,462,460,1,0,0,0,462,463,1,0,0,0,463,
        465,1,0,0,0,464,452,1,0,0,0,464,465,1,0,0,0,465,466,1,0,0,0,466,
        467,5,35,0,0,467,39,1,0,0,0,468,469,5,8,0,0,469,470,5,49,0,0,470,
        487,5,32,0,0,471,474,5,49,0,0,472,473,5,21,0,0,473,475,3,46,23,0,
        474,472,1,0,0,0,474,475,1,0,0,0,475,484,1,0,0,0,476,477,5,46,0,0,
        477,480,5,49,0,0,478,479,5,21,0,0,479,481,3,46,23,0,480,478,1,0,
        0,0,480,481,1,0,0,0,481,483,1,0,0,0,482,476,1,0,0,0,483,486,1,0,
        0,0,484,482,1,0,0,0,484,485,1,0,0,0,485,488,1,0,0,0,486,484,1,0,
        0,0,487,471,1,0,0,0,487,488,1,0,0,0,488,489,1,0,0,0,489,490,5,33,
        0,0,490,494,5,34,0,0,491,493,3,6,3,0,492,491,1,0,0,0,493,496,1,0,
        0,0,494,492,1,0,0,0,494,495,1,0,0,0,495,497,1,0,0,0,496,494,1,0,
        0,0,497,498,5,35,0,0,498,41,1,0,0,0,499,500,5,49,0,0,500,509,5,32,
        0,0,501,506,3,46,23,0,502,503,5,46,0,0,503,505,3,46,23,0,504,502,
        1,0,0,0,505,508,1,0,0,0,506,504,1,0,0,0,506,507,1,0,0,0,507,510,
        1,0,0,0,508,506,1,0,0,0,509,501,1,0,0,0,509,510,1,0,0,0,510,511,
        1,0,0,0,511,512,5,33,0,0,512,43,1,0,0,0,513,514,5,49,0,0,514,515,
        5,36,0,0,515,516,5,38,0,0,516,517,5,37,0,0,517,45,1,0,0,0,518,519,
        6,23,-1,0,519,520,5,32,0,0,520,521,3,46,23,0,521,522,5,33,0,0,522,
        531,1,0,0,0,523,531,5,38,0,0,524,531,5,39,0,0,525,531,5,40,0,0,526,
        531,5,41,0,0,527,531,3,42,21,0,528,531,3,44,22,0,529,531,5,49,0,
        0,530,518,1,0,0,0,530,523,1,0,0,0,530,524,1,0,0,0,530,525,1,0,0,
        0,530,526,1,0,0,0,530,527,1,0,0,0,530,528,1,0,0,0,530,529,1,0,0,
        0,531,549,1,0,0,0,532,533,10,12,0,0,533,534,5,30,0,0,534,548,3,46,
        23,13,535,536,10,11,0,0,536,537,7,1,0,0,537,548,3,46,23,12,538,539,
        10,10,0,0,539,540,7,2,0,0,540,548,3,46,23,11,541,542,10,9,0,0,542,
        543,7,3,0,0,543,548,3,46,23,10,544,545,10,8,0,0,545,546,7,4,0,0,
        546,548,3,46,23,9,547,532,1,0,0,0,547,535,1,0,0,0,547,538,1,0,0,
        0,547,541,1,0,0,0,547,544,1,0,0,0,548,551,1,0,0,0,549,547,1,0,0,
        0,549,550,1,0,0,0,550,47,1,0,0,0,551,549,1,0,0,0,57,51,75,97,121,
        146,162,165,168,174,188,199,206,214,218,226,237,244,252,256,264,
        275,282,290,294,302,313,320,328,332,336,340,352,367,378,389,403,
        408,412,420,425,427,440,445,449,457,462,464,474,480,484,487,494,
        506,509,530,547,549
    ]

class AMMScriptParser ( Parser ):

    grammarFileName = "AMMScriptParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'set'", "'print'", "'if'", 
                     "'else'", "'for'", "'while'", "'func'", "'return'", 
                     "'break'", "'continue'", "'switch'", "'case'", "'default'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", 
                     "'+='", "'-='", "'*='", "'/='", "'+'", "'-'", "'*'", 
                     "'/'", "'^'", "'%'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "<INVALID>", "<INVALID>", "'true'", "'false'", 
                     "'&&'", "'||'", "'!'", "<INVALID>", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "SET", "PRINT", "IF", "ELSE", 
                      "FOR", "WHILE", "FUNCTION", "RETURN", "BREAK", "CONTINUE", 
                      "SWITCH", "CASE", "DEFAULT", "EQUAL_EQUAL", "NOT_EQUAL", 
                      "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
                      "EQUAL", "PLUS_EQUAL", "MINUS_EQUAL", "MULTIPLY_EQUAL", 
                      "DIVIDE_EQUAL", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                      "POWER", "MODULO", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "NUMBER", "STRING", "TRUE", 
                      "FALSE", "AND", "OR", "NOT", "COMMENT", "COMMA", "SEMICOLON", 
                      "COLON", "ID" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_statementInLoop = 2
    RULE_statementInFunction = 3
    RULE_statementInFunctionAndLoop = 4
    RULE_variableDeclaration = 5
    RULE_variableAsignment = 6
    RULE_print = 7
    RULE_if = 8
    RULE_ifInLoop = 9
    RULE_ifInFunction = 10
    RULE_ifInFunctionAndLoop = 11
    RULE_loop = 12
    RULE_loopInFunction = 13
    RULE_forLoop = 14
    RULE_forLoopInFunction = 15
    RULE_whileLoop = 16
    RULE_whileLoopInFunction = 17
    RULE_switch = 18
    RULE_switchInFunction = 19
    RULE_functionDeclaration = 20
    RULE_functionCall = 21
    RULE_arrayExpr = 22
    RULE_expr = 23

    ruleNames =  [ "program", "statement", "statementInLoop", "statementInFunction", 
                   "statementInFunctionAndLoop", "variableDeclaration", 
                   "variableAsignment", "print", "if", "ifInLoop", "ifInFunction", 
                   "ifInFunctionAndLoop", "loop", "loopInFunction", "forLoop", 
                   "forLoopInFunction", "whileLoop", "whileLoopInFunction", 
                   "switch", "switchInFunction", "functionDeclaration", 
                   "functionCall", "arrayExpr", "expr" ]

    EOF = Token.EOF
    WHITESPACE=1
    SET=2
    PRINT=3
    IF=4
    ELSE=5
    FOR=6
    WHILE=7
    FUNCTION=8
    RETURN=9
    BREAK=10
    CONTINUE=11
    SWITCH=12
    CASE=13
    DEFAULT=14
    EQUAL_EQUAL=15
    NOT_EQUAL=16
    LESS=17
    GREATER=18
    LESS_EQUAL=19
    GREATER_EQUAL=20
    EQUAL=21
    PLUS_EQUAL=22
    MINUS_EQUAL=23
    MULTIPLY_EQUAL=24
    DIVIDE_EQUAL=25
    PLUS=26
    MINUS=27
    MULTIPLY=28
    DIVIDE=29
    POWER=30
    MODULO=31
    LPAREN=32
    RPAREN=33
    LBRACE=34
    RBRACE=35
    LBRACKET=36
    RBRACKET=37
    NUMBER=38
    STRING=39
    TRUE=40
    FALSE=41
    AND=42
    OR=43
    NOT=44
    COMMENT=45
    COMMA=46
    SEMICOLON=47
    COLON=48
    ID=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AMMScriptParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return AMMScriptParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AMMScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997340) != 0):
                self.state = 48
                self.statement()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(AMMScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableDeclarationContext,0)


        def SEMICOLON(self):
            return self.getToken(AMMScriptParser.SEMICOLON, 0)

        def variableAsignment(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableAsignmentContext,0)


        def print_(self):
            return self.getTypedRuleContext(AMMScriptParser.PrintContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(AMMScriptParser.FunctionCallContext,0)


        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)


        def if_(self):
            return self.getTypedRuleContext(AMMScriptParser.IfContext,0)


        def loop(self):
            return self.getTypedRuleContext(AMMScriptParser.LoopContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(AMMScriptParser.FunctionDeclarationContext,0)


        def switch(self):
            return self.getTypedRuleContext(AMMScriptParser.SwitchContext,0)


        def getRuleIndex(self):
            return AMMScriptParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = AMMScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.variableDeclaration()
                self.state = 57
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.variableAsignment()
                self.state = 60
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.print_()
                self.state = 63
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.functionCall()
                self.state = 66
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.expr(0)
                self.state = 69
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.if_()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 73
                self.functionDeclaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 74
                self.switch()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementInLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableDeclarationContext,0)


        def SEMICOLON(self):
            return self.getToken(AMMScriptParser.SEMICOLON, 0)

        def variableAsignment(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableAsignmentContext,0)


        def print_(self):
            return self.getTypedRuleContext(AMMScriptParser.PrintContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(AMMScriptParser.FunctionCallContext,0)


        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)


        def ifInLoop(self):
            return self.getTypedRuleContext(AMMScriptParser.IfInLoopContext,0)


        def loop(self):
            return self.getTypedRuleContext(AMMScriptParser.LoopContext,0)


        def BREAK(self):
            return self.getToken(AMMScriptParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(AMMScriptParser.CONTINUE, 0)

        def switch(self):
            return self.getTypedRuleContext(AMMScriptParser.SwitchContext,0)


        def getRuleIndex(self):
            return AMMScriptParser.RULE_statementInLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementInLoop" ):
                return visitor.visitStatementInLoop(self)
            else:
                return visitor.visitChildren(self)




    def statementInLoop(self):

        localctx = AMMScriptParser.StatementInLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statementInLoop)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.variableDeclaration()
                self.state = 78
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.variableAsignment()
                self.state = 81
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.print_()
                self.state = 84
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.functionCall()
                self.state = 87
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.expr(0)
                self.state = 90
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 92
                self.ifInLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 93
                self.loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 94
                self.match(AMMScriptParser.BREAK)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 95
                self.match(AMMScriptParser.CONTINUE)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 96
                self.switch()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementInFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableDeclarationContext,0)


        def SEMICOLON(self):
            return self.getToken(AMMScriptParser.SEMICOLON, 0)

        def variableAsignment(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableAsignmentContext,0)


        def print_(self):
            return self.getTypedRuleContext(AMMScriptParser.PrintContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(AMMScriptParser.FunctionCallContext,0)


        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)


        def ifInFunction(self):
            return self.getTypedRuleContext(AMMScriptParser.IfInFunctionContext,0)


        def loopInFunction(self):
            return self.getTypedRuleContext(AMMScriptParser.LoopInFunctionContext,0)


        def RETURN(self):
            return self.getToken(AMMScriptParser.RETURN, 0)

        def switchInFunction(self):
            return self.getTypedRuleContext(AMMScriptParser.SwitchInFunctionContext,0)


        def getRuleIndex(self):
            return AMMScriptParser.RULE_statementInFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementInFunction" ):
                return visitor.visitStatementInFunction(self)
            else:
                return visitor.visitChildren(self)




    def statementInFunction(self):

        localctx = AMMScriptParser.StatementInFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statementInFunction)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.variableDeclaration()
                self.state = 100
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.variableAsignment()
                self.state = 103
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.print_()
                self.state = 106
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 108
                self.functionCall()
                self.state = 109
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 111
                self.expr(0)
                self.state = 112
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 114
                self.ifInFunction()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 115
                self.loopInFunction()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 116
                self.match(AMMScriptParser.RETURN)
                self.state = 117
                self.expr(0)
                self.state = 118
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 120
                self.switchInFunction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementInFunctionAndLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableDeclarationContext,0)


        def SEMICOLON(self):
            return self.getToken(AMMScriptParser.SEMICOLON, 0)

        def variableAsignment(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableAsignmentContext,0)


        def print_(self):
            return self.getTypedRuleContext(AMMScriptParser.PrintContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(AMMScriptParser.FunctionCallContext,0)


        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)


        def ifInFunctionAndLoop(self):
            return self.getTypedRuleContext(AMMScriptParser.IfInFunctionAndLoopContext,0)


        def loopInFunction(self):
            return self.getTypedRuleContext(AMMScriptParser.LoopInFunctionContext,0)


        def BREAK(self):
            return self.getToken(AMMScriptParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(AMMScriptParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(AMMScriptParser.RETURN, 0)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_statementInFunctionAndLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementInFunctionAndLoop" ):
                return visitor.visitStatementInFunctionAndLoop(self)
            else:
                return visitor.visitChildren(self)




    def statementInFunctionAndLoop(self):

        localctx = AMMScriptParser.StatementInFunctionAndLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statementInFunctionAndLoop)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.variableDeclaration()
                self.state = 124
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.variableAsignment()
                self.state = 127
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.print_()
                self.state = 130
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.functionCall()
                self.state = 133
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.expr(0)
                self.state = 136
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 138
                self.ifInFunctionAndLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 139
                self.loopInFunction()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 140
                self.match(AMMScriptParser.BREAK)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 141
                self.match(AMMScriptParser.CONTINUE)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 142
                self.match(AMMScriptParser.RETURN)
                self.state = 143
                self.expr(0)
                self.state = 144
                self.match(AMMScriptParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(AMMScriptParser.SET, 0)

        def ID(self):
            return self.getToken(AMMScriptParser.ID, 0)

        def EQUAL(self):
            return self.getToken(AMMScriptParser.EQUAL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)


        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.LBRACKET)
            else:
                return self.getToken(AMMScriptParser.LBRACKET, i)

        def NUMBER(self):
            return self.getToken(AMMScriptParser.NUMBER, 0)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.RBRACKET)
            else:
                return self.getToken(AMMScriptParser.RBRACKET, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.COMMA)
            else:
                return self.getToken(AMMScriptParser.COMMA, i)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_variableDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = AMMScriptParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(AMMScriptParser.SET)
            self.state = 149
            self.match(AMMScriptParser.ID)
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 150
                self.match(AMMScriptParser.EQUAL)
                self.state = 151
                self.expr(0)
                pass
            elif token in [36]:
                self.state = 152
                self.match(AMMScriptParser.LBRACKET)
                self.state = 153
                self.match(AMMScriptParser.NUMBER)
                self.state = 154
                self.match(AMMScriptParser.RBRACKET)
                self.state = 155
                self.match(AMMScriptParser.EQUAL)
                self.state = 156
                self.match(AMMScriptParser.LBRACKET)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416992768) != 0):
                    self.state = 157
                    self.expr(0)
                    self.state = 162
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==46:
                        self.state = 158
                        self.match(AMMScriptParser.COMMA)
                        self.state = 159
                        self.expr(0)
                        self.state = 164
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 167
                self.match(AMMScriptParser.RBRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableAsignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AMMScriptParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)


        def EQUAL(self):
            return self.getToken(AMMScriptParser.EQUAL, 0)

        def PLUS_EQUAL(self):
            return self.getToken(AMMScriptParser.PLUS_EQUAL, 0)

        def MINUS_EQUAL(self):
            return self.getToken(AMMScriptParser.MINUS_EQUAL, 0)

        def MULTIPLY_EQUAL(self):
            return self.getToken(AMMScriptParser.MULTIPLY_EQUAL, 0)

        def DIVIDE_EQUAL(self):
            return self.getToken(AMMScriptParser.DIVIDE_EQUAL, 0)

        def LBRACKET(self):
            return self.getToken(AMMScriptParser.LBRACKET, 0)

        def NUMBER(self):
            return self.getToken(AMMScriptParser.NUMBER, 0)

        def RBRACKET(self):
            return self.getToken(AMMScriptParser.RBRACKET, 0)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_variableAsignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableAsignment" ):
                return visitor.visitVariableAsignment(self)
            else:
                return visitor.visitChildren(self)




    def variableAsignment(self):

        localctx = AMMScriptParser.VariableAsignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableAsignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(AMMScriptParser.ID)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 171
                self.match(AMMScriptParser.LBRACKET)
                self.state = 172
                self.match(AMMScriptParser.NUMBER)
                self.state = 173
                self.match(AMMScriptParser.RBRACKET)


            self.state = 176
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65011712) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 177
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(AMMScriptParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return AMMScriptParser.RULE_print

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = AMMScriptParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(AMMScriptParser.PRINT)
            self.state = 180
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.IF)
            else:
                return self.getToken(AMMScriptParser.IF, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)


        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.LBRACE)
            else:
                return self.getToken(AMMScriptParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.RBRACE)
            else:
                return self.getToken(AMMScriptParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.ELSE)
            else:
                return self.getToken(AMMScriptParser.ELSE, i)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = AMMScriptParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(AMMScriptParser.IF)
            self.state = 183
            self.expr(0)
            self.state = 184
            self.match(AMMScriptParser.LBRACE)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997340) != 0):
                self.state = 185
                self.statement()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
            self.match(AMMScriptParser.RBRACE)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 192
                    self.match(AMMScriptParser.ELSE)
                    self.state = 193
                    self.match(AMMScriptParser.IF)
                    self.state = 194
                    self.expr(0)
                    self.state = 195
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 199
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997340) != 0):
                        self.state = 196
                        self.statement()
                        self.state = 201
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 202
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 209
                self.match(AMMScriptParser.ELSE)
                self.state = 210
                self.match(AMMScriptParser.LBRACE)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997340) != 0):
                    self.state = 211
                    self.statement()
                    self.state = 216
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 217
                self.match(AMMScriptParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfInLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.IF)
            else:
                return self.getToken(AMMScriptParser.IF, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)


        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.LBRACE)
            else:
                return self.getToken(AMMScriptParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.RBRACE)
            else:
                return self.getToken(AMMScriptParser.RBRACE, i)

        def statementInLoop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementInLoopContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementInLoopContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.ELSE)
            else:
                return self.getToken(AMMScriptParser.ELSE, i)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_ifInLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfInLoop" ):
                return visitor.visitIfInLoop(self)
            else:
                return visitor.visitChildren(self)




    def ifInLoop(self):

        localctx = AMMScriptParser.IfInLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifInLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(AMMScriptParser.IF)
            self.state = 221
            self.expr(0)
            self.state = 222
            self.match(AMMScriptParser.LBRACE)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077417000156) != 0):
                self.state = 223
                self.statementInLoop()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
            self.match(AMMScriptParser.RBRACE)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 230
                    self.match(AMMScriptParser.ELSE)
                    self.state = 231
                    self.match(AMMScriptParser.IF)
                    self.state = 232
                    self.expr(0)
                    self.state = 233
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 237
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077417000156) != 0):
                        self.state = 234
                        self.statementInLoop()
                        self.state = 239
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 240
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 247
                self.match(AMMScriptParser.ELSE)
                self.state = 248
                self.match(AMMScriptParser.LBRACE)
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077417000156) != 0):
                    self.state = 249
                    self.statementInLoop()
                    self.state = 254
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 255
                self.match(AMMScriptParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfInFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.IF)
            else:
                return self.getToken(AMMScriptParser.IF, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)


        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.LBRACE)
            else:
                return self.getToken(AMMScriptParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.RBRACE)
            else:
                return self.getToken(AMMScriptParser.RBRACE, i)

        def statementInFunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementInFunctionContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementInFunctionContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.ELSE)
            else:
                return self.getToken(AMMScriptParser.ELSE, i)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_ifInFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfInFunction" ):
                return visitor.visitIfInFunction(self)
            else:
                return visitor.visitChildren(self)




    def ifInFunction(self):

        localctx = AMMScriptParser.IfInFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifInFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(AMMScriptParser.IF)
            self.state = 259
            self.expr(0)
            self.state = 260
            self.match(AMMScriptParser.LBRACE)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                self.state = 261
                self.statementInFunction()
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 267
            self.match(AMMScriptParser.RBRACE)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 268
                    self.match(AMMScriptParser.ELSE)
                    self.state = 269
                    self.match(AMMScriptParser.IF)
                    self.state = 270
                    self.expr(0)
                    self.state = 271
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 275
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                        self.state = 272
                        self.statementInFunction()
                        self.state = 277
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 278
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 285
                self.match(AMMScriptParser.ELSE)
                self.state = 286
                self.match(AMMScriptParser.LBRACE)
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                    self.state = 287
                    self.statementInFunction()
                    self.state = 292
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 293
                self.match(AMMScriptParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfInFunctionAndLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.IF)
            else:
                return self.getToken(AMMScriptParser.IF, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)


        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.LBRACE)
            else:
                return self.getToken(AMMScriptParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.RBRACE)
            else:
                return self.getToken(AMMScriptParser.RBRACE, i)

        def statementInFunctionAndLoop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementInFunctionAndLoopContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementInFunctionAndLoopContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.ELSE)
            else:
                return self.getToken(AMMScriptParser.ELSE, i)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_ifInFunctionAndLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfInFunctionAndLoop" ):
                return visitor.visitIfInFunctionAndLoop(self)
            else:
                return visitor.visitChildren(self)




    def ifInFunctionAndLoop(self):

        localctx = AMMScriptParser.IfInFunctionAndLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifInFunctionAndLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(AMMScriptParser.IF)
            self.state = 297
            self.expr(0)
            self.state = 298
            self.match(AMMScriptParser.LBRACE)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416996572) != 0):
                self.state = 299
                self.statementInFunctionAndLoop()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 305
            self.match(AMMScriptParser.RBRACE)
            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 306
                    self.match(AMMScriptParser.ELSE)
                    self.state = 307
                    self.match(AMMScriptParser.IF)
                    self.state = 308
                    self.expr(0)
                    self.state = 309
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 313
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416996572) != 0):
                        self.state = 310
                        self.statementInFunctionAndLoop()
                        self.state = 315
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 316
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 323
                self.match(AMMScriptParser.ELSE)
                self.state = 324
                self.match(AMMScriptParser.LBRACE)
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416996572) != 0):
                    self.state = 325
                    self.statementInFunctionAndLoop()
                    self.state = 330
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 331
                self.match(AMMScriptParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forLoop(self):
            return self.getTypedRuleContext(AMMScriptParser.ForLoopContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(AMMScriptParser.WhileLoopContext,0)


        def getRuleIndex(self):
            return AMMScriptParser.RULE_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = AMMScriptParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_loop)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.forLoop()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.whileLoop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopInFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forLoopInFunction(self):
            return self.getTypedRuleContext(AMMScriptParser.ForLoopInFunctionContext,0)


        def whileLoopInFunction(self):
            return self.getTypedRuleContext(AMMScriptParser.WhileLoopInFunctionContext,0)


        def getRuleIndex(self):
            return AMMScriptParser.RULE_loopInFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopInFunction" ):
                return visitor.visitLoopInFunction(self)
            else:
                return visitor.visitChildren(self)




    def loopInFunction(self):

        localctx = AMMScriptParser.LoopInFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_loopInFunction)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.forLoopInFunction()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.whileLoopInFunction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(AMMScriptParser.FOR, 0)

        def variableDeclaration(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableDeclarationContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.SEMICOLON)
            else:
                return self.getToken(AMMScriptParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)


        def variableAsignment(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableAsignmentContext,0)


        def LBRACE(self):
            return self.getToken(AMMScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AMMScriptParser.RBRACE, 0)

        def statementInLoop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementInLoopContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementInLoopContext,i)


        def getRuleIndex(self):
            return AMMScriptParser.RULE_forLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = AMMScriptParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(AMMScriptParser.FOR)
            self.state = 343
            self.variableDeclaration()
            self.state = 344
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 345
            self.expr(0)
            self.state = 346
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 347
            self.variableAsignment()
            self.state = 348
            self.match(AMMScriptParser.LBRACE)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077417000156) != 0):
                self.state = 349
                self.statementInLoop()
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 355
            self.match(AMMScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopInFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(AMMScriptParser.FOR, 0)

        def variableDeclaration(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableDeclarationContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.SEMICOLON)
            else:
                return self.getToken(AMMScriptParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)


        def variableAsignment(self):
            return self.getTypedRuleContext(AMMScriptParser.VariableAsignmentContext,0)


        def LBRACE(self):
            return self.getToken(AMMScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AMMScriptParser.RBRACE, 0)

        def statementInFunctionAndLoop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementInFunctionAndLoopContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementInFunctionAndLoopContext,i)


        def getRuleIndex(self):
            return AMMScriptParser.RULE_forLoopInFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoopInFunction" ):
                return visitor.visitForLoopInFunction(self)
            else:
                return visitor.visitChildren(self)




    def forLoopInFunction(self):

        localctx = AMMScriptParser.ForLoopInFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_forLoopInFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(AMMScriptParser.FOR)
            self.state = 358
            self.variableDeclaration()
            self.state = 359
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 360
            self.expr(0)
            self.state = 361
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 362
            self.variableAsignment()
            self.state = 363
            self.match(AMMScriptParser.LBRACE)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416996572) != 0):
                self.state = 364
                self.statementInFunctionAndLoop()
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 370
            self.match(AMMScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(AMMScriptParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)


        def LBRACE(self):
            return self.getToken(AMMScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AMMScriptParser.RBRACE, 0)

        def statementInLoop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementInLoopContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementInLoopContext,i)


        def getRuleIndex(self):
            return AMMScriptParser.RULE_whileLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = AMMScriptParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(AMMScriptParser.WHILE)
            self.state = 373
            self.expr(0)
            self.state = 374
            self.match(AMMScriptParser.LBRACE)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077417000156) != 0):
                self.state = 375
                self.statementInLoop()
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 381
            self.match(AMMScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopInFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(AMMScriptParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)


        def LBRACE(self):
            return self.getToken(AMMScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AMMScriptParser.RBRACE, 0)

        def statementInFunctionAndLoop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementInFunctionAndLoopContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementInFunctionAndLoopContext,i)


        def getRuleIndex(self):
            return AMMScriptParser.RULE_whileLoopInFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoopInFunction" ):
                return visitor.visitWhileLoopInFunction(self)
            else:
                return visitor.visitChildren(self)




    def whileLoopInFunction(self):

        localctx = AMMScriptParser.WhileLoopInFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_whileLoopInFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(AMMScriptParser.WHILE)
            self.state = 384
            self.expr(0)
            self.state = 385
            self.match(AMMScriptParser.LBRACE)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416996572) != 0):
                self.state = 386
                self.statementInFunctionAndLoop()
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 392
            self.match(AMMScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(AMMScriptParser.SWITCH, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)


        def LBRACE(self):
            return self.getToken(AMMScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AMMScriptParser.RBRACE, 0)

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.CASE)
            else:
                return self.getToken(AMMScriptParser.CASE, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.COLON)
            else:
                return self.getToken(AMMScriptParser.COLON, i)

        def DEFAULT(self):
            return self.getToken(AMMScriptParser.DEFAULT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementContext,i)


        def BREAK(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.BREAK)
            else:
                return self.getToken(AMMScriptParser.BREAK, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.SEMICOLON)
            else:
                return self.getToken(AMMScriptParser.SEMICOLON, i)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_switch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch" ):
                return visitor.visitSwitch(self)
            else:
                return visitor.visitChildren(self)




    def switch(self):

        localctx = AMMScriptParser.SwitchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_switch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(AMMScriptParser.SWITCH)
            self.state = 395
            self.expr(0)
            self.state = 396
            self.match(AMMScriptParser.LBRACE)
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 397
                self.match(AMMScriptParser.CASE)
                self.state = 398
                self.expr(0)
                self.state = 399
                self.match(AMMScriptParser.COLON)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997340) != 0):
                    self.state = 400
                    self.statement()
                    self.state = 405
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 406
                    self.match(AMMScriptParser.BREAK)
                    self.state = 407
                    self.match(AMMScriptParser.SEMICOLON)


                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 415
                self.match(AMMScriptParser.DEFAULT)
                self.state = 416
                self.match(AMMScriptParser.COLON)
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997340) != 0):
                    self.state = 417
                    self.statement()
                    self.state = 422
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 425
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 423
                    self.match(AMMScriptParser.BREAK)
                    self.state = 424
                    self.match(AMMScriptParser.SEMICOLON)




            self.state = 429
            self.match(AMMScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchInFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(AMMScriptParser.SWITCH, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)


        def LBRACE(self):
            return self.getToken(AMMScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AMMScriptParser.RBRACE, 0)

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.CASE)
            else:
                return self.getToken(AMMScriptParser.CASE, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.COLON)
            else:
                return self.getToken(AMMScriptParser.COLON, i)

        def DEFAULT(self):
            return self.getToken(AMMScriptParser.DEFAULT, 0)

        def statementInFunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementInFunctionContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementInFunctionContext,i)


        def BREAK(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.BREAK)
            else:
                return self.getToken(AMMScriptParser.BREAK, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.SEMICOLON)
            else:
                return self.getToken(AMMScriptParser.SEMICOLON, i)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_switchInFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchInFunction" ):
                return visitor.visitSwitchInFunction(self)
            else:
                return visitor.visitChildren(self)




    def switchInFunction(self):

        localctx = AMMScriptParser.SwitchInFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_switchInFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(AMMScriptParser.SWITCH)
            self.state = 432
            self.expr(0)
            self.state = 433
            self.match(AMMScriptParser.LBRACE)
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 434
                self.match(AMMScriptParser.CASE)
                self.state = 435
                self.expr(0)
                self.state = 436
                self.match(AMMScriptParser.COLON)
                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                    self.state = 437
                    self.statementInFunction()
                    self.state = 442
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 445
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 443
                    self.match(AMMScriptParser.BREAK)
                    self.state = 444
                    self.match(AMMScriptParser.SEMICOLON)


                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 464
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 452
                self.match(AMMScriptParser.DEFAULT)
                self.state = 453
                self.match(AMMScriptParser.COLON)
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                    self.state = 454
                    self.statementInFunction()
                    self.state = 459
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 462
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 460
                    self.match(AMMScriptParser.BREAK)
                    self.state = 461
                    self.match(AMMScriptParser.SEMICOLON)




            self.state = 466
            self.match(AMMScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(AMMScriptParser.FUNCTION, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.ID)
            else:
                return self.getToken(AMMScriptParser.ID, i)

        def LPAREN(self):
            return self.getToken(AMMScriptParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AMMScriptParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(AMMScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AMMScriptParser.RBRACE, 0)

        def statementInFunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.StatementInFunctionContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.StatementInFunctionContext,i)


        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.EQUAL)
            else:
                return self.getToken(AMMScriptParser.EQUAL, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.COMMA)
            else:
                return self.getToken(AMMScriptParser.COMMA, i)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_functionDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = AMMScriptParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(AMMScriptParser.FUNCTION)
            self.state = 469
            self.match(AMMScriptParser.ID)
            self.state = 470
            self.match(AMMScriptParser.LPAREN)
            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 471
                self.match(AMMScriptParser.ID)
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 472
                    self.match(AMMScriptParser.EQUAL)
                    self.state = 473
                    self.expr(0)


                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 476
                    self.match(AMMScriptParser.COMMA)
                    self.state = 477
                    self.match(AMMScriptParser.ID)
                    self.state = 480
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==21:
                        self.state = 478
                        self.match(AMMScriptParser.EQUAL)
                        self.state = 479
                        self.expr(0)


                    self.state = 486
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 489
            self.match(AMMScriptParser.RPAREN)
            self.state = 490
            self.match(AMMScriptParser.LBRACE)
            self.state = 494
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                self.state = 491
                self.statementInFunction()
                self.state = 496
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 497
            self.match(AMMScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AMMScriptParser.ID, 0)

        def LPAREN(self):
            return self.getToken(AMMScriptParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AMMScriptParser.RPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.COMMA)
            else:
                return self.getToken(AMMScriptParser.COMMA, i)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = AMMScriptParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(AMMScriptParser.ID)
            self.state = 500
            self.match(AMMScriptParser.LPAREN)
            self.state = 509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416992768) != 0):
                self.state = 501
                self.expr(0)
                self.state = 506
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 502
                    self.match(AMMScriptParser.COMMA)
                    self.state = 503
                    self.expr(0)
                    self.state = 508
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 511
            self.match(AMMScriptParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AMMScriptParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(AMMScriptParser.LBRACKET, 0)

        def NUMBER(self):
            return self.getToken(AMMScriptParser.NUMBER, 0)

        def RBRACKET(self):
            return self.getToken(AMMScriptParser.RBRACKET, 0)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_arrayExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)




    def arrayExpr(self):

        localctx = AMMScriptParser.ArrayExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_arrayExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(AMMScriptParser.ID)
            self.state = 514
            self.match(AMMScriptParser.LBRACKET)
            self.state = 515
            self.match(AMMScriptParser.NUMBER)
            self.state = 516
            self.match(AMMScriptParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AMMScriptParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprPlusMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(AMMScriptParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(AMMScriptParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPlusMinus" ):
                return visitor.visitExprPlusMinus(self)
            else:
                return visitor.visitChildren(self)


    class ExprMultDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)

        def MULTIPLY(self):
            return self.getToken(AMMScriptParser.MULTIPLY, 0)
        def DIVIDE(self):
            return self.getToken(AMMScriptParser.DIVIDE, 0)
        def MODULO(self):
            return self.getToken(AMMScriptParser.MODULO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMultDivMod" ):
                return visitor.visitExprMultDivMod(self)
            else:
                return visitor.visitChildren(self)


    class ExprComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)

        def EQUAL_EQUAL(self):
            return self.getToken(AMMScriptParser.EQUAL_EQUAL, 0)
        def NOT_EQUAL(self):
            return self.getToken(AMMScriptParser.NOT_EQUAL, 0)
        def LESS(self):
            return self.getToken(AMMScriptParser.LESS, 0)
        def GREATER(self):
            return self.getToken(AMMScriptParser.GREATER, 0)
        def LESS_EQUAL(self):
            return self.getToken(AMMScriptParser.LESS_EQUAL, 0)
        def GREATER_EQUAL(self):
            return self.getToken(AMMScriptParser.GREATER_EQUAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprComparison" ):
                return visitor.visitExprComparison(self)
            else:
                return visitor.visitChildren(self)


    class ExprNumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(AMMScriptParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNumber" ):
                return visitor.visitExprNumber(self)
            else:
                return visitor.visitChildren(self)


    class ExprTrueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(AMMScriptParser.TRUE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprTrue" ):
                return visitor.visitExprTrue(self)
            else:
                return visitor.visitChildren(self)


    class ExprAndOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)

        def AND(self):
            return self.getToken(AMMScriptParser.AND, 0)
        def OR(self):
            return self.getToken(AMMScriptParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAndOr" ):
                return visitor.visitExprAndOr(self)
            else:
                return visitor.visitChildren(self)


    class ExprStringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(AMMScriptParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprString" ):
                return visitor.visitExprString(self)
            else:
                return visitor.visitChildren(self)


    class ExprFalseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(AMMScriptParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprFalse" ):
                return visitor.visitExprFalse(self)
            else:
                return visitor.visitChildren(self)


    class ExprIdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AMMScriptParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprId" ):
                return visitor.visitExprId(self)
            else:
                return visitor.visitChildren(self)


    class ExprPowerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)

        def POWER(self):
            return self.getToken(AMMScriptParser.POWER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPower" ):
                return visitor.visitExprPower(self)
            else:
                return visitor.visitChildren(self)


    class ExprParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(AMMScriptParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(AMMScriptParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParenthesis" ):
                return visitor.visitExprParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class ExprArrayContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayExpr(self):
            return self.getTypedRuleContext(AMMScriptParser.ArrayExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprArray" ):
                return visitor.visitExprArray(self)
            else:
                return visitor.visitChildren(self)


    class ExprFunctionCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(AMMScriptParser.FunctionCallContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprFunctionCall" ):
                return visitor.visitExprFunctionCall(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AMMScriptParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = AMMScriptParser.ExprParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 519
                self.match(AMMScriptParser.LPAREN)
                self.state = 520
                self.expr(0)
                self.state = 521
                self.match(AMMScriptParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = AMMScriptParser.ExprNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 523
                self.match(AMMScriptParser.NUMBER)
                pass

            elif la_ == 3:
                localctx = AMMScriptParser.ExprStringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 524
                self.match(AMMScriptParser.STRING)
                pass

            elif la_ == 4:
                localctx = AMMScriptParser.ExprTrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 525
                self.match(AMMScriptParser.TRUE)
                pass

            elif la_ == 5:
                localctx = AMMScriptParser.ExprFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 526
                self.match(AMMScriptParser.FALSE)
                pass

            elif la_ == 6:
                localctx = AMMScriptParser.ExprFunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 527
                self.functionCall()
                pass

            elif la_ == 7:
                localctx = AMMScriptParser.ExprArrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 528
                self.arrayExpr()
                pass

            elif la_ == 8:
                localctx = AMMScriptParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 529
                self.match(AMMScriptParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 549
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 547
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = AMMScriptParser.ExprPowerContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 532
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 533
                        self.match(AMMScriptParser.POWER)
                        self.state = 534
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = AMMScriptParser.ExprMultDivModContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 535
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 536
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2952790016) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 537
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = AMMScriptParser.ExprPlusMinusContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 538
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 539
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 540
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = AMMScriptParser.ExprComparisonContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 541
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 542
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 543
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = AMMScriptParser.ExprAndOrContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 544
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 545
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==42 or _la==43):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 546
                        self.expr(9)
                        pass

             
                self.state = 551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         




