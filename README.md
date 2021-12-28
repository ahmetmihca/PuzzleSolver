# PuzzleSolver #

A word search puzzle is a word puzzle that consists of letters placed as a grid, as shown below in Figure. The aim is to find some given words in this puzzle. The words can be found in different orientations. The words can be placed both horizontally and vertically. In both of these, there are two possible directions. Horizontally placed words can be found left to right or right to left, and vertically placed words can be found the top to bottom or bottom to top.

The program first gets two inputs: the puzzle and the words it will search for. Then, it displays the puzzle as a grid. Finally, it searches for the words in the puzzle and displays their starting and ending positions.

# The first input to the program, the puzzle, will have the following format: #

***row1-row2-row3-row4-...-rowN***

Each row on the puzzle is separated by a dash ("-") character. Once the program gets this input from the user, it needs to check the validity of this input. For this purpose, the checkInput() function will be used. This function takes a single parameter, the puzzle, which is the first input obtained from the user, and returns True if it is in the correct format, and False otherwise. Note that True and False are boolean values.

This function should check the followings:

• The input should contain at least one dash ("-") character.

• Each row should consist only of alphabetical characters.

• All rows should have the same length.


The program will ask for the first input until it is entered correctly. It means that the user may need to enter the first input more than once.

When the first input is valid, the program will get the second input, the words to be searched in the puzzle, again using the getInput() function. This input will have the following format:

***word1,word2,word3,word4,...,wordM***

Each word is separated by a comma. the program does not need to perform any checks on this second input. The user will always enter this input correctly and the words will be at least 3 letters long.

After the program gets these two inputs from the user, it will print the puzzle as a matrix. For this purpose, the printPuzzle() function is used. This function gets the puzzle string as its only parameter, and prints each row in a separate line. For example, if the puzzle is row1-row2-row3-row4-...-rowN, then this function should print the following:

   row1
   
   row2
   
   row3
   
   row4
   
   ...
   
   rowN
   

Finally, the program will search for the words in the puzzle, in the given order, using the function findWords(). This function takes two parameters (puzzle and words), and it prints the location of each word that can be found in the given puzzle. Each word appearing in the second input entered by the user will occur at most once in the puzzle given as the first input by the user. If the program can find a word, it should print its starting position and ending position. For example, if word1 is found in the given puzzle, then the program should print the following for that word:

  **Found word1 at (starting_row,starting_column)-(ending_row,ending_column)**


If a word2 does not exist in the given puzzle, then the program should display the following prompt:

**word2 does not exist.** 

The row and column indices should start from 0. The top row and the leftmost column will have the index 0. 


# Sample Run 1 (Example from the figure, correct input format) #

    Please enter the puzzle: pdlxkgafvbx-hdhcraesexh-vrcyppxtrdf-iotnkyqrtuh-iwryktpoimd-qhcrahshcum-horizontali-hldmvnthlul
    Please enter the words: python,vertical,horizontal,word,search
    pdlxkgafvbx
    hdhcraesexh
    vrcyppxtrdf
    iotnkyqrtuh
    iwryktpoimd
    qhcrahshcum
    horizontali
    hldmvnthlul
    Found python at (2,5)-(7,5)
    Found vertical at (0,8)-(7,8)
    Found horizontal at (6,0)-(6,9)
    Found word at (4,1)-(1,1)
    Found search at (1,7)-(1,2)
 
 # Sample Run 2 (Only horizontal, uppercase-lowercase mixed input) #
 
    Please enter the puzzle: MPOOLMPTCGY-ABSTRACTION-vnoiTCNUFPU-ALGOritHMSD-ZPSeuDOCODE-RGNIRTSLIST-hooxchacler-svariablewg
    Please enter the words: function,pseudocode,LOOP,abstraction,stRIng,algorithm,VARiable,list
    mpoolmptcgy
    abstraction
    vnoitcnufpu
    algorithmsd
    zpseudocode
    rgnirtslist
    hooxchacler
    svariablewg
    Found function at (2,8)-(2,1)
    Found pseudocode at (4,1)-(4,10)
    Found loop at (0,4)-(0,1)
    Found abstraction at (1,0)-(1,10)
    Found string at (5,6)-(5,1)
    Found algorithm at (3,0)-(3,8)
    Found variable at (7,1)-(7,8)
    Found list at (5,7)-(5,10)


# Sample Run 3 (Only vertical, uppercase input) #

    Please enter the puzzle: LVNMEFOPEA-IOKLBXRCJR-MTEOIBKAJA-ATIHCESNVK-BABKAINBIN-OWOCIJIEEA-YARORIMRNR-KLITONLRNO-OYASEGIAAM-TVNAERYLCE
    Please enter the words: OTTAWA,VIENNA,ANKARA,BEIJING,NAIROBI,ROME,MINSK,CANBERRA,LIMA,TOKYO,CAIRO,STOCKHOLM
    lvnmefopea
    ioklbxrcjr
    mteoibkaja
    atihcesnvk
    babkainbin
    owocijieea
    yarorimrnr
    klitonlrno
    oyasegiaam
    tvnaerylce
    Found ottawa at (1,1)-(6,1)
    Found vienna at (3,8)-(8,8)
    Found ankara at (5,9)-(0,9)
    Found beijing at (2,5)-(8,5)
    Found nairobi at (9,2)-(3,2)
    Found rome at (6,9)-(9,9)
    Found minsk at (6,6)-(2,6)
    Found canberra at (1,7)-(8,7)
    Found lima at (0,0)-(3,0)
    Found tokyo at (9,0)-(5,0)
    Found cairo at (3,4)-(7,4)
    Found stockholm at (8,3)-(0,3)

# Sample Run 4 (Horizontal and vertical with wrong inputs) #

    Please enter the puzzle: yngejzfocox-jflapbenorangehksy-ydnuarqfuiishcaepbhqkhq-shdbryjlicotknhbmmaz
    Wrong input format.
    Please enter the puzzle: yngejzfocoxxmwhqpeue
    Wrong input format.
    Please enter the puzzle: yngejzfoco45mwhqpe1e-jflap34nora5gehkklce
    Wrong input format.
    Please enter the puzzle: yngejzfocoxxmwhqpeue-jflapbenorangehkklce-nifiiugdcsbfmscasqex-sucynzsgoynnesynblbf-ggfqefrnnyrrebwartsy-ydnuarqfuiimspknwanz-gfwypdbmtykhyiyazzyw-qgcfpearirxhrczbsies-okjvlphnkrrnmorlowcj-grapehhvsebfzvzfjief-jzipwvnhshcaepbhqkhq-shdbryjlicotknhbmmaz
    Please enter the words: pear,banana,orange,pineapple,grape,cherry,peach,strawberry,coconut,kiwi
    yngejzfocoxxmwhqpeue
    jflapbenorangehkklce
    nifiiugdcsbfmscasqex
    sucynzsgoynnesynblbf
    ggfqefrnnyrrebwartsy
    ydnuarqfuiimspknwanz
    gfwypdbmtykhyiyazzyw
    qgcfpearirxhrczbsies
    okjvlphnkrrnmorlowcj
    grapehhvsebfzvzfjief
    jzipwvnhshcaepbhqkhq
    shdbryjlicotknhbmmaz
    Found pear at (7,4)-(7,7)
    Found banana at (7,15)-(2,15)
    Found orange at (1,8)-(1,13)
    Found pineapple at (1,4)-(9,4)
    Found grape at (9,0)-(9,4)
    Found cherry at (11,9)-(6,9)
    Found peach at (10,13)-(10,9)
    Found strawberry at (4,18)-(4,9)
    Found coconut at (0,8)-(6,8)
    Found kiwi at (10,17)-(7,17)


# Sample Run 5 (Horizontal and vertical with some words not in puzzle) #

    Please enter the puzzle: pandaxngeqrymtso-ezmlaesowxaqbujl-noilktxreecytrql-gskaboofsfoxdtei-utsmakotufodhlrd-iroachimpanzeesa-nintrwflyrkhcdum-jcecahkktiklsvhr-mhvsbaykagodwgca-koalatcwlkfmrwbb-jsrrfdolphinuytc
    Please enter the words: platypus,dolphin,penguin,unicorn,armadillo,seal,dog,giraffe,panda,racoon,dragon,frog,kraken,ostrich,llama,lion,chimpanzee,phoenix,turtle,raven,fox,koala,crab
    pandaxngeqrymtso
    ezmlaesowxaqbujl
    noilktxreecytrql
    gskaboofsfoxdtei
    utsmakotufodhlrd
    iroachimpanzeesa
    nintrwflyrkhcdum
    jcecahkktiklsvhr
    mhvsbaykagodwgca
    koalatcwlkfmrwbb
    jsrrfdolphinuytc
    Found platypus at (10,8)-(3,8)
    Found dolphin at (10,5)-(10,11)
    Found penguin at (0,0)-(6,0)
    unicorn does not exist.
    Found armadillo at (8,15)-(0,15)
    Found seal at (1,6)-(1,3)
    Found dog at (8,11)-(8,9)
    Found giraffe at (8,9)-(2,9)
    Found panda at (0,0)-(0,4)
    Found racoon at (0,10)-(5,10)
    dragon does not exist.
    Found frog at (3,7)-(0,7)
    kraken does not exist.
    Found ostrich at (2,1)-(8,1)
    Found llama at (1,3)-(5,3)
    Found lion at (2,3)-(2,0)
    Found chimpanzee at (5,4)-(5,13)
    phoenix does not exist.
    Found turtle at (0,13)-(5,13)
    Found raven at (10,2)-(6,2)
    Found fox at (3,9)-(3,11)
    Found koala at (9,0)-(9,4)
    Found crab at (5,4)-(8,4)
