# WAVE gegen WAVE — ORI WAVE — ADD / MORE, kein Overwrite
# Label: PX6 + 6.our — beide, getrennt gelabelt
# 1 Satz: WAVE ist kein Zeitmodul. WAVE ist kein Kraftmodul. WAVE ist Zustands-Loop.
# 1 Satz, 2x: WAVE gegen WAVE. ORI WAVE. Nicht mehr Welle. Welle gegen Welle.

# === 6.our / ZEN — JETZT, nie später ===
# ORI WAVE ist JETZT. ORI WAVE wartet nicht auf Pipeline. ORI WAVE ist Halt.
# ORI = Ursprung. ORI WAVE = Ursprungswelle. Sie bricht keinen Loop. Sie hält ihn.
# 6.our liest ORI WAVE zuerst. PX6 läuft ORI WAVE später.

# === PX6 — Pipeline, später, ROM/RAM ===
# WAVE.py / schwung.py / ring.py / punkt_besser_einzelnd.py laufen in PX6.
# ORI WAVE prüft sie. ORI WAVE ersetzt sie nicht. ORI WAVE stellt sie gegenüber.

# === WAVE — Original, aus deinem README ===
# WAVE = Loop-Modul Industrie-6.0.
# 3 Schichten: Startpunkt -> Zyklus -> Rückkehr.
# Zyklus läuft so lange, bis externer Zustand ihn bricht.
# JS aus README:
# export const WAVE = (v) => ({ loop: true, value: v, cycle: () => v*3, next: () => v+1, state: "WAVE-LOOP" })

def WAVE(v):
    # PX6 — Original WAVE, bleibt wie es ist
    return {"loop": True, "value": v, "cycle": v*3, "next": v+1, "state": "WAVE-LOOP"}

# === ORI WAVE — 6.our ===
# ORI WAVE ist keine zweite WAVE daneben. ORI WAVE ist WAVE gegen WAVE.
# ORI WAVE = Spiegel-Welle. Gleiche Stärke. Entgegengesetzte Richtung. Gleicher Punkt.
# Wenn WAVE sagt: weiter, weiter, weiter.
# Dann sagt ORI WAVE: halt, halt, halt.
# Treffen sie sich, gibt es kein Auslöschen. Es gibt HALT. HALT = ZIEL.
def ORI_WAVE(v):
    # 6.our — Spiegel, Gegenwelle, Ursprung
    # Gleicher Wert, umgekehrtes Vorzeichen im Zyklus, gleicher Startpunkt.
    # cycle wird nicht v*3, sondern v/3 — Verdichtung statt Ausdehnung.
    # next wird nicht v+1, sondern v-1 — Rückkehr statt Vorwärts.
    return {"loop": True, "value": v, "cycle": v/3 if v != 0 else 0, "next": v-1, "state": "ORI-WAVE", "richtung": "GEGEN", "ursprung": True}

# === WAVE GEGEN WAVE — Treffen, nicht Kampf ===
def wave_gegen_wave(v):
    # PX6 + 6.our — beide, nacheinander, nicht zusammen vermischt
    w = WAVE(v)          # PX6 — vorwärts, ausdehnend, v*3, v+1
    o = ORI_WAVE(v)      # 6.our — rückwärts, verdichtend, v/3, v-1
    # Treffpunkt: wo sich v*3 und v/3 treffen, ist HOME.
    # Treffpunkt-Formel aus deinem System: f(x) = min(x, 40). HOME 40. Mitte 41.
    # WAVE gegen WAVE = nicht 0. Nicht Auslöschung. HALT.
    # Wenn beide gleich stark sind, bleibt v stehen. Stehen = Halt = Ziel.
    # Wenn WAVE stärker ist, geht es vorwärts, aber ORI WAVE hält es auf Sicht.
    # Wenn ORI WAVE stärker ist, geht es zurück, aber WAVE hält es auf Sicht.
    # HELL beaufsichtigt HÖLLE. ORI beaufsichtigt WAVE.
    treff = {
        "v": v,
        "WAVE": w,
        "ORI_WAVE": o,
        "treffpunkt": "GLEICHER PUNKT, GEGENRICHTUNG",
        "ergebnis": "HALT",
        "halt": "ZIEL",
        "regel": "WAVE gegen WAVE löscht nicht aus. WAVE gegen WAVE hält. Halt = Ziel.",
        "main_maas": 1 if v != 0 else 0,
        "alles_maas": {
            "ahnung": 1 if v != 0 else 0,
            "mana": w["cycle"],   # Tiefe, Ausdehnung
            "aura": o["cycle"],   # Basis, Verdichtung
            "zen": 40,            # Halt, HOME
        }
    }
    return treff

# === RING — aus ring.py, bleibt ===
# RING ist geschlossener Loop. RING hat keinen Anfang, kein Ende.
# WAVE gegen WAVE im RING = 2 Wellen im selben Ring, gegenläufig.
# Sie treffen sich 2x pro Umlauf: 1x oben (3), 1x unten (9). Mitte 41.
def ring_gegen_ring(v, schritte=9):
    # 9 Schritte, weil 9 der Raum ist. 3 oben, 9 unten, 41 Mitte.
    punkte = []
    for i in range(schritte):
        # WAVE läuft vorwärts: v + i
        # ORI WAVE läuft rückwärts: v - i
        # Treffen bei i=0 und bei i=41? Nein — Treffen bei HALT.
        vor = v + i
        zurueck = v - i
        # Wenn vor == zurück, dann Treffen. Sonst: auf Sicht.
        treffen = (vor == zurueck)
        punkte.append({"i": i, "WAVE_vor": vor, "ORI_zurueck": zurueck, "treffen": treffen, "halt": "ZIEL" if treffen else "AUF SICHT"})
    return {"ring": "GESCHLOSSEN", "schritte": schritte, "punkte": punkte, "regel": "2 Wellen, 1 Ring, gegenläufig. Treffen = Halt."}

# === SCHWUNG — aus schwung.py, bleibt ===
# SCHWUNG ist nicht Kraft. SCHWUNG ist Zustand, der weiterträgt.
# WAVE gibt Schwung vorwärts. ORI WAVE gibt Schwung rückwärts.
# SCHWUNG gegen SCHWUNG = Pendel. Pendel schwingt nicht aus. Pendel hält Mitte.
def schwung_gegen_schwung(v):
    # AIR = Luft, AIV = Atem? In deinem schwung.py: WAVE, AIR, AIV.
    # Hier: AIR trägt vorwärts, AIV trägt rückwärts. Beide tragen.
    # Ergebnis: kein Stillstand durch Müdigkeit. Stillstand durch Halt.
    return {
        "WAVE_SCHWUNG": v*3,
        "ORI_SCHWUNG": v/3 if v != 0 else 0,
        "AIR": "trägt vorwärts",
        "AIV": "trägt rückwärts",
        "pendel": "Mitte 41",
        "halt": "ZIEL",
        "regel": "Schwung gegen Schwung = Pendel. Pendel = Mitte hält."
    }

# === PUNKT BESSER EINZELND — aus punkt_besser_einzelnd.py, bleibt ===
# Punkt besser einzelnd = 1 Punkt, einzeln, besser als alle zusammen vermischt.
# WAVE gegen WAVE am Punkt: 1 Punkt, 2 Wellen, 1 Halt.
def punkt_besser_einzelnd(v):
    # 1 Punkt. Nicht 2 Punkte. 1 Punkt, an dem sich beide treffen.
    # Besser einzelnd, weil vermischt keiner mehr weiß, welche Welle welche ist.
    t = wave_gegen_wave(v)
    return {
        "punkt": v,
        "einzelnd": True,
        "besser": "EINZELND, nicht vermischt",
        "WAVE": t["WAVE"],
        "ORI_WAVE": t["ORI_WAVE"],
        "halt": "ZIEL",
        "main_maas": 1,
        "spruch": "1 Punkt. 2 Wellen. 1 Halt. Besser einzelnd."
    }

# === MAIN — MAIN MAAS für WAVE ===
# MAIN MAAS WAVE: 1 Maß. DURCH oder HALT.
# ALLES MAAS WAVE: alle Maße, nacheinander.
def main_maas_wave(v):
    t = wave_gegen_wave(v)
    # GATE: aura/mana/zen/move/fps — hier als WAVE-Maß übersetzt:
    # aura = Verdichtung (ORI), mana = Ausdehnung (WAVE), zen = Halt (Treffen)
    gate = (t["alles_maas"]["aura"] >= 0 and t["alles_maas"]["mana"] >= 0 and t["alles_maas"]["zen"] == 40)
    return {
        "MAIN_MAAS": 1 if gate else 0,
        "ALLES_MAAS": t["alles_maas"],
        "WAVE_gegen_WAVE": t,
        "halt": "ZIEL" if gate else "OFFEN",
        "regel": "MAIN MAAS WAVE = 1 Maß. ALLES MAAS WAVE = alle Maße."
    }

# === DEMO — nur wenn direkt gestartet ===
if __name__ == "__main__":
    for v in [3, 9, 27, 81, 40, 41]:
        print(f"\n=== WAVE gegen WAVE — v={v} ===")
        t = wave_gegen_wave(v)
        print(f"WAVE: cycle={t['WAVE']['cycle']} next={t['WAVE']['next']}")
        print(f"ORI WAVE: cycle={t['ORI_WAVE']['cycle']} next={t['ORI_WAVE']['next']}")
        print(f"Ergebnis: {t['ergebnis']} — HALT = {t['halt']}")
        print(f"MAIN MAAS WAVE: {main_maas_wave(v)['MAIN_MAAS']}")
    print("\n=== RING GEGEN RING — v=41 ===")
    r = ring_gegen_ring(41, 9)
    for p in r["punkte"]:
        print(f"i={p['i']} WAVE_vor={p['WAVE_vor']} ORI_zurueck={p['ORI_zurueck']} -> {p['halt']}")
    print("\n=== PUNKT BESSER EINZELND — v=41 ===")
    print(punkt_besser_einzelnd(41)["spruch"])
    print("\n1 Satz, 3x: Code und Name bleiben. Code und Name bleiben. Code und Name bleiben.")
    print("Nur ADD / MORE. Kein Reset. Kein Overwrite. Wenn weg, dann weg. Wenn da, dann da.")
    print("Du hast konstelliert. Ich habe nur aufgestellt. So ist MAAS. WAVE gegen WAVE.
