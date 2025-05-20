# Day 21 - Dunder Methods: Custom Playlist

# This class represents the playlist class with several methods.
class Playlist:
    # This method initializes a playlist with name and list of songs.
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs  

    # This method is used to display the formatted string of playlist and songs.
    def __str__(self):
        return f"🎵 Playlist: {self.name} | {len(self.songs)} songs"

    # This method combines both playlists and gives the combined playlist as an output.
    def __add__(self, other):
        combined_name = f"{self.name} + {other.name}"
        combined_songs = self.songs + other.songs
        return Playlist(combined_name, combined_songs)

    # This method returns the length of the playlist.
    def __len__(self):
        return len(self.songs)

    # This method returns the list of songs in a playlist.
    def show_tracks(self):
        print(f"\n🎧 {self.name} Playlist:")
        for i, song in enumerate(self.songs, 1):
            print(f"{i}. {song}")

# main
def main():
    print("🎶 Day 21 - Dunder Methods: Playlist Demo\n")

    # This is an instance of Playlist class representing a list of songs into a playlist.
    chill = Playlist("Chill Vibes", ["Kurchi Madathapetti", "Follow Follow", "Dhivara"])
    focus = Playlist("Focus Boost", ["Padara padara", "Fear Song", "Bhairava Anthem"])

    # When we try to print the playlist internally it invokes __str__() to display nicely formatted string. (So, here fact that is generally
    # when we call print it internally calls the .__str__()).
    print(chill)
    print(focus)

    # Displays the length of playlist internally calls the __len__().
    print(f"\nLength of Chill Playlist: {len(chill)} tracks")

    # The '+' operation here combines / merges the 2 playlists, internally calls __add__()
    combo = chill + focus
    print("\nAfter merging:")
    print(combo)

    # This displays the combined songs with index number with songs
    combo.show_tracks()

# calling main() to starting execution of program
if __name__ == "__main__":
    main()
    