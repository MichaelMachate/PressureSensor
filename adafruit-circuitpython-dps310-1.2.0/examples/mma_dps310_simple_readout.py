import time
import board
import busio
import adafruit_dps310

i2c = busio.I2C(board.SCL, board.SDA)

dps310 = adafruit_dps310.DPS310(i2c)


dps310.reset()
dps310.pressure_oversample_count = adafruit_dps310.SampleCount.COUNT_128
dps310.pressure_rate = adafruit_dps310.Rate.RATE_4_HZ
dps310.mode = adafruit_dps310.Mode.CONT_PRESSURE
timestamp = time.strftime("%b-%d-%Y_Time_%H-%M-%S", time.localtime())
filename = "PressureList_" + timestamp + ".csv"
csvfile = open(filename, 'w', 1)

while True:
    dps310.wait_pressure_ready()
    timestamp = time.strftime("%y.%m.%d_%H:%M:%S;", time.localtime())
    
    #print("Temperature = %.3f *C" % dps310.temperature)
    print("Pressure = %.4f hPa" % dps310.pressure)
    print("")
    csvfile.write(str(timestamp)+''.join(" {0:0.4f}".format(dps310.pressure)) + "\n")
