# files 
2 # dna example 
3 # 
4 
 
5nucleotides = ["A", "C", "T", "G"] 
6 
 
ucl_complement = { 
8                "A":"T",  
9                "C":"G",  
10                "T":"A", 
11                "G":"C"  
12 	      } 
13 
 
14 rna_transcription = { 
15 	       "A":"U", 
16 	       "C":"G", 
17                "T":"A", 
18                "G":"C" 
19 	      } 
20 
 
21 
 
22 nucl_codon = []; 
23 
 
24 dna = "ACCGTT" 
25 dna_complement = "" 
26 rna = "" 
27 
 
28 # complementary seq  
29 # 
30 for x in dna: 
31   dna_complement = dna_complement + nucl_complement[x] 
32    
33 
 
34 n = len(dna) 
35 print " dna length  = ", n 
36 
 
37 n = len(dna_complement) 
38 print " dna length complementary  = ", n 
39 
 
40 
 
41 for i in range(0, n): 
42   print i, dna[i], dna_complement[i] 
43 
 
44 print "dna, dna complementary : " 
45 print dna 
46 print dna_complement 

