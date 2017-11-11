Replace occurences of a string recursivly for all files in a folder:
`find /home/www -type f -print0 | xargs -0 sed -i 's/subdomainA\.example\.com/subdomainB.example.com/g'`
