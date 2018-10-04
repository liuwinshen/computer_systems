# Clean File
The program `clean.py` removes whitespace and, if specified, comments, from a
given text file. It runs in Python 3.

## How to run the program
1. From the command line, navigate to the folder `src/` that contains `clean.py`.
2. To remove only whitespace, type the command `python3 clean.py <filename>`.
Note: Input filenames are assumed to be in the format `name.in`. The output file
with whitespace removed will be `name.out` and placed in the same folder as the
input file.

To remove comments as well, type `no-comments` at the end of the command. Example:
`python3 clean.py testfile.in no-comments`
Note: Comments are assumed to be preceded by `//`

No additional compilation is needed.

## Sample input
`// Draws a rectangle at the top-left corner of the screen.
// The rectangle is 16 pixels wide and R0 pixels high.

(KBDLOOP)
  @KBD      // loop until key pressed
  D=M
  @KBDLOOP
  D;JEQ

  @50       // setup: rect will be 50 high
  D=A
  @R0
`

## Sample output if comments are kept
`//Drawsarectangleatthetop-leftcornerofthescreen.
//Therectangleis16pixelswideandR0pixelshigh.
(KBDLOOP)
@KBD//loopuntilkeypressed
D=M
@KBDLOOP
D;JEQ
@50//setup:rectwillbe50high
D=A
@R0
`

## Sample output if comments are removed
`(KBDLOOP)
@KBD
D=M
@KBDLOOP
D;JEQ
@50
D=A
@R0
`
