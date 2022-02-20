from PIL import Image
from mss import mss
from time import time

class ScreenShot:
    def take_screenshot(self, type, monitor):
        with mss() as sct:
            if type == 1:
                try:
                    sct.shot(mon=monitor, output='./positive/{}.png'.format(time()))
                except:
                    print('Error taking screenshot')
            else:
                try:
                    sct.shot(mon=monitor, output=f'./negative/{time()}.png')
                except:
                    print('Error taking screenshot')