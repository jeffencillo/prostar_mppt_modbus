from pyModbusTCP.client import ModbusClient
import time
import numpy as np
import struct
import sys
from ast import literal_eval 

def main():
	ip = sys.argv[1]


SERVER_HOST = sys.argv[1]
SERVER_PORT = 502

c = ModbusClient()

c.host(SERVER_HOST)
c.port(SERVER_PORT)

while True:
# open or reconnect TCP to server
	if not c.is_open():
		if not c.open():
			print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    # if open() is ok, read register (modbus function 0x03)
	if c.is_open():
		print ("hourmeter, alarm_daily, load_fault_daily, array_fault_daily, Vb_min_daily, Vb_max_daily, Ahc_daily, Ahl_daily, Va_max_daily, Time in Absorption(HR)), Time in Equalize(HR), Time in Float(HR)")
		varhex = "0x8000"
		for i in range(0,255):
			i = int(varhex, 16)
			regs = c.read_input_registers(i,17)
			hourmeter = regs[0] + ((regs[1] & 0x00FF) << 32)
			print (hourmeter, end=",")
			
			alarm = (regs[3] << 16) + (regs[2] >> 16)
			if alarm == 0:
				print ("No alarms", end=",")
			elif (alarm & 1):
				print ("RTS OPEN", end=",")
			elif ((alarm & (1 << 1)) >> 1):
				print("RTS shorted", end=",") 
			elif ((alarm & (1 << 2)) >> 2):
				print("RTS Disconnected", end=",")
			elif ((alarm & (1 << 3)) >> 3):
				print("Ths (heatsink temp sensor) Open", end=",")
			elif ((alarm & (1 << 4)) >> 4):
				print("Ths (heatsink temp sensor)Sorted", end=",")
			elif ((alarm & (1 << 5)) >> 5):
				print("Heatsink Hot (active temp limiting)", end=",")
			elif ((alarm & (1 << 6)) >> 6):
				print("Tind (inductor temp sensor) Open", end=",")
			elif ((alarm & (1 << 7)) >> 7):
				print("Tind (inductor temp sensor) Short", end=",")
			elif ((alarm & (1 << 8)) >> 8):
				print("Tind Hot (active temp limiting)", end=",")
			elif ((alarm & (1 << 9)) >> 9):
				print("Current Limit", end=",")
			elif ((alarm & (1 << 10)) >> 10):
				print("I Offset", end=",")
			elif ((alarm & (1 << 11)) >> 11):
				print("Battery Sense Out of Range", end=",")
			elif ((alarm & (1 << 12)) >> 12):
				print("Battery Sense Disconnected", end=",")
			elif ((alarm & (1 << 13)) >> 13):
				print("Uncalibrated", end=",")
			elif ((alarm & (1 << 14)) >> 14):
				print("TB 5V", end=",")
			elif ((alarm & (1 << 15)) >> 15):
				print("FP10 Supply Out of Range", end=",")
			elif ((alarm & (1 << 16)) >> 16):
				print("[unused]", end=",")
			elif ((alarm & (1 << 17)) >> 17):
				print("FET Open", end=",")
			elif ((alarm & (1 << 18)) >> 18):
				print("IA Offset", end=",")
			elif ((alarm & (1 << 19)) >> 19):
				print("IL Offset", end=",")
			elif ((alarm & (1 << 20)) >> 20):
				print("3V Supply Out of Range", end=",")
			elif ((alarm & (1 << 21)) >> 21):
				print("12V Supply Out of Range", end=",")
			elif ((alarm & (1 << 22)) >> 22):
				print("VA High (current limit due to high Voc)", end=",")
			elif ((alarm & (1 << 23)) >> 23):
				print("Reset", end=",")
			elif ((alarm & (1 << 24)) >> 24):
				print("LVD", end=",")
			elif ((alarm & (1 << 25)) >> 25):
				print("Log Timeout", end=",")
			elif ((alarm & (1 << 26)) >> 26):
				print("EEPROM Access Failure", end=",")
			
			load_fault = (regs[5] << 16) + (regs[4] >> 16)

			if load_fault == 0:
				print ("no faults", end=",")
			elif (load_fault & 1):
				print ("External Short Circuit", end=",")
			elif ((load_fault & (1 << 1)) >> 1):
				print("Overcurrent", end=",")
			elif ((load_fault & (1 << 2)) >> 2):
				print("FET(s) Shorted", end=",")
			elif ((load_fault & (1 << 3)) >> 3):
				print("Software Bug", end=",")
			elif ((load_fault & (1 << 4)) >> 4):
				print("High Voltage Disconnect", end=",")
			elif ((load_fault & (1 << 5)) >> 5):
				print("Heatsink Over-Temperature", end=",")
			elif ((load_fault & (1 << 6)) >> 6):
				print("DIP Switch Changed (excl. DIP 8)", end=",")
			elif ((load_fault & (1 << 7)) >> 7):
				print("EEPROM Setting Edit (reset required)", end=",")


			array_fault = (regs[7] << 16) + (regs[6] >> 16)


			if array_fault == 0:
				print ("no faults", end=",")
			elif (array_fault & 1):
				print ("Overcurrent Phase 1", end=",")
			elif ((array_fault & (1 << 1)) >> 1):
				print("FET(s) Shorted", end=",")
			elif ((array_fault & (1 << 2)) >> 2):
				print("Software Bug", end=",")
			elif ((array_fault & (1 << 3)) >> 3):
				print("Battery HVD (High Voltage Disconnect)", end=",")
			elif ((array_fault & (1 << 4)) >> 4):
				print("Array HVD (High Voltage Disconnect)", end=",")
			elif ((array_fault & (1 << 5)) >> 5):
				print("EEPROM Setting Edit (reset required)", end=",")
			elif ((array_fault & (1 << 6)) >> 6):
				print("RTS Shorted", end=",")
			elif ((array_fault & (1 << 7)) >> 7):
				print("RTS was valid, now disconnected", end=",")
			elif ((array_fault & (1 << 8)) >> 8):
				print("Local temp. sensor failed", end=",")
			elif ((array_fault & (1 << 9)) >> 9):
				print("Battery LVD (Low Voltage Disconnect)", end=",")
			elif ((array_fault & (1 << 10)) >> 10):
				print("Slave Control Timeout", end=",")
			elif ((array_fault & (1 << 11)) >> 11):
				print("DIP Switch Changed (excl. DIP 8)", end=",")
			
			VBatt_min = bin(regs[8])
			a = struct.pack("H", int(VBatt_min,2))
			batt_min = np.frombuffer(a, dtype =np.float16)[0]
			print ( batt_min, end=",")

			VBatt_max = bin(regs[9])
			a = struct.pack("H", int(VBatt_max,2))
			batt_max = np.frombuffer(a, dtype =np.float16)[0]
			print (batt_max, end=",")

			Ahc = bin(regs[10])
			a = struct.pack("H", int(Ahc,2))
			ahc_daily = np.frombuffer(a, dtype =np.float16)[0]
			print (ahc_daily, end=",")

			Ahl = bin(regs[11])
			a = struct.pack("H", int(Ahl,2))
			ahl_daily = np.frombuffer(a, dtype =np.float16)[0]
			print (ahl_daily, end=",")
			
			Va = bin(regs[12])
			a = struct.pack("H", int(Va,2))
			Va_max_daily = np.frombuffer(a, dtype =np.float16)[0]
			print (Va_max_daily, end=",")
			
			print(regs[13]/3600, end=",")

			print(regs[14]/3600, end=",")
			
			print(regs[15]/3600)

			i += 0x0010
			varhex = hex(i)
	exit()
