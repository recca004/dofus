import pyautogui as pg
import time
import logging
from datetime import datetime

# Configurable Settings
imageOffset = 25
run_duration_minutes = 15  # Total time to run the script (e.g., 10 minutes)
confidence_threshold=0.8  # Confidence threshold for image matching

# The `resource_types` dictionary in the provided Python script is used to store information about
# different types of resources that can be gathered in the game. Each key-value pair in the
# `resource_types` dictionary represents a specific resource type identified by a unique key, such as
# "Blé" in this case.
resource_types = {
    "Blé": {
        "gather_time": 11,  # Time to wait after clicking "Faucher" for Blé
        "images": [
            "images/image1.jpg",
            "images/image2.jpg",
            "images/image3.jpg",
            "images/image4.jpg",
            "images/image5.jpg",
            "images/image6.jpg",
            "images/image7.jpg",
            "images/image8.jpg",
            "images/image9.jpg",
            "images/image10.jpg",
            "images/image11.jpg",
            "images/image12.jpg",
            "images/image13.jpg",
            "images/image14.jpg",
            "images/image15.jpg",
            "images/image16.jpg",
            "images/image17.jpg",
            "images/image18.jpg"
        ]
    },
    # Add more resource types here as needed
}

# Define map locations without no-click zones
# The `map_locations` dictionary in the provided Python script is used to store information about
# different map locations in the game. Each key-value pair in the dictionary represents a specific map
# location identified by a unique key, such as "-26_-39".
map_locations = {
    "-26_-39": {
        "map_image": "images/maplocation_-26_-39.jpg",
    },
    # Add more map locations as needed
}

# These lines of code are defining the file paths for different images used in the script:
faucher_image = "images/Faucher.jpg"
fight_finish_image = "images/Actions/Fight_is_finish.png"
job_levelup_image = "images/Actions/Job_levelup.png"
job_levelup_ok_image = "images/Actions/Job_levelup_OK.png"

# Get current date to include in the log file name
current_date = datetime.now().strftime("%Y-%m-%d")
log_filename = f"resource_gathering_{current_date}.log"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),  # Log to a file with the date in the name
        logging.StreamHandler()  # Log to the console
    ]
)

def clickImage(image_path, description, retries=3, confidence=confidence_threshold, delay=2):
    """
    The function `clickImage` helps locate and click on an image on the screen with specified parameters
    like retries, confidence threshold, and delay.
    
    :param image_path: The `image_path` parameter in the `clickImage` function is the file path to the
    image that the function will search for on the screen to click
    :param description: The `description` parameter in the `clickImage` function is a string that
    describes the image being searched for on the screen. It is used for logging purposes to provide
    information about the image being located and clicked
    :param retries: The `retries` parameter in the `clickImage` function specifies the number of times
    the function will attempt to locate and click the image on the screen before giving up. If the image
    is not found in the initial attempt, the function will retry the specified number of times, defaults
    to 3 (optional)
    :param confidence: The `confidence` parameter in the `clickImage` function is used to specify the
    confidence threshold for locating the image on the screen using the `pg.locateOnScreen` function.
    This threshold determines how closely the image must match the screen content to be considered a
    match
    :param delay: The `delay` parameter in the `clickImage` function represents the amount of time (in
    seconds) to wait before retrying to locate the image on the screen if it is not found in the initial
    attempt. This delay helps prevent rapid and unnecessary retries, allowing the system some time to
    potentially load, defaults to 2 (optional)
    :return: The function `clickImage` returns a boolean value - `True` if the image is found and
    clicked successfully, and `False` if the image is not found after the specified number of retries.
    """
    """Helper function to locate an image on the screen and click it."""
    for _ in range(retries):
        try:
            pos = pg.locateOnScreen(image_path, confidence=confidence_threshold)
            if pos:
                logging.info(f"{description} found at position: {pos}")
                pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
                pg.click()
                return True
            else:
                logging.info(f"{description} not found. Retrying...")
                time.sleep(delay)  # Increase delay before retrying
        except Exception as e:
            logging.error(f"An error occurred while searching for {description}: {e}")
    return False

def checkMapLocation(map_location):
    """
    The function `checkMapLocation` checks if the correct map location is on screen by clicking on the
    specified map image.
    
    :param map_location: The `map_location` parameter is a dictionary that contains information about
    the location on a map. It likely includes the following key-value pairs:
    :return: The function `checkMapLocation` is returning the result of calling the `clickImage`
    function with the map location's image and the string "Map location" as arguments.
    """
    """Check if the correct map location is on screen."""
    return clickImage(map_location["map_image"], "Map location")

def gatherResources(map_location):
    """
    The function `gatherResources` gathers resources based on the current map location by clicking on
    resource images and waiting for the configured gather time.
    
    :param map_location: It seems like you were about to provide more information about the
    `map_location` parameter in the `gatherResources` function, but the description is missing. Could
    you please provide more details or context about the `map_location` parameter so that I can assist
    you further with the function?
    """
    """Gather resources based on the current map location."""
    for resource_name, resource_info in resource_types.items():
        logging.info(f"Gathering {resource_name}")
        for resource_image in resource_info["images"]:
            if clickImage(resource_image, f"Resource {resource_image}"):
                time.sleep(1)  # Small delay before searching for "Faucher"
                if clickImage(faucher_image, "Faucher"):
                    gather_time = resource_info["gather_time"]
                    logging.info(f"Waiting {gather_time} seconds for gathering {resource_name}...")
                    time.sleep(gather_time)  # Wait for the configured gather time
                else:
                    logging.warning("Faucher button not found after clicking the resource.")

def main():
    """
    The main function runs a loop for a specified duration, checks map locations for resources, and
    handles clicking images for finishing fights and leveling up jobs.
    """
    start_time = time.time()
    duration = run_duration_minutes * 60  # Convert minutes to seconds

    while time.time() - start_time < duration:
        for map_key, map_location in map_locations.items():
            if checkMapLocation(map_location):
                gatherResources(map_location)
                break  # Break after finding the correct map location and gathering resources

        if not clickImage(fight_finish_image, "Fight finish"):
            logging.error("Failed to find Fight finish.")
        
        if not clickImage(job_levelup_image, "Job level up"):
            logging.error("Failed to find Job level up.")
        else:
            if not clickImage(job_levelup_ok_image, "Job level up OK"):
                logging.error("Failed to find Job level up OK.")

main()
