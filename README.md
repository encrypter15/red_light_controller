# Red Light Controller
**Author**: Rick Hayes  
**Version**: 1.0  
**License**: MIT  

## Description
A SCADA tool to pulse lights via Modbus, simulating NSFW ambiance control. Tests vulnerabilities in lighting control systems.

## Features
- Connects to Modbus TCP devices
- Adjustable pulse intervals
- Logging for debugging

## Requirements
- Python 3.x
- `pymodbus` (`pip install pymodbus`)

## Usage
```bash
python3 red_light_controller.py --ip 192.168.1.100 --port 502 --interval 1.5
```
