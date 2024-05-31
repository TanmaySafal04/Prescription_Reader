import numpy as np
import cv2

def convert_to_rgb(image):
    """
    Convert an image of any dimension to RGB format.
    Args:
        image (numpy.ndarray): Input image array.
    Returns:
        numpy.ndarray: RGB image array with dimensions (height, width, 3).
    """
    # Check the number of channels in the input image
    if len(image.shape) == 2:
        # If the image is grayscale (2D), convert it to RGB by duplicating the single channel
        rgb_image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.shape[2] == 1:
        # If the image has a single channel, duplicate the channel to get RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.shape[2] == 3:
        # If the image already has 3 channels, it's already RGB
        rgb_image = image
    elif image.shape[2] == 4:
        # If the image has 4 channels (e.g., RGBA), discard the alpha channel
        rgb_image = image[:, :, :3]
    else:
        # For other cases with more than 3 channels, select the first 3 channels
        rgb_image = image[:, :, :3]
    
    return rgb_image

# Example usage:
# Create a sample grayscale image
gray_image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
# Create a sample RGBA image
rgba_image = np.random.randint(0, 256, (100, 100, 4), dtype=np.uint8)

# Convert the grayscale image to RGB
rgb_from_gray = convert_to_rgb(gray_image)
print("Converted grayscale to RGB shape:", rgb_from_gray.shape)

# Convert the RGBA image to RGB
rgb_from_rgba = convert_to_rgb(rgba_image)
print("Converted RGBA to RGB shape:", rgb_from_rgba.shape)
