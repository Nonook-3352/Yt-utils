from pytube import YouTube

def download_as_mp4(url):
    try:
        yt = YouTube(url)
        filename = yt.title.replace('/', '∕') + ".mp4"
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=filename)
        # Replace '/' with fraction slash in the title
        #filename = yt.title.replace('/', '∕') + ".mp3"
        #video_stream.download(filename=filename)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    print("Type list to download all the urls in the urls.txt\nType url to download a single url via input")
    inp = input("> ")
    if inp == "list":
        with open('urls.txt', 'r') as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                if url:
                    download_as_mp4(url)
    elif inp == "url":
        url_inp = input("Url > ")
        download_as_mp4(url_inp)
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()

