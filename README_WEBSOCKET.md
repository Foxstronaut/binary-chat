# P2P WebSocket Chat with QR Code Pairing

A fully peer-to-peer (P2P) messaging app using WebRTC data channels. Device discovery uses QR codes or manual ID entry.

## How It Works

1. **Signaling**: WebSocket server routes WebRTC offer/answer/ICE candidates
2. **P2P**: Once connected, messages go directly via WebRTC data channel (not through server)
3. **Discovery**: Share QR code or peer ID to initiate connection
4. **Fully P2P**: No message relay through server (only initial negotiation)

## Files

- `index.html` — Frontend (QR code generation, chat UI)
- `signaling_server.py` — WebSocket signaling server

## Setup

### Install Python dependencies

```bash
pip install websockets
```

### Run the signaling server

```bash
python3 signaling_server.py
```

Server will run on `ws://0.0.0.0:8765`

### Run the web server (HTTP in separate terminal)

```bash
cd "/home/foxstronaut/Scripts/binary chat"
python3 -m http.server 8000
```

Web UI available at `http://localhost:8000/index.html`

## Usage

### Device 1 (Initiator)
1. Open `http://localhost:8000/index.html`
2. Click "Show QR" to display your peer ID as QR code
3. Share QR code or manually share your ID

### Device 2 (Responder)
1. Open the same URL
2. Click "New Peer"
3. Scan QR code or paste the peer ID from Device 1
4. Connection establishes automatically
5. Start chatting!

## Architecture

```
Device A                                 Device B
  ↓                                         ↓
Browser ←→ WebSocket (signaling) ←→ Browser
  ↓                                         ↓
  ├─ Generate offer                      ├─ Receive offer
  ├─ Send via WebSocket                  ├─ Generate answer
  │                                       ├─ Send via WebSocket
  ├─ Receive answer                      └─ Setup data channel
  ├─ Setup data channel
  │
  ↓ [Data Channel Established]
  
Messages now flow directly P2P ←→ via WebRTC data channel
(no server involvement)
```

## Features

- ✅ Fully P2P (signaling only, not messaging)
- ✅ QR code pairing
- ✅ No account/login required
- ✅ End-to-end: can add encryption easily
- ✅ Works on any WebRTC-capable browser

## Limitations

- Signaling server needed (can be deployed anywhere)
- Works best on same LAN (public relay servers needed for NAT traversal)
- Browser must support WebRTC (most modern browsers do)

## Next Steps

- Add STUN/TURN servers for NAT traversal (public internet)
- Add message encryption (libsodium.js or TweetNaCl.js)
- Deploy signaling server to cloud (Heroku, AWS, DigitalOcean, etc.)
- PWA for offline access

## License

Public domain demo
