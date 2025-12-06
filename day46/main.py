import requests  # For making HTTP requests to websites
from bs4 import BeautifulSoup  # For parsing and navigating HTML content
from dotenv import load_dotenv  # For loading environment variables from a .env file
import spotipy  # Python wrapper for the Spotify Web API
from spotipy.oauth2 import SpotifyOAuth  # Handles Spotify OAuth authentication
import os  # Provides access to environment variables and OS-level features

# Load all environment variables from .env into the program
load_dotenv()

class spotify_app:
    """
    A Spotify automation application that:
    1. Scrapes the Billboard Hot 100 chart
    2. Searches for each song on Spotify
    3. Creates a playlist if it does not already exist
    4. Adds songs to the playlist while preventing duplicates
    """

    def __init__(self):
        """
        Initialize the Spotify application.
        - Loads credentials from environment variables
        - Authenticates the user using Spotify OAuth
        - Creates a Spotipy client for interacting with Spotify APIs
        """
        self.CLIENTID = os.getenv('clientID')        # Spotify application client ID
        self.SECRET = os.getenv('clientSecret')      # Spotify application client secret
        self.userID = os.getenv('userId')             # Spotify user ID

        # Authenticate with Spotify using OAuth
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",     # Permission to modify private playlists
                redirect_uri="https://example.org/callback",  # OAuth redirect URI
                client_id=self.CLIENTID,             # Client ID for Spotify app
                client_secret=self.SECRET,            # Client secret for Spotify app
                show_dialog=True,                     # Force login/consent dialog
                cache_path="token.txt",               # Store auth token locally
                username="Awapk",                     # Spotify username
            )
        )

    def music_uri(self):
        """
        Scrapes the Billboard Hot 100 page and retrieves a list of Spotify track URIs.

        Returns:
            list: A list of Spotify track URIs corresponding to Billboard songs.
        """
        music_uri_list = []  # Stores Spotify URIs for found songs

        # Request the Billboard Hot 100 chart page
        reponse = requests.get("https://www.billboard.com/charts/hot-100/")
        music_titles = reponse.text

        # Parse the returned HTML content
        music_soup = BeautifulSoup(music_titles, "html.parser")

        # Locate all song containers
        music_info_list = music_soup.find_all(
            class_="o-chart-results-list-row-container"
        )

        for music_info in music_info_list:
            # Extract song metadata from HTML
            music_position = music_info.find(class_="c-label").get_text().strip()
            music_title = music_info.find(id="title-of-a-story").text.strip()
            music_artist = music_info.select_one(".a-no-trucate").text.strip()

            try:
                # Search Spotify for the song
                musics_data = self.sp.search(
                    q=f"track:{music_title} year:{2025}",
                    type="track"
                )

                # Take the first search result and extract its URI
                uri = musics_data["tracks"]["items"][0]["uri"]
                music_uri_list.append(uri)

            except Exception as e:
                # Handles cases where the song cannot be found on Spotify
                print(f"song not found because of {e}")

        return music_uri_list  # Return all collected URIs

    def new_playlist(self):
        """
        Creates a Spotify playlist only if a playlist with the same name
        does not already exist.

        Returns:
            str: The Spotify playlist ID (existing or newly created).
        """
        playlist_name = "top 100 billboard"

        # Retrieve user's playlists (paginated)
        playlists = self.sp.current_user_playlists(limit=50)

        # Check through playlists for an existing one with the same name
        while playlists:
            for playlist in playlists["items"]:
                if playlist["name"].lower() == playlist_name.lower():
                    print("Playlist already exists. Using existing playlist.")
                    return playlist["id"]

            # Handle pagination
            if playlists["next"]:
                playlists = self.sp.next(playlists)
            else:
                playlists = None

        # If playlist does not exist, create it
        user_playlist = self.sp.user_playlist_create(
            user=self.userID,
            name=playlist_name,
            public=True,
            collaborative=False,
            description='playlist created from top 100 billboard'
        )

        print("New playlist created.")
        return user_playlist["id"]

    def add_music(self):
        """
        Adds Billboard Hot 100 songs to the playlist.
        - Prevents duplicate playlists
        - Prevents duplicate songs in the playlist
        """

        # Get the playlist ID (existing or newly created)
        playlist_id = self.new_playlist()

        # Get URIs for Billboard songs
        music_uri = self.music_uri()

        # Retrieve existing tracks already in the playlist
        existing_tracks = self.sp.playlist_items(playlist_id)

        # Extract existing song URIs into a set for fast lookup
        existing_uris = {
            item["track"]["uri"]
            for item in existing_tracks["items"]
            if item["track"]
        }

        # Keep only songs that are not already in the playlist
        new_tracks = [uri for uri in music_uri if uri not in existing_uris]

        if new_tracks:
            # Add only new (non-duplicate) songs
            self.sp.playlist_add_items(
                playlist_id=playlist_id,
                items=new_tracks
            )
            print(f"{len(new_tracks)} new songs added to playlist.")
        else:
            print("No new songs to add (playlist already up to date).")

# Run the application
spotify_app().add_music()
