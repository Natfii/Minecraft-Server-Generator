import requests, json, subprocess, os


def getPaper():
    print("Getting Paper\nInput MC Version: ")
    mcVersion = input()
    try:
        response = requests.get("https://api.papermc.io/v2/projects/paper/versions/{}/builds".format(mcVersion), headers = {'accept': 'application/json'})
        
        if response.status_code != 200: #make sure we can get something
            print("Error getting Paper: Status code returned {}".format(response.status_code))
            return
        
        paperBuilds = []
        for build in (response.json()).get('builds'):
            paperBuilds.append("Build number: {} Build Date: {}".format(build.get('build'), build.get('time')))

        print("Latest Paper build is {} \n1. Download and install latest (RECCOMENDED) \n2. List additional builds ".format(paperBuilds[-1]))
        x = input()
        if x == '1':
            print(paperBuilds[-1].split(' '))
            build = paperBuilds[-1].split(' ')[2]
        elif x == '2':
            for build in paperBuilds:
                print(build)
            print("Enter the build number you want to download:")
            build = input()
        else:
            print("Invalid input")
            return

        print("Downloading Paper Build {} for MC Version {}".format(build, mcVersion))
        response = requests.get("https://papermc.io/api/v2/projects/paper/versions/{}/builds/{}/downloads/paper-{}-{}.jar".format(mcVersion, build, mcVersion, build))
        open('paper.jar', 'wb').write(response.content)
    except:
        print("Error getting Paper: Invalid download or no connection can be made")
        return
    



def main():
    jarType = ''
    print("Choose a Server Type: \n1. Paper \n2. Vanilla")
    serverType = input()
    if serverType == '1':
        print("Paper Selected")
        jarType = 'paper'
        getPaper()
    elif serverType == '2':
        print("Vanilla Selected")
        jarType = 'vanilla'
    
    print("Installing...")
    subprocess.call(['java', '-Xmx1024M', '-Xms1024M', '-jar', jarType + '.jar', 'nogui'])


if __name__ == "__main__":
    main()