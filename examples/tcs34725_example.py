# TinyCircuits Color Sensor Wireling Python Example
# Prints color temperature, lux, and RGB values. There is a commented 
# out option that can be used to turn the LEDs on.
# Adapted from Adafruit example by:  Laverena Wienclaw for TinyCircuits
# Last updated: 1-10-20

import time
import board
import busio
import adafruit_tcs34725
import tinycircuits_wireling

# Enable and power Wireling Pi Hat
wireling = tinycircuits_wireling.Wireling()

# Set and selectPort matching Color Sensor Wireling and Pi Hat port
port = 0
wireling.selectPort(0)

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

# Main loop reading color temp, lux, and RGB values and printing it every second
while True:
    # Turn on on-board LEDs
    #sensor.cycles = 0 # Set to -1 to turn off

    # Read  and print the color temperature and lux of the sensor 
    temp = sensor.color_temperature
    lux = sensor.lux
    print('Temperature: {0}K Lux: {1}'.format(temp, lux))

    # Read and print the RGB values read by sensor
    r, g, b = sensor.color_rgb_bytes
    print('R: {0}  G: {1}  B: {2}'.format(r, g, b))
    
    # Delay for a second and repeat.
    time.sleep(1.0)