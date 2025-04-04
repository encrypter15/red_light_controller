#!/usr/bin/env python3
import time, sys, logging
from pymodbus.client import ModbusTcpClient
from argparse import ArgumentParser

# Author: Rick Hayes, Version: 1.0, License: MIT

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def control_lights(ip, port=502, pulse_interval=2):
    """Control SCADA lighting with NSFW pulsing effect."""
    try:
        client = ModbusTcpClient(ip, port=port)
        if not client.connect():
            logger.error("Failed to connect to SCADA device at %s:%d", ip, port)
            sys.exit(1)
        
        logger.info("Connected to %s:%d. Pulsing lights...", ip, port)
        state = True
        while True:
            client.write_coil(0, state)  # Toggle coil 0 (e.g., light switch)
            logger.debug("Light state: %s", "ON" if state else "OFF")
            time.sleep(pulse_interval)
            state = not state
    except Exception as e:
        logger.error("Error: %s", e)
    finally:
        client.close()

if __name__ == "__main__":
    parser = ArgumentParser(description="NSFW SCADA Light Controller")
    parser.add_argument("--ip", required=True, help="SCADA device IP")
    parser.add_argument("--port", type=int, default=502, help="Modbus port")
    parser.add_argument("--interval", type=float, default=2, help="Pulse interval in seconds")
    args = parser.parse_args()
    control_lights(args.ip, args.port, args.interval)
