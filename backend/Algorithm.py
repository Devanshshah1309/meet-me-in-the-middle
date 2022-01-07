def dijkstra(start):
    start_index = mrt[start]
    temp = [inf for _ in '.' * len(mrt)]
    temp[start_index] = 0  # distance from start to itself is 0
    queue = [start]
    while len(queue) > 0:
        cur = queue.pop(0)
        cur_index = mrt[cur]
        neighbours = graph[cur]
        for n in neighbours:
            n_index = mrt[n]
            if temp[cur_index] + 1 < temp[n_index]:
                temp[n_index] = temp[cur_index] + 1
                queue.append(n)
    return temp


inf = 10e8

# MRT Lines with stations and indices to make it easier

mrt = {
    'Jurong East': 0,
    'Bukit Batok': 1,
    'Bukit Gombak': 2,
    'Choa Chu Kang': 3,
    'Yew Tee': 4,
    'Kranji': 5,
    'Marsiling': 6,
    'Woodlands': 7,
    'Admiralty': 8,
    'Sembawang': 9,
    'Canberra': 10,
    'Yishun': 11,
    'Khatib': 12,
    'Yio Chu Kang': 13,
    'Ang Mo Kio': 14,
    'Bishan': 15,
    'Braddell': 16,
    'Toa Payoh': 17,
    'Novena': 18,
    'Newton': 19,
    'Orchard': 20,
    'Somerset': 21,
    'Dhoby Ghaut': 22,
    'City Hall': 23,
    'Raffles Place': 24,
    'Marina Bay': 25,
    'Marina South Pier': 26,
    'Pasir Ris': 27,
    'Tampines': 28,
    'Simei': 29,
    'Tanah Merah': 30,
    'Bedok': 31,
    'Kembangan': 32,
    'Eunos': 33,
    'Paya Lebar': 34,
    'Aljunied': 35,
    'Kallang': 36,
    'Lavender': 37,
    'Bugis': 38,
    'Tanjong Pagar': 39,
    'Outram Park': 40,
    'Tiong Bahru': 41,
    'Redhill': 42,
    'Queenstown': 43,
    'Commonwealth': 44,
    'Buona Vista': 45,
    'Dover': 46,
    'Clementi': 47,
    'Chinese Garden': 48,
    'Lakeside': 49,
    'Boon Lay': 50,
    'Pioneer': 51,
    'Joo Koon': 52,
    'Gul Circle': 53,
    'Tuas Crescent': 54,
    'Tuas West Road': 55,
    'Tuas Link': 56,
    'Expo': 57,
    'Changi Airport': 58,
    'HarbourFront': 59,
    'Outram Park': 60,
    'Chinatown': 61,
    'Clarke Quay': 62,
    'Little India': 63,
    'Farrer Park': 64,
    'Boon Keng': 65,
    'Potong Pasir': 66,
    'Woodleigh': 67,
    'Serangoon': 68,
    'Kovan': 69,
    'Hougang': 70,
    'Buangkok': 71,
    'Sengkang': 72,
    'Punggol': 73,
    'Bras Basah': 74,
    'Esplanade': 75,
    'Promenade': 76,
    'Nicoll Highway': 77,
    'Stadium': 78,
    'Mountbatten': 79,
    'Dakota': 80,
    'MacPherson': 81,
    'Tai Seng': 82,
    'Bartley': 83,
    'Lorong Chuan': 84,
    'Marymount': 85,
    'Caldecott': 86,
    'Botanic Gardens': 87,
    'Farrer Road': 88,
    'Holland Village': 89,
    'one-north': 90,
    'Kent Ridge': 91,
    'Haw Par Villa': 92,
    'Pasir Panjang': 93,
    'Labrador Park': 94,
    'Telok Blangah': 95,
    'Bayfront': 96,
    'Bukit Panjang': 97,
    'Cashew': 98,
    'Hillview': 99,
    'Beauty World': 100,
    'King Albert Park': 101,
    'Sixth Avenue': 102,
    'Tan Kah Kee': 103,
    'Stevens': 104,
    'Rochor': 105,
    'Downtown': 106,
    'Telok Ayer': 107,
    'Fort Canning': 108,
    'Bencoolen': 109,
    'Jalan Besar': 110,
    'Bendemeer': 111,
    'Geylang Bahru': 112,
    'Mattar': 113,
    'Ubi': 114,
    'Kaki Bukit': 115,
    'Bedok North': 116,
    'Bedok Reservoir': 117,
    'Tampines West': 118,
    'Tampines East': 119,
    'Upper Changi': 120,
    'Woodlands North': 121,
    'Woodlands South': 122
}

mrt_names = list(mrt.keys())
mrt_indices = list(mrt.values())

green_graph = {
    'Tuas Link': ['Tuas West Road'],
    'Tuas West Road': ['Tuas Link', 'Tuas Crescent'],
    'Tuas Crescent': ['Tuas West Road', 'Gul Circle'],
    'Gul Circle': ['Tuas Crescent', 'Joo Koon'],
    'Joo Koon': ['Gul Circle', 'Pioneer'],
    'Pioneer': ['Joo Koon', 'Boon Lay'],
    'Boon Lay': ['Pioneer', 'Lakeside'],
    'Lakeside': ['Boon Lay', 'Chinese Garden'],
    'Chinese Garden': ['Lakeside', 'Jurong East'],
    'Jurong East': ['Chinese Garden', 'Clementi', 'Bukit Batok'],
    'Clementi': ['Jurong East', 'Dover'],
    'Dover': ['Clementi', 'Buona Vista'],
    'Buona Vista': ['Dover', 'Commonwealth', 'Holland Village'],
    'Commonwealth': ['Buona Vista', 'Queenstown'],
    'Queenstown': ['Commonwealth', 'Redhill'],
    'Redhill': ['Queenstown', 'Tiong Bahru'],
    'Tiong Bahru': ['Redhill', 'Outram Park'],
    'Outram Park': ['Tiong Bahru', 'Tanjong Pagar', 'HabourFront', 'Chinatown'],
    'Tanjong Pagar': ['Outram Park', 'Raffles Place'],
    'Raffles Place': ['Tanjong Pagar', 'City Hall', 'Marina Bay'],
    'City Hall': ['Raffles Place', 'Dhoby Ghaut', 'Bugis'],
    'Bugis': ['City Hall', 'Lavender', 'Rocher', 'Promenade'],
    'Lavender': ['Kallang', 'Bugis'],
    'Kallang': ['Lavender', 'Aljunied'],
    'Aljunied': ['Kallang', 'Paya Lebar'],
    'Paya Lebar': ['Aljunied', 'Eunos', 'MacPherson', 'Dakota'],
    'Eunos': ['Paya Lebar', 'Kembangan'],
    'Kembangan': ['Eunos', 'Bedok'],
    'Bedok': ['Kembangan', 'Tanah Merah'],
    'Tanah Merah': ['Bedok', 'Simei', 'Expo'],
    'Simei': ['Tanah Merah', 'Tampines'],
    'Tampines': ['Simei', 'Pasir Ris', 'Tampines Wesr', 'Tampines East'],
    'Pasir Ris': ['Tampines'],
    'Expo': ['Tanah Merah', 'Changi Airport', 'Upper Changi'],
    'Changi Airport': ['Expo']

}

red_graph = {
    'Jurong East': ['Chinese Garden', 'Clementi', 'Bukit Batok'],
    'Bukit Batok': ['Jurong East', 'Bukit Gombak'],
    'Bukit Gombak': ['Bukit Batok', 'Choa Chu Kang'],
    'Choa Chu Kang': ['Bukit Gombak', 'Yew Tee'],
    'Yew Tee': ['Choa Chu Kang', 'Kranji'],
    'Kranji': ['Yew Tee', 'Marsiling'],
    'Marsiling': ['Kranji', 'Woodlands'],
    'Woodlands': ['Marsiling', 'Admiralty'],
    'Admiralty': ['Woodlands', 'Sembawang'],
    'Sembawang': ['Admiralty', 'Canberra'],
    'Canberra': ['Sembawang', 'Yishun'],
    'Yishun': ['Canberra', 'Khatib'],
    'Khatib': ['Yishun', 'Yio Chu Kang'],
    'Yio Chu Kang': ['Khatib', 'Ang Mo Kio'],
    'Ang Mo Kio': ['Yio Chu Kang', 'Bishan'],
    'Bishan': ['Ang Mo Kio', 'Braddell', 'Loring Chuan', 'Marymount'],
    'Braddell': ['Bishan', 'Toa Payoh'],
    'Toa Payoh': ['Braddell', 'Novena'],
    'Novena': ['Toa Payoh', 'Newton'],
    'Newton': ['Novena', 'Orchard', 'Stevens', 'Little India'],
    'Orchard': ['Newton', 'Somerset'],
    'Somerset': ['Orchard', 'Dhoby Ghaut'],
    'Dhoby Ghaut': ['Somerset', 'City Hall', 'Clarke Quay', 'Little India', 'Bras Basah', ],
    'City Hall': ['Dhoby Ghaut', 'Raffles Place', 'Bugis'],
    'Raffles Place': ['City Hall', 'Marina Bay', 'Tanjong Pagar'],
    'Marina Bay': ['Raffles Place', 'Marina South Pier', 'Bayfront'],
    'Marina South Pier': ['Marina Bay'],

}
blue_graph = {
    'Bukit Panjang': ['Cashew'],
    'Cashew': ['Bukit Panjang', 'Hillview'],
    'Hillview': ['Cashew', 'Beauty World'],
    'Beauty World': ['Hillview', 'King Albert Park'],
    'King Albert Park': ['Beauty World', 'Sixth Avenue'],
    'Sixth Avenue': ['King Albert Park', 'Tan Kah Kee'],
    'Tan Kah Kee': ['Sixth Avenue', 'Botanic Gardens'],
    'Botanic Gardens': ['Tan Kah Kee', 'Stevens', 'Farrer Road', 'Caldecott'],
    'Stevens': ['Botanic Gardens', 'Newton'],
    'Newton': ['Stevens', 'Little India', 'Orchard', 'Novena'],
    'Little India': ['Newton', 'Rochor', 'Farrer Park', 'Dhoby Ghaut'],
    'Rochor': ['Little India', 'Bugis'],
    'Bugis': ['Rochor', 'Promenade', 'Lavender', 'City Hall'],
    'Promenade': ['Bugis', 'Bayfront', 'Esplanade', 'Nicoll Highway'],
    'Bayfront': ['Promenade', 'Downtown', 'Marina Bay'],
    'Downtown': ['Bayfront', 'Telok Ayer'],
    'Telok Ayer': ['Downtown', 'Chinatown'],
    'Chinatown': ['Telok Ayer', 'Fort Canning', 'Clarke Quay', 'Outram Park'],
    'Fort Canning': ['Chinatown', 'Bencoolen'],
    'Bencoolen': ['Fort Canning', 'Jalan Besar'],
    'Jalan Besar': ['Bencoolen', 'Bendemeer'],
    'Bendemeer': ['Jalan Besar', 'Geylang Bahru'],
    'Geylang Bahru': ['Bendemeer', 'Mattar'],
    'Mattar': ['Geylang Bahru', 'MacPherson'],
    'MacPherson': ['Mattar', 'Ubi', 'Tai Seng', 'Paya Lebar'],
    'Ubi': ['MacPherson', 'Kaki Bukit'],
    'Kaki Bukit': ['Ubi', 'Bedok North'],
    'Bedok North': ['Kaki Bukit', 'Bedok Reservoir'],
    'Bedok Reservoir': ['Bedok North', 'Tampines West'],
    'Tampines West': ['Bedok Reservoir', 'Tampines'],
    'Tampines': ['Tampines West', 'Tampines East', 'Pasir Ris', 'Simei'],
    'Tampines East': ['Upper Changi', 'Tampines'],
    'Upper Changi': ['Tampines East', 'Expo'],
    'Expo': ['Upper Changi', 'Changi Airport', 'Tanah Merah'],

}
yellow_graph = {
    'HarbourFront': ['Telok Blangah', 'Outram Park'],
    'Telok Blangah': ['HarbourFront', 'Labrador Park'],
    'Labrador Park': ['Pasir Panjang', 'Telok Blangah'],
    'Pasir Panjang': ['Labrador Park', 'Haw Par Villa'],
    'Haw Par Villa': ['Pasir Panjang', 'Kent Ridge'],
    'Kent Ridge': ['Haw Par Villa', 'one-north'],
    'one-north': ['Kent Ridge', 'Buona Vista'],
    'Buona Vista': ['one-north', 'Holland Village', 'Dover', 'Commonwealth'],
    'Holland Village': ['Buona Vista', 'Farrer Road'],
    'Farrer Road': ['Holland Village', 'Botanic Gardens'],
    'Botanic Gardens': ['Tan Kah Kee', 'Stevens', 'Farrer Road', 'Caldecott'],
    'Caldecott': ['Botanic Gardens', 'Marymount'],
    'Marymount': ['Caldecott', 'Bishan'],
    'Bishan': ['Marymount', 'Lorong Chuan'],
    'Lorong Chuan': ['Bishan', 'Serangoon'],
    'Serangoon': ['Lorong Chuan', 'Bartley', 'Kovan', 'Woodleigh'],
    'Bartley': ['Serangoon', 'Tai Seng'],
    'Tai Seng': ['Bartley', 'MacPherson'],
    'MacPherson': ['Mattar', 'Ubi', 'Tai Seng', 'Paya Lebar'],
    'Paya Lebar': ['MacPherson', 'Dakota', 'Aljunied', 'Eunos'],
    'Dakota': ['Paya Lebar', 'Mountbatten'],
    'Mountbatten': ['Dakota', 'Stadium'],
    'Stadium': ['Mountbatten', 'Nicoll Highway'],
    'Nicoll Highway': ['Stadium', 'Promenade'],
    'Promenade': ['Bugis', 'Bayfront', 'Esplanade', 'Nicoll Highway'],
    'Esplanade': ['Promenade', 'Bras Basah'],
    'Bras Basah': ['Esplanade', 'Dhoby Ghaut'],
    'Dhoby Ghaut': ['Bras Basah', 'Little India', 'Clarke Quay', 'Somerset', 'City Hall'],
    'Bayfront': ['Promenade', 'Marina Bay'],
    'Marina Bay': ['Bayfront', 'Marina South Pier', 'Raffles Place'],

}
purple_graph = {
    'Punggol': ['Sengkang'],
    'Sengkang': ['Punggol', 'Buangkok'],
    'Buangkok': ['Sengkang', 'Hougang'],
    'Hougang': ['Buangkok', 'Kovan'],
    'Kovan': ['Hougang', 'Serangoon'],
    'Serangoon': ['Lorong Chuan', 'Bartley', 'Kovan', 'Woodleigh'],
    'Woodleigh': ['Serangoon', 'Potong Pasir'],
    'Potong Pasir': ['Woodleigh', 'Boon Keng'],
    'Boon Keng': ['Potong Pasir', 'Farrer Park'],
    'Farrer Park': ['Boon Keng', 'Little India'],
    'Little India': ['Newton', 'Rochor', 'Farrer Park', 'Dhoby Ghaut'],
    'Dhoby Ghaut': ['Bras Basah', 'Little India', 'Clarke Quay', 'Somerset', 'City Hall'],
    'Clarke Quay': ['Dhoby Ghaut', 'Chinatown'],
    'Chinatown': ['Telok Ayer', 'Fort Canning', 'Clarke Quay', 'Outram Park'],
    'Outram Park': ['Chinatown', 'HarbourFront', 'Tiong Bahru', 'Tanjong Pagar'],
    'HarbourFront': ['Telok Blangah', 'Outram Park']
}

graph = {
    'Tuas Link': ['Tuas West Road'],
    'Tuas West Road': ['Tuas Link', 'Tuas Crescent'],
    'Tuas Crescent': ['Tuas West Road', 'Gul Circle'],
    'Gul Circle': ['Tuas Crescent', 'Joo Koon'],
    'Joo Koon': ['Gul Circle', 'Pioneer'],
    'Pioneer': ['Joo Koon', 'Boon Lay'],
    'Boon Lay': ['Pioneer', 'Lakeside'],
    'Lakeside': ['Boon Lay', 'Chinese Garden'],
    'Chinese Garden': ['Lakeside', 'Jurong East'],
    'Jurong East': ['Chinese Garden', 'Clementi', 'Bukit Batok'],
    'Clementi': ['Jurong East', 'Dover'],
    'Dover': ['Clementi', 'Buona Vista'],
    'Buona Vista': ['one-north', 'Holland Village', 'Dover', 'Commonwealth'],
    'Commonwealth': ['Buona Vista', 'Queenstown'],
    'Queenstown': ['Commonwealth', 'Redhill'],
    'Redhill': ['Queenstown', 'Tiong Bahru'],
    'Tiong Bahru': ['Redhill', 'Outram Park'],
    'Outram Park': ['Chinatown', 'HarbourFront', 'Tiong Bahru', 'Tanjong Pagar'],
    'Tanjong Pagar': ['Outram Park', 'Raffles Place'],
    'Raffles Place': ['City Hall', 'Marina Bay', 'Tanjong Pagar'],
    'City Hall': ['Dhoby Ghaut', 'Raffles Place', 'Bugis'],
    'Bugis': ['Rochor', 'Promenade', 'Lavender', 'City Hall'],
    'Lavender': ['Kallang', 'Bugis'],
    'Kallang': ['Lavender', 'Aljunied'],
    'Aljunied': ['Kallang', 'Paya Lebar'],
    'Paya Lebar': ['MacPherson', 'Dakota', 'Aljunied', 'Eunos'],
    'Eunos': ['Paya Lebar', 'Kembangan'],
    'Kembangan': ['Eunos', 'Bedok'],
    'Bedok': ['Kembangan', 'Tanah Merah'],
    'Tanah Merah': ['Bedok', 'Simei', 'Expo'],
    'Simei': ['Tanah Merah', 'Tampines'],
    'Tampines': ['Tampines West', 'Tampines East', 'Pasir Ris', 'Simei'],
    'Pasir Ris': ['Tampines'],
    'Expo': ['Upper Changi', 'Changi Airport', 'Tanah Merah'],
    'Changi Airport': ['Expo'],
    'Bukit Batok': ['Jurong East', 'Bukit Gombak'],
    'Bukit Gombak': ['Bukit Batok', 'Choa Chu Kang'],
    'Choa Chu Kang': ['Bukit Gombak', 'Yew Tee'],
    'Yew Tee': ['Choa Chu Kang', 'Kranji'],
    'Kranji': ['Yew Tee', 'Marsiling'],
    'Marsiling': ['Kranji', 'Woodlands'],
    'Woodlands': ['Marsiling', 'Admiralty'],
    'Admiralty': ['Woodlands', 'Sembawang'],
    'Sembawang': ['Admiralty', 'Canberra'],
    'Canberra': ['Sembawang', 'Yishun'],
    'Yishun': ['Canberra', 'Khatib'],
    'Khatib': ['Yishun', 'Yio Chu Kang'],
    'Yio Chu Kang': ['Khatib', 'Ang Mo Kio'],
    'Ang Mo Kio': ['Yio Chu Kang', 'Bishan'],
    'Bishan': ['Marymount', 'Lorong Chuan'],
    'Braddell': ['Bishan', 'Toa Payoh'],
    'Toa Payoh': ['Braddell', 'Novena'],
    'Novena': ['Toa Payoh', 'Newton'],
    'Newton': ['Stevens', 'Little India', 'Orchard', 'Novena'],
    'Orchard': ['Newton', 'Somerset'],
    'Somerset': ['Orchard', 'Dhoby Ghaut'],
    'Dhoby Ghaut': ['Bras Basah', 'Little India', 'Clarke Quay', 'Somerset', 'City Hall'],
    'Marina Bay': ['Bayfront', 'Marina South Pier', 'Raffles Place'],
    'Marina South Pier': ['Marina Bay'],
    'Bukit Panjang': ['Cashew'],
    'Cashew': ['Bukit Panjang', 'Hillview'],
    'Hillview': ['Cashew', 'Beauty World'],
    'Beauty World': ['Hillview', 'King Albert Park'],
    'King Albert Park': ['Beauty World', 'Sixth Avenue'],
    'Sixth Avenue': ['King Albert Park', 'Tan Kah Kee'],
    'Tan Kah Kee': ['Sixth Avenue', 'Botanic Gardens'],
    'Botanic Gardens': ['Tan Kah Kee', 'Stevens', 'Farrer Road', 'Caldecott'],
    'Stevens': ['Botanic Gardens', 'Newton'],
    'Little India': ['Newton', 'Rochor', 'Farrer Park', 'Dhoby Ghaut'],
    'Rochor': ['Little India', 'Bugis'],
    'Promenade': ['Bugis', 'Bayfront', 'Esplanade', 'Nicoll Highway'],
    'Bayfront': ['Promenade', 'Marina Bay'],
    'Downtown': ['Bayfront', 'Telok Ayer'],
    'Telok Ayer': ['Downtown', 'Chinatown'],
    'Chinatown': ['Telok Ayer', 'Fort Canning', 'Clarke Quay', 'Outram Park'],
    'Fort Canning': ['Chinatown', 'Bencoolen'],
    'Bencoolen': ['Fort Canning', 'Jalan Besar'],
    'Jalan Besar': ['Bencoolen', 'Bendemeer'],
    'Bendemeer': ['Jalan Besar', 'Geylang Bahru'],
    'Geylang Bahru': ['Bendemeer', 'Mattar'],
    'Mattar': ['Geylang Bahru', 'MacPherson'],
    'MacPherson': ['Mattar', 'Ubi', 'Tai Seng', 'Paya Lebar'],
    'Ubi': ['MacPherson', 'Kaki Bukit'],
    'Kaki Bukit': ['Ubi', 'Bedok North'],
    'Bedok North': ['Kaki Bukit', 'Bedok Reservoir'],
    'Bedok Reservoir': ['Bedok North', 'Tampines West'],
    'Tampines West': ['Bedok Reservoir', 'Tampines'],
    'Tampines East': ['Upper Changi', 'Tampines'],
    'Upper Changi': ['Tampines East', 'Expo'],
    'HarbourFront': ['Telok Blangah', 'Outram Park'],
    'Telok Blangah': ['HarbourFront', 'Labrador Park'],
    'Labrador Park': ['Pasir Panjang', 'Telok Blangah'],
    'Pasir Panjang': ['Labrador Park', 'Haw Par Villa'],
    'Haw Par Villa': ['Pasir Panjang', 'Kent Ridge'],
    'Kent Ridge': ['Haw Par Villa', 'one-north'],
    'one-north': ['Kent Ridge', 'Buona Vista'],
    'Holland Village': ['Buona Vista', 'Farrer Road'],
    'Farrer Road': ['Holland Village', 'Botanic Gardens'],
    'Caldecott': ['Botanic Gardens', 'Marymount'],
    'Marymount': ['Caldecott', 'Bishan'],
    'Lorong Chuan': ['Bishan', 'Serangoon'],
    'Serangoon': ['Lorong Chuan', 'Bartley', 'Kovan', 'Woodleigh'],
    'Bartley': ['Serangoon', 'Tai Seng'],
    'Tai Seng': ['Bartley', 'MacPherson'],
    'Dakota': ['Paya Lebar', 'Mountbatten'],
    'Mountbatten': ['Dakota', 'Stadium'],
    'Stadium': ['Mountbatten', 'Nicoll Highway'],
    'Nicoll Highway': ['Stadium', 'Promenade'],
    'Esplanade': ['Promenade', 'Bras Basah'],
    'Bras Basah': ['Esplanade', 'Dhoby Ghaut'],
    'Punggol': ['Sengkang'],
    'Sengkang': ['Punggol', 'Buangkok'],
    'Buangkok': ['Sengkang', 'Hougang'],
    'Hougang': ['Buangkok', 'Kovan'],
    'Kovan': ['Hougang', 'Serangoon'],
    'Woodleigh': ['Serangoon', 'Potong Pasir'],
    'Potong Pasir': ['Woodleigh', 'Boon Keng'],
    'Boon Keng': ['Potong Pasir', 'Farrer Park'],
    'Farrer Park': ['Boon Keng', 'Little India'],
    'Clarke Quay': ['Dhoby Ghaut', 'Chinatown']
}


# graph.update(green_graph)
# graph.update(red_graph)
# graph.update(blue_graph)
# graph.update(yellow_graph)
# graph.update(purple_graph)


# the difference in travel time should be less than 2*bias minutes for each person
# (can be changed later if its too hard to find such a place)
# logic: (2 important criteria!!)
# each person should travel nearly the same amount and,
# the total distance should be as low as possible while ensuring equality


def main_logic(starting_locations):
    number = len(starting_locations)
    bias = 1
    total = [0 for _ in '.' * len(mrt)]
    trial = []
    for location in starting_locations:
        temp = dijkstra(location)
        trial.append(temp)
        total = [sum(x) for x in zip(temp, total)]

    # keep 3 optimal locations? sorted by total distance
    # optimals is a list of optimal locations
    # first value stores the total distance, second value stores the index of the mrt
    optimals = [[inf, False], [inf, False], [inf, False]]
    distances = [[] for x in range(len(mrt))]

    for l in trial:
        for i in range(len(mrt)):
            distances[i].append(l[i])
    # distances[i] gives a list of distances from all input stations to ith station

    # finding optimal location
    while not (optimals[0][1] and optimals[1][1] and optimals[2][1]):
        for i in range(len(mrt)):
            avg = total[i] / number  # expected ideal scenario in which each person travels same amount
            distance = distances[i]
            flag = True
            for j in range(number):
                if abs(distance[j] - avg) > bias:  # ensures equality in travelling
                    flag = False
            if flag:
                if total[i] < optimals[2][0]:
                    optimals[2] = [total[i], i]
                    optimals.sort()
        bias += 1  # if you can't find 3 places that everyone travels nearly equally, increase the tolerance amount
    names_of_optimals = []
    names_of_optimals.append(mrt_names[optimals[0][1]])
    names_of_optimals.append(mrt_names[optimals[1][1]])
    names_of_optimals.append(mrt_names[optimals[2][1]])
    return names_of_optimals

# test
# print(MainLogic(['Bukit Panjang', 'Expo']))
# print(MainLogic(['Boon Lay', 'Punggol']))

# tagging system

# suggested tags
# 1. cycling
# 2. library
# 3. shopping
# 4. no preference

# at position i, assign the cycling score for mrt with index i
# tip: set everything to 0 first by using
# cycling_scores = [0 for _ in '.'*len(mrt)]
# and then assign scores for the best 15-20 of the mrts like this:
# cycling_scores[0] = 1 #if the mrt with index 0 should have a score
# im guessing most of the mrt's will have a score of 0 so you'll only have to edit a few of them
# once you edit it. just print it out and copy paste the list instead of the assignment statements and send it :)

# so you should have something like this in the end:
# cycling_scores = [1, 0, 0, 0, 10, 4, 5,0,0,0,1,3,.......]
