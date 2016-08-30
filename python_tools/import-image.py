import os
import sys
import uuid
import base64
from PIL import Image
import datetime 
import shutil

def main(_, file_path,
         date_string = datetime.date.today().strftime('%Y%m%d'),
         max_width = 1280):
    print(sys.argv)
    print(file_path)
    dir_name, file_name = os.path.split(os.path.abspath(file_path))
    dest_dir = os.path.join(os.path.dirname(__file__), '..', 'images')
    image_id = str(uuid.uuid4())[:8]
    dest_filename = os.path.join(dest_dir, date_string + '_' + image_id + '_' + file_name)
    with Image.open(file_path) as img:
        w, h = img.size
        img_format = img.format
        if img_format == 'GIF':
            shutil.copy(file_path, dest_filename)
        else:
            if w > max_width:
                w_ratio = max_width / w
                new_h = int(h*w_ratio)
                img = img.resize((max_width, new_h), Image.ANTIALIAS)
            img.save(dest_filename, img_format)


if __name__ == '__main__':
    sys.exit(int(main(*sys.argv) or 0))



