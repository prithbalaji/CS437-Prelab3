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
