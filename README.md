# TelCrap
Cut and crop Telpark invoice and generating another invoice with some invoices to avoid kill some trees when you print the invoice for your company

This utility is useful for situations with your company when you need to provide invoices to RRHH/Financial department and
you don't have much free time...just for lazies, like me :-)

## How to¿?
You must to install a library in you system called:

- **Fedora:** ``` yum install -y ImageMagick```
- **OSX:** ``` brew install imagemagick```

And now for your virtualenv (yeah, use virtualenv!):

```
pip install wand
```

## Folders
- **dest:** Just download here your raw invoices from the website
- **source:** Here will be generated your mixes

## Execution
Now execute the script:

Input:
```
python telpark_crop.p
```

Output:
```
(.virtualenv)➜  telcrap git:(master) ✗ python telpark_crop.py
Cropping files...
Concatenating files...
	 history_payment (11).pdf + history_payment (12).pdf
	 history_payment (10).pdf + history_payment (9).pdf
	 history_payment.pdf + history_payment (4).pdf
	 history_payment (6).pdf + history_payment (2).pdf
	 history_payment (8).pdf + history_payment (1).pdf
	 history_payment (7).pdf + history_payment (3).pdf

```
