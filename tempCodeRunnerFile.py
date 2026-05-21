import time
start=time.perf_counter()
LETTER_FILE=open('Input/Letters/starting_letter.txt','r').read().strip()
NAMES_FILE=open('Names/invited_names.txt','r').readlines()
for n in [n.strip() for n in NAMES_FILE if n.strip()]:
    with open(f'Output/Ready_to_send/{n.lower()}.txt','w') as f:
        f.write(LETTER_FILE.replace('{name}',n).replace('{signature}','Octucode Team'))
        print(f"Successful Create Letter for {n}")
end=time.perf_counter()
print(f"1-Execution time: {end - start:.6f} seconds")
start=time.perf_counter()

with open('Input/Letters/starting_letter.txt') as f:
    letter_template = f.read().strip()

with open('Names/invited_names.txt') as f:
    names = [n.strip() for n in f if n.strip()]

for name in names:
    filename = name.lower()
    content = letter_template.replace('{name}', name)\
                              .replace('{signature}', 'Octucode Team')

    with open(f'Output/Ready_to_send1/{filename}.txt', 'w') as file:
        file.write(content)

    print(f"Successful Create Letter for {name}")
end=time.perf_counter()
print(f"2-Execution time: {end - start:.6f} seconds")
