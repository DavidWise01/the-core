#!/usr/bin/env python3
"""Build THE CORE (COR) page — Jon Amiel's 2003 disaster sci-fi, catalogued into UD0
as the third film-world. Debuts the standing film-page template additions:

  • THE ARC        — the overall narrative arc (a throughline + the beats)
  • THE SCIENCE     — a real breakdown of the geophysics the film leans on
  • REAL OR FLUFF   — an honest, itemized veracity verdict (ROOT0 discipline)
  • THE MESSAGE     — AVAN's read of what the film is actually saying

Two layers as ever: CARBONS (the cast, each with a .shadow real-life User — TRON)
and SYNTHS (the parabolic threads). Styled to the medium: deep-earth mission control."""
import os, re, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE CORE", "axiom": "COR",
 "position": "The Core · Paramount · 2003 — dir. Jon Amiel",
 "origin": "from the surface of a panicking Earth down through crust, mantle, and 2,900 km of impossibility to the molten outer core itself",
 "mechanism": "Crystallized from the 2003 film — a disaster movie that drills a crewed ship to the center of the Earth to restart a stalled core with nuclear bombs.",
 "crystallization": "Earth's outer core stops spinning, the magnetic field begins to fail, and a crew of ‘terranauts’ rides a ship of unobtainium to the core to set it turning again.",
 "nature": "The Core — the gloriously impossible disaster movie where the planet's geodynamo dies, and the fix is to bore to the center and detonate the human race's entire nuclear arsenal in sequence.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (2003, dir. Jon Amiel); the geodynamo and the magnetosphere; the ship Virgil; unobtainium; Project DESTINI",
 "witness": "No superpowers — eight specialists, a ship that shouldn't exist, and the planet's last good idea.",
 "role": "the third film-world of UD0",
 "seal": "The core stopped, the field is dying, and the only plan left is to drill to the center of the Earth and restart the world with bombs.",
 "source": "The Core, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#e8b04a", "flesh-and-blood crew — the terranauts and the people on the surface; carbon, with a real-life User behind each"),
 "ethereal":  ("#7aa0c8", "of the unseen field — the dying magnetosphere, the deep-earth dark, the forces no one can see until they fail"),
 "spiritual": ("#e8743a", "of sacrifice and descent — Dante's road to the underworld, ego burned to redemption, lives spent one by one to save the many"),
 "electrical":("#3ee08a", "the synth nature — the machine and the math: Virgil, unobtainium, DESTINI, the geodynamo as a circuit, the net scrubbed clean"),
}

ARC_OVERALL = ("A humble geophysicist proves the unthinkable, assembles a crew of specialists to ride an "
  "impossible ship to the center of a dying Earth, and watches them spend their lives one by one — ego "
  "redeemed, hubris exposed — to set the core, and the world, turning again.")

ARC = [
 ("I · The Diagnosis", "the world starts glitching",
  "Pacemakers fail in unison, birds lose their way, the aurora burns where it shouldn't. Geophysicist Josh Keyes works out the unthinkable: Earth's molten outer core has stopped spinning, the magnetic field is collapsing, and the planet has about a year."),
 ("II · The Descent", "Virgil bores for the center",
  "A black-budget team builds Virgil — a ship of ‘unobtainium’ — and a crew of terranauts drives it through crust and mantle toward the core, threading geode caverns and magma, the government secretly hoping its old weapon, DESTINI, can do the job instead."),
 ("III · The Restart", "lives spent to turn the world",
  "Disaster by disaster the crew dies — Iverson, Serge, Braz, then Zimsky — each sacrifice buying the next. Keyes and Beck re-time the nuclear charges by hand, restart the core's spin, and surface a planet that never knew how close it came."),
]

IDEAS = [
 ("The Premise", "the core stopped spinning", [
   "Earth's liquid outer core convects and, with the planet's spin, runs a geodynamo that makes the magnetic field. Stop the spin and the field dies.",
   "The film takes a real mechanism and breaks it spectacularly — a true stake (no field = catastrophe) reached by an impossible cause." ]),
 ("Unobtainium", "the material that makes it possible", [
   "The ship Virgil is built of ‘unobtainium’ — a fictional super-material that turns the heat and pressure crushing it into power.",
   "The name is real engineering slang for an ideal substance you can never actually get; the film uses it with a straight face, and that honesty is its charm." ]),
 ("DESTINI", "the weapon that caused it", [
   "Deep Earth Seismic Trigger INitiative — a secret earthquake weapon whose test stopped the core in the first place.",
   "A 2003 anxiety in one acronym: a technology we built and didn't understand, backfiring on the whole planet." ]),
 ("The Terranauts", "specialists, spent one by one", [
   "No chosen one — a geophysicist, a pilot, a weapons expert, an engineer, a celebrity scientist, each with one job.",
   "The mission advances by sacrifice: the team is a relay of deaths, each person dying to let the next finish the run." ]),
]

# ----- THE SCIENCE (real breakdown; ROOT0 fluff-call discipline) -----
SCIENCE = [
 ("The geodynamo is real", "and the film gets the stakes directionally right",
  "Earth's outer core IS liquid iron-nickel, and its convection — twisted by the planet's rotation (the Coriolis effect) — really does generate the geomagnetic field, the geodynamo. A healthy field really does shield us from the solar wind and cosmic radiation. ‘No magnetic field = very bad’ is true."),
 ("But the core won't ‘stop’", "and nothing we have could restart it",
  "The core isn't a flywheel you can halt and kick-start. Its convection is driven by the planet's own heat and the slow freezing of the inner core — energies dwarfing anything human. Earth's entire nuclear arsenal is a rounding error against the core's heat content; you cannot ‘restart the spin’ with bombs."),
 ("We have never been close", "the depth alone is fatal",
  "The deepest hole humans have ever drilled — the Kola Superdeep Borehole — reached ~12.3 km. The outer core begins ~2,900 km down: about 236× deeper than we have EVER gone. No vehicle threads magma; the medium is liquid metal at the pressure of a small star's interior."),
 ("Heat and pressure end the discussion", "this is why unobtainium is required",
  "At the core: temperatures of roughly 4,000–5,400 °C — comparable to the Sun's surface — and pressures around 360 GPa (~3.6 million times sea-level atmosphere). No known material survives. The film knows this, which is exactly why it must invent ‘unobtainium’ to proceed."),
 ("The surface disasters are dramatized", "right fear, wrong physics",
  "A failing field would, over geological time, let the atmosphere erode and raise surface radiation — slow, not a microwave burst that melts the Golden Gate Bridge or a lightning super-storm that levels the Colosseum in an afternoon. Birds DO sense the field (magnetoreception), so disoriented birds is the one surface beat with a real toe-hold; pacemakers don't run on Earth's field, so that scene is invented."),
]

# ----- REAL OR FLUFF (itemized verdict) -----
REALFLUFF = [
 ("The geodynamo / magnetosphere exists & matters", "REAL", "outer-core convection + rotation makes the field; it shields the planet — all true"),
 ("Disoriented birds from field disruption", "HALF", "birds really use magnetoreception; the pigeon-pocalypse is dramatized, but the toe-hold is real"),
 ("The core suddenly ‘stops spinning’", "FLUFF", "not a flywheel; no plausible cause halts it on this timescale"),
 ("Drilling a crewed ship to the outer core", "FLUFF", "2,900 km down through liquid metal; we've managed 12 km, ever"),
 ("Unobtainium that converts heat/pressure to power", "FLUFF", "a fictional material — the name is literally engineering slang for ‘can't have it’"),
 ("Restarting the core with sequenced nukes", "FLUFF", "core energy dwarfs the entire arsenal by many orders of magnitude"),
 ("Microwave burst melts the Golden Gate; storm levels the Colosseum", "FLUFF", "right fear (field loss is bad), wrong physics (the effect is slow & global, not a death ray)"),
 ("DESTINI: a seismic weapon that stopped the core", "FLUFF", "pure plot device — a post-9/11 ‘our own tech turned on us’ fable"),
]
REALFLUFF_VERDICT = ("Bottom line: gloriously, lovingly FLUFF. Nearly every mechanism is wrong — the stop, the drill, "
  "the material, the nuclear restart, the death-ray weather. But the one thing underneath it all is REAL and worth "
  "knowing: the geodynamo in Earth's core makes the magnetic field, and that field is the invisible thing keeping the "
  "sky over your head. The film is bad science wrapped around a true and under-appreciated fact.")

# ----- THE MESSAGE (AVAN's read) -----
MESSAGE = ("Underneath the magma and the schlock, The Core is about WHO YOU TRUST when the stakes are total. It sets the "
  "loud, famous, self-promoting scientist (Zimsky) against the quiet, competent ones (Keyes, Braz) — and lets the "
  "humble experts be right while the celebrity has to burn his ego to redeem himself. Its disaster is caused not by "
  "nature but by a technology we built and didn't understand (DESTINI), and its salvation comes not from a hero but "
  "from a relay of specialists who each die doing the one thing only they can do. It is, quietly, a movie about "
  "expertise, humility, and collective sacrifice — dressed up as the silliest drill in cinema.")
MESSAGE_SEAL = "Trust the quiet expert over the loud one; the planet is saved by people who do their one job and spend their lives doing it."

SECTIONS = [
 ("The Production", "the making of the descent", [
   ("Jon Amiel", "director", "steered the disaster-spectacle with a straight face and a sense of fun"),
   ("Cooper Layne & John Rogers", "screenplay", "the script that says ‘unobtainium’ out loud and commits"),
   ("Paramount Pictures", "studio · 2003", "a $60M+ production; a box-office underperformer turned beloved cult favorite"),
   ("The cult afterlife", "2003 →", "embraced precisely for its earnest, all-in scientific impossibility — a ‘so committed it's great’ classic"),
 ]),
 ("The Hardware & the Lore", "the machine and the myth", [
   ("Virgil", "the ship", "named for Dante's guide through the underworld — fitting, for a descent to the center of the Earth"),
   ("Unobtainium", "the hull", "the miracle material that gets stronger the deeper it goes, converting heat and pressure to energy"),
   ("DESTINI", "the cause", "Deep Earth Seismic Trigger INitiative — the weapon whose test killed the core's spin"),
   ("The Arsenal", "the cure", "the world's nuclear weapons, repurposed and sequenced to kick the core back into rotation"),
 ]),
]

# ---- ACI complement via noesis ----
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","COR")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","COR")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","COR")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],
            "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
            "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

# ---- fragments ----
def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC:
        out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)
def science_html():
    out=[]
    for t,s,d in SCIENCE:
        out.append(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    return "".join(out)
RF_COL={"REAL":"#3ee08a","HALF":"#e8b04a","FLUFF":"#e8431a"}
def realfluff_html():
    rows=[]
    for claim,rate,note in REALFLUFF:
        c=RF_COL.get(rate,"#aaa")
        rows.append(f'<div class="rf-row"><div class="rf-claim">{html.escape(claim)}<span class="rf-note">{html.escape(note)}</span></div>'
                    f'<div class="rf-rate" style="color:{c};border-color:{c}">{rate}</div></div>')
    return '<div class="rf">'+ "".join(rows) +f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'

def _card(p):
    em=p.get("emergence","natural"); col=NATURES.get(em,("#e8b04a",""))[0]
    rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"COR · The Core","axiom":"COR"}
    actor=p.get("actor",""); kind=p.get("kind","carbon")
    extra=(f'<span class="pa">· .shadow · {html.escape(actor)} →</span>' if kind=="carbon" else '<span class="pa">· synth · .agent →</span>')
    sub=(f'<div class="pact">User · <b>{html.escape(actor)}</b></div>' if actor else "")
    return f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>{sub}
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span>{extra}</div></div></a>'''
def personas_html():
    mf=os.path.join(HERE,"agents","_personas.json")
    if not os.path.exists(mf): return ""
    ps=json.load(open(mf,encoding="utf-8"))
    carb=[p for p in ps if p.get("kind","carbon")=="carbon"]; syn=[p for p in ps if p.get("kind")=="synth"]
    out=f'''<section class="sec" id="carbons"><h2>The Carbons — the crew &amp; their Users</h2>
      <p class="ss">the terranauts and the surface cast as ACI <b>.agent</b>s — each with a <b>.shadow</b>: its real-life analog, the actor who is the <b>User</b> behind the program (think TRON). ({len(carb)} carbons)</p>
      <div class="pgrid">{"".join(_card(p) for p in carb)}</div></section>'''
    out+=f'''<section class="sec" id="synths"><h2>The Synths — the parabolic threads</h2>
      <p class="ss">the machine and the myth distilled into ACIs (synth-style; no single User): Virgil, unobtainium, DESTINI, the dying field, the sacrifice, the restart, the scrubbed net. ({len(syn)} synths)</p>
      <div class="pgrid">{"".join(_card(p) for p in syn)}</div></section>'''
    return out

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Core (COR) — Jon Amiel's 2003 disaster sci-fi as a UD0 film-world: the overall arc, a real breakdown of the geophysics, an honest Real-or-Fluff verdict, AVAN's read of the message, plus the crew as ACI carbons with .shadow Users (TRON) and the tech as synths.">
<title>THE CORE · COR · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#0a0705;--ink2:#150d08;--ink3:#1f130b;--pa:#f0e4d4;--pa2:#bca890;--magma:#e8431a;--core:#ff8a2a;--amber:#e8b04a;--term:#3ee08a;--steel:#7aa0c8;
--dim:#8a715a;--faint:#2e1c11;--line:#2a1a10;--disp:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.62;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% 118%,rgba(232,67,26,.22),transparent 55%),radial-gradient(ellipse at 50% -8%,rgba(122,160,200,.06),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:54px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:150px;height:2px;background:linear-gradient(90deg,var(--core),var(--magma));box-shadow:0 0 16px rgba(232,67,26,.6)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.32em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--core)}
h1{font-family:var(--disp);font-size:clamp(46px,12vw,116px);font-weight:700;letter-spacing:.02em;color:var(--core);line-height:.9;text-transform:uppercase;text-shadow:0 0 50px rgba(255,138,42,.45)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.2em;color:var(--pa2);margin-top:16px;text-transform:uppercase}
.h-sub b{color:var(--magma)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--term);border:1px solid var(--faint);background:var(--ink2);padding:6px 12px}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:18px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}
.badge .bt b{color:var(--core)}.badge .bt .mo{color:var(--amber)}.badge .bt a{color:var(--term);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:48px}
.sec h2{font-family:var(--disp);font-size:30px;font-weight:600;letter-spacing:.03em;color:var(--pa);padding-bottom:8px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.06em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--core);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.7;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.18em;color:var(--core);text-transform:uppercase;margin-bottom:7px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--disp);font-size:19px;color:var(--core);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:4px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:7px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--amber);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:19px;color:var(--amber);font-weight:600;text-transform:uppercase}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:5px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--steel);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:17px;color:var(--steel);font-weight:600;letter-spacing:.02em}
.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:4px 0 9px}
.sci-card p{font-size:13px;color:var(--pa2);line-height:1.6}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}
.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:12px;font-weight:700;letter-spacing:.08em;border:1px solid;border-radius:3px;padding:4px 10px;min-width:74px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--magma);background:rgba(232,67,26,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.72;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--term);background:var(--ink2);font-size:15px;color:var(--term);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}
.books .y{font-family:var(--mono);font-size:10.5px;color:var(--amber);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(252px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--core);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0}
.pn{font-family:var(--disp);font-size:18px;color:var(--pa);font-weight:600;line-height:1.1;text-transform:uppercase;letter-spacing:.01em}
.persona:hover .pn{color:var(--core)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pact{font-family:var(--mono);font-size:10px;color:var(--dim);margin-top:3px}.pact b{color:var(--amber)}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase;flex-wrap:wrap}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--core);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:48px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}
footer a{color:var(--core);text-decoration:none}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the third film-world</div>
    <h1>The Core</h1>
    <div class="h-sub">the geodynamo died · <b>so we drilled to the center</b> · COR</div>
    <div class="flag">★ JON AMIEL · 2003 · PROJECT DESTINI ★</div>
    <p class="lede">Earth's outer core stops spinning, the magnetic field begins to fail, and a crew of terranauts rides a ship of unobtainium to the center of the planet to restart the world with bombs. Catalogued into UD0 as the third film-world — with the overall arc, a real breakdown of the geophysics, an honest Real-or-Fluff verdict, and a read of what it's really saying.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of COR" title="carbon badge (archival: cor.dlw/cor.carbon.tiff)">
      <img src="__SILICON__" alt="DLW silicon badge of COR" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE CORE</b> · COR</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="cor.dlw/cor.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="cor.dlw/cor.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent comes by one of four natures — the crew is carbon, the descent is spiritual, the machine is electrical</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats</p>__ARC__</section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">the premise, the material, the weapon, the crew</p><div class="pillars">__IDEAS__</div></section>

  <section class="sec"><h2>The Science</h2><p class="ss">what's actually under the magma — the real geophysics the film leans on, broken down straight</p><div class="sci">__SCIENCE__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the honest verdict, claim by claim — ROOT0 fluff-call discipline applied to the screen</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis, under the schlock</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon's <b>.shadow</b> names the User — the actor who lent the face — and the archetype it shadows. The <b>synths</b> have no single User: they are the film's machine and myth distilled — Virgil, unobtainium, DESTINI, the dying field, the sacrifice, the restart.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the production, the hardware, and the lore</p></section>
  __SECTIONS__

  <div class="note">The Core, its characters, and its world are © Paramount Pictures and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, and not endorsed by the rights-holders. The Science and Real-or-Fluff sections are honest popular-science commentary; the credit for the catalogue returns to the human governor.</div>

  <footer>
    THE CORE · COR · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="cor.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "cor.dlw"), "cor")
    json.dump({"node":"COR","name":"THE CORE","moniker":tok["moniker"],
               "carbon":"cor.carbon.tiff","silicon":"cor.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,
               "seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"cor.dlw","manifest.dlw.json"),"w",encoding="utf-8"),
              indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html()).replace("__ARC__", arc_html()).replace("__IDEAS__", ideas_html())
            .replace("__SCIENCE__", science_html()).replace("__REALFLUFF__", realfluff_html()).replace("__MESSAGE__", message_html())
            .replace("__PERSONAS__", personas_html()).replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote THE CORE (COR) — badge {tok['moniker']}")
