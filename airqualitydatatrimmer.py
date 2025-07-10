from citylatitudelongitudelookup import lookupcitylatitudeandlongitude

infile = open("csv/waqi-covid19-airqualitydata-2025.csv", "r")
outfile = open("csv/Air_Quality_Global_Cities_2015-2025.csv", "w")

print(infile)
print(outfile)
print()
print("Date,City,Latitude,Longitude,pm25,Metric".rstrip(), file=outfile)

for line in infile:
    try:
        date = line.split(",")[0]
        pollutant = line.split(",")[3]
        if date != "Date" and pollutant == "pm25":
            city = line.split(",")[2]
            pollutantcount = line.split(",")[4]
            latlon = lookupcitylatitudeandlongitude(city)
            latitude = latlon[0]
            longitude = latlon[1]
            newline=f"{date},{city},{latitude},{longitude},{pollutantcount},{pollutant}"
            print(newline)
            print(newline.rstrip(), file=outfile)
    except:
        print("Error!")
        print("Problem with the following line")
        print(line)

infile.close()
outfile.close()
