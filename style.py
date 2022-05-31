from PIL import Image


def con(self):
        # Convert Image to White and Black 
        i = Image.open(self)
        ibw = i.convert('L')

        ibw.show()
