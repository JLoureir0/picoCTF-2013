# Spamcarver

* Download the acient jpg
* Open it with a hex editor
* Search for jpg End of Image bytes `0xFF 0xD9`
* Delete all the data prior to the EOI flag and the flag itself
* The new file is a zip that contains a new jpg with the key
