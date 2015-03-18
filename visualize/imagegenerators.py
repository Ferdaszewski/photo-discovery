"""ImageKit generators for use in templates. ImageKit automatically
loads files named 'generatedimages' in Django app folders.
"""
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFit, SmartResize


class WebSize(ImageSpec):
    """Resize images for web display."""
    processors = [ResizeToFit(
        width=1200,
        height=790,
        upscale=False,
        )]
    format = 'JPEG'
    options = {'quality': 90}


class Thumbnail(ImageSpec):
    """Resize and smart crop images for web thumbnail use."""
    processors = [SmartResize(
        width=100,
        height=100,
        upscale=False,
        )]
    format = 'JPEG'
    options = {'quality': 70}


# Register image generators for use in templates
register.generator('visualize:websize', WebSize)
register.generator('visualize:thumbnail', Thumbnail)
