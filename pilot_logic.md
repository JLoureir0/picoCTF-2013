# Pilot Logic

* Download the partial dump of the disk
* Mount the file with `sudo mount -o loop pilot_logic_image_file folder_to_mount_the_fs`
* Change directory to the folder where you mounted the image
* List all the files with `ls -lRa` or `find .` or if you have tree installed `tree . -a`
* Read the key file in the secret folder running `cat home/pilotbot/.secret/key`
