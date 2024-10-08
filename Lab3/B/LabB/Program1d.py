arrival_rate = float(input("Please input the arrival rate in packets/second: "))
service_rate = float(input("Please input the service rate in packets/second (must be greater than arrival rate): "))
print(f"The average length of the M/M/1 queue is {arrival_rate ** 2 / (service_rate - arrival_rate)} packets.")