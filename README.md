# TelCrap
Cut and crop Telpark invoice and generating another one with some of them mixed to avoid kill some trees when you print the invoice for your company

This utility is useful for situations with your company when you need to provide invoices to RRHH/Financial department and
you don't have much free time...just for lazies, like me :-)

## How to¿?
You must to install a library in you system called:

- **Fedora:** ``` yum install -y ImageMagick```

And now for your virtualenv (yeah, use a virtualenv!):

```
pip install -r requirements.txt
```

## Folders
- **source:** Just download here your raw invoices from the website
- **final.pdf:** The resultant pdf with all invoices concatenated
- **tmp:** during the execution this folder will be created to operate with temporary files, but will be erased at the end of the execution

## Execution
Now execute the script:

Input:
```
python telpark_crop.py
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
Creating release pdf...
```
