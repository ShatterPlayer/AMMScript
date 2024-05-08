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
        4,1,51,566,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,78,8,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,100,
        8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,124,8,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,149,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        5,5,163,8,5,10,5,12,5,166,9,5,3,5,168,8,5,1,5,3,5,171,8,5,1,6,1,
        6,1,6,1,6,3,6,177,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,
        8,189,8,8,10,8,12,8,192,9,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,200,8,8,
        10,8,12,8,203,9,8,1,8,1,8,5,8,207,8,8,10,8,12,8,210,9,8,1,8,1,8,
        1,8,5,8,215,8,8,10,8,12,8,218,9,8,1,8,3,8,221,8,8,1,9,1,9,1,9,1,
        9,5,9,227,8,9,10,9,12,9,230,9,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,238,
        8,9,10,9,12,9,241,9,9,1,9,1,9,5,9,245,8,9,10,9,12,9,248,9,9,1,9,
        1,9,1,9,5,9,253,8,9,10,9,12,9,256,9,9,1,9,3,9,259,8,9,1,10,1,10,
        1,10,1,10,5,10,265,8,10,10,10,12,10,268,9,10,1,10,1,10,1,10,1,10,
        1,10,1,10,5,10,276,8,10,10,10,12,10,279,9,10,1,10,1,10,5,10,283,
        8,10,10,10,12,10,286,9,10,1,10,1,10,1,10,5,10,291,8,10,10,10,12,
        10,294,9,10,1,10,3,10,297,8,10,1,11,1,11,1,11,1,11,5,11,303,8,11,
        10,11,12,11,306,9,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,314,8,11,
        10,11,12,11,317,9,11,1,11,1,11,5,11,321,8,11,10,11,12,11,324,9,11,
        1,11,1,11,1,11,5,11,329,8,11,10,11,12,11,332,9,11,1,11,3,11,335,
        8,11,1,12,1,12,3,12,339,8,12,1,13,1,13,3,13,343,8,13,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,5,14,353,8,14,10,14,12,14,356,9,14,1,
        14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,368,8,15,10,
        15,12,15,371,9,15,1,15,1,15,1,16,1,16,1,16,1,16,5,16,379,8,16,10,
        16,12,16,382,9,16,1,16,1,16,1,17,1,17,1,17,1,17,5,17,390,8,17,10,
        17,12,17,393,9,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,
        18,404,8,18,10,18,12,18,407,9,18,1,18,1,18,3,18,411,8,18,5,18,413,
        8,18,10,18,12,18,416,9,18,1,18,1,18,1,18,5,18,421,8,18,10,18,12,
        18,424,9,18,1,18,1,18,3,18,428,8,18,3,18,430,8,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,5,19,441,8,19,10,19,12,19,444,9,19,
        1,19,1,19,3,19,448,8,19,5,19,450,8,19,10,19,12,19,453,9,19,1,19,
        1,19,1,19,5,19,458,8,19,10,19,12,19,461,9,19,1,19,1,19,3,19,465,
        8,19,3,19,467,8,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,3,20,
        477,8,20,1,20,1,20,1,20,1,20,3,20,483,8,20,5,20,485,8,20,10,20,12,
        20,488,9,20,3,20,490,8,20,1,20,1,20,1,20,5,20,495,8,20,10,20,12,
        20,498,9,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,5,21,507,8,21,10,
        21,12,21,510,9,21,3,21,512,8,21,1,21,1,21,1,22,1,22,1,22,1,22,1,
        22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,3,23,534,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,5,23,551,8,23,10,23,12,23,554,9,23,1,
        24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,564,8,24,1,24,0,1,46,
        25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,0,5,1,0,21,25,2,0,28,29,31,31,1,0,26,27,1,0,15,20,1,0,44,
        45,640,0,53,1,0,0,0,2,77,1,0,0,0,4,99,1,0,0,0,6,123,1,0,0,0,8,148,
        1,0,0,0,10,150,1,0,0,0,12,172,1,0,0,0,14,181,1,0,0,0,16,184,1,0,
        0,0,18,222,1,0,0,0,20,260,1,0,0,0,22,298,1,0,0,0,24,338,1,0,0,0,
        26,342,1,0,0,0,28,344,1,0,0,0,30,359,1,0,0,0,32,374,1,0,0,0,34,385,
        1,0,0,0,36,396,1,0,0,0,38,433,1,0,0,0,40,470,1,0,0,0,42,501,1,0,
        0,0,44,515,1,0,0,0,46,533,1,0,0,0,48,563,1,0,0,0,50,52,3,2,1,0,51,
        50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,
        0,55,53,1,0,0,0,56,57,5,0,0,1,57,1,1,0,0,0,58,59,3,10,5,0,59,60,
        5,49,0,0,60,78,1,0,0,0,61,62,3,12,6,0,62,63,5,49,0,0,63,78,1,0,0,
        0,64,65,3,14,7,0,65,66,5,49,0,0,66,78,1,0,0,0,67,68,3,42,21,0,68,
        69,5,49,0,0,69,78,1,0,0,0,70,71,3,46,23,0,71,72,5,49,0,0,72,78,1,
        0,0,0,73,78,3,16,8,0,74,78,3,24,12,0,75,78,3,40,20,0,76,78,3,36,
        18,0,77,58,1,0,0,0,77,61,1,0,0,0,77,64,1,0,0,0,77,67,1,0,0,0,77,
        70,1,0,0,0,77,73,1,0,0,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,
        0,78,3,1,0,0,0,79,80,3,10,5,0,80,81,5,49,0,0,81,100,1,0,0,0,82,83,
        3,12,6,0,83,84,5,49,0,0,84,100,1,0,0,0,85,86,3,14,7,0,86,87,5,49,
        0,0,87,100,1,0,0,0,88,89,3,42,21,0,89,90,5,49,0,0,90,100,1,0,0,0,
        91,92,3,46,23,0,92,93,5,49,0,0,93,100,1,0,0,0,94,100,3,18,9,0,95,
        100,3,24,12,0,96,100,5,10,0,0,97,100,5,11,0,0,98,100,3,36,18,0,99,
        79,1,0,0,0,99,82,1,0,0,0,99,85,1,0,0,0,99,88,1,0,0,0,99,91,1,0,0,
        0,99,94,1,0,0,0,99,95,1,0,0,0,99,96,1,0,0,0,99,97,1,0,0,0,99,98,
        1,0,0,0,100,5,1,0,0,0,101,102,3,10,5,0,102,103,5,49,0,0,103,124,
        1,0,0,0,104,105,3,12,6,0,105,106,5,49,0,0,106,124,1,0,0,0,107,108,
        3,14,7,0,108,109,5,49,0,0,109,124,1,0,0,0,110,111,3,42,21,0,111,
        112,5,49,0,0,112,124,1,0,0,0,113,114,3,46,23,0,114,115,5,49,0,0,
        115,124,1,0,0,0,116,124,3,20,10,0,117,124,3,26,13,0,118,119,5,9,
        0,0,119,120,3,46,23,0,120,121,5,49,0,0,121,124,1,0,0,0,122,124,3,
        38,19,0,123,101,1,0,0,0,123,104,1,0,0,0,123,107,1,0,0,0,123,110,
        1,0,0,0,123,113,1,0,0,0,123,116,1,0,0,0,123,117,1,0,0,0,123,118,
        1,0,0,0,123,122,1,0,0,0,124,7,1,0,0,0,125,126,3,10,5,0,126,127,5,
        49,0,0,127,149,1,0,0,0,128,129,3,12,6,0,129,130,5,49,0,0,130,149,
        1,0,0,0,131,132,3,14,7,0,132,133,5,49,0,0,133,149,1,0,0,0,134,135,
        3,42,21,0,135,136,5,49,0,0,136,149,1,0,0,0,137,138,3,46,23,0,138,
        139,5,49,0,0,139,149,1,0,0,0,140,149,3,22,11,0,141,149,3,26,13,0,
        142,149,5,10,0,0,143,149,5,11,0,0,144,145,5,9,0,0,145,146,3,46,23,
        0,146,147,5,49,0,0,147,149,1,0,0,0,148,125,1,0,0,0,148,128,1,0,0,
        0,148,131,1,0,0,0,148,134,1,0,0,0,148,137,1,0,0,0,148,140,1,0,0,
        0,148,141,1,0,0,0,148,142,1,0,0,0,148,143,1,0,0,0,148,144,1,0,0,
        0,149,9,1,0,0,0,150,151,5,2,0,0,151,170,5,51,0,0,152,153,5,21,0,
        0,153,171,3,46,23,0,154,155,5,38,0,0,155,156,5,40,0,0,156,157,5,
        39,0,0,157,158,5,21,0,0,158,167,5,38,0,0,159,164,3,46,23,0,160,161,
        5,48,0,0,161,163,3,46,23,0,162,160,1,0,0,0,163,166,1,0,0,0,164,162,
        1,0,0,0,164,165,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,167,159,
        1,0,0,0,167,168,1,0,0,0,168,169,1,0,0,0,169,171,5,39,0,0,170,152,
        1,0,0,0,170,154,1,0,0,0,171,11,1,0,0,0,172,176,5,51,0,0,173,174,
        5,38,0,0,174,175,5,40,0,0,175,177,5,39,0,0,176,173,1,0,0,0,176,177,
        1,0,0,0,177,178,1,0,0,0,178,179,7,0,0,0,179,180,3,46,23,0,180,13,
        1,0,0,0,181,182,5,3,0,0,182,183,3,46,23,0,183,15,1,0,0,0,184,185,
        5,4,0,0,185,186,3,46,23,0,186,190,5,36,0,0,187,189,3,2,1,0,188,187,
        1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,193,
        1,0,0,0,192,190,1,0,0,0,193,208,5,37,0,0,194,195,5,5,0,0,195,196,
        5,4,0,0,196,197,3,46,23,0,197,201,5,36,0,0,198,200,3,2,1,0,199,198,
        1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,204,
        1,0,0,0,203,201,1,0,0,0,204,205,5,37,0,0,205,207,1,0,0,0,206,194,
        1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,220,
        1,0,0,0,210,208,1,0,0,0,211,212,5,5,0,0,212,216,5,36,0,0,213,215,
        3,2,1,0,214,213,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,
        1,0,0,0,217,219,1,0,0,0,218,216,1,0,0,0,219,221,5,37,0,0,220,211,
        1,0,0,0,220,221,1,0,0,0,221,17,1,0,0,0,222,223,5,4,0,0,223,224,3,
        46,23,0,224,228,5,36,0,0,225,227,3,4,2,0,226,225,1,0,0,0,227,230,
        1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,231,1,0,0,0,230,228,
        1,0,0,0,231,246,5,37,0,0,232,233,5,5,0,0,233,234,5,4,0,0,234,235,
        3,46,23,0,235,239,5,36,0,0,236,238,3,4,2,0,237,236,1,0,0,0,238,241,
        1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,242,1,0,0,0,241,239,
        1,0,0,0,242,243,5,37,0,0,243,245,1,0,0,0,244,232,1,0,0,0,245,248,
        1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,258,1,0,0,0,248,246,
        1,0,0,0,249,250,5,5,0,0,250,254,5,36,0,0,251,253,3,4,2,0,252,251,
        1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,255,1,0,0,0,255,257,
        1,0,0,0,256,254,1,0,0,0,257,259,5,37,0,0,258,249,1,0,0,0,258,259,
        1,0,0,0,259,19,1,0,0,0,260,261,5,4,0,0,261,262,3,46,23,0,262,266,
        5,36,0,0,263,265,3,6,3,0,264,263,1,0,0,0,265,268,1,0,0,0,266,264,
        1,0,0,0,266,267,1,0,0,0,267,269,1,0,0,0,268,266,1,0,0,0,269,284,
        5,37,0,0,270,271,5,5,0,0,271,272,5,4,0,0,272,273,3,46,23,0,273,277,
        5,36,0,0,274,276,3,6,3,0,275,274,1,0,0,0,276,279,1,0,0,0,277,275,
        1,0,0,0,277,278,1,0,0,0,278,280,1,0,0,0,279,277,1,0,0,0,280,281,
        5,37,0,0,281,283,1,0,0,0,282,270,1,0,0,0,283,286,1,0,0,0,284,282,
        1,0,0,0,284,285,1,0,0,0,285,296,1,0,0,0,286,284,1,0,0,0,287,288,
        5,5,0,0,288,292,5,36,0,0,289,291,3,6,3,0,290,289,1,0,0,0,291,294,
        1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,295,1,0,0,0,294,292,
        1,0,0,0,295,297,5,37,0,0,296,287,1,0,0,0,296,297,1,0,0,0,297,21,
        1,0,0,0,298,299,5,4,0,0,299,300,3,46,23,0,300,304,5,36,0,0,301,303,
        3,8,4,0,302,301,1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,305,
        1,0,0,0,305,307,1,0,0,0,306,304,1,0,0,0,307,322,5,37,0,0,308,309,
        5,5,0,0,309,310,5,4,0,0,310,311,3,46,23,0,311,315,5,36,0,0,312,314,
        3,8,4,0,313,312,1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,315,316,
        1,0,0,0,316,318,1,0,0,0,317,315,1,0,0,0,318,319,5,37,0,0,319,321,
        1,0,0,0,320,308,1,0,0,0,321,324,1,0,0,0,322,320,1,0,0,0,322,323,
        1,0,0,0,323,334,1,0,0,0,324,322,1,0,0,0,325,326,5,5,0,0,326,330,
        5,36,0,0,327,329,3,8,4,0,328,327,1,0,0,0,329,332,1,0,0,0,330,328,
        1,0,0,0,330,331,1,0,0,0,331,333,1,0,0,0,332,330,1,0,0,0,333,335,
        5,37,0,0,334,325,1,0,0,0,334,335,1,0,0,0,335,23,1,0,0,0,336,339,
        3,28,14,0,337,339,3,32,16,0,338,336,1,0,0,0,338,337,1,0,0,0,339,
        25,1,0,0,0,340,343,3,30,15,0,341,343,3,34,17,0,342,340,1,0,0,0,342,
        341,1,0,0,0,343,27,1,0,0,0,344,345,5,6,0,0,345,346,3,10,5,0,346,
        347,5,49,0,0,347,348,3,46,23,0,348,349,5,49,0,0,349,350,3,12,6,0,
        350,354,5,36,0,0,351,353,3,4,2,0,352,351,1,0,0,0,353,356,1,0,0,0,
        354,352,1,0,0,0,354,355,1,0,0,0,355,357,1,0,0,0,356,354,1,0,0,0,
        357,358,5,37,0,0,358,29,1,0,0,0,359,360,5,6,0,0,360,361,3,10,5,0,
        361,362,5,49,0,0,362,363,3,46,23,0,363,364,5,49,0,0,364,365,3,12,
        6,0,365,369,5,36,0,0,366,368,3,8,4,0,367,366,1,0,0,0,368,371,1,0,
        0,0,369,367,1,0,0,0,369,370,1,0,0,0,370,372,1,0,0,0,371,369,1,0,
        0,0,372,373,5,37,0,0,373,31,1,0,0,0,374,375,5,7,0,0,375,376,3,46,
        23,0,376,380,5,36,0,0,377,379,3,4,2,0,378,377,1,0,0,0,379,382,1,
        0,0,0,380,378,1,0,0,0,380,381,1,0,0,0,381,383,1,0,0,0,382,380,1,
        0,0,0,383,384,5,37,0,0,384,33,1,0,0,0,385,386,5,7,0,0,386,387,3,
        46,23,0,387,391,5,36,0,0,388,390,3,8,4,0,389,388,1,0,0,0,390,393,
        1,0,0,0,391,389,1,0,0,0,391,392,1,0,0,0,392,394,1,0,0,0,393,391,
        1,0,0,0,394,395,5,37,0,0,395,35,1,0,0,0,396,397,5,12,0,0,397,398,
        3,46,23,0,398,414,5,36,0,0,399,400,5,13,0,0,400,401,3,46,23,0,401,
        405,5,50,0,0,402,404,3,2,1,0,403,402,1,0,0,0,404,407,1,0,0,0,405,
        403,1,0,0,0,405,406,1,0,0,0,406,410,1,0,0,0,407,405,1,0,0,0,408,
        409,5,10,0,0,409,411,5,49,0,0,410,408,1,0,0,0,410,411,1,0,0,0,411,
        413,1,0,0,0,412,399,1,0,0,0,413,416,1,0,0,0,414,412,1,0,0,0,414,
        415,1,0,0,0,415,429,1,0,0,0,416,414,1,0,0,0,417,418,5,14,0,0,418,
        422,5,50,0,0,419,421,3,2,1,0,420,419,1,0,0,0,421,424,1,0,0,0,422,
        420,1,0,0,0,422,423,1,0,0,0,423,427,1,0,0,0,424,422,1,0,0,0,425,
        426,5,10,0,0,426,428,5,49,0,0,427,425,1,0,0,0,427,428,1,0,0,0,428,
        430,1,0,0,0,429,417,1,0,0,0,429,430,1,0,0,0,430,431,1,0,0,0,431,
        432,5,37,0,0,432,37,1,0,0,0,433,434,5,12,0,0,434,435,3,46,23,0,435,
        451,5,36,0,0,436,437,5,13,0,0,437,438,3,46,23,0,438,442,5,50,0,0,
        439,441,3,6,3,0,440,439,1,0,0,0,441,444,1,0,0,0,442,440,1,0,0,0,
        442,443,1,0,0,0,443,447,1,0,0,0,444,442,1,0,0,0,445,446,5,10,0,0,
        446,448,5,49,0,0,447,445,1,0,0,0,447,448,1,0,0,0,448,450,1,0,0,0,
        449,436,1,0,0,0,450,453,1,0,0,0,451,449,1,0,0,0,451,452,1,0,0,0,
        452,466,1,0,0,0,453,451,1,0,0,0,454,455,5,14,0,0,455,459,5,50,0,
        0,456,458,3,6,3,0,457,456,1,0,0,0,458,461,1,0,0,0,459,457,1,0,0,
        0,459,460,1,0,0,0,460,464,1,0,0,0,461,459,1,0,0,0,462,463,5,10,0,
        0,463,465,5,49,0,0,464,462,1,0,0,0,464,465,1,0,0,0,465,467,1,0,0,
        0,466,454,1,0,0,0,466,467,1,0,0,0,467,468,1,0,0,0,468,469,5,37,0,
        0,469,39,1,0,0,0,470,471,5,8,0,0,471,472,5,51,0,0,472,489,5,34,0,
        0,473,476,5,51,0,0,474,475,5,21,0,0,475,477,3,46,23,0,476,474,1,
        0,0,0,476,477,1,0,0,0,477,486,1,0,0,0,478,479,5,48,0,0,479,482,5,
        51,0,0,480,481,5,21,0,0,481,483,3,46,23,0,482,480,1,0,0,0,482,483,
        1,0,0,0,483,485,1,0,0,0,484,478,1,0,0,0,485,488,1,0,0,0,486,484,
        1,0,0,0,486,487,1,0,0,0,487,490,1,0,0,0,488,486,1,0,0,0,489,473,
        1,0,0,0,489,490,1,0,0,0,490,491,1,0,0,0,491,492,5,35,0,0,492,496,
        5,36,0,0,493,495,3,6,3,0,494,493,1,0,0,0,495,498,1,0,0,0,496,494,
        1,0,0,0,496,497,1,0,0,0,497,499,1,0,0,0,498,496,1,0,0,0,499,500,
        5,37,0,0,500,41,1,0,0,0,501,502,5,51,0,0,502,511,5,34,0,0,503,508,
        3,46,23,0,504,505,5,48,0,0,505,507,3,46,23,0,506,504,1,0,0,0,507,
        510,1,0,0,0,508,506,1,0,0,0,508,509,1,0,0,0,509,512,1,0,0,0,510,
        508,1,0,0,0,511,503,1,0,0,0,511,512,1,0,0,0,512,513,1,0,0,0,513,
        514,5,35,0,0,514,43,1,0,0,0,515,516,5,51,0,0,516,517,5,38,0,0,517,
        518,5,40,0,0,518,519,5,39,0,0,519,45,1,0,0,0,520,521,6,23,-1,0,521,
        522,5,34,0,0,522,523,3,46,23,0,523,524,5,35,0,0,524,534,1,0,0,0,
        525,534,5,40,0,0,526,534,5,41,0,0,527,534,5,42,0,0,528,534,5,43,
        0,0,529,534,3,42,21,0,530,534,3,48,24,0,531,534,3,44,22,0,532,534,
        5,51,0,0,533,520,1,0,0,0,533,525,1,0,0,0,533,526,1,0,0,0,533,527,
        1,0,0,0,533,528,1,0,0,0,533,529,1,0,0,0,533,530,1,0,0,0,533,531,
        1,0,0,0,533,532,1,0,0,0,534,552,1,0,0,0,535,536,10,13,0,0,536,537,
        5,30,0,0,537,551,3,46,23,14,538,539,10,12,0,0,539,540,7,1,0,0,540,
        551,3,46,23,13,541,542,10,11,0,0,542,543,7,2,0,0,543,551,3,46,23,
        12,544,545,10,10,0,0,545,546,7,3,0,0,546,551,3,46,23,11,547,548,
        10,9,0,0,548,549,7,4,0,0,549,551,3,46,23,10,550,535,1,0,0,0,550,
        538,1,0,0,0,550,541,1,0,0,0,550,544,1,0,0,0,550,547,1,0,0,0,551,
        554,1,0,0,0,552,550,1,0,0,0,552,553,1,0,0,0,553,47,1,0,0,0,554,552,
        1,0,0,0,555,556,5,51,0,0,556,564,5,33,0,0,557,558,5,51,0,0,558,564,
        5,32,0,0,559,560,5,33,0,0,560,564,5,51,0,0,561,562,5,32,0,0,562,
        564,5,51,0,0,563,555,1,0,0,0,563,557,1,0,0,0,563,559,1,0,0,0,563,
        561,1,0,0,0,564,49,1,0,0,0,58,53,77,99,123,148,164,167,170,176,190,
        201,208,216,220,228,239,246,254,258,266,277,284,292,296,304,315,
        322,330,334,338,342,354,369,380,391,405,410,414,422,427,429,442,
        447,451,459,464,466,476,482,486,489,496,508,511,533,550,552,563
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
                     "'/'", "'^'", "'%'", "'--'", "'++'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "<INVALID>", "<INVALID>", 
                     "'true'", "'false'", "'&&'", "'||'", "'!'", "<INVALID>", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "SET", "PRINT", "IF", "ELSE", 
                      "FOR", "WHILE", "FUNCTION", "RETURN", "BREAK", "CONTINUE", 
                      "SWITCH", "CASE", "DEFAULT", "EQUAL_EQUAL", "NOT_EQUAL", 
                      "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
                      "EQUAL", "PLUS_EQUAL", "MINUS_EQUAL", "MULTIPLY_EQUAL", 
                      "DIVIDE_EQUAL", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                      "POWER", "MODULO", "MINUS_MINUS", "PLUS_PLUS", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                      "NUMBER", "STRING", "TRUE", "FALSE", "AND", "OR", 
                      "NOT", "COMMENT", "COMMA", "SEMICOLON", "COLON", "ID" ]

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
    RULE_unaryExpr = 24

    ruleNames =  [ "program", "statement", "statementInLoop", "statementInFunction", 
                   "statementInFunctionAndLoop", "variableDeclaration", 
                   "variableAsignment", "print", "if", "ifInLoop", "ifInFunction", 
                   "ifInFunctionAndLoop", "loop", "loopInFunction", "forLoop", 
                   "forLoopInFunction", "whileLoop", "whileLoopInFunction", 
                   "switch", "switchInFunction", "functionDeclaration", 
                   "functionCall", "arrayExpr", "expr", "unaryExpr" ]

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
    MINUS_MINUS=32
    PLUS_PLUS=33
    LPAREN=34
    RPAREN=35
    LBRACE=36
    RBRACE=37
    LBRACKET=38
    RBRACKET=39
    NUMBER=40
    STRING=41
    TRUE=42
    FALSE=43
    AND=44
    OR=45
    NOT=46
    COMMENT=47
    COMMA=48
    SEMICOLON=49
    COLON=50
    ID=51

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
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877532) != 0):
                self.state = 50
                self.statement()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
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
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.variableDeclaration()
                self.state = 59
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.variableAsignment()
                self.state = 62
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.print_()
                self.state = 65
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.functionCall()
                self.state = 68
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.expr(0)
                self.state = 71
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.if_()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.functionDeclaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 76
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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.variableDeclaration()
                self.state = 80
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.variableAsignment()
                self.state = 83
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.print_()
                self.state = 86
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.functionCall()
                self.state = 89
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.expr(0)
                self.state = 92
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.ifInLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 95
                self.loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 96
                self.match(AMMScriptParser.BREAK)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 97
                self.match(AMMScriptParser.CONTINUE)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 98
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
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.variableDeclaration()
                self.state = 102
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.variableAsignment()
                self.state = 105
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.print_()
                self.state = 108
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 110
                self.functionCall()
                self.state = 111
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.expr(0)
                self.state = 114
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 116
                self.ifInFunction()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 117
                self.loopInFunction()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 118
                self.match(AMMScriptParser.RETURN)
                self.state = 119
                self.expr(0)
                self.state = 120
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 122
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
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.variableDeclaration()
                self.state = 126
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.variableAsignment()
                self.state = 129
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.print_()
                self.state = 132
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.functionCall()
                self.state = 135
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.expr(0)
                self.state = 138
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 140
                self.ifInFunctionAndLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 141
                self.loopInFunction()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 142
                self.match(AMMScriptParser.BREAK)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 143
                self.match(AMMScriptParser.CONTINUE)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 144
                self.match(AMMScriptParser.RETURN)
                self.state = 145
                self.expr(0)
                self.state = 146
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
            self.state = 150
            self.match(AMMScriptParser.SET)
            self.state = 151
            self.match(AMMScriptParser.ID)
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 152
                self.match(AMMScriptParser.EQUAL)
                self.state = 153
                self.expr(0)
                pass
            elif token in [38]:
                self.state = 154
                self.match(AMMScriptParser.LBRACKET)
                self.state = 155
                self.match(AMMScriptParser.NUMBER)
                self.state = 156
                self.match(AMMScriptParser.RBRACKET)
                self.state = 157
                self.match(AMMScriptParser.EQUAL)
                self.state = 158
                self.match(AMMScriptParser.LBRACKET)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552872960) != 0):
                    self.state = 159
                    self.expr(0)
                    self.state = 164
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==48:
                        self.state = 160
                        self.match(AMMScriptParser.COMMA)
                        self.state = 161
                        self.expr(0)
                        self.state = 166
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 169
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
            self.state = 172
            self.match(AMMScriptParser.ID)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 173
                self.match(AMMScriptParser.LBRACKET)
                self.state = 174
                self.match(AMMScriptParser.NUMBER)
                self.state = 175
                self.match(AMMScriptParser.RBRACKET)


            self.state = 178
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65011712) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 179
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
            self.state = 181
            self.match(AMMScriptParser.PRINT)
            self.state = 182
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
            self.state = 184
            self.match(AMMScriptParser.IF)
            self.state = 185
            self.expr(0)
            self.state = 186
            self.match(AMMScriptParser.LBRACE)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877532) != 0):
                self.state = 187
                self.statement()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 193
            self.match(AMMScriptParser.RBRACE)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 194
                    self.match(AMMScriptParser.ELSE)
                    self.state = 195
                    self.match(AMMScriptParser.IF)
                    self.state = 196
                    self.expr(0)
                    self.state = 197
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877532) != 0):
                        self.state = 198
                        self.statement()
                        self.state = 203
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 204
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 211
                self.match(AMMScriptParser.ELSE)
                self.state = 212
                self.match(AMMScriptParser.LBRACE)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877532) != 0):
                    self.state = 213
                    self.statement()
                    self.state = 218
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 219
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
            self.state = 222
            self.match(AMMScriptParser.IF)
            self.state = 223
            self.expr(0)
            self.state = 224
            self.match(AMMScriptParser.LBRACE)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552880348) != 0):
                self.state = 225
                self.statementInLoop()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 231
            self.match(AMMScriptParser.RBRACE)
            self.state = 246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 232
                    self.match(AMMScriptParser.ELSE)
                    self.state = 233
                    self.match(AMMScriptParser.IF)
                    self.state = 234
                    self.expr(0)
                    self.state = 235
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 239
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552880348) != 0):
                        self.state = 236
                        self.statementInLoop()
                        self.state = 241
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 242
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 249
                self.match(AMMScriptParser.ELSE)
                self.state = 250
                self.match(AMMScriptParser.LBRACE)
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552880348) != 0):
                    self.state = 251
                    self.statementInLoop()
                    self.state = 256
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 257
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
            self.state = 260
            self.match(AMMScriptParser.IF)
            self.state = 261
            self.expr(0)
            self.state = 262
            self.match(AMMScriptParser.LBRACE)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877788) != 0):
                self.state = 263
                self.statementInFunction()
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 269
            self.match(AMMScriptParser.RBRACE)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 270
                    self.match(AMMScriptParser.ELSE)
                    self.state = 271
                    self.match(AMMScriptParser.IF)
                    self.state = 272
                    self.expr(0)
                    self.state = 273
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 277
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877788) != 0):
                        self.state = 274
                        self.statementInFunction()
                        self.state = 279
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 280
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 287
                self.match(AMMScriptParser.ELSE)
                self.state = 288
                self.match(AMMScriptParser.LBRACE)
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877788) != 0):
                    self.state = 289
                    self.statementInFunction()
                    self.state = 294
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 295
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
            self.state = 298
            self.match(AMMScriptParser.IF)
            self.state = 299
            self.expr(0)
            self.state = 300
            self.match(AMMScriptParser.LBRACE)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552876764) != 0):
                self.state = 301
                self.statementInFunctionAndLoop()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 307
            self.match(AMMScriptParser.RBRACE)
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 308
                    self.match(AMMScriptParser.ELSE)
                    self.state = 309
                    self.match(AMMScriptParser.IF)
                    self.state = 310
                    self.expr(0)
                    self.state = 311
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 315
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552876764) != 0):
                        self.state = 312
                        self.statementInFunctionAndLoop()
                        self.state = 317
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 318
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 325
                self.match(AMMScriptParser.ELSE)
                self.state = 326
                self.match(AMMScriptParser.LBRACE)
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552876764) != 0):
                    self.state = 327
                    self.statementInFunctionAndLoop()
                    self.state = 332
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 333
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
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.forLoop()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.forLoopInFunction()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
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
            self.state = 344
            self.match(AMMScriptParser.FOR)
            self.state = 345
            self.variableDeclaration()
            self.state = 346
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 347
            self.expr(0)
            self.state = 348
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 349
            self.variableAsignment()
            self.state = 350
            self.match(AMMScriptParser.LBRACE)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552880348) != 0):
                self.state = 351
                self.statementInLoop()
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 357
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
            self.state = 359
            self.match(AMMScriptParser.FOR)
            self.state = 360
            self.variableDeclaration()
            self.state = 361
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 362
            self.expr(0)
            self.state = 363
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 364
            self.variableAsignment()
            self.state = 365
            self.match(AMMScriptParser.LBRACE)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552876764) != 0):
                self.state = 366
                self.statementInFunctionAndLoop()
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 372
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
            self.state = 374
            self.match(AMMScriptParser.WHILE)
            self.state = 375
            self.expr(0)
            self.state = 376
            self.match(AMMScriptParser.LBRACE)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552880348) != 0):
                self.state = 377
                self.statementInLoop()
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 383
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
            self.state = 385
            self.match(AMMScriptParser.WHILE)
            self.state = 386
            self.expr(0)
            self.state = 387
            self.match(AMMScriptParser.LBRACE)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552876764) != 0):
                self.state = 388
                self.statementInFunctionAndLoop()
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 394
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
            self.state = 396
            self.match(AMMScriptParser.SWITCH)
            self.state = 397
            self.expr(0)
            self.state = 398
            self.match(AMMScriptParser.LBRACE)
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 399
                self.match(AMMScriptParser.CASE)
                self.state = 400
                self.expr(0)
                self.state = 401
                self.match(AMMScriptParser.COLON)
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877532) != 0):
                    self.state = 402
                    self.statement()
                    self.state = 407
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 408
                    self.match(AMMScriptParser.BREAK)
                    self.state = 409
                    self.match(AMMScriptParser.SEMICOLON)


                self.state = 416
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 417
                self.match(AMMScriptParser.DEFAULT)
                self.state = 418
                self.match(AMMScriptParser.COLON)
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877532) != 0):
                    self.state = 419
                    self.statement()
                    self.state = 424
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 427
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 425
                    self.match(AMMScriptParser.BREAK)
                    self.state = 426
                    self.match(AMMScriptParser.SEMICOLON)




            self.state = 431
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
            self.state = 433
            self.match(AMMScriptParser.SWITCH)
            self.state = 434
            self.expr(0)
            self.state = 435
            self.match(AMMScriptParser.LBRACE)
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 436
                self.match(AMMScriptParser.CASE)
                self.state = 437
                self.expr(0)
                self.state = 438
                self.match(AMMScriptParser.COLON)
                self.state = 442
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877788) != 0):
                    self.state = 439
                    self.statementInFunction()
                    self.state = 444
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 445
                    self.match(AMMScriptParser.BREAK)
                    self.state = 446
                    self.match(AMMScriptParser.SEMICOLON)


                self.state = 453
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 454
                self.match(AMMScriptParser.DEFAULT)
                self.state = 455
                self.match(AMMScriptParser.COLON)
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877788) != 0):
                    self.state = 456
                    self.statementInFunction()
                    self.state = 461
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 462
                    self.match(AMMScriptParser.BREAK)
                    self.state = 463
                    self.match(AMMScriptParser.SEMICOLON)




            self.state = 468
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
            self.state = 470
            self.match(AMMScriptParser.FUNCTION)
            self.state = 471
            self.match(AMMScriptParser.ID)
            self.state = 472
            self.match(AMMScriptParser.LPAREN)
            self.state = 489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 473
                self.match(AMMScriptParser.ID)
                self.state = 476
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 474
                    self.match(AMMScriptParser.EQUAL)
                    self.state = 475
                    self.expr(0)


                self.state = 486
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==48:
                    self.state = 478
                    self.match(AMMScriptParser.COMMA)
                    self.state = 479
                    self.match(AMMScriptParser.ID)
                    self.state = 482
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==21:
                        self.state = 480
                        self.match(AMMScriptParser.EQUAL)
                        self.state = 481
                        self.expr(0)


                    self.state = 488
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 491
            self.match(AMMScriptParser.RPAREN)
            self.state = 492
            self.match(AMMScriptParser.LBRACE)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552877788) != 0):
                self.state = 493
                self.statementInFunction()
                self.state = 498
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 499
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
            self.state = 501
            self.match(AMMScriptParser.ID)
            self.state = 502
            self.match(AMMScriptParser.LPAREN)
            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2268322552872960) != 0):
                self.state = 503
                self.expr(0)
                self.state = 508
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==48:
                    self.state = 504
                    self.match(AMMScriptParser.COMMA)
                    self.state = 505
                    self.expr(0)
                    self.state = 510
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 513
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
            self.state = 515
            self.match(AMMScriptParser.ID)
            self.state = 516
            self.match(AMMScriptParser.LBRACKET)
            self.state = 517
            self.match(AMMScriptParser.NUMBER)
            self.state = 518
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


    class ExprUnaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AMMScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryExpr(self):
            return self.getTypedRuleContext(AMMScriptParser.UnaryExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprUnary" ):
                return visitor.visitExprUnary(self)
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
            self.state = 533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = AMMScriptParser.ExprParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 521
                self.match(AMMScriptParser.LPAREN)
                self.state = 522
                self.expr(0)
                self.state = 523
                self.match(AMMScriptParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = AMMScriptParser.ExprNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 525
                self.match(AMMScriptParser.NUMBER)
                pass

            elif la_ == 3:
                localctx = AMMScriptParser.ExprStringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 526
                self.match(AMMScriptParser.STRING)
                pass

            elif la_ == 4:
                localctx = AMMScriptParser.ExprTrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 527
                self.match(AMMScriptParser.TRUE)
                pass

            elif la_ == 5:
                localctx = AMMScriptParser.ExprFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 528
                self.match(AMMScriptParser.FALSE)
                pass

            elif la_ == 6:
                localctx = AMMScriptParser.ExprFunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 529
                self.functionCall()
                pass

            elif la_ == 7:
                localctx = AMMScriptParser.ExprUnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 530
                self.unaryExpr()
                pass

            elif la_ == 8:
                localctx = AMMScriptParser.ExprArrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 531
                self.arrayExpr()
                pass

            elif la_ == 9:
                localctx = AMMScriptParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 532
                self.match(AMMScriptParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 552
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 550
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = AMMScriptParser.ExprPowerContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 535
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 536
                        self.match(AMMScriptParser.POWER)
                        self.state = 537
                        self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = AMMScriptParser.ExprMultDivModContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 538
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 539
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2952790016) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 540
                        self.expr(13)
                        pass

                    elif la_ == 3:
                        localctx = AMMScriptParser.ExprPlusMinusContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 541
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 542
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 543
                        self.expr(12)
                        pass

                    elif la_ == 4:
                        localctx = AMMScriptParser.ExprComparisonContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 544
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 545
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 546
                        self.expr(11)
                        pass

                    elif la_ == 5:
                        localctx = AMMScriptParser.ExprAndOrContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 547
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 548
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==44 or _la==45):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 549
                        self.expr(10)
                        pass

             
                self.state = 554
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AMMScriptParser.ID, 0)

        def PLUS_PLUS(self):
            return self.getToken(AMMScriptParser.PLUS_PLUS, 0)

        def MINUS_MINUS(self):
            return self.getToken(AMMScriptParser.MINUS_MINUS, 0)

        def getRuleIndex(self):
            return AMMScriptParser.RULE_unaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = AMMScriptParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_unaryExpr)
        try:
            self.state = 563
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.match(AMMScriptParser.ID)
                self.state = 556
                self.match(AMMScriptParser.PLUS_PLUS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
                self.match(AMMScriptParser.ID)
                self.state = 558
                self.match(AMMScriptParser.MINUS_MINUS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 559
                self.match(AMMScriptParser.PLUS_PLUS)
                self.state = 560
                self.match(AMMScriptParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 561
                self.match(AMMScriptParser.MINUS_MINUS)
                self.state = 562
                self.match(AMMScriptParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         




