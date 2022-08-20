import memory_profiler
import random
import time

names = ['Kiran', 'King', 'John', 'Corey']
majors = ['Math', 'Comps', 'Science']

print(f'Memory before: {memory_profiler.memory_usage()}Mb')


def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        results.append(person)
    return results


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


# t1 = time.perf_counter()
# people_list(1000000)
# t2 = time.perf_counter()

t1 = time.process_time()
people_generator(1000000)
t2 = time.process_time()

print(f'Memory after: {memory_profiler.memory_usage()}Mb')
print(f'Time taken: {t2-t1} seconds')
