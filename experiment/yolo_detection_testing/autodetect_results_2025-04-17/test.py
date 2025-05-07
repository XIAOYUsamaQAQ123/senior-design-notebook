#!/usr/bin/env python3
import sys
import time
import serial
import serial.tools.list_ports

def list_ports():
    ports = serial.tools.list_ports.comports()
    for i, p in enumerate(ports):
        print(f"[{i}] {p.device} — {p.description}")
    return ports

def select_port(ports):
    idx = input("Select port number: ")
    try:
        return ports[int(idx)].device
    except:
        print("Invalid selection.")
        sys.exit(1)

def main():
    print("Scanning serial ports...")
    ports = list_ports()
    if not ports:
        print("No serial ports found. Plug in your Nano and try again.")
        return

    port = select_port(ports)
    print(f"Opening {port} @ 115200 baud…")
    try:
        ser = serial.Serial(port, 115200, timeout=1)
    except serial.SerialException as e:
        print("Failed to open serial port:", e)
        return

    time.sleep(2)  # allow Nano to reset
    print("Nano should say “Nano ready” now.")
    line = ser.readline().decode(errors='ignore').strip()
    if line:
        print("→", line)

    def send(cmd, wait=0.5):
        ser.write(cmd.encode())
        time.sleep(wait)
        resp = ser.readline().decode(errors='ignore').strip()
        print(f"Sent '{cmd}', Nano replied:", resp)

    print("\nTesting LED:")
    send('L')   # LED on
    time.sleep(1)
    send('l')   # LED off

    print("\nTesting Buzzer:")
    send('B')   # buzzer on
    time.sleep(1)
    send('b')   # buzzer off

    ser.close()
    print("\nDone.")

if __name__ == "__main__":
    main()
