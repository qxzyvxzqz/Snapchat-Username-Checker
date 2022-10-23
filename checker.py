import requests

try:
    usernames = list(open(input("Username File Path: ")).read().strip().split())
    output = input("Output File Path: ")
except Exception as e:
    print(f"[-] {e}")


def main():
    try:
        for username in usernames:
            res = requests.post(f"https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={username}&xsrf_token=PlEcin8s5H600toD4Swngg", headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Referer": "https://accounts.snapchat.com/", "Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==", "Connection": "keep-alive", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"})
            if "OK" in res.text:
                print(f"[+] {username} is available.")
                open(output, 'a').write(username + "\n")
            else:
                print(f"[-] {res.json()['value']['error_message']}")
    except Exception as e:
        print(f'[-] {e}')


if __name__ == "__main__":
    main()
