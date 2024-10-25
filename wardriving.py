import csv
import subprocess
import time

# GPS coordinates (you can replace this with your actual GPS data)
gps_coords = ['37.7749', '-122.4194']

# Function to run the wifi wardriving command and extract relevant data
def wardrive():
    # Run the command to scan for wifi networks
    output = subprocess.check_output(['sudo', 'airmon-ng', 'start', 'wlan0'])
    
    # Extract ESSID, BSSID, and signal strength from the output
    essid = output.decode().split('ESSID: ')[1].split('\n')[0]
    bssid = output.decode().split('BSSID: ')[1].split('\n')[0]
    strength = output.decode().split('Signal level: ')[1].split('\n')[0]
    
    return essid, bssid, strength

# Function to save data to an Excel file
def save_to_excel(essid, bssid, strength, gps_coords):
    with open('wardriving_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([essid, bssid, gps_coords[0], gps_coords[1], strength])

# Main function
def main():
    while True:
        essid, bssid, strength = wardrive()
        save_to_excel(essid, bssid, strength, gps_coords)
        time.sleep(1)  # Update data every second

if __name__ == '__main__':
    main()
