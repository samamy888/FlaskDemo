import asyncio
from bleak import BleakScanner, BleakClient
import time

async def scan_devices():
    devices = await BleakScanner.discover()
    filtered_devices = list(filter(lambda device: device.name != None, devices))
    for device in filtered_devices:
        rssi = get_rssi(device.details)
        print(f"Device: {device.name}, RSSI: {rssi}")


async def connect_to_device(device_address):
    async with BleakClient(device_address) as client:
        await client.is_connected()
        print(f"Connected to {device_address}")
        
        # 在此处添加与BLE设备的交互逻辑
        # 例如读取特征值、写入数据等

def get_rssi(device):
    if device is None:
        return None

    if hasattr(device, 'adv') and hasattr(device.adv, 'raw_signal_strength_in_d_bm'):
        return device.adv.raw_signal_strength_in_d_bm
    else:
        return None

if __name__ == "__main__":
    while True:
        # 扫描附近的BLE设备
        loop = asyncio.get_event_loop()
        loop.run_until_complete(scan_devices())

    # 连接到特定的BLE设备
    # device_address = "设备的地址"
    # loop.run_until_complete(connect_to_device(device_address))