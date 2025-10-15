# 📚 LectioBot

**LectioBot** var en Discord-bot, der automatisk hentede og viste Lectio-skemaer i en dedikeret kanal på serveren.
Projektet blev udviklet som et hobbyprojekt for at gøre det nemt at se dagens eller ugens skema direkte i Discord uden at logge ind på Lectio.
Bemærk: botten er ikke længere aktivt i brug.

---

## 📌 Eksempel

Sådan kan et skema se ud (for en dag), når LectioBot sender det i Discord:

<img width="353" height="202" alt="Eksempel på skema" src="https://github.com/user-attachments/assets/a82e71f0-594f-4029-a90e-50582d617e98" />

Botten bruger Discord embeds til at vise dag, uge og fag på en overskuelig måde, hvilket gør det nemt for brugere at få overblik over dagens eller ugens skema direkte i Discord.

---

## 🧠 Funktioner
- Henter og viser dagens eller ugens skema fra Lectio  
- Sender skemaer automatisk i en dedikeret Discord-kanal  
- Understøtter kommandoer, fx `!skema dag uge`  
- Bruger embeds til at vise skemaet pænt i Discord  
- Logger aktivitet og fejl med et simpelt logsystem  

---

## 🧰 Brugte teknologier
- **Python**  
- **Discord API / discord.py**  
- **dotenv** til miljøvariabler  
- Integration med Lectio via brugerlogin og custom handler  

---

## ⚠️ Disclaimer

Dette projekt er udviklet som et sjovt "side-projekt" i 2023 i løbet af min HTX uddannelse.
Koden fungerer kun med de korrekte miljøvariabler og Lectio-login, og skal tilpasses for at kunne bruges på andre servere eller med andre konti.

---
