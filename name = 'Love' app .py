from colorama import Fore, Style, init
import time

name = "Ali❣️"
nombre = input("💖 Hola, ¿quién eres? ")

if nombre.lower() != "ali":
    print("❌ Este regalo es solo para Ali ❤️")
    exit()

print("❤️ Bienvenida, mi Ali ❤️")
print(Fore.RED + '\n'.join(
    ''.join(
        name[(x-y) % len(name)]
        if ((x*0.05)**2 + (y*0.1)**2 - 1)**3
        - (x*0.05)**2 * (y*0.1)**3 <= 0 else ' '
        for x in range(-30, 30)
    )
    for y in range(15, -15, -1)
))

print(Style.RESET_ALL)

time.sleep(1)


print(Fore.RED + "❣️ Te amo mi ali ❣️")
print(Fore.RED + "❣️ infinitooo ❣️")

print(Style.RESET_ALL)

print("""
╔════════════════════════════╗
║        PARA MI ALI ❤️      ║
╠════════════════════════════╣
║ Te amo infinitooo          ║
║ usted es muy especial para ║
║  mi                        ║
╚════════════════════════════╝
""")

print("""
╔════════════════════════════╗
║ COSITAS QUE AMO DE MI ALI  ║
╠════════════════════════════╣
║  sus ojitos                ║
║  su sonrisa                ║
║  sus rizitos               ║
║  su forma de ser           ║
║  su corazoncito            ║
║  su carisma                ║
╚════════════════════════════╝
""")
 
input("\n💌 Presiona ENTER para ver mi último mensaje...")

print("""

╔══════════════════════════════╗
║          PARA MI ALI❣️       ║
╚══════════════════════════════╝

Aunque no pueda verte
todos los días,

cada día pienso en ti.

❣️ la amo infinito ❣️
""")
print("\n🌹 Fin del programa...")
time.sleep(1)
print(" " \
"Pero no de mi amor por usted ")
