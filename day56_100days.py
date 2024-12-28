#myGPTexperiment
# using Copilot with GPT-4o
# Day 56: Project Day: Music Streaming

# Specs:
# - Read the data from the csv file '100MostStreamedSongs.csv' in the same folder.
# - Create a folder called '100MostStreamedSongs' in the same folder.
# - Create an empty sub-folder inside the '100MostStreamedSongs' folder for each 'Artist'.
# - Create one blank text file per 'Song' with the name of the 'Song' by that 'Artist(s)' in the sub-folder. 
# - For each 'Artist(s)', check the folder to see if it already has a folder. If it exists, then use it. If not, create a new one.

import os
import csv

# Define the path to the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), '100MostStreamedSongs.csv')
# Define the path to the main folder
main_folder_path = os.path.join(os.path.dirname(__file__), '100MostStreamedSongs')

# Create the main folder if it doesn't exist
if not os.path.exists(main_folder_path):
    os.makedirs(main_folder_path)

# Read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(f"Processing row: {row}")  # Log the row being processed
        if 'Artist(s)' in row and 'Song' in row:
            artist = row['Artist(s)']
            song = row['Song']
            
            # Define the path to the artist's folder
            artist_folder_path = os.path.join(main_folder_path, artist)
            
            # Create the artist's folder if it doesn't exist
            if not os.path.exists(artist_folder_path):
                os.makedirs(artist_folder_path)
            
            # Define the path to the song file
            song_file_path = os.path.join(artist_folder_path, f"{song}.txt")
            
            # Create an empty text file for the song
            with open(song_file_path, mode='w', encoding='utf-8') as song_file:
                pass
        else:
            print("Error: 'Artist(s)' or 'Song' key not found in the row")