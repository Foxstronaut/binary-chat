# Optical P2P: screen/flash ↔ camera

This is a simple single-file web app that demonstrates peer-to-peer messaging using visible light: one device flashes its screen (or flashlight) and the other device receives by sampling the camera.

Files:
- `index.html` — main app (UI + JavaScript)

How it works (brief):
- Sender builds a packet: 16-bit length + payload bytes + 32-bit CRC.
- Packet bits are Manchester-encoded and preceded by a 16-bit alternating preamble.
- Sender flashes the screen (and optionally device torch) at a user-selected symbol duration.
- Receiver samples camera frames, bins samples at the symbol interval, detects the preamble, decodes Manchester, checks CRC, and displays the message.

Usage:
1. Open `index.html` on both devices (use mobile browser for torch support and camera access).
2. On the sender device choose `Sender` mode, enter your message, optionally enable `Try torch`, and press `Send (flash)`.
3. On the receiver device choose `Receiver` mode and press `Start Receiver`.
4. Ensure both devices use the same symbol duration (default 100 ms). If the receiver can't decode, try increasing symbol duration to 150–200 ms.

Tips:
- Keep the camera exposure stable and avoid rapid auto-adjust (point device before sending to let AE/AF settle).
- For screen-to-camera, use full-screen and maximum brightness for best results.
- For flashlight-to-camera, the app attempts to enable the camera torch (if supported).
- Start with short messages for testing.

Limitations & notes:
- This is a basic demo, built for clarity and portability in browsers. It trades raw throughput for robustness.
- Symbol duration, camera frame-rate, and auto-exposure behavior on different devices affect reliability.
- For production-grade optical communication you'd use hardware sync, better modulation (multi-level or OFDM), and stronger FEC.

License: public domain demo
