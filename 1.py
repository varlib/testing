aliens = []
for alien_0 in range(31):
    new_alien = {'number': alien_0, 'color': 'green', 'points': 5+alien_0, 'speed': 'slow'}
    aliens.append(new_alien)

for all in aliens[:5]:
    print(all)
print(len(aliens))
message = input("Введите значение: ")
message = int(message)
if message < 50:
    print("Маловато будет")
else:
    print("Вот теперь норма")
while message>=7:
    print(f"Ждём... {message}")
    message -= 1