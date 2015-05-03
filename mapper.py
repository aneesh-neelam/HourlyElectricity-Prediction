#!/usr/bin/env python3

import sys

services = ['Bank', 'AutomobileIndustry', 'BpoIndustry', 'CementIndustry', 'Farmers1', 'Farmers2',
            'HealthCareResources', 'TextileIndustry', 'PoultryIndustry', 'Residential(individual)',
            'Residential(Apartments)', 'FoodIndustry', 'ChemicalIndustry', 'Handlooms', 'FertilizerIndustry', 'Hostel',
            'Hospital', 'Supermarket', 'Theatre', 'University']

service_count = {'Bank': 0, 'AutomobileIndustry': 0, 'BpoIndustry': 0, 'CementIndustry': 0, 'Farmers1': 0,
                 'Farmers2': 0, 'HealthCareResources': 0, 'TextileIndustry': 0, 'PoultryIndustry': 0,
                 'Residential(individual)': 0, 'Residential(Apartments)': 0, 'FoodIndustry': 0, 'ChemicalIndustry': 0,
                 'Handlooms': 0, 'FertilizerIndustry': 0, 'Hostel': 0, 'Hospital': 0, 'Supermarket': 0, 'Theatre': 0,
                 'University': 0}

for line in sys.stdin:
    line = line.strip()

    forkVA, forkW, service = line.split(',')

    service_count[service] += 1
    if service_count[service] >= 750:
        print(str(2) + ',' + service + ',' + forkW)
    else:
        print(str(1) + ',' + service + ',' + forkW)
