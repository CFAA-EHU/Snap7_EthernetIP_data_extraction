# Import necessary modules
import time
import snap7
import struct

# Define the IP address of the PLC
plc_ip = 'PLC_IP'  # Replace 'PLC_IP' with the actual IP address of the PLC

# Define the DB number and starting byte of the variable you want to read
db_number = 500
start_byte = 1

# Create a client object for communication with the PLC
client = snap7.client.Client()

# Connect to the PLC using the specified IP address and TCP port 102 (default)
client.connect(plc_ip, 0, 2)

# Uncomment the following lines if you want to list the blocks in the PLC
# blocks = client.list_blocks()
# print(blocks)

while True:
    # Read a single byte (4 bytes) from the specified DB

    # Axis X1
    byte_array = client.db_read(db_number, start_byte, 4)
    value = snap7.util.get_real(byte_array, 0)  # Convert the byte array to a floating-point number
    # Print the value read from Axis X1
    print("Axis X1 Value:", value)

    # Axis Z1
    byte_array2 = client.db_read(db_number, 4, 4)
    value2 = snap7.util.get_real(byte_array2, 0)  # Convert the byte array to a floating-point number
    # Print the value read from Axis Z1
    print("Axis Z1 Value:", value2)


# disconnect from the PLC
client.disconnect()


