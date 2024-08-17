#pip install Pillow
import time

from function import generate_pic

try:
    generate_pic()
    time.sleep(10)
except Exception as e:
    print(e)
    time.sleep(10)
