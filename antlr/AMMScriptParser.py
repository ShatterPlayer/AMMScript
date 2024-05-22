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
        4,1,50,592,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,5,0,54,
        8,0,10,0,12,0,57,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,80,8,1,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,104,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,128,8,3,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,155,8,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,169,8,5,10,5,12,5,172,9,5,3,5,174,
        8,5,1,5,3,5,177,8,5,1,6,1,6,1,6,1,6,1,6,3,6,184,8,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,196,8,8,10,8,12,8,199,9,8,1,8,1,
        8,1,8,1,8,1,8,1,8,5,8,207,8,8,10,8,12,8,210,9,8,1,8,1,8,5,8,214,
        8,8,10,8,12,8,217,9,8,1,8,1,8,1,8,5,8,222,8,8,10,8,12,8,225,9,8,
        1,8,3,8,228,8,8,1,9,1,9,1,9,1,9,5,9,234,8,9,10,9,12,9,237,9,9,1,
        9,1,9,1,9,1,9,1,9,1,9,5,9,245,8,9,10,9,12,9,248,9,9,1,9,1,9,5,9,
        252,8,9,10,9,12,9,255,9,9,1,9,1,9,1,9,5,9,260,8,9,10,9,12,9,263,
        9,9,1,9,3,9,266,8,9,1,10,1,10,1,10,1,10,5,10,272,8,10,10,10,12,10,
        275,9,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,283,8,10,10,10,12,10,
        286,9,10,1,10,1,10,5,10,290,8,10,10,10,12,10,293,9,10,1,10,1,10,
        1,10,5,10,298,8,10,10,10,12,10,301,9,10,1,10,3,10,304,8,10,1,11,
        1,11,1,11,1,11,5,11,310,8,11,10,11,12,11,313,9,11,1,11,1,11,1,11,
        1,11,1,11,1,11,5,11,321,8,11,10,11,12,11,324,9,11,1,11,1,11,5,11,
        328,8,11,10,11,12,11,331,9,11,1,11,1,11,1,11,5,11,336,8,11,10,11,
        12,11,339,9,11,1,11,3,11,342,8,11,1,12,1,12,1,12,3,12,347,8,12,1,
        13,1,13,1,13,3,13,352,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,5,14,362,8,14,10,14,12,14,365,9,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,5,15,377,8,15,10,15,12,15,380,9,15,1,15,1,
        15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,391,8,16,10,16,12,16,
        394,9,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,5,17,405,8,
        17,10,17,12,17,408,9,17,1,17,1,17,1,18,1,18,1,18,1,18,5,18,416,8,
        18,10,18,12,18,419,9,18,1,18,1,18,1,19,1,19,1,19,1,19,5,19,427,8,
        19,10,19,12,19,430,9,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,5,20,441,8,20,10,20,12,20,444,9,20,1,20,1,20,3,20,448,8,20,
        5,20,450,8,20,10,20,12,20,453,9,20,1,20,1,20,1,20,5,20,458,8,20,
        10,20,12,20,461,9,20,1,20,1,20,3,20,465,8,20,3,20,467,8,20,1,20,
        1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,478,8,21,10,21,12,21,
        481,9,21,1,21,1,21,3,21,485,8,21,5,21,487,8,21,10,21,12,21,490,9,
        21,1,21,1,21,1,21,5,21,495,8,21,10,21,12,21,498,9,21,1,21,1,21,3,
        21,502,8,21,3,21,504,8,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,
        3,22,514,8,22,1,22,1,22,1,22,1,22,3,22,520,8,22,5,22,522,8,22,10,
        22,12,22,525,9,22,3,22,527,8,22,1,22,1,22,1,22,5,22,532,8,22,10,
        22,12,22,535,9,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,5,23,544,8,
        23,10,23,12,23,547,9,23,3,23,549,8,23,1,23,1,23,1,24,1,24,1,24,1,
        24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,3,25,570,8,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,5,25,587,8,25,10,25,12,25,590,9,25,1,
        25,0,1,50,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,0,5,1,0,22,26,2,0,29,30,32,32,1,0,27,28,1,0,
        16,21,1,0,43,44,665,0,55,1,0,0,0,2,79,1,0,0,0,4,103,1,0,0,0,6,127,
        1,0,0,0,8,154,1,0,0,0,10,156,1,0,0,0,12,178,1,0,0,0,14,188,1,0,0,
        0,16,191,1,0,0,0,18,229,1,0,0,0,20,267,1,0,0,0,22,305,1,0,0,0,24,
        346,1,0,0,0,26,351,1,0,0,0,28,353,1,0,0,0,30,368,1,0,0,0,32,383,
        1,0,0,0,34,397,1,0,0,0,36,411,1,0,0,0,38,422,1,0,0,0,40,433,1,0,
        0,0,42,470,1,0,0,0,44,507,1,0,0,0,46,538,1,0,0,0,48,552,1,0,0,0,
        50,569,1,0,0,0,52,54,3,2,1,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,
        0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,0,0,1,59,
        1,1,0,0,0,60,61,3,10,5,0,61,62,5,48,0,0,62,80,1,0,0,0,63,64,3,12,
        6,0,64,65,5,48,0,0,65,80,1,0,0,0,66,67,3,14,7,0,67,68,5,48,0,0,68,
        80,1,0,0,0,69,70,3,46,23,0,70,71,5,48,0,0,71,80,1,0,0,0,72,73,3,
        50,25,0,73,74,5,48,0,0,74,80,1,0,0,0,75,80,3,16,8,0,76,80,3,24,12,
        0,77,80,3,44,22,0,78,80,3,40,20,0,79,60,1,0,0,0,79,63,1,0,0,0,79,
        66,1,0,0,0,79,69,1,0,0,0,79,72,1,0,0,0,79,75,1,0,0,0,79,76,1,0,0,
        0,79,77,1,0,0,0,79,78,1,0,0,0,80,3,1,0,0,0,81,82,3,10,5,0,82,83,
        5,48,0,0,83,104,1,0,0,0,84,85,3,12,6,0,85,86,5,48,0,0,86,104,1,0,
        0,0,87,88,3,14,7,0,88,89,5,48,0,0,89,104,1,0,0,0,90,91,3,46,23,0,
        91,92,5,48,0,0,92,104,1,0,0,0,93,94,3,50,25,0,94,95,5,48,0,0,95,
        104,1,0,0,0,96,104,3,18,9,0,97,104,3,24,12,0,98,99,5,11,0,0,99,104,
        5,48,0,0,100,101,5,12,0,0,101,104,5,48,0,0,102,104,3,40,20,0,103,
        81,1,0,0,0,103,84,1,0,0,0,103,87,1,0,0,0,103,90,1,0,0,0,103,93,1,
        0,0,0,103,96,1,0,0,0,103,97,1,0,0,0,103,98,1,0,0,0,103,100,1,0,0,
        0,103,102,1,0,0,0,104,5,1,0,0,0,105,106,3,10,5,0,106,107,5,48,0,
        0,107,128,1,0,0,0,108,109,3,12,6,0,109,110,5,48,0,0,110,128,1,0,
        0,0,111,112,3,14,7,0,112,113,5,48,0,0,113,128,1,0,0,0,114,115,3,
        46,23,0,115,116,5,48,0,0,116,128,1,0,0,0,117,118,3,50,25,0,118,119,
        5,48,0,0,119,128,1,0,0,0,120,128,3,20,10,0,121,128,3,26,13,0,122,
        123,5,10,0,0,123,124,3,50,25,0,124,125,5,48,0,0,125,128,1,0,0,0,
        126,128,3,42,21,0,127,105,1,0,0,0,127,108,1,0,0,0,127,111,1,0,0,
        0,127,114,1,0,0,0,127,117,1,0,0,0,127,120,1,0,0,0,127,121,1,0,0,
        0,127,122,1,0,0,0,127,126,1,0,0,0,128,7,1,0,0,0,129,130,3,10,5,0,
        130,131,5,48,0,0,131,155,1,0,0,0,132,133,3,12,6,0,133,134,5,48,0,
        0,134,155,1,0,0,0,135,136,3,14,7,0,136,137,5,48,0,0,137,155,1,0,
        0,0,138,139,3,46,23,0,139,140,5,48,0,0,140,155,1,0,0,0,141,142,3,
        50,25,0,142,143,5,48,0,0,143,155,1,0,0,0,144,155,3,22,11,0,145,155,
        3,26,13,0,146,147,5,11,0,0,147,155,5,48,0,0,148,149,5,12,0,0,149,
        155,5,48,0,0,150,151,5,10,0,0,151,152,3,50,25,0,152,153,5,48,0,0,
        153,155,1,0,0,0,154,129,1,0,0,0,154,132,1,0,0,0,154,135,1,0,0,0,
        154,138,1,0,0,0,154,141,1,0,0,0,154,144,1,0,0,0,154,145,1,0,0,0,
        154,146,1,0,0,0,154,148,1,0,0,0,154,150,1,0,0,0,155,9,1,0,0,0,156,
        157,5,2,0,0,157,176,5,50,0,0,158,159,5,22,0,0,159,177,3,50,25,0,
        160,161,5,37,0,0,161,162,5,39,0,0,162,163,5,38,0,0,163,164,5,22,
        0,0,164,173,5,37,0,0,165,170,3,50,25,0,166,167,5,47,0,0,167,169,
        3,50,25,0,168,166,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,
        1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,173,165,1,0,0,0,173,174,
        1,0,0,0,174,175,1,0,0,0,175,177,5,38,0,0,176,158,1,0,0,0,176,160,
        1,0,0,0,177,11,1,0,0,0,178,183,5,50,0,0,179,180,5,37,0,0,180,181,
        3,50,25,0,181,182,5,38,0,0,182,184,1,0,0,0,183,179,1,0,0,0,183,184,
        1,0,0,0,184,185,1,0,0,0,185,186,7,0,0,0,186,187,3,50,25,0,187,13,
        1,0,0,0,188,189,5,3,0,0,189,190,3,50,25,0,190,15,1,0,0,0,191,192,
        5,4,0,0,192,193,3,50,25,0,193,197,5,35,0,0,194,196,3,2,1,0,195,194,
        1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,200,
        1,0,0,0,199,197,1,0,0,0,200,215,5,36,0,0,201,202,5,5,0,0,202,203,
        5,4,0,0,203,204,3,50,25,0,204,208,5,35,0,0,205,207,3,2,1,0,206,205,
        1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,211,
        1,0,0,0,210,208,1,0,0,0,211,212,5,36,0,0,212,214,1,0,0,0,213,201,
        1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,227,
        1,0,0,0,217,215,1,0,0,0,218,219,5,5,0,0,219,223,5,35,0,0,220,222,
        3,2,1,0,221,220,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,224,
        1,0,0,0,224,226,1,0,0,0,225,223,1,0,0,0,226,228,5,36,0,0,227,218,
        1,0,0,0,227,228,1,0,0,0,228,17,1,0,0,0,229,230,5,4,0,0,230,231,3,
        50,25,0,231,235,5,35,0,0,232,234,3,4,2,0,233,232,1,0,0,0,234,237,
        1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,238,1,0,0,0,237,235,
        1,0,0,0,238,253,5,36,0,0,239,240,5,5,0,0,240,241,5,4,0,0,241,242,
        3,50,25,0,242,246,5,35,0,0,243,245,3,4,2,0,244,243,1,0,0,0,245,248,
        1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,249,1,0,0,0,248,246,
        1,0,0,0,249,250,5,36,0,0,250,252,1,0,0,0,251,239,1,0,0,0,252,255,
        1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,265,1,0,0,0,255,253,
        1,0,0,0,256,257,5,5,0,0,257,261,5,35,0,0,258,260,3,4,2,0,259,258,
        1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,264,
        1,0,0,0,263,261,1,0,0,0,264,266,5,36,0,0,265,256,1,0,0,0,265,266,
        1,0,0,0,266,19,1,0,0,0,267,268,5,4,0,0,268,269,3,50,25,0,269,273,
        5,35,0,0,270,272,3,6,3,0,271,270,1,0,0,0,272,275,1,0,0,0,273,271,
        1,0,0,0,273,274,1,0,0,0,274,276,1,0,0,0,275,273,1,0,0,0,276,291,
        5,36,0,0,277,278,5,5,0,0,278,279,5,4,0,0,279,280,3,50,25,0,280,284,
        5,35,0,0,281,283,3,6,3,0,282,281,1,0,0,0,283,286,1,0,0,0,284,282,
        1,0,0,0,284,285,1,0,0,0,285,287,1,0,0,0,286,284,1,0,0,0,287,288,
        5,36,0,0,288,290,1,0,0,0,289,277,1,0,0,0,290,293,1,0,0,0,291,289,
        1,0,0,0,291,292,1,0,0,0,292,303,1,0,0,0,293,291,1,0,0,0,294,295,
        5,5,0,0,295,299,5,35,0,0,296,298,3,6,3,0,297,296,1,0,0,0,298,301,
        1,0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,302,1,0,0,0,301,299,
        1,0,0,0,302,304,5,36,0,0,303,294,1,0,0,0,303,304,1,0,0,0,304,21,
        1,0,0,0,305,306,5,4,0,0,306,307,3,50,25,0,307,311,5,35,0,0,308,310,
        3,8,4,0,309,308,1,0,0,0,310,313,1,0,0,0,311,309,1,0,0,0,311,312,
        1,0,0,0,312,314,1,0,0,0,313,311,1,0,0,0,314,329,5,36,0,0,315,316,
        5,5,0,0,316,317,5,4,0,0,317,318,3,50,25,0,318,322,5,35,0,0,319,321,
        3,8,4,0,320,319,1,0,0,0,321,324,1,0,0,0,322,320,1,0,0,0,322,323,
        1,0,0,0,323,325,1,0,0,0,324,322,1,0,0,0,325,326,5,36,0,0,326,328,
        1,0,0,0,327,315,1,0,0,0,328,331,1,0,0,0,329,327,1,0,0,0,329,330,
        1,0,0,0,330,341,1,0,0,0,331,329,1,0,0,0,332,333,5,5,0,0,333,337,
        5,35,0,0,334,336,3,8,4,0,335,334,1,0,0,0,336,339,1,0,0,0,337,335,
        1,0,0,0,337,338,1,0,0,0,338,340,1,0,0,0,339,337,1,0,0,0,340,342,
        5,36,0,0,341,332,1,0,0,0,341,342,1,0,0,0,342,23,1,0,0,0,343,347,
        3,32,16,0,344,347,3,28,14,0,345,347,3,36,18,0,346,343,1,0,0,0,346,
        344,1,0,0,0,346,345,1,0,0,0,347,25,1,0,0,0,348,352,3,34,17,0,349,
        352,3,30,15,0,350,352,3,38,19,0,351,348,1,0,0,0,351,349,1,0,0,0,
        351,350,1,0,0,0,352,27,1,0,0,0,353,354,5,6,0,0,354,355,3,10,5,0,
        355,356,5,48,0,0,356,357,3,50,25,0,357,358,5,48,0,0,358,359,3,12,
        6,0,359,363,5,35,0,0,360,362,3,4,2,0,361,360,1,0,0,0,362,365,1,0,
        0,0,363,361,1,0,0,0,363,364,1,0,0,0,364,366,1,0,0,0,365,363,1,0,
        0,0,366,367,5,36,0,0,367,29,1,0,0,0,368,369,5,6,0,0,369,370,3,10,
        5,0,370,371,5,48,0,0,371,372,3,50,25,0,372,373,5,48,0,0,373,374,
        3,12,6,0,374,378,5,35,0,0,375,377,3,8,4,0,376,375,1,0,0,0,377,380,
        1,0,0,0,378,376,1,0,0,0,378,379,1,0,0,0,379,381,1,0,0,0,380,378,
        1,0,0,0,381,382,5,36,0,0,382,31,1,0,0,0,383,384,5,6,0,0,384,385,
        5,2,0,0,385,386,5,50,0,0,386,387,5,7,0,0,387,388,5,50,0,0,388,392,
        5,35,0,0,389,391,3,4,2,0,390,389,1,0,0,0,391,394,1,0,0,0,392,390,
        1,0,0,0,392,393,1,0,0,0,393,395,1,0,0,0,394,392,1,0,0,0,395,396,
        5,36,0,0,396,33,1,0,0,0,397,398,5,6,0,0,398,399,5,2,0,0,399,400,
        5,50,0,0,400,401,5,7,0,0,401,402,5,50,0,0,402,406,5,35,0,0,403,405,
        3,8,4,0,404,403,1,0,0,0,405,408,1,0,0,0,406,404,1,0,0,0,406,407,
        1,0,0,0,407,409,1,0,0,0,408,406,1,0,0,0,409,410,5,36,0,0,410,35,
        1,0,0,0,411,412,5,8,0,0,412,413,3,50,25,0,413,417,5,35,0,0,414,416,
        3,4,2,0,415,414,1,0,0,0,416,419,1,0,0,0,417,415,1,0,0,0,417,418,
        1,0,0,0,418,420,1,0,0,0,419,417,1,0,0,0,420,421,5,36,0,0,421,37,
        1,0,0,0,422,423,5,8,0,0,423,424,3,50,25,0,424,428,5,35,0,0,425,427,
        3,8,4,0,426,425,1,0,0,0,427,430,1,0,0,0,428,426,1,0,0,0,428,429,
        1,0,0,0,429,431,1,0,0,0,430,428,1,0,0,0,431,432,5,36,0,0,432,39,
        1,0,0,0,433,434,5,13,0,0,434,435,3,50,25,0,435,451,5,35,0,0,436,
        437,5,14,0,0,437,438,3,50,25,0,438,442,5,49,0,0,439,441,3,2,1,0,
        440,439,1,0,0,0,441,444,1,0,0,0,442,440,1,0,0,0,442,443,1,0,0,0,
        443,447,1,0,0,0,444,442,1,0,0,0,445,446,5,11,0,0,446,448,5,48,0,
        0,447,445,1,0,0,0,447,448,1,0,0,0,448,450,1,0,0,0,449,436,1,0,0,
        0,450,453,1,0,0,0,451,449,1,0,0,0,451,452,1,0,0,0,452,466,1,0,0,
        0,453,451,1,0,0,0,454,455,5,15,0,0,455,459,5,49,0,0,456,458,3,2,
        1,0,457,456,1,0,0,0,458,461,1,0,0,0,459,457,1,0,0,0,459,460,1,0,
        0,0,460,464,1,0,0,0,461,459,1,0,0,0,462,463,5,11,0,0,463,465,5,48,
        0,0,464,462,1,0,0,0,464,465,1,0,0,0,465,467,1,0,0,0,466,454,1,0,
        0,0,466,467,1,0,0,0,467,468,1,0,0,0,468,469,5,36,0,0,469,41,1,0,
        0,0,470,471,5,13,0,0,471,472,3,50,25,0,472,488,5,35,0,0,473,474,
        5,14,0,0,474,475,3,50,25,0,475,479,5,49,0,0,476,478,3,6,3,0,477,
        476,1,0,0,0,478,481,1,0,0,0,479,477,1,0,0,0,479,480,1,0,0,0,480,
        484,1,0,0,0,481,479,1,0,0,0,482,483,5,11,0,0,483,485,5,48,0,0,484,
        482,1,0,0,0,484,485,1,0,0,0,485,487,1,0,0,0,486,473,1,0,0,0,487,
        490,1,0,0,0,488,486,1,0,0,0,488,489,1,0,0,0,489,503,1,0,0,0,490,
        488,1,0,0,0,491,492,5,15,0,0,492,496,5,49,0,0,493,495,3,6,3,0,494,
        493,1,0,0,0,495,498,1,0,0,0,496,494,1,0,0,0,496,497,1,0,0,0,497,
        501,1,0,0,0,498,496,1,0,0,0,499,500,5,11,0,0,500,502,5,48,0,0,501,
        499,1,0,0,0,501,502,1,0,0,0,502,504,1,0,0,0,503,491,1,0,0,0,503,
        504,1,0,0,0,504,505,1,0,0,0,505,506,5,36,0,0,506,43,1,0,0,0,507,
        508,5,9,0,0,508,509,5,50,0,0,509,526,5,33,0,0,510,513,5,50,0,0,511,
        512,5,22,0,0,512,514,3,50,25,0,513,511,1,0,0,0,513,514,1,0,0,0,514,
        523,1,0,0,0,515,516,5,47,0,0,516,519,5,50,0,0,517,518,5,22,0,0,518,
        520,3,50,25,0,519,517,1,0,0,0,519,520,1,0,0,0,520,522,1,0,0,0,521,
        515,1,0,0,0,522,525,1,0,0,0,523,521,1,0,0,0,523,524,1,0,0,0,524,
        527,1,0,0,0,525,523,1,0,0,0,526,510,1,0,0,0,526,527,1,0,0,0,527,
        528,1,0,0,0,528,529,5,34,0,0,529,533,5,35,0,0,530,532,3,6,3,0,531,
        530,1,0,0,0,532,535,1,0,0,0,533,531,1,0,0,0,533,534,1,0,0,0,534,
        536,1,0,0,0,535,533,1,0,0,0,536,537,5,36,0,0,537,45,1,0,0,0,538,
        539,5,50,0,0,539,548,5,33,0,0,540,545,3,50,25,0,541,542,5,47,0,0,
        542,544,3,50,25,0,543,541,1,0,0,0,544,547,1,0,0,0,545,543,1,0,0,
        0,545,546,1,0,0,0,546,549,1,0,0,0,547,545,1,0,0,0,548,540,1,0,0,
        0,548,549,1,0,0,0,549,550,1,0,0,0,550,551,5,34,0,0,551,47,1,0,0,
        0,552,553,5,50,0,0,553,554,5,37,0,0,554,555,3,50,25,0,555,556,5,
        38,0,0,556,49,1,0,0,0,557,558,6,25,-1,0,558,559,5,33,0,0,559,560,
        3,50,25,0,560,561,5,34,0,0,561,570,1,0,0,0,562,570,5,39,0,0,563,
        570,5,40,0,0,564,570,5,41,0,0,565,570,5,42,0,0,566,570,3,46,23,0,
        567,570,3,48,24,0,568,570,5,50,0,0,569,557,1,0,0,0,569,562,1,0,0,
        0,569,563,1,0,0,0,569,564,1,0,0,0,569,565,1,0,0,0,569,566,1,0,0,
        0,569,567,1,0,0,0,569,568,1,0,0,0,570,588,1,0,0,0,571,572,10,12,
        0,0,572,573,5,31,0,0,573,587,3,50,25,13,574,575,10,11,0,0,575,576,
        7,1,0,0,576,587,3,50,25,12,577,578,10,10,0,0,578,579,7,2,0,0,579,
        587,3,50,25,11,580,581,10,9,0,0,581,582,7,3,0,0,582,587,3,50,25,
        10,583,584,10,8,0,0,584,585,7,4,0,0,585,587,3,50,25,9,586,571,1,
        0,0,0,586,574,1,0,0,0,586,577,1,0,0,0,586,580,1,0,0,0,586,583,1,
        0,0,0,587,590,1,0,0,0,588,586,1,0,0,0,588,589,1,0,0,0,589,51,1,0,
        0,0,590,588,1,0,0,0,59,55,79,103,127,154,170,173,176,183,197,208,
        215,223,227,235,246,253,261,265,273,284,291,299,303,311,322,329,
        337,341,346,351,363,378,392,406,417,428,442,447,451,459,464,466,
        479,484,488,496,501,503,513,519,523,526,533,545,548,569,586,588
    ]

class AMMScriptParser ( Parser ):

    grammarFileName = "AMMScriptParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'set'", "'print'", "'if'", 
                     "'else'", "'for'", "'of'", "'while'", "'func'", "'return'", 
                     "'break'", "'continue'", "'switch'", "'case'", "'default'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", 
                     "'+='", "'-='", "'*='", "'/='", "'+'", "'-'", "'*'", 
                     "'/'", "'^'", "'%'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "<INVALID>", "<INVALID>", "'true'", "'false'", 
                     "'&&'", "'||'", "'!'", "<INVALID>", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "SET", "PRINT", "IF", "ELSE", 
                      "FOR", "OF", "WHILE", "FUNCTION", "RETURN", "BREAK", 
                      "CONTINUE", "SWITCH", "CASE", "DEFAULT", "EQUAL_EQUAL", 
                      "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
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
    RULE_forOfLoop = 16
    RULE_forOfLoopInFunction = 17
    RULE_whileLoop = 18
    RULE_whileLoopInFunction = 19
    RULE_switch = 20
    RULE_switchInFunction = 21
    RULE_functionDeclaration = 22
    RULE_functionCall = 23
    RULE_arrayExpr = 24
    RULE_expr = 25

    ruleNames =  [ "program", "statement", "statementInLoop", "statementInFunction", 
                   "statementInFunctionAndLoop", "variableDeclaration", 
                   "variableAsignment", "print", "if", "ifInLoop", "ifInFunction", 
                   "ifInFunctionAndLoop", "loop", "loopInFunction", "forLoop", 
                   "forLoopInFunction", "forOfLoop", "forOfLoopInFunction", 
                   "whileLoop", "whileLoopInFunction", "switch", "switchInFunction", 
                   "functionDeclaration", "functionCall", "arrayExpr", "expr" ]

    EOF = Token.EOF
    WHITESPACE=1
    SET=2
    PRINT=3
    IF=4
    ELSE=5
    FOR=6
    OF=7
    WHILE=8
    FUNCTION=9
    RETURN=10
    BREAK=11
    CONTINUE=12
    SWITCH=13
    CASE=14
    DEFAULT=15
    EQUAL_EQUAL=16
    NOT_EQUAL=17
    LESS=18
    GREATER=19
    LESS_EQUAL=20
    GREATER_EQUAL=21
    EQUAL=22
    PLUS_EQUAL=23
    MINUS_EQUAL=24
    MULTIPLY_EQUAL=25
    DIVIDE_EQUAL=26
    PLUS=27
    MINUS=28
    MULTIPLY=29
    DIVIDE=30
    POWER=31
    MODULO=32
    LPAREN=33
    RPAREN=34
    LBRACE=35
    RBRACE=36
    LBRACKET=37
    RBRACKET=38
    NUMBER=39
    STRING=40
    TRUE=41
    FALSE=42
    AND=43
    OR=44
    NOT=45
    COMMENT=46
    COMMA=47
    SEMICOLON=48
    COLON=49
    ID=50

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
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833994588) != 0):
                self.state = 52
                self.statement()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.variableDeclaration()
                self.state = 61
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.variableAsignment()
                self.state = 64
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.print_()
                self.state = 67
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.functionCall()
                self.state = 70
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.expr(0)
                self.state = 73
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 75
                self.if_()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 76
                self.loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 77
                self.functionDeclaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 78
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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.variableDeclaration()
                self.state = 82
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.variableAsignment()
                self.state = 85
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.print_()
                self.state = 88
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.functionCall()
                self.state = 91
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.ifInLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 97
                self.loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 98
                self.match(AMMScriptParser.BREAK)
                self.state = 99
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 100
                self.match(AMMScriptParser.CONTINUE)
                self.state = 101
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 102
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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.variableDeclaration()
                self.state = 106
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.variableAsignment()
                self.state = 109
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.print_()
                self.state = 112
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.functionCall()
                self.state = 115
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 117
                self.expr(0)
                self.state = 118
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 120
                self.ifInFunction()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 121
                self.loopInFunction()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 122
                self.match(AMMScriptParser.RETURN)
                self.state = 123
                self.expr(0)
                self.state = 124
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 126
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
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.variableDeclaration()
                self.state = 130
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.variableAsignment()
                self.state = 133
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.print_()
                self.state = 136
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.functionCall()
                self.state = 139
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.expr(0)
                self.state = 142
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 144
                self.ifInFunctionAndLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 145
                self.loopInFunction()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 146
                self.match(AMMScriptParser.BREAK)
                self.state = 147
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 148
                self.match(AMMScriptParser.CONTINUE)
                self.state = 149
                self.match(AMMScriptParser.SEMICOLON)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 150
                self.match(AMMScriptParser.RETURN)
                self.state = 151
                self.expr(0)
                self.state = 152
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
            self.state = 156
            self.match(AMMScriptParser.SET)
            self.state = 157
            self.match(AMMScriptParser.ID)
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 158
                self.match(AMMScriptParser.EQUAL)
                self.state = 159
                self.expr(0)
                pass
            elif token in [37]:
                self.state = 160
                self.match(AMMScriptParser.LBRACKET)
                self.state = 161
                self.match(AMMScriptParser.NUMBER)
                self.state = 162
                self.match(AMMScriptParser.RBRACKET)
                self.state = 163
                self.match(AMMScriptParser.EQUAL)
                self.state = 164
                self.match(AMMScriptParser.LBRACKET)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833985536) != 0):
                    self.state = 165
                    self.expr(0)
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==47:
                        self.state = 166
                        self.match(AMMScriptParser.COMMA)
                        self.state = 167
                        self.expr(0)
                        self.state = 172
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 175
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AMMScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(AMMScriptParser.ExprContext,i)


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
            self.state = 178
            self.match(AMMScriptParser.ID)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 179
                self.match(AMMScriptParser.LBRACKET)
                self.state = 180
                self.expr(0)
                self.state = 181
                self.match(AMMScriptParser.RBRACKET)


            self.state = 185
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 130023424) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 186
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
            self.state = 188
            self.match(AMMScriptParser.PRINT)
            self.state = 189
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
            self.state = 191
            self.match(AMMScriptParser.IF)
            self.state = 192
            self.expr(0)
            self.state = 193
            self.match(AMMScriptParser.LBRACE)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833994588) != 0):
                self.state = 194
                self.statement()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            self.match(AMMScriptParser.RBRACE)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 201
                    self.match(AMMScriptParser.ELSE)
                    self.state = 202
                    self.match(AMMScriptParser.IF)
                    self.state = 203
                    self.expr(0)
                    self.state = 204
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833994588) != 0):
                        self.state = 205
                        self.statement()
                        self.state = 210
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 211
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 218
                self.match(AMMScriptParser.ELSE)
                self.state = 219
                self.match(AMMScriptParser.LBRACE)
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833994588) != 0):
                    self.state = 220
                    self.statement()
                    self.state = 225
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 226
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
            self.state = 229
            self.match(AMMScriptParser.IF)
            self.state = 230
            self.expr(0)
            self.state = 231
            self.match(AMMScriptParser.LBRACE)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154834000220) != 0):
                self.state = 232
                self.statementInLoop()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 238
            self.match(AMMScriptParser.RBRACE)
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 239
                    self.match(AMMScriptParser.ELSE)
                    self.state = 240
                    self.match(AMMScriptParser.IF)
                    self.state = 241
                    self.expr(0)
                    self.state = 242
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 246
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154834000220) != 0):
                        self.state = 243
                        self.statementInLoop()
                        self.state = 248
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 249
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 256
                self.match(AMMScriptParser.ELSE)
                self.state = 257
                self.match(AMMScriptParser.LBRACE)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154834000220) != 0):
                    self.state = 258
                    self.statementInLoop()
                    self.state = 263
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 264
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
            self.state = 267
            self.match(AMMScriptParser.IF)
            self.state = 268
            self.expr(0)
            self.state = 269
            self.match(AMMScriptParser.LBRACE)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833995100) != 0):
                self.state = 270
                self.statementInFunction()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 276
            self.match(AMMScriptParser.RBRACE)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 277
                    self.match(AMMScriptParser.ELSE)
                    self.state = 278
                    self.match(AMMScriptParser.IF)
                    self.state = 279
                    self.expr(0)
                    self.state = 280
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 284
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833995100) != 0):
                        self.state = 281
                        self.statementInFunction()
                        self.state = 286
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 287
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 294
                self.match(AMMScriptParser.ELSE)
                self.state = 295
                self.match(AMMScriptParser.LBRACE)
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833995100) != 0):
                    self.state = 296
                    self.statementInFunction()
                    self.state = 301
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 302
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
            self.state = 305
            self.match(AMMScriptParser.IF)
            self.state = 306
            self.expr(0)
            self.state = 307
            self.match(AMMScriptParser.LBRACE)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833993052) != 0):
                self.state = 308
                self.statementInFunctionAndLoop()
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 314
            self.match(AMMScriptParser.RBRACE)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 315
                    self.match(AMMScriptParser.ELSE)
                    self.state = 316
                    self.match(AMMScriptParser.IF)
                    self.state = 317
                    self.expr(0)
                    self.state = 318
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 322
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833993052) != 0):
                        self.state = 319
                        self.statementInFunctionAndLoop()
                        self.state = 324
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 325
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 332
                self.match(AMMScriptParser.ELSE)
                self.state = 333
                self.match(AMMScriptParser.LBRACE)
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833993052) != 0):
                    self.state = 334
                    self.statementInFunctionAndLoop()
                    self.state = 339
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 340
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

        def forOfLoop(self):
            return self.getTypedRuleContext(AMMScriptParser.ForOfLoopContext,0)


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
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.forOfLoop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.forLoop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.whileLoop()
                pass


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

        def forOfLoopInFunction(self):
            return self.getTypedRuleContext(AMMScriptParser.ForOfLoopInFunctionContext,0)


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
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.forOfLoopInFunction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.forLoopInFunction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
                self.whileLoopInFunction()
                pass


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
            self.state = 353
            self.match(AMMScriptParser.FOR)
            self.state = 354
            self.variableDeclaration()
            self.state = 355
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 356
            self.expr(0)
            self.state = 357
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 358
            self.variableAsignment()
            self.state = 359
            self.match(AMMScriptParser.LBRACE)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154834000220) != 0):
                self.state = 360
                self.statementInLoop()
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 366
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
            self.state = 368
            self.match(AMMScriptParser.FOR)
            self.state = 369
            self.variableDeclaration()
            self.state = 370
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 371
            self.expr(0)
            self.state = 372
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 373
            self.variableAsignment()
            self.state = 374
            self.match(AMMScriptParser.LBRACE)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833993052) != 0):
                self.state = 375
                self.statementInFunctionAndLoop()
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


    class ForOfLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(AMMScriptParser.FOR, 0)

        def SET(self):
            return self.getToken(AMMScriptParser.SET, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.ID)
            else:
                return self.getToken(AMMScriptParser.ID, i)

        def OF(self):
            return self.getToken(AMMScriptParser.OF, 0)

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
            return AMMScriptParser.RULE_forOfLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForOfLoop" ):
                return visitor.visitForOfLoop(self)
            else:
                return visitor.visitChildren(self)




    def forOfLoop(self):

        localctx = AMMScriptParser.ForOfLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forOfLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(AMMScriptParser.FOR)
            self.state = 384
            self.match(AMMScriptParser.SET)
            self.state = 385
            self.match(AMMScriptParser.ID)
            self.state = 386
            self.match(AMMScriptParser.OF)
            self.state = 387
            self.match(AMMScriptParser.ID)
            self.state = 388
            self.match(AMMScriptParser.LBRACE)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154834000220) != 0):
                self.state = 389
                self.statementInLoop()
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 395
            self.match(AMMScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForOfLoopInFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(AMMScriptParser.FOR, 0)

        def SET(self):
            return self.getToken(AMMScriptParser.SET, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AMMScriptParser.ID)
            else:
                return self.getToken(AMMScriptParser.ID, i)

        def OF(self):
            return self.getToken(AMMScriptParser.OF, 0)

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
            return AMMScriptParser.RULE_forOfLoopInFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForOfLoopInFunction" ):
                return visitor.visitForOfLoopInFunction(self)
            else:
                return visitor.visitChildren(self)




    def forOfLoopInFunction(self):

        localctx = AMMScriptParser.ForOfLoopInFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_forOfLoopInFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(AMMScriptParser.FOR)
            self.state = 398
            self.match(AMMScriptParser.SET)
            self.state = 399
            self.match(AMMScriptParser.ID)
            self.state = 400
            self.match(AMMScriptParser.OF)
            self.state = 401
            self.match(AMMScriptParser.ID)
            self.state = 402
            self.match(AMMScriptParser.LBRACE)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833993052) != 0):
                self.state = 403
                self.statementInFunctionAndLoop()
                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 409
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
        self.enterRule(localctx, 36, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(AMMScriptParser.WHILE)
            self.state = 412
            self.expr(0)
            self.state = 413
            self.match(AMMScriptParser.LBRACE)
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154834000220) != 0):
                self.state = 414
                self.statementInLoop()
                self.state = 419
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 420
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
        self.enterRule(localctx, 38, self.RULE_whileLoopInFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(AMMScriptParser.WHILE)
            self.state = 423
            self.expr(0)
            self.state = 424
            self.match(AMMScriptParser.LBRACE)
            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833993052) != 0):
                self.state = 425
                self.statementInFunctionAndLoop()
                self.state = 430
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 431
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
        self.enterRule(localctx, 40, self.RULE_switch)
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
            while _la==14:
                self.state = 436
                self.match(AMMScriptParser.CASE)
                self.state = 437
                self.expr(0)
                self.state = 438
                self.match(AMMScriptParser.COLON)
                self.state = 442
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833994588) != 0):
                    self.state = 439
                    self.statement()
                    self.state = 444
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
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
            if _la==15:
                self.state = 454
                self.match(AMMScriptParser.DEFAULT)
                self.state = 455
                self.match(AMMScriptParser.COLON)
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833994588) != 0):
                    self.state = 456
                    self.statement()
                    self.state = 461
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
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
        self.enterRule(localctx, 42, self.RULE_switchInFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(AMMScriptParser.SWITCH)
            self.state = 471
            self.expr(0)
            self.state = 472
            self.match(AMMScriptParser.LBRACE)
            self.state = 488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 473
                self.match(AMMScriptParser.CASE)
                self.state = 474
                self.expr(0)
                self.state = 475
                self.match(AMMScriptParser.COLON)
                self.state = 479
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833995100) != 0):
                    self.state = 476
                    self.statementInFunction()
                    self.state = 481
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 482
                    self.match(AMMScriptParser.BREAK)
                    self.state = 483
                    self.match(AMMScriptParser.SEMICOLON)


                self.state = 490
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 491
                self.match(AMMScriptParser.DEFAULT)
                self.state = 492
                self.match(AMMScriptParser.COLON)
                self.state = 496
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833995100) != 0):
                    self.state = 493
                    self.statementInFunction()
                    self.state = 498
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 501
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 499
                    self.match(AMMScriptParser.BREAK)
                    self.state = 500
                    self.match(AMMScriptParser.SEMICOLON)




            self.state = 505
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
        self.enterRule(localctx, 44, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(AMMScriptParser.FUNCTION)
            self.state = 508
            self.match(AMMScriptParser.ID)
            self.state = 509
            self.match(AMMScriptParser.LPAREN)
            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 510
                self.match(AMMScriptParser.ID)
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 511
                    self.match(AMMScriptParser.EQUAL)
                    self.state = 512
                    self.expr(0)


                self.state = 523
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==47:
                    self.state = 515
                    self.match(AMMScriptParser.COMMA)
                    self.state = 516
                    self.match(AMMScriptParser.ID)
                    self.state = 519
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==22:
                        self.state = 517
                        self.match(AMMScriptParser.EQUAL)
                        self.state = 518
                        self.expr(0)


                    self.state = 525
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 528
            self.match(AMMScriptParser.RPAREN)
            self.state = 529
            self.match(AMMScriptParser.LBRACE)
            self.state = 533
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833995100) != 0):
                self.state = 530
                self.statementInFunction()
                self.state = 535
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 536
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
        self.enterRule(localctx, 46, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(AMMScriptParser.ID)
            self.state = 539
            self.match(AMMScriptParser.LPAREN)
            self.state = 548
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134154833985536) != 0):
                self.state = 540
                self.expr(0)
                self.state = 545
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==47:
                    self.state = 541
                    self.match(AMMScriptParser.COMMA)
                    self.state = 542
                    self.expr(0)
                    self.state = 547
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 550
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

        def expr(self):
            return self.getTypedRuleContext(AMMScriptParser.ExprContext,0)


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
        self.enterRule(localctx, 48, self.RULE_arrayExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.match(AMMScriptParser.ID)
            self.state = 553
            self.match(AMMScriptParser.LBRACKET)
            self.state = 554
            self.expr(0)
            self.state = 555
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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                localctx = AMMScriptParser.ExprParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 558
                self.match(AMMScriptParser.LPAREN)
                self.state = 559
                self.expr(0)
                self.state = 560
                self.match(AMMScriptParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = AMMScriptParser.ExprNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 562
                self.match(AMMScriptParser.NUMBER)
                pass

            elif la_ == 3:
                localctx = AMMScriptParser.ExprStringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 563
                self.match(AMMScriptParser.STRING)
                pass

            elif la_ == 4:
                localctx = AMMScriptParser.ExprTrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 564
                self.match(AMMScriptParser.TRUE)
                pass

            elif la_ == 5:
                localctx = AMMScriptParser.ExprFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 565
                self.match(AMMScriptParser.FALSE)
                pass

            elif la_ == 6:
                localctx = AMMScriptParser.ExprFunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 566
                self.functionCall()
                pass

            elif la_ == 7:
                localctx = AMMScriptParser.ExprArrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 567
                self.arrayExpr()
                pass

            elif la_ == 8:
                localctx = AMMScriptParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 568
                self.match(AMMScriptParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 588
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 586
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                    if la_ == 1:
                        localctx = AMMScriptParser.ExprPowerContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 571
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 572
                        self.match(AMMScriptParser.POWER)
                        self.state = 573
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = AMMScriptParser.ExprMultDivModContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 574
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 575
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 5905580032) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 576
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = AMMScriptParser.ExprPlusMinusContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 577
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 578
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 579
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = AMMScriptParser.ExprComparisonContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 580
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 581
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 582
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = AMMScriptParser.ExprAndOrContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 583
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 584
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==43 or _la==44):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 585
                        self.expr(9)
                        pass

             
                self.state = 590
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

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
        self._predicates[25] = self.expr_sempred
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
         




