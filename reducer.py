#!/usr/bin/env python3

import json
import sys

total_count = 0

services = ['Bank', 'AutomobileIndustry', 'BpoIndustry', 'CementIndustry', 'Farmers1', 'Farmers2',
            'HealthCareResources', 'TextileIndustry', 'PoultryIndustry', 'Residential(individual)',
            'Residential(Apartments)', 'FoodIndustry', 'ChemicalIndustry', 'Handlooms', 'FertilizerIndustry', 'Hostel',
            'Hospital', 'Supermarket', 'Theatre', 'University']

service_count = {'Bank': 0, 'AutomobileIndustry': 0, 'BpoIndustry': 0, 'CementIndustry': 0, 'Farmers1': 0,
                 'Farmers2': 0, 'HealthCareResources': 0, 'TextileIndustry': 0, 'PoultryIndustry': 0,
                 'Residential(individual)': 0, 'Residential(Apartments)': 0, 'FoodIndustry': 0, 'ChemicalIndustry': 0,
                 'Handlooms': 0, 'FertilizerIndustry': 0, 'Hostel': 0, 'Hospital': 0, 'Supermarket': 0, 'Theatre': 0,
                 'University': 0}

service_probable = {'Bank': 0, 'AutomobileIndustry': 0, 'BpoIndustry': 0, 'CementIndustry': 0, 'Farmers1': 0,
                    'Farmers2': 0, 'HealthCareResources': 0, 'TextileIndustry': 0, 'PoultryIndustry': 0,
                    'Residential(individual)': 0, 'Residential(Apartments)': 0, 'FoodIndustry': 0,
                    'ChemicalIndustry': 0,
                    'Handlooms': 0, 'FertilizerIndustry': 0, 'Hostel': 0, 'Hospital': 0, 'Supermarket': 0,
                    'Theatre': 0,
                    'University': 0}

service_error = {'Bank': 0, 'AutomobileIndustry': 0, 'BpoIndustry': 0, 'CementIndustry': 0, 'Farmers1': 0,
                 'Farmers2': 0, 'HealthCareResources': 0, 'TextileIndustry': 0, 'PoultryIndustry': 0,
                 'Residential(individual)': 0, 'Residential(Apartments)': 0, 'FoodIndustry': 0,
                 'ChemicalIndustry': 0,
                 'Handlooms': 0, 'FertilizerIndustry': 0, 'Hostel': 0, 'Hospital': 0, 'Supermarket': 0,
                 'Theatre': 0,
                 'University': 0}

training_count = 0
testing_count = 0

for line in sys.stdin:
    line = line.strip()

    t, service, forkW = line.split(',')

    total_count += 1
    service_count[service] += 1

    if int(t) == 1:
        training_count += 1
        service_probable[service] = (service_probable[service] * service_count[service] + float(forkW)) / (service_count[service] + 1)

    elif int(t) == 2:
        testing_count += 1
        error = abs(float(service_probable[service]) - float(forkW))
        service_error[service] = (service_error[service] * service_count[service] + error) / service_count[service]

print(total_count, training_count, testing_count)
print(json.dumps(service_error))
