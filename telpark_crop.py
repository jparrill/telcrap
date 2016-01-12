from wand.image import Image
import os
import glob

def get_file_name (path_to_file):
    return path_to_file.split('/')[-1]

def crop_source_files (_path):
    print "Cropping files..."
    for _file in glob.glob(_path):
        with Image(filename=_file, resolution=200) as img:
             img.compression_quality = 99
             img.crop(170, 100, width=1320, height=900)
             img.save(filename="./dest/" + get_file_name(_file))

def concatenate_files(_path):
    print "Concatenating files..."
    file_list = glob.glob(_path)
    for _file in range(0, len(file_list), 2):
        if file_list.index(file_list[_file]) != len(file_list) - 1:
            file1 = file_list[_file]
            file2 = file_list[_file + 1]
            print "\t {} + {}".format(get_file_name(file1),get_file_name(file2))
            with Image() as blankimage:
                with Image(filename=file1, resolution=200) as img1:
                    w = img1.width; h = img1.height
                    with Image(filename=file2, resolution=200) as img2:
                        blankimage.blank(w, h*2)
                        blankimage.composite(img1, 0, 0)
                        blankimage.composite(img2, 0, h)
                        blankimage.save(filename=file1)
            os.remove(file2)
        os.rename(file_list[_file], "./dest/new_mix_" + str(_file))

crop_source_files("./source/*.pdf")
concatenate_files("./dest/*.pdf")
