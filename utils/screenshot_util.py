import os
from datetime import datetime


def capture_screenshot(page, test_name):

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = f"screenshots/{test_name}_{timestamp}.png"

    page.screenshot(path=file_path)

    return file_path

