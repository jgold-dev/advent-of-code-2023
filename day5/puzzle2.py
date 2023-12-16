
seeds = []
seed_soil = []
soil_fertilizer = []
fertilizer_water = []
water_light = []
light_temp = []
temp_humidity = []
humidity_loc = []

with open('puzzle_input.txt') as fh:

    mode = ""; # modes: s_s, s_f, f_w, w_l, l_t, t_h, h_l
    mode_info = []
    for line in fh:
        line = str.strip(line)

        if line.startswith("seeds"):
            seed_list = str.strip(line.split(':')[1]).split(' ')
            seed_list = list(map(int, seed_list))
            seed_index = 0
            while seed_index < len(seed_list):
                pair1 = seed_list[seed_index]
                pair2 = pair1 + seed_list[seed_index + 1] - 1  # inclusive range
                seeds.append([pair1, pair2])
                seed_index += 2
        elif line.startswith("seed-to-soil map:"):
            mode = "s_s"
        elif line.startswith("soil-to-fertilizer map:"):
            mode = "s_f"
        elif line.startswith("fertilizer-to-water map:"):
            mode = "f_w"
        elif line.startswith("water-to-light map:"):
            mode = "w_l"
        elif line.startswith("light-to-temperature map:"):
            mode = "l_t"
        elif line.startswith("temperature-to-humidity map:"):
            mode = "t_h"
        elif line.startswith("humidity-to-location map:"):
            mode = "h_l"
        elif len(line) != 0 and line[0].isdigit():
            mode_info.append(line.split(' '))

        if len(line) == 0:
            # process mode_info -- [dest, source, range]
            # create map for specific mode
            map = []
            for m in mode_info:
                src = int(m[1])
                dest = int(m[0])
                rng = int(m[2])
                map.append([src, src + (rng - 1), dest, dest + (rng - 1)])

            if mode == "s_s":
                seed_soil = map.copy()
            elif mode == "s_f":
                soil_fertilizer = map.copy()
            elif mode == "f_w":
                fertilizer_water = map.copy()
            elif mode == "w_l":
                water_light = map.copy()
            elif mode == "l_t":
                light_temp = map.copy()
            elif mode == "t_h":
                temp_humidity = map.copy()
            elif mode == "h_l":
                humidity_loc = map.copy()

            mode_info = []


    min_loc = 9999999999
    # Trace each seed to location
    print(seeds)
    for seed_pair in seeds:
        print("Find Seed Values in Range:", seed_pair)
        for seed in range(seed_pair[0], seed_pair[1]):
            soil = seed
            for m in seed_soil:
                if seed >= m[0] and seed <= m[1]:
                    soil = m[2] + (seed - m[0])
                    break
                
            fert = soil
            for m in soil_fertilizer:
                if soil >= m[0] and soil <= m[1]:
                    fert = m[2] + (soil - m[0])
                    break

            water = fert
            for m in fertilizer_water:
                if fert >= m[0] and fert <= m[1]:
                    water = m[2] + (fert - m[0])
                    break

            light = water
            for m in water_light:
                if water >= m[0] and water <= m[1]:
                    light = m[2] + (water - m[0])
                    break

            temp = light
            for m in light_temp:
                if light >= m[0] and light <= m[1]:
                    temp = m[2] + (light - m[0])
                    break

            humid = temp
            for m in temp_humidity:
                if temp >= m[0] and temp <= m[1]:
                    humid = m[2] + (temp - m[0])
                    break

            loc = humid
            for m in humidity_loc:
                if humid >= m[0] and humid <= m[1]:
                    loc = m[2] + (humid - m[0])
                    break

#            print("Seed: ", seed, ", Location: ", loc)
            if loc < min_loc:
                min_loc = loc

    print(min_loc)
