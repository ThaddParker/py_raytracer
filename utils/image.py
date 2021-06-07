from utils.functions import clamp


class Image:
    def __init__(self, width, height, samples=50):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]
        self.samples_per_pixel = samples
    def set_pixel(self, x, y, col):
        self.pixels[y][x] = col

    def write_ppm(self, img_fileobj):
        Image.write_ppm_header(img_fileobj, height=self.height, width=self.width)
        self.write_ppm_raw(img_fileobj)

    @staticmethod
    def write_ppm_header(img_fileobj, height=None, width=None):
        """Writes only the header of a PPM file"""
        img_fileobj.write("P3 {} {}\n255\n".format(width, height))

    def write_ppm_raw(self, img_fileobj):
        def to_byte(c):
            return round(max(min(c * 255, 255), 0))

        for row in self.pixels:
            for color in row:
                #scale = 1. / self.samples_per_pixel
                #corrected_color = Color(math.sqrt(scale*color.red), math.sqrt(scale*color.green), math.sqrt(scale*color.blue))
                img_fileobj.write(
                    "{} {} {} ".format(
                        to_byte(color.red), to_byte(color.green), to_byte(color.blue)
                    )
                )
            img_fileobj.write("\n")
