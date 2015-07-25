BIOL3014/BINF700 Practical 1
============================

* Due: TODO
* Revision: 1


Python programming
------------------

This practical familiarises you with the key elements of the python programming 
language. Both understanding and writing python code is fundamental for 
understanding BIOL3014/BINF7000 practicals, projects and lectures.


Requirements
------------

Write code in a plain text editor. TextWrangler or Atom are good GUI based 
editors.

Try and follow the style PEP8_ guide.

Submit all code with filenames as requested.

.. _PEP8: https://www.python.org/dev/peps/pep-0008/


Exercise 1: Data types & conditionals (1/2 mark)
------------------------------------------------

Modify the program *one_to_three_letter_code.py* in::

    src/one_to_three_letter_code.py 

So that:

**(1):** It prints/outputs::

    The provided letter is W
    This letter is in the list, it corresponds to the amino acid TRP

**(2):** When changing the letter to 'Z', it prints/outputs::

    The provided letter is Z
    This letter is not the list and therefore does not correspond to an amino acid

**Submit both programs as q11.py and q12.py respectively.**


Exercise 2:  (1 mark)
-------------------

By using/modifying the program *hydrophobic_detection.py* in::

    src/hydrophobic_detection.py

**(1):** How does the output change when the sequence variable is changed to 
*sequence = "MHKL"*. Explain what has happened.

**(2):** Modify the code so that instead of printing *It is hydrophobic* if 
a residue is hydrophobic, you instead print the sequence, then use a '*' 
on the line/position below to denote hydrophobicity.

The expected output is::

    MHKL
    *  *

**(3):** Using the program you wrote in (2), change the sequence variable to the contents of::

    src/sequence.txt

How many hydrophobic clusters do you see? What kind of protein is this and why?

**Submit your written answers and program q22.py.**
