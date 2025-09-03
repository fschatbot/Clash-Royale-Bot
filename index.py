from PIL import ImageGrab


def screenshot():
    bbox = (690, 145, 1179, 808)  # right = left + width, bottom = top + height

# Capture the region
    screenshot= ImageGrab.grab(bbox=bbox)
    grayscale_screenshot= screenshot.convert("L")

# Save the file
    grayscale_screenshot.save("region_screenshot_pil.png")

    print("Region screenshot saved as region_screenshot_pil.png")


def is_end_screen():
    ...

def count_crown():
    ...


def main():
    ...

if __name__ == "__main__":
    screenshot()