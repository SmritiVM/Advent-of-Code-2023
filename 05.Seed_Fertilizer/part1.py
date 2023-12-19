import re
def parse_almanac(almanac):
    seed_pos = re.search("seeds: ",almanac[0])
    SEEDS = list(map(int, almanac[0][seed_pos.end():].split()))

    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    MAPS = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light,
            light_to_temperature, temperature_to_humidity, humidity_to_location]
    
    map_index = -1
    for line in almanac[1:]:
        if re.match("^\d", line):
            MAPS[map_index].append(list(map(int, line.split())))
        elif re.match("^\w", line):
            map_index += 1
    return SEEDS, MAPS

def find_min_location(SEEDS, MAPS):
    min_location = float('INF')
    for seed in SEEDS:
        soil = convert_source(0, MAPS, seed) #seed to soil
        fertilizer = convert_source(1, MAPS, soil) #soil to fertilizer
        water = convert_source(2, MAPS, fertilizer) #fertilizer to water
        light = convert_source(3, MAPS, water) #water to light
        temperature = convert_source(4, MAPS, light) #light to temperature
        humidity = convert_source(5, MAPS, temperature) #temperature to humidity
        location = convert_source(6, MAPS, humidity) #humidity to location
        min_location = min(min_location, location)
    return min_location

        

def convert_source(map_index, MAPS, source):
    dest = source
    for dest_range, source_range, range_length in MAPS[map_index]:
        try:
            pos = range(source_range, source_range + range_length + 1).index(source)
            dest = dest_range + pos
            break
        except: continue
    return dest
  

with open("05.Fertilizer\input.txt") as file:
    SEEDS, MAPS = parse_almanac(file.read().split('\n'))
    print(find_min_location(SEEDS, MAPS))