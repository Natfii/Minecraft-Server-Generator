import requests, json

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
            paperBuilds.append("Build number:{} Build Date:{}".format(build.get('build'), build.get('time')))

        print("Latest Paper build is {} \n1. Download and install \n2. List additional builds ".format(paperBuilds[-1]))

    except:
        print("Error getting Paper: No connection can be made")
        return
    



def main():
    print("Choose a Server Type: \n1. Paper \n2. Vanilla")
    serverType = input()
    if serverType == '1':
        print("Paper Selected")
        getPaper()

if __name__ == "__main__":
    main()