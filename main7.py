import pyautogui as pg
import time
import logging
from datetime import datetime

# Configurable Settings
imageOffset = 25
run_duration_minutes = 10  # Total time to run the script (e.g., 10 minutes)
error_timeout_seconds = 20  # Time to wait before skipping to the next map
confidence_threshold = 0.8  # Confidence threshold for image matching

# Define resource types with their specific images and gathering times
resource_types = {
 
    "Orge": {
        "gather_time": 10,  # Time to wait after clicking "Faucher" for Avoine
        "images": [
            "images/Plaine_de_cania_-20_-42_Orge_.png",
            "images/Plaine_de_cania_-20_-42_Orge_(1).png",
            "images/Plaine_de_cania_-20_-42_Orge_(2).png",
            "images/Plaine_de_cania_-20_-42_Orge_(3).png",
            "images/Plaine_de_cania_-20_-42_Orge_(4).png",
            "images/Plaine_de_cania_-20_-42_Orge_(5).png",
            "images/Plaine_de_cania_-20_-42_Orge_(6).png",
            "images/Plaine_de_cania_-20_-42_Orge_(7).png",
            "images/Plaine_de_cania_-20_-42_Orge_(8).png",
            "images/Plaine_de_cania_-20_-42_Orge_(9).png",
            "images/Plaine_de_cania_-20_-42_Orge_(10).png",
            "images/Plaine_de_cania_-20_-42_Orge_(11).png",
            "images/Plaine_de_cania_-20_-42_Orge_(12).png",
            "images/Plaine_de_cania_-20_-42_Orge_(13).png",
            "images/Plaine_de_cania_-20_-42_Orge_(14).png",
            "images/Plaine_de_cania_-20_-42_Orge_(15).png",
            "images/Plaine_de_cania_-20_-42_Orge_(16).png",
            "images/Plaine_de_cania_-20_-42_Orge_(17).png",
            "images/Plaine_de_cania_-20_-42_Orge_(18).png",
            "images/Plaine_de_cania_-20_-42_Orge_(19).png",
            "images/Plaine_de_cania_-20_-42_Orge_(20).png",
            "images/Plaine_de_cania_-20_-42_Orge_(21).png",
            "images/Plaine_de_cania_-20_-42_Orge_(22).png",
            "images/Plaine_de_cania_-20_-42_Orge_(23).png"
        ]
    },
    # Add more resource types here as needed
}

# Define map locations with their specific images
map_locations = {
    "-26_-39": {
        "map_image": "images/maplocation_-26_-39.png",
    },
    "-21_-40": {
        "map_image": "images/maplocation_-21_-40.png",
    },
    "-20_-42": {
        "map_image": "images/maplocation_-20_-42.png",
    },
    # Add more map locations as needed
}

faucher_image = "images/Actions/Faucher.jpg"
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
    """Helper function to locate an image on the screen and click it."""
    for _ in range(retries):
        try:
            pos = pg.locateOnScreen(image_path, confidence=confidence)
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
    """Check if the correct map location is on screen."""
    return clickImage(map_location["map_image"], "Map location")

def gatherResources(map_location):
    """Gather resources based on the current map location."""
    start_error_time = None
    for resource_name, resource_info in resource_types.items():
        logging.info(f"Gathering {resource_name}")
        for resource_image in resource_info["images"]:
            if clickImage(resource_image, f"Resource {resource_image}"):
                # Now locate and click on the "Faucher" button
                time.sleep(1)  # Small delay before searching for "Faucher"
                if clickImage(faucher_image, "Faucher"):
                    gather_time = resource_info["gather_time"]
                    logging.info(f"Waiting {gather_time} seconds for gathering {resource_name}...")
                    time.sleep(gather_time)  # Wait for the configured gather time
                    start_error_time = None  # Reset error timer
                else:
                    logging.warning("Faucher button not found after clicking the resource.")
            else:
                if start_error_time is None:
                    start_error_time = time.time()
                elif time.time() - start_error_time > error_timeout_seconds:
                    logging.error(f"Error encountered for more than {error_timeout_seconds} seconds, moving to next map location.")
                    return  # Exit and move to the next map location

def main():
    start_time = time.time()
    duration = run_duration_minutes * 60  # Convert minutes to seconds

    while time.time() - start_time < duration:
        # Iterate over each map location and check if it's the current one
        for map_key, map_location in map_locations.items():
            if checkMapLocation(map_location):
                gatherResources(map_location)
                break  # Break after finding the correct map location and gathering resources

        # Check for Fight Finish
        if not clickImage(fight_finish_image, "Fight finish"):
            logging.error("Failed to find Fight finish.")
        
        # Check for Job Level Up
        if not clickImage(job_levelup_image, "Job level up"):
            logging.error("Failed to find Job level up.")
        else:
            # If the Job Level Up screen is detected, click the OK button
            if not clickImage(job_levelup_ok_image, "Job level up OK"):
                logging.error("Failed to find Job level up OK.")

main()
