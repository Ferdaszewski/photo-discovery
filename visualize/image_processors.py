import colorific
import colorsys

from visualize.models import Metadata


def primary_color(filename):
    """Takes a file and returns the web hex value of the primary color
    as a string.
    """
    palette = colorific.extract_colors(filename)
    return colorific.rgb_to_hex(palette.colors[0].value)


def webhex_to_rgb(hexrgb):
    """Takes a string representation of a web RGB hex value and returns
    the float representation (0 to 1) as a tuple (R, G, B).
    """
    hexrgb = hexrgb.lstrip('#')
    return (int(hexrgb[i:i+2], 16) / 255.0 for i in xrange(0, 5, 2))


def process_image(photo):
    """Run all the necessary calculations for an image and save the data
    to the metadata model."""
    file_path = photo.original.path

    # Primary Color Visualization metadata
    hexrgb = primary_color(file_path)
    r, g, b = webhex_to_rgb(hexrgb)
    y, i, q = colorsys.rgb_to_yiq(r, g, b)
    h, l, s = colorsys.rgb_to_hls(r, g, b)

    # Save new Metadata row
    new_metadata = Metadata(image_file=photo,
                            pc_hex=hexrgb,
                            pc_y=y,
                            pc_i=i,
                            pc_q=q,
                            pc_h=h,
                            pc_s=s,
                            pc_l=l)
    new_metadata.save()
