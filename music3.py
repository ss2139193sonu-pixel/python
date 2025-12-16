import time
import sys
def print_lyrics():
    lyrics = [
        " tere dil pa haq mera hai💝",
        " tu sanam beshak mera hai🥰",
        " phir lakerein✋",
        " ho ya na ho😍",
        " tu mera hai🫴",
        " tu mera hai..."
    ]
    delays = [0.7,0.7,0.7,0.7,0.7,,0.7,0.7]

   print("girls like you:") 
time.sleep(1.2)

for i, line in enumerate(lyrics):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)
        print()
        time.sleep(delays[i])
