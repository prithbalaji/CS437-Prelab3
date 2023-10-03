    time = date_time[1]
    
    if os.path.isfile('collect_rssi.csv'):
        with open('collect_rssi.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([cur_dict['rssi'], time])
    else:
        with open('collect_rssi.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['RSSI', 'Timestamp'])
            writer.writerow([cur_dict['rssi'], time])


df = pd.read_csv(file_name, parse_dates=["timestamp"])

plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["rssi"], label="RSSI")
plt.xlabel("Time")
plt.ylabel("RSSI (dBm)")
plt.title("RSSI vs. Time")
plt.legend()
plt.grid(True)
plt.show()
