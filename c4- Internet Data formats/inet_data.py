#import data from internet
import urllib.request
def main():
    # pass # this is a placeholder, do-nothing statement
    weburl = urllib.request.urlopen("http://www.google.com")
    print("result code:", weburl.getcode())   #result code: 200

    data = weburl.read()
    print(data)

if __name__ == "__main__":
    main()
