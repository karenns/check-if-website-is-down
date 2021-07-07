import urllib.request


# Using readlines()
file1 = open('websites.txt', 'r')
Lines = file1.readlines()

# Erase 
file2 = open('output.txt', 'r+')
file2.truncate(0) 
file2.writelines("website,server IP");
file2.writelines("\n");

# Websites that are not in our hosting
websitesDown = []

# Strips the newline character
for line in Lines:
    website = line.strip()
    website = "https://" + website;
    requestCode = urllib.request.urlopen(website).getcode()
    
    # Check if is one of our hostings
    if requestCode != '200':
        websitesDown.append(website);
    
    # writing to file
    output = [website, ",", str(requestCode), "\n"]
    file2 = open('output.txt', 'a')
    file2.writelines(output)
    file2.close()

#Output websites not in our hosting
file2 = open('output.txt', 'a') 
file2.writelines("\n")
file2.writelines("\n")
file2.writelines("Websites Down")
file2.writelines("\n")
 
for website in websitesDown:
    file2.writelines(website)
    file2.writelines("\n")
    file2.close()
