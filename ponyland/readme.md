# How to connect to ponyland:
- From RU network: ssh myusername@servername.science.ru.nl
- From outside RU network: ssh -t username@applejack.science.ru.nl ssh servername


# Corpora
- [List of corpora can be found here](https://ponyland.science.ru.nl/wiki:ponyland:corpora)
- Can be found at /vol/bigdata/corpora


# Downloading stuff
Probably best to use FTP: [see site for specifics](https://ponyland.science.ru.nl/wiki:ponyland:sftp)

Or use ssh (overwrites local existing files): `scp -r user@host:/path/to/folder/ local-copy-of-folder`
Or use ssh (skips existing files): `rsync -au user@host:/path/to/folder/ local-copy-of-folder`




# Watch over resources:
- type htop

scp -r thaije@applejack.science.ru.nl:/vol/tensusers/klux/trainedModels/comp-a/* /home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/trainedData/comp-a
