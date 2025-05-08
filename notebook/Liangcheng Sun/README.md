# Liangcheng Sun’s Worklog

Here is Liangcheng Sun’s worklog.

---
[Project spec (Word)](./docs/spec.docx)
- [**2025-02-12 – Project design & proposal**] 
  I am drawing the full block diagram for our system and then writing up the project proposal so we have a clear plan.
  [Proposal](./block_diagram.pdf)![image]
  PCB schematic and design:(https://github.com/user-attachments/assets/8c1546c0-e529-433e-b971-230e47ce6992)![image](https://github.com/user-attachments/assets/3243513e-a6d3-4d07-b386-b5bfd8e293c6)


- [**2025-02-21 – Hardware components ordered online**]
  Based on our design, I went online to order all the needed parts, and I made sure each piece matches our specs.
  Order![image](https://github.com/user-attachments/assets/89c70b14-fde2-48f5-bdf8-28354ee2a668)

- [**2025-02-25 – PCB design kickoff**] 
  After a quick study of PCB layout rules, I began designing our board, placing components and routing tracks step by step.

- [**2025-03-02 – OLED troubleshooting on breadboard**]  
  I built the main circuit on a breadboard, but the OLED display stayed blank—so I measured every pin voltage on both the ESP32 and the OLED, and all readings looked normal.
  OLED Screen:![image](https://github.com/user-attachments/assets/cd2a97a7-a4a8-47d6-b282-ef72f9d72fbb)
  ESP32 Wroom 32:![image](https://github.com/user-attachments/assets/27411732-fa22-4b97-b2b4-47cb807eaf21)

- [**2025-03-06 – Swapped ESP32 for ATmega328**]  
  To isolate the issue, I replaced the ESP32 with an ATmega328, but despite the swap, the screen still would not turn on.
  Arduino nano board ATmega328:![image](https://github.com/user-attachments/assets/8944e127-89aa-4dc3-b464-f021acc434f6)

- [**2025-03-12 – Demo & TA feedback (moved to ML training)**]
  During our breadboard demo, we showed partial functions and explained the OLED issue to TA Maanas and Professor—then they suggested skipping the OLED for now and focusing on ML model training and the camera interface.

- [**2025-03-23 – OLED still failing after hardware swap**]
  Even after replacing all hardware modules and checking connections again, the OLED remains unresponsive, so I need another plan.

- [**2025-04-15 – Raspberry Pi camera setup & capture via SSH**] 
  I successfully set up the Raspberry Pi camera, and now I can control it from my laptop via SSH to capture images automatically.
  Raspberry Pi 4: ![image](https://github.com/user-attachments/assets/3e7ee2f7-dba8-4c05-93c0-f05cc2d24c53)
  Camera Module:![image](https://github.com/user-attachments/assets/0a77d8b9-543b-45af-937e-16b6bd9cdf50)

- [**2025-04-23 – Redesign: ATmega328 + remote display + nRF24L01**]
  We redesigned our system: kept the ATmega328, removed the OLED in favor of a screen on a remote device, and added two nRF24L01 modules so the Pi and ATmega can talk wirelessly; I then laid out and ordered a new PCB.
  nRF24L01:![image](https://github.com/user-attachments/assets/b5c3dcf5-8f0e-4e9d-a20b-c091f208e49f)

- [**2025-04-26 – Swapped Pi camera for webcam**(./2025-04-26.md)  
  To improve reliability, I replaced the Pi camera module with a standard USB webcam that works smoothly.

- [**2025-04-27 – nRF24L01 issues → fallback to USB cable**]
  After facing unreliable links with the nRF24L01 modules, I decided to use a USB cable to connect the Pi and ATmega directly, which is more stable.
