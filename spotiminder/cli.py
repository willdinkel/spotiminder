"""Console script for spotiminder."""
import argparse
import sys
import os
import spotiminder.spotiminder as core

def main():
    """Console script for spotiminder."""
    parser = argparse.ArgumentParser(description='Regularly check one or more Spotify playlists to ensure that their metadata is up-to-date.',
                                     allow_abbrev=False)
    parser.add_argument('client_id',
                        type=str,
                        help='your Spotify Web API client id')
    parser.add_argument('client_secret',
                        type=str,
                        help='your Spotify Web API client secret')
    parser.add_argument('json_file',
                        type=str,
                        help='path to your playlist metadata json file')
    parser.add_argument('--redirect_uri',
                        type=str,
                        default='http://localhost:8080',
                        help='your Spotify Web API redirect URI (defaults to http://localhost:8080)'
                        )
    parser.add_argument('--interval',
                        type=int,
                        default=60,
                        help='the time between checks, in seconds (default 60)')
    parser.add_argument('--image_folder',
                        type=str,
                        default="",
                        help='path to the folder that contains playlist cover images. Images must be JPEGs named <playlistID>.jpg and can\'t exceed 256KB in size.')
    args = parser.parse_args()

    # Verify the file is readable.
    if not os.access(args.json_file, os.R_OK):
        print(args.json_file, "is not readable.")
        sys.exit()

    return core.main(args)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
