from rembg import remove
import numpy as np
import cv2

def bg_remove(input_path, output_path, write=0):
    input_path = input_path
    output_path = output_path

    input = cv2.imread(input_path)
    output = remove(input)
    if write:
        cv2.imwrite(output_path, output)
    return output

def create_mask(output, output_path, write=0):
    mask = output[:, :, -1]
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGBA)
    if write:
        cv2.imwrite(output_path, mask)

    return mask

# example
# write => 저장할 것인지 안할 것인지
input_path = r"C:\Users\HP\Desktop\myRepo\ChildDetect\rembg-main\testoutput\input\human3.jpg"
output_path = r"C:\Users\HP\Desktop\myRepo\ChildDetect\rembg-main\testoutput\output\output7.png"
output = bg_remove(input_path=input_path, output_path=output_path, write=1)
create_mask(output=output, output_path=output_path, write=1)
