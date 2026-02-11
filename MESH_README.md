# Bluetooth Mesh Chat

A peer-to-peer mesh networking app using Bluetooth Low Energy (BLE) for device-to-device messaging without internet or centralized servers.

## Files

- `mesh.html` — main app (single-file web app with UI + JavaScript)
- `index.html` — original optical communication version (archive)

## How It Works

### Architecture
- **Node ID**: Each device gets a unique persistent ID stored in localStorage
- **Mesh Routing**: Packets are relayed between nodes with a hop count limit (default 5 hops)
- **Packet Format**: `[packetId] [hopCount] [source] [dest] [type] [payload_len] [payload] [CRC]`
- **Message Types**: 
  - `0` = message
  - `1` = acknowledgment
  - `2` = relay notification

### Features
- Multi-hop message relay (can reach nodes not directly visible)
- Duplicate packet detection (prevents infinite loops)
- Nearby node discovery and display
- Message history with timestamps
- Visual distinction between sent, received, and relayed messages

## Setup & Usage

### Requirements
- Modern browser with Web Bluetooth API support (Chrome, Edge, Opera, Samsung Internet)
- Android device or Bluetooth-capable Linux with proper browser

### Running

```bash
# Serve the app locally
cd "/home/foxstronaut/Scripts/binary chat"
python3 -m http.server 8000

# Open http://localhost:8000/mesh.html on multiple devices or browser tabs
```

### Testing

1. **Single Device (Tab 1)**: 
   - Open `http://localhost:8000/mesh.html`
   - Press "Start Node"
   - Send a message

2. **Second Device (Tab 2 or Another Phone)**:
   - Open the same URL
   - Press "Start Node"
   - Send a message
   - Messages should appear on Tab 1

3. **Multi-hop (3+ Devices)**:
   - Set up 3 devices in separate rooms/areas
   - Device A → Device B → Device C
   - Messages from A should reach C via B's relay

## Configuration

Edit the `CONFIG` object in `mesh.html` to tune:

```javascript
CONFIG = {
  MESH_UUID: '12345678-1234-5678-1234-56789abcdef0',  // BLE service UUID
  MAX_HOP_COUNT: 5,           // Max relay distance
  RELAY_TIMEOUT: 2000,        // ms before allowing relay of same packet
  SCAN_INTERVAL: 5000,        // How often to scan for nodes
  SCAN_DURATION: 4000         // Scan duration
};
```

## Limitations

- **Web Bluetooth API**: Requires browser support and user permission each time
- **Advertisement Data Size**: BLE advertisements limited to 31 bytes, so large messages require fragmentation (not yet implemented)
- **Range**: Typically 10–100 meters depending on device and environment
- **Latency**: Not real-time; designed for casual messaging

## Future Enhancements

- Fragmentation and reassembly for larger messages
- Persistent message storage and offline queuing
- ACK-based reliability
- Encrypted payload
- Better node discovery (continuous background scanning)
- PWA support for better UX

## License

Public domain demo

