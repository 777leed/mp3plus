function get_link() {
    linkbox = document.getElementById("link");
    link = linkbox.value;
    console.log("your link is the following: "+ link)
    url = link.replace(/\s+/g, '');
    eel.download_mp3(url);
}