# Top-100-Songs

This project extracts the top 100 songs from the Billboard Hot 100 chart for a specified date and creates a Spotify playlist with those songs.

## Features

- Extracts top 100 songs from Billboard Hot 100 based on a user-specified date.
- Authenticates with Spotify using OAuth.
- Creates a private Spotify playlist with the extracted songs.

## Requirements

- `requests`
- `beautifulsoup4`
- `spotipy`
- `python-dotenv`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Top-100-Songs.git
    cd Top-100-Songs
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project directory and add your Spotify API credentials:
    ```env
    SPOTIFY_CLIENT_ID=your_client_id
    SPOTIFY_CLIENT_SECRET=your_client_secret
    SPOTIPY_REDIRECT_URI=your_redirect_uri
    ```