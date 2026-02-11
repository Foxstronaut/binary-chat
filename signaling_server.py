#!/usr/bin/env python3
"""
Minimal WebSocket signaling server for P2P WebRTC connections.
Routes SDP offers/answers and ICE candidates between peers.
"""

import asyncio
import json
import sys
from pathlib import Path

try:
    import websockets
except ImportError:
    print("Installing websockets...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "websockets"])
    import websockets

# Store connected peers: peerId -> websocket
peers = {}

async def handler(websocket, path):
    """Handle WebSocket connections from peers."""
    peer_id = None
    
    try:
        async for message in websocket:
            try:
                msg = json.loads(message)
                msg_type = msg.get('type')
                
                if msg_type == 'register':
                    peer_id = msg.get('peerId')
                    peers[peer_id] = websocket
                    print(f"✓ Peer registered: {peer_id}")
                    
                elif msg_type == 'offer':
                    target = msg.get('to')
                    if target in peers:
                        await peers[target].send(json.stringify({
                            'type': 'offer',
                            'from': peer_id,
                            'offer': msg.get('offer')
                        }))
                        print(f"→ Offer: {peer_id} → {target}")
                    
                elif msg_type == 'answer':
                    target = msg.get('to')
                    if target in peers:
                        await peers[target].send(json.stringify({
                            'type': 'answer',
                            'from': peer_id,
                            'answer': msg.get('answer')
                        }))
                        print(f"→ Answer: {peer_id} → {target}")
                    
                elif msg_type == 'candidate':
                    target = msg.get('to')
                    if target in peers:
                        await peers[target].send(json.stringify({
                            'type': 'candidate',
                            'from': peer_id,
                            'candidate': msg.get('candidate')
                        }))
                        
            except json.JSONDecodeError:
                pass
                
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        if peer_id in peers:
            del peers[peer_id]
            print(f"✗ Peer disconnected: {peer_id}")

async def main():
    port = 8765
    async with websockets.serve(handler, "0.0.0.0", port):
        print(f"WebSocket signaling server running on ws://0.0.0.0:{port}")
        print(f"Open http://localhost:{port}/../index.html in browser")
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nShutdown.")
