# README

## Overview

This script is designed to automate the process of gathering resources in a game by using image recognition to identify specific elements on the screen. The script runs for a specified duration and repeatedly checks various map locations to gather resources. It also handles tasks such as clicking on buttons to finish fights and leveling up jobs.

## Features

- **Resource Gathering**: Automatically identifies and clicks on specific resources in the game.
- **Map Location Check**: Verifies if the correct map location is displayed before gathering resources.
- **Job Leveling**: Automates the process of leveling up jobs by clicking appropriate buttons.
- **Fight Completion**: Automatically clicks to finish fights when detected.

## Requirements

- Python 3.x
- `pyautogui` library
- A collection of images that match in-game elements, stored in an `images/` directory.

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the required library using pip:

   ```bash
   pip install pyautogui
   ```

3. Place the necessary images in the `images/` directory. These images should match the in-game elements that the script will interact with.

## Configuration

Several settings can be configured at the beginning of the script:

- `imageOffset`: The pixel offset for clicking on images.
- `run_duration_minutes`: The total time the script should run (in minutes).
- `confidence_threshold`: The confidence level for image matching (default is 0.8).

### Resource Types

You can define different types of resources that the script should gather in the `resource_types` dictionary. Each resource type includes:

- `gather_time`: Time to wait after clicking the resource.
- `images`: A list of image paths that represent the resource.

### Map Locations

Map locations can be defined in the `map_locations` dictionary, where each location is associated with an image of the map.

## Usage

1. Configure the script by setting the appropriate values for `run_duration_minutes`, `confidence_threshold`, and adding any additional resources or map locations.
2. Run the script:

   ```bash
   python main6.py
   ```

3. The script will log its actions to a file with the current date and also print logs to the console.

## Functions

- **`clickImage(image_path, description, retries=3, confidence=confidence_threshold, delay=2)`**: Attempts to find and click an image on the screen. Returns `True` if successful.
- **`checkMapLocation(map_location)`**: Checks if the correct map location is displayed.
- **`gatherResources(map_location)`**: Gathers resources based on the current map location.
- **`main()`**: The main function that controls the script's execution.

## Logs

Logs are saved to a file named `resource_gathering_<date>.log` and include details of the script's actions, such as whether images were successfully found and clicked.

## Customization

You can extend the script by adding more resource types or map locations as needed. Simply update the `resource_types` and `map_locations` dictionaries with the appropriate data.

## Troubleshooting

- **Images Not Found**: Ensure that the images in the `images/` directory match the in-game elements exactly, and adjust the `confidence_threshold` if needed.
- **Script Not Working as Expected**: Check the log file for any errors or warnings that could indicate where the issue lies.

----------- FR ----------
# README

## Aperçu

Ce script est conçu pour automatiser le processus de collecte de ressources dans un jeu en utilisant la reconnaissance d'images pour identifier des éléments spécifiques à l'écran. Le script s'exécute pendant une durée spécifiée et vérifie à plusieurs reprises différentes locations sur la carte pour collecter des ressources. Il gère également des tâches telles que le clic sur des boutons pour terminer des combats et monter de niveau des métiers.

## Fonctionnalités

- **Collecte de Ressources** : Identifie et clique automatiquement sur des ressources spécifiques dans le jeu.
- **Vérification de la Location sur la Carte** : Vérifie si la bonne location sur la carte est affichée avant de collecter des ressources.
- **Montée en Niveau des Métiers** : Automatise le processus de montée en niveau des métiers en cliquant sur les boutons appropriés.
- **Fin des Combats** : Clique automatiquement pour terminer les combats lorsqu'ils sont détectés.

## Prérequis

- Python 3.x
- Bibliothèque `pyautogui`
- Une collection d'images correspondant aux éléments du jeu, stockées dans un répertoire `images/`.

## Installation

1. Assurez-vous que Python 3.x est installé sur votre système.
2. Installez la bibliothèque requise avec pip :

   ```bash
   pip install pyautogui
   ```

3. Placez les images nécessaires dans le répertoire `images/`. Ces images doivent correspondre aux éléments du jeu avec lesquels le script interagira.

## Configuration

Plusieurs paramètres peuvent être configurés au début du script :

- `imageOffset` : Le décalage en pixels pour cliquer sur les images.
- `run_duration_minutes` : Le temps total pendant lequel le script doit s'exécuter (en minutes).
- `confidence_threshold` : Le niveau de confiance pour la correspondance des images (par défaut à 0,8).

### Types de Ressources

Vous pouvez définir différents types de ressources que le script doit collecter dans le dictionnaire `resource_types`. Chaque type de ressource comprend :

- `gather_time` : Temps d'attente après avoir cliqué sur la ressource.
- `images` : Une liste de chemins d'images représentant la ressource.

### Locations sur la Carte

Les locations sur la carte peuvent être définies dans le dictionnaire `map_locations`, où chaque location est associée à une image de la carte.

## Utilisation

1. Configurez le script en définissant les valeurs appropriées pour `run_duration_minutes`, `confidence_threshold`, et en ajoutant toute ressource ou location supplémentaire.
2. Exécutez le script :

   ```bash
   python main6.py
   ```

3. Le script enregistrera ses actions dans un fichier avec la date actuelle et imprimera également les journaux dans la console.

## Fonctions

- **`clickImage(image_path, description, retries=3, confidence=confidence_threshold, delay=2)`** : Tente de trouver et de cliquer sur une image à l'écran. Retourne `True` si réussi.
- **`checkMapLocation(map_location)`** : Vérifie si la bonne location sur la carte est affichée.
- **`gatherResources(map_location)`** : Collecte les ressources en fonction de la location actuelle sur la carte.
- **`main()`** : La fonction principale qui contrôle l'exécution du script.

## Journaux

Les journaux sont enregistrés dans un fichier nommé `resource_gathering_<date>.log` et incluent des détails sur les actions du script, comme si les images ont été trouvées et cliquées avec succès.

## Personnalisation

Vous pouvez étendre le script en ajoutant plus de types de ressources ou de locations sur la carte selon vos besoins. Mettez simplement à jour les dictionnaires `resource_types` et `map_locations` avec les données appropriées.

## Dépannage

- **Images Non Trouvées** : Assurez-vous que les images dans le répertoire `images/` correspondent exactement aux éléments du jeu, et ajustez le `confidence_threshold` si nécessaire.
- **Script Ne Fonctionne Pas Comme Prévu** : Vérifiez le fichier journal pour toute erreur ou avertissement qui pourrait indiquer où se trouve le problème.
