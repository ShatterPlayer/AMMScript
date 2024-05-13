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
        4,1,49,554,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        10,5,12,5,164,9,5,3,5,166,8,5,1,5,3,5,169,8,5,1,6,1,6,1,6,1,6,1,
        6,3,6,176,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,188,8,
        8,10,8,12,8,191,9,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,199,8,8,10,8,12,
        8,202,9,8,1,8,1,8,5,8,206,8,8,10,8,12,8,209,9,8,1,8,1,8,1,8,5,8,
        214,8,8,10,8,12,8,217,9,8,1,8,3,8,220,8,8,1,9,1,9,1,9,1,9,5,9,226,
        8,9,10,9,12,9,229,9,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,237,8,9,10,9,12,
        9,240,9,9,1,9,1,9,5,9,244,8,9,10,9,12,9,247,9,9,1,9,1,9,1,9,5,9,
        252,8,9,10,9,12,9,255,9,9,1,9,3,9,258,8,9,1,10,1,10,1,10,1,10,5,
        10,264,8,10,10,10,12,10,267,9,10,1,10,1,10,1,10,1,10,1,10,1,10,5,
        10,275,8,10,10,10,12,10,278,9,10,1,10,1,10,5,10,282,8,10,10,10,12,
        10,285,9,10,1,10,1,10,1,10,5,10,290,8,10,10,10,12,10,293,9,10,1,
        10,3,10,296,8,10,1,11,1,11,1,11,1,11,5,11,302,8,11,10,11,12,11,305,
        9,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,313,8,11,10,11,12,11,316,
        9,11,1,11,1,11,5,11,320,8,11,10,11,12,11,323,9,11,1,11,1,11,1,11,
        5,11,328,8,11,10,11,12,11,331,9,11,1,11,3,11,334,8,11,1,12,1,12,
        3,12,338,8,12,1,13,1,13,3,13,342,8,13,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,5,14,352,8,14,10,14,12,14,355,9,14,1,14,1,14,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,367,8,15,10,15,12,15,370,9,
        15,1,15,1,15,1,16,1,16,1,16,1,16,5,16,378,8,16,10,16,12,16,381,9,
        16,1,16,1,16,1,17,1,17,1,17,1,17,5,17,389,8,17,10,17,12,17,392,9,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,403,8,18,10,
        18,12,18,406,9,18,1,18,1,18,3,18,410,8,18,5,18,412,8,18,10,18,12,
        18,415,9,18,1,18,1,18,1,18,5,18,420,8,18,10,18,12,18,423,9,18,1,
        18,1,18,3,18,427,8,18,3,18,429,8,18,1,18,1,18,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,5,19,440,8,19,10,19,12,19,443,9,19,1,19,1,19,3,19,
        447,8,19,5,19,449,8,19,10,19,12,19,452,9,19,1,19,1,19,1,19,5,19,
        457,8,19,10,19,12,19,460,9,19,1,19,1,19,3,19,464,8,19,3,19,466,8,
        19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,3,20,476,8,20,1,20,1,
        20,1,20,1,20,3,20,482,8,20,5,20,484,8,20,10,20,12,20,487,9,20,3,
        20,489,8,20,1,20,1,20,1,20,5,20,494,8,20,10,20,12,20,497,9,20,1,
        20,1,20,1,21,1,21,1,21,1,21,1,21,5,21,506,8,21,10,21,12,21,509,9,
        21,3,21,511,8,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,532,8,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,5,23,549,8,23,10,23,12,23,552,9,23,1,23,0,1,46,24,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,5,
        1,0,21,25,2,0,28,29,31,31,1,0,26,27,1,0,15,20,1,0,42,43,625,0,51,
        1,0,0,0,2,75,1,0,0,0,4,97,1,0,0,0,6,121,1,0,0,0,8,146,1,0,0,0,10,
        148,1,0,0,0,12,170,1,0,0,0,14,180,1,0,0,0,16,183,1,0,0,0,18,221,
        1,0,0,0,20,259,1,0,0,0,22,297,1,0,0,0,24,337,1,0,0,0,26,341,1,0,
        0,0,28,343,1,0,0,0,30,358,1,0,0,0,32,373,1,0,0,0,34,384,1,0,0,0,
        36,395,1,0,0,0,38,432,1,0,0,0,40,469,1,0,0,0,42,500,1,0,0,0,44,514,
        1,0,0,0,46,531,1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,
        51,49,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,
        0,0,1,55,1,1,0,0,0,56,57,3,10,5,0,57,58,5,47,0,0,58,76,1,0,0,0,59,
        60,3,12,6,0,60,61,5,47,0,0,61,76,1,0,0,0,62,63,3,14,7,0,63,64,5,
        47,0,0,64,76,1,0,0,0,65,66,3,42,21,0,66,67,5,47,0,0,67,76,1,0,0,
        0,68,69,3,46,23,0,69,70,5,47,0,0,70,76,1,0,0,0,71,76,3,16,8,0,72,
        76,3,24,12,0,73,76,3,40,20,0,74,76,3,36,18,0,75,56,1,0,0,0,75,59,
        1,0,0,0,75,62,1,0,0,0,75,65,1,0,0,0,75,68,1,0,0,0,75,71,1,0,0,0,
        75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,3,1,0,0,0,77,78,3,10,
        5,0,78,79,5,47,0,0,79,98,1,0,0,0,80,81,3,12,6,0,81,82,5,47,0,0,82,
        98,1,0,0,0,83,84,3,14,7,0,84,85,5,47,0,0,85,98,1,0,0,0,86,87,3,42,
        21,0,87,88,5,47,0,0,88,98,1,0,0,0,89,90,3,46,23,0,90,91,5,47,0,0,
        91,98,1,0,0,0,92,98,3,18,9,0,93,98,3,24,12,0,94,98,5,10,0,0,95,98,
        5,11,0,0,96,98,3,36,18,0,97,77,1,0,0,0,97,80,1,0,0,0,97,83,1,0,0,
        0,97,86,1,0,0,0,97,89,1,0,0,0,97,92,1,0,0,0,97,93,1,0,0,0,97,94,
        1,0,0,0,97,95,1,0,0,0,97,96,1,0,0,0,98,5,1,0,0,0,99,100,3,10,5,0,
        100,101,5,47,0,0,101,122,1,0,0,0,102,103,3,12,6,0,103,104,5,47,0,
        0,104,122,1,0,0,0,105,106,3,14,7,0,106,107,5,47,0,0,107,122,1,0,
        0,0,108,109,3,42,21,0,109,110,5,47,0,0,110,122,1,0,0,0,111,112,3,
        46,23,0,112,113,5,47,0,0,113,122,1,0,0,0,114,122,3,20,10,0,115,122,
        3,26,13,0,116,117,5,9,0,0,117,118,3,46,23,0,118,119,5,47,0,0,119,
        122,1,0,0,0,120,122,3,38,19,0,121,99,1,0,0,0,121,102,1,0,0,0,121,
        105,1,0,0,0,121,108,1,0,0,0,121,111,1,0,0,0,121,114,1,0,0,0,121,
        115,1,0,0,0,121,116,1,0,0,0,121,120,1,0,0,0,122,7,1,0,0,0,123,124,
        3,10,5,0,124,125,5,47,0,0,125,147,1,0,0,0,126,127,3,12,6,0,127,128,
        5,47,0,0,128,147,1,0,0,0,129,130,3,14,7,0,130,131,5,47,0,0,131,147,
        1,0,0,0,132,133,3,42,21,0,133,134,5,47,0,0,134,147,1,0,0,0,135,136,
        3,46,23,0,136,137,5,47,0,0,137,147,1,0,0,0,138,147,3,22,11,0,139,
        147,3,26,13,0,140,147,5,10,0,0,141,147,5,11,0,0,142,143,5,9,0,0,
        143,144,3,46,23,0,144,145,5,47,0,0,145,147,1,0,0,0,146,123,1,0,0,
        0,146,126,1,0,0,0,146,129,1,0,0,0,146,132,1,0,0,0,146,135,1,0,0,
        0,146,138,1,0,0,0,146,139,1,0,0,0,146,140,1,0,0,0,146,141,1,0,0,
        0,146,142,1,0,0,0,147,9,1,0,0,0,148,149,5,2,0,0,149,168,5,49,0,0,
        150,151,5,21,0,0,151,169,3,46,23,0,152,153,5,36,0,0,153,154,5,38,
        0,0,154,155,5,37,0,0,155,156,5,21,0,0,156,165,5,36,0,0,157,162,3,
        46,23,0,158,159,5,46,0,0,159,161,3,46,23,0,160,158,1,0,0,0,161,164,
        1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,166,1,0,0,0,164,162,
        1,0,0,0,165,157,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,169,
        5,37,0,0,168,150,1,0,0,0,168,152,1,0,0,0,169,11,1,0,0,0,170,175,
        5,49,0,0,171,172,5,36,0,0,172,173,3,46,23,0,173,174,5,37,0,0,174,
        176,1,0,0,0,175,171,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,
        178,7,0,0,0,178,179,3,46,23,0,179,13,1,0,0,0,180,181,5,3,0,0,181,
        182,3,46,23,0,182,15,1,0,0,0,183,184,5,4,0,0,184,185,3,46,23,0,185,
        189,5,34,0,0,186,188,3,2,1,0,187,186,1,0,0,0,188,191,1,0,0,0,189,
        187,1,0,0,0,189,190,1,0,0,0,190,192,1,0,0,0,191,189,1,0,0,0,192,
        207,5,35,0,0,193,194,5,5,0,0,194,195,5,4,0,0,195,196,3,46,23,0,196,
        200,5,34,0,0,197,199,3,2,1,0,198,197,1,0,0,0,199,202,1,0,0,0,200,
        198,1,0,0,0,200,201,1,0,0,0,201,203,1,0,0,0,202,200,1,0,0,0,203,
        204,5,35,0,0,204,206,1,0,0,0,205,193,1,0,0,0,206,209,1,0,0,0,207,
        205,1,0,0,0,207,208,1,0,0,0,208,219,1,0,0,0,209,207,1,0,0,0,210,
        211,5,5,0,0,211,215,5,34,0,0,212,214,3,2,1,0,213,212,1,0,0,0,214,
        217,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,218,1,0,0,0,217,
        215,1,0,0,0,218,220,5,35,0,0,219,210,1,0,0,0,219,220,1,0,0,0,220,
        17,1,0,0,0,221,222,5,4,0,0,222,223,3,46,23,0,223,227,5,34,0,0,224,
        226,3,4,2,0,225,224,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,
        228,1,0,0,0,228,230,1,0,0,0,229,227,1,0,0,0,230,245,5,35,0,0,231,
        232,5,5,0,0,232,233,5,4,0,0,233,234,3,46,23,0,234,238,5,34,0,0,235,
        237,3,4,2,0,236,235,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,
        239,1,0,0,0,239,241,1,0,0,0,240,238,1,0,0,0,241,242,5,35,0,0,242,
        244,1,0,0,0,243,231,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,
        246,1,0,0,0,246,257,1,0,0,0,247,245,1,0,0,0,248,249,5,5,0,0,249,
        253,5,34,0,0,250,252,3,4,2,0,251,250,1,0,0,0,252,255,1,0,0,0,253,
        251,1,0,0,0,253,254,1,0,0,0,254,256,1,0,0,0,255,253,1,0,0,0,256,
        258,5,35,0,0,257,248,1,0,0,0,257,258,1,0,0,0,258,19,1,0,0,0,259,
        260,5,4,0,0,260,261,3,46,23,0,261,265,5,34,0,0,262,264,3,6,3,0,263,
        262,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,
        268,1,0,0,0,267,265,1,0,0,0,268,283,5,35,0,0,269,270,5,5,0,0,270,
        271,5,4,0,0,271,272,3,46,23,0,272,276,5,34,0,0,273,275,3,6,3,0,274,
        273,1,0,0,0,275,278,1,0,0,0,276,274,1,0,0,0,276,277,1,0,0,0,277,
        279,1,0,0,0,278,276,1,0,0,0,279,280,5,35,0,0,280,282,1,0,0,0,281,
        269,1,0,0,0,282,285,1,0,0,0,283,281,1,0,0,0,283,284,1,0,0,0,284,
        295,1,0,0,0,285,283,1,0,0,0,286,287,5,5,0,0,287,291,5,34,0,0,288,
        290,3,6,3,0,289,288,1,0,0,0,290,293,1,0,0,0,291,289,1,0,0,0,291,
        292,1,0,0,0,292,294,1,0,0,0,293,291,1,0,0,0,294,296,5,35,0,0,295,
        286,1,0,0,0,295,296,1,0,0,0,296,21,1,0,0,0,297,298,5,4,0,0,298,299,
        3,46,23,0,299,303,5,34,0,0,300,302,3,8,4,0,301,300,1,0,0,0,302,305,
        1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,0,304,306,1,0,0,0,305,303,
        1,0,0,0,306,321,5,35,0,0,307,308,5,5,0,0,308,309,5,4,0,0,309,310,
        3,46,23,0,310,314,5,34,0,0,311,313,3,8,4,0,312,311,1,0,0,0,313,316,
        1,0,0,0,314,312,1,0,0,0,314,315,1,0,0,0,315,317,1,0,0,0,316,314,
        1,0,0,0,317,318,5,35,0,0,318,320,1,0,0,0,319,307,1,0,0,0,320,323,
        1,0,0,0,321,319,1,0,0,0,321,322,1,0,0,0,322,333,1,0,0,0,323,321,
        1,0,0,0,324,325,5,5,0,0,325,329,5,34,0,0,326,328,3,8,4,0,327,326,
        1,0,0,0,328,331,1,0,0,0,329,327,1,0,0,0,329,330,1,0,0,0,330,332,
        1,0,0,0,331,329,1,0,0,0,332,334,5,35,0,0,333,324,1,0,0,0,333,334,
        1,0,0,0,334,23,1,0,0,0,335,338,3,28,14,0,336,338,3,32,16,0,337,335,
        1,0,0,0,337,336,1,0,0,0,338,25,1,0,0,0,339,342,3,30,15,0,340,342,
        3,34,17,0,341,339,1,0,0,0,341,340,1,0,0,0,342,27,1,0,0,0,343,344,
        5,6,0,0,344,345,3,10,5,0,345,346,5,47,0,0,346,347,3,46,23,0,347,
        348,5,47,0,0,348,349,3,12,6,0,349,353,5,34,0,0,350,352,3,4,2,0,351,
        350,1,0,0,0,352,355,1,0,0,0,353,351,1,0,0,0,353,354,1,0,0,0,354,
        356,1,0,0,0,355,353,1,0,0,0,356,357,5,35,0,0,357,29,1,0,0,0,358,
        359,5,6,0,0,359,360,3,10,5,0,360,361,5,47,0,0,361,362,3,46,23,0,
        362,363,5,47,0,0,363,364,3,12,6,0,364,368,5,34,0,0,365,367,3,8,4,
        0,366,365,1,0,0,0,367,370,1,0,0,0,368,366,1,0,0,0,368,369,1,0,0,
        0,369,371,1,0,0,0,370,368,1,0,0,0,371,372,5,35,0,0,372,31,1,0,0,
        0,373,374,5,7,0,0,374,375,3,46,23,0,375,379,5,34,0,0,376,378,3,4,
        2,0,377,376,1,0,0,0,378,381,1,0,0,0,379,377,1,0,0,0,379,380,1,0,
        0,0,380,382,1,0,0,0,381,379,1,0,0,0,382,383,5,35,0,0,383,33,1,0,
        0,0,384,385,5,7,0,0,385,386,3,46,23,0,386,390,5,34,0,0,387,389,3,
        8,4,0,388,387,1,0,0,0,389,392,1,0,0,0,390,388,1,0,0,0,390,391,1,
        0,0,0,391,393,1,0,0,0,392,390,1,0,0,0,393,394,5,35,0,0,394,35,1,
        0,0,0,395,396,5,12,0,0,396,397,3,46,23,0,397,413,5,34,0,0,398,399,
        5,13,0,0,399,400,3,46,23,0,400,404,5,48,0,0,401,403,3,2,1,0,402,
        401,1,0,0,0,403,406,1,0,0,0,404,402,1,0,0,0,404,405,1,0,0,0,405,
        409,1,0,0,0,406,404,1,0,0,0,407,408,5,10,0,0,408,410,5,47,0,0,409,
        407,1,0,0,0,409,410,1,0,0,0,410,412,1,0,0,0,411,398,1,0,0,0,412,
        415,1,0,0,0,413,411,1,0,0,0,413,414,1,0,0,0,414,428,1,0,0,0,415,
        413,1,0,0,0,416,417,5,14,0,0,417,421,5,48,0,0,418,420,3,2,1,0,419,
        418,1,0,0,0,420,423,1,0,0,0,421,419,1,0,0,0,421,422,1,0,0,0,422,
        426,1,0,0,0,423,421,1,0,0,0,424,425,5,10,0,0,425,427,5,47,0,0,426,
        424,1,0,0,0,426,427,1,0,0,0,427,429,1,0,0,0,428,416,1,0,0,0,428,
        429,1,0,0,0,429,430,1,0,0,0,430,431,5,35,0,0,431,37,1,0,0,0,432,
        433,5,12,0,0,433,434,3,46,23,0,434,450,5,34,0,0,435,436,5,13,0,0,
        436,437,3,46,23,0,437,441,5,48,0,0,438,440,3,6,3,0,439,438,1,0,0,
        0,440,443,1,0,0,0,441,439,1,0,0,0,441,442,1,0,0,0,442,446,1,0,0,
        0,443,441,1,0,0,0,444,445,5,10,0,0,445,447,5,47,0,0,446,444,1,0,
        0,0,446,447,1,0,0,0,447,449,1,0,0,0,448,435,1,0,0,0,449,452,1,0,
        0,0,450,448,1,0,0,0,450,451,1,0,0,0,451,465,1,0,0,0,452,450,1,0,
        0,0,453,454,5,14,0,0,454,458,5,48,0,0,455,457,3,6,3,0,456,455,1,
        0,0,0,457,460,1,0,0,0,458,456,1,0,0,0,458,459,1,0,0,0,459,463,1,
        0,0,0,460,458,1,0,0,0,461,462,5,10,0,0,462,464,5,47,0,0,463,461,
        1,0,0,0,463,464,1,0,0,0,464,466,1,0,0,0,465,453,1,0,0,0,465,466,
        1,0,0,0,466,467,1,0,0,0,467,468,5,35,0,0,468,39,1,0,0,0,469,470,
        5,8,0,0,470,471,5,49,0,0,471,488,5,32,0,0,472,475,5,49,0,0,473,474,
        5,21,0,0,474,476,3,46,23,0,475,473,1,0,0,0,475,476,1,0,0,0,476,485,
        1,0,0,0,477,478,5,46,0,0,478,481,5,49,0,0,479,480,5,21,0,0,480,482,
        3,46,23,0,481,479,1,0,0,0,481,482,1,0,0,0,482,484,1,0,0,0,483,477,
        1,0,0,0,484,487,1,0,0,0,485,483,1,0,0,0,485,486,1,0,0,0,486,489,
        1,0,0,0,487,485,1,0,0,0,488,472,1,0,0,0,488,489,1,0,0,0,489,490,
        1,0,0,0,490,491,5,33,0,0,491,495,5,34,0,0,492,494,3,6,3,0,493,492,
        1,0,0,0,494,497,1,0,0,0,495,493,1,0,0,0,495,496,1,0,0,0,496,498,
        1,0,0,0,497,495,1,0,0,0,498,499,5,35,0,0,499,41,1,0,0,0,500,501,
        5,49,0,0,501,510,5,32,0,0,502,507,3,46,23,0,503,504,5,46,0,0,504,
        506,3,46,23,0,505,503,1,0,0,0,506,509,1,0,0,0,507,505,1,0,0,0,507,
        508,1,0,0,0,508,511,1,0,0,0,509,507,1,0,0,0,510,502,1,0,0,0,510,
        511,1,0,0,0,511,512,1,0,0,0,512,513,5,33,0,0,513,43,1,0,0,0,514,
        515,5,49,0,0,515,516,5,36,0,0,516,517,3,46,23,0,517,518,5,37,0,0,
        518,45,1,0,0,0,519,520,6,23,-1,0,520,521,5,32,0,0,521,522,3,46,23,
        0,522,523,5,33,0,0,523,532,1,0,0,0,524,532,5,38,0,0,525,532,5,39,
        0,0,526,532,5,40,0,0,527,532,5,41,0,0,528,532,3,42,21,0,529,532,
        3,44,22,0,530,532,5,49,0,0,531,519,1,0,0,0,531,524,1,0,0,0,531,525,
        1,0,0,0,531,526,1,0,0,0,531,527,1,0,0,0,531,528,1,0,0,0,531,529,
        1,0,0,0,531,530,1,0,0,0,532,550,1,0,0,0,533,534,10,12,0,0,534,535,
        5,30,0,0,535,549,3,46,23,13,536,537,10,11,0,0,537,538,7,1,0,0,538,
        549,3,46,23,12,539,540,10,10,0,0,540,541,7,2,0,0,541,549,3,46,23,
        11,542,543,10,9,0,0,543,544,7,3,0,0,544,549,3,46,23,10,545,546,10,
        8,0,0,546,547,7,4,0,0,547,549,3,46,23,9,548,533,1,0,0,0,548,536,
        1,0,0,0,548,539,1,0,0,0,548,542,1,0,0,0,548,545,1,0,0,0,549,552,
        1,0,0,0,550,548,1,0,0,0,550,551,1,0,0,0,551,47,1,0,0,0,552,550,1,
        0,0,0,57,51,75,97,121,146,162,165,168,175,189,200,207,215,219,227,
        238,245,253,257,265,276,283,291,295,303,314,321,329,333,337,341,
        353,368,379,390,404,409,413,421,426,428,441,446,450,458,463,465,
        475,481,485,488,495,507,510,531,548,550
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
            self.state = 170
            self.match(AMMScriptParser.ID)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 171
                self.match(AMMScriptParser.LBRACKET)
                self.state = 172
                self.expr(0)
                self.state = 173
                self.match(AMMScriptParser.RBRACKET)


            self.state = 177
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65011712) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 178
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
            self.state = 180
            self.match(AMMScriptParser.PRINT)
            self.state = 181
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
            self.state = 183
            self.match(AMMScriptParser.IF)
            self.state = 184
            self.expr(0)
            self.state = 185
            self.match(AMMScriptParser.LBRACE)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997340) != 0):
                self.state = 186
                self.statement()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 192
            self.match(AMMScriptParser.RBRACE)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 193
                    self.match(AMMScriptParser.ELSE)
                    self.state = 194
                    self.match(AMMScriptParser.IF)
                    self.state = 195
                    self.expr(0)
                    self.state = 196
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 200
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997340) != 0):
                        self.state = 197
                        self.statement()
                        self.state = 202
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 203
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 210
                self.match(AMMScriptParser.ELSE)
                self.state = 211
                self.match(AMMScriptParser.LBRACE)
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997340) != 0):
                    self.state = 212
                    self.statement()
                    self.state = 217
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 218
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
            self.state = 221
            self.match(AMMScriptParser.IF)
            self.state = 222
            self.expr(0)
            self.state = 223
            self.match(AMMScriptParser.LBRACE)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077417000156) != 0):
                self.state = 224
                self.statementInLoop()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 230
            self.match(AMMScriptParser.RBRACE)
            self.state = 245
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 231
                    self.match(AMMScriptParser.ELSE)
                    self.state = 232
                    self.match(AMMScriptParser.IF)
                    self.state = 233
                    self.expr(0)
                    self.state = 234
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 238
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077417000156) != 0):
                        self.state = 235
                        self.statementInLoop()
                        self.state = 240
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 241
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 247
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 248
                self.match(AMMScriptParser.ELSE)
                self.state = 249
                self.match(AMMScriptParser.LBRACE)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077417000156) != 0):
                    self.state = 250
                    self.statementInLoop()
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 256
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
            self.state = 259
            self.match(AMMScriptParser.IF)
            self.state = 260
            self.expr(0)
            self.state = 261
            self.match(AMMScriptParser.LBRACE)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                self.state = 262
                self.statementInFunction()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 268
            self.match(AMMScriptParser.RBRACE)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 269
                    self.match(AMMScriptParser.ELSE)
                    self.state = 270
                    self.match(AMMScriptParser.IF)
                    self.state = 271
                    self.expr(0)
                    self.state = 272
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 276
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                        self.state = 273
                        self.statementInFunction()
                        self.state = 278
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 279
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 286
                self.match(AMMScriptParser.ELSE)
                self.state = 287
                self.match(AMMScriptParser.LBRACE)
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                    self.state = 288
                    self.statementInFunction()
                    self.state = 293
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 294
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
            self.state = 297
            self.match(AMMScriptParser.IF)
            self.state = 298
            self.expr(0)
            self.state = 299
            self.match(AMMScriptParser.LBRACE)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416996572) != 0):
                self.state = 300
                self.statementInFunctionAndLoop()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 306
            self.match(AMMScriptParser.RBRACE)
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 307
                    self.match(AMMScriptParser.ELSE)
                    self.state = 308
                    self.match(AMMScriptParser.IF)
                    self.state = 309
                    self.expr(0)
                    self.state = 310
                    self.match(AMMScriptParser.LBRACE)
                    self.state = 314
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416996572) != 0):
                        self.state = 311
                        self.statementInFunctionAndLoop()
                        self.state = 316
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 317
                    self.match(AMMScriptParser.RBRACE) 
                self.state = 323
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 324
                self.match(AMMScriptParser.ELSE)
                self.state = 325
                self.match(AMMScriptParser.LBRACE)
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416996572) != 0):
                    self.state = 326
                    self.statementInFunctionAndLoop()
                    self.state = 331
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 332
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
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.forLoop()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
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
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.forLoopInFunction()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
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
            self.state = 343
            self.match(AMMScriptParser.FOR)
            self.state = 344
            self.variableDeclaration()
            self.state = 345
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 346
            self.expr(0)
            self.state = 347
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 348
            self.variableAsignment()
            self.state = 349
            self.match(AMMScriptParser.LBRACE)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077417000156) != 0):
                self.state = 350
                self.statementInLoop()
                self.state = 355
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 356
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
            self.state = 358
            self.match(AMMScriptParser.FOR)
            self.state = 359
            self.variableDeclaration()
            self.state = 360
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 361
            self.expr(0)
            self.state = 362
            self.match(AMMScriptParser.SEMICOLON)
            self.state = 363
            self.variableAsignment()
            self.state = 364
            self.match(AMMScriptParser.LBRACE)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416996572) != 0):
                self.state = 365
                self.statementInFunctionAndLoop()
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 371
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
            self.state = 373
            self.match(AMMScriptParser.WHILE)
            self.state = 374
            self.expr(0)
            self.state = 375
            self.match(AMMScriptParser.LBRACE)
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077417000156) != 0):
                self.state = 376
                self.statementInLoop()
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 382
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
            self.state = 384
            self.match(AMMScriptParser.WHILE)
            self.state = 385
            self.expr(0)
            self.state = 386
            self.match(AMMScriptParser.LBRACE)
            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416996572) != 0):
                self.state = 387
                self.statementInFunctionAndLoop()
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 393
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
            self.state = 395
            self.match(AMMScriptParser.SWITCH)
            self.state = 396
            self.expr(0)
            self.state = 397
            self.match(AMMScriptParser.LBRACE)
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 398
                self.match(AMMScriptParser.CASE)
                self.state = 399
                self.expr(0)
                self.state = 400
                self.match(AMMScriptParser.COLON)
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997340) != 0):
                    self.state = 401
                    self.statement()
                    self.state = 406
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 409
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 407
                    self.match(AMMScriptParser.BREAK)
                    self.state = 408
                    self.match(AMMScriptParser.SEMICOLON)


                self.state = 415
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 416
                self.match(AMMScriptParser.DEFAULT)
                self.state = 417
                self.match(AMMScriptParser.COLON)
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997340) != 0):
                    self.state = 418
                    self.statement()
                    self.state = 423
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 424
                    self.match(AMMScriptParser.BREAK)
                    self.state = 425
                    self.match(AMMScriptParser.SEMICOLON)




            self.state = 430
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
            self.state = 432
            self.match(AMMScriptParser.SWITCH)
            self.state = 433
            self.expr(0)
            self.state = 434
            self.match(AMMScriptParser.LBRACE)
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 435
                self.match(AMMScriptParser.CASE)
                self.state = 436
                self.expr(0)
                self.state = 437
                self.match(AMMScriptParser.COLON)
                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                    self.state = 438
                    self.statementInFunction()
                    self.state = 443
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 444
                    self.match(AMMScriptParser.BREAK)
                    self.state = 445
                    self.match(AMMScriptParser.SEMICOLON)


                self.state = 452
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 453
                self.match(AMMScriptParser.DEFAULT)
                self.state = 454
                self.match(AMMScriptParser.COLON)
                self.state = 458
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                    self.state = 455
                    self.statementInFunction()
                    self.state = 460
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 461
                    self.match(AMMScriptParser.BREAK)
                    self.state = 462
                    self.match(AMMScriptParser.SEMICOLON)




            self.state = 467
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
            self.state = 469
            self.match(AMMScriptParser.FUNCTION)
            self.state = 470
            self.match(AMMScriptParser.ID)
            self.state = 471
            self.match(AMMScriptParser.LPAREN)
            self.state = 488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 472
                self.match(AMMScriptParser.ID)
                self.state = 475
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 473
                    self.match(AMMScriptParser.EQUAL)
                    self.state = 474
                    self.expr(0)


                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 477
                    self.match(AMMScriptParser.COMMA)
                    self.state = 478
                    self.match(AMMScriptParser.ID)
                    self.state = 481
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==21:
                        self.state = 479
                        self.match(AMMScriptParser.EQUAL)
                        self.state = 480
                        self.expr(0)


                    self.state = 487
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 490
            self.match(AMMScriptParser.RPAREN)
            self.state = 491
            self.match(AMMScriptParser.LBRACE)
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416997596) != 0):
                self.state = 492
                self.statementInFunction()
                self.state = 497
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 498
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
            self.state = 500
            self.match(AMMScriptParser.ID)
            self.state = 501
            self.match(AMMScriptParser.LPAREN)
            self.state = 510
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 567077416992768) != 0):
                self.state = 502
                self.expr(0)
                self.state = 507
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 503
                    self.match(AMMScriptParser.COMMA)
                    self.state = 504
                    self.expr(0)
                    self.state = 509
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 512
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
        self.enterRule(localctx, 44, self.RULE_arrayExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(AMMScriptParser.ID)
            self.state = 515
            self.match(AMMScriptParser.LBRACKET)
            self.state = 516
            self.expr(0)
            self.state = 517
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
            self.state = 531
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = AMMScriptParser.ExprParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 520
                self.match(AMMScriptParser.LPAREN)
                self.state = 521
                self.expr(0)
                self.state = 522
                self.match(AMMScriptParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = AMMScriptParser.ExprNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 524
                self.match(AMMScriptParser.NUMBER)
                pass

            elif la_ == 3:
                localctx = AMMScriptParser.ExprStringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 525
                self.match(AMMScriptParser.STRING)
                pass

            elif la_ == 4:
                localctx = AMMScriptParser.ExprTrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 526
                self.match(AMMScriptParser.TRUE)
                pass

            elif la_ == 5:
                localctx = AMMScriptParser.ExprFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 527
                self.match(AMMScriptParser.FALSE)
                pass

            elif la_ == 6:
                localctx = AMMScriptParser.ExprFunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 528
                self.functionCall()
                pass

            elif la_ == 7:
                localctx = AMMScriptParser.ExprArrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 529
                self.arrayExpr()
                pass

            elif la_ == 8:
                localctx = AMMScriptParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 530
                self.match(AMMScriptParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 550
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 548
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = AMMScriptParser.ExprPowerContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 533
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 534
                        self.match(AMMScriptParser.POWER)
                        self.state = 535
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = AMMScriptParser.ExprMultDivModContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 536
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 537
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2952790016) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 538
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = AMMScriptParser.ExprPlusMinusContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 539
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 540
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 541
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = AMMScriptParser.ExprComparisonContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 542
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 543
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 544
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = AMMScriptParser.ExprAndOrContext(self, AMMScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 545
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 546
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==42 or _la==43):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 547
                        self.expr(9)
                        pass

             
                self.state = 552
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
         




