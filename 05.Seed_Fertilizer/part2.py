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
    for i in range(0,len(SEEDS),2):
        start, end = SEEDS[i], SEEDS[i] + SEEDS[i + 1] - 1
        seed = [(start, end)]
        soil = convert_source(0, MAPS, seed) #seed to soil
        fertilizer = convert_source(1, MAPS, soil) #soil to fertilizer
        water = convert_source(2, MAPS, fertilizer) #fertilizer to water
        light = convert_source(3, MAPS, water) #water to light
        temperature = convert_source(4, MAPS, light) #light to temperature
        humidity = convert_source(5, MAPS, temperature) #temperature to humidity
        location = convert_source(6, MAPS, humidity) #humidity to location
        min_location = min(min_location, min(loc[0] for loc in location))
    return min_location

        
#Reference for convert_source logic:
# https://github.com/nitekat1124/advent-of-code-2023/blob/main/solutions/day05.py

def convert_source(map_index, MAPS, remain):
    result = []
    while remain:
        start, end = remain.pop()
        for dest_range, source_range, range_length in MAPS[map_index]:
            if end < source_range or source_range + range_length <= start:
                continue
            elif source_range <= start <= end < source_range + range_length: #inside this range
                offset = start - source_range
                result.append((dest_range + offset, dest_range + offset + end - start))
                break
            elif start < source_range <= end < source_range + range_length:
                offset = end - source_range
                remain.append((start, source_range - 1))
                result.append((dest_range, dest_range + offset))
                break
            elif source_range <= start < source_range + range_length <= end:
                offset = start - source_range
                remain.append((source_range + range_length, end))
                result.append((dest_range + offset, dest_range + range_length + 1))
                break
            elif start < source_range <= source_range + range_length + end:
                remain.append((start, source_range - 1))
                remain.append((source_range + range_length, end))
                result.append((dest_range, dest_range + range_length - 1))
                break
        else:
            result.append((start, end))
    return result


with open("05.Fertilizer\input.txt") as file:
    SEEDS, MAPS = parse_almanac(file.read().split('\n'))
    print(find_min_location(SEEDS, MAPS))
    # puzzle = Solution()
    # print(puzzle.part2(file.read().split('\n')))