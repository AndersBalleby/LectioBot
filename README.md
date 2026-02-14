# LectioBot

**LectioBot** var en Discord-bot, der automatisk hentede og viste Lectio-skemaer i en dedikeret kanal på serveren.
Projektet blev udviklet som et hobbyprojekt for at gøre det nemt at se dagens eller ugens skema direkte i Discord uden at logge ind på Lectio.
Der videreudvikles ikke på projektet

---

## Eksempel

Sådan kan et skema se ud (for en dag), når LectioBot sender det i Discord:

<img width="353" height="202" alt="Eksempel på skema" src="https://github.com/user-attachments/assets/a82e71f0-594f-4029-a90e-50582d617e98" />

Botten bruger Discord embeds til at vise dag, uge og fag på en overskuelig måde, hvilket gør det nemt for brugere at få overblik over dagens eller ugens skema direkte i Discord.

---

## Funktionalitet
- Henter og viser dagens eller ugens skema fra Lectio  
- Sender skemaer automatisk i en dedikeret Discord-kanal  
- Understøtter kommandoer, fx `!skema dag uge`    
- Logger aktivitet og fejl med et simpelt logging system

---

## Benyttede Teknologier
- **Python**  
- **Discord API / discord.py**  
- **dotenv** til miljøvariabler  
- Integration med Lectio via brugerlogin og custom handler  

---

## Disclaimer

Projektet blev udviklet som et sjovt "side-projekt" i 2023 i løbet af min HTX uddannelse.
Koden fungerer kun med de korrekte environment variables og et gyldigt Lectio login.

---
