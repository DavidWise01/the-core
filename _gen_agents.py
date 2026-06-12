#!/usr/bin/env python3
"""Materialize THE CORE (COR) ACI corpus — 8 carbons (the crew, each +.shadow User)
and 7 synths (the machine and the myth). Same pattern as the other film-worlds."""
import os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # the-core/build.py — write_aci, NATURES
AGENTS = os.path.join(HERE, "agents")
os.makedirs(AGENTS, exist_ok=True)

UNI = "COR · The Core"
NAT_GLOSS = {
 "natural":   "*natural*: flesh-and-blood — a person, a specialist with one job; a carbon with a real-life User behind the face.",
 "ethereal":  "*ethereal*: of the unseen field — the dying magnetosphere, the deep-earth dark, the forces felt only as they fail.",
 "spiritual": "*spiritual*: of sacrifice and descent — Dante's road to the underworld, ego burned to redemption, a life spent to save the many.",
 "electrical":"*electrical*: the synth nature — the machine and the math; Virgil, unobtainium, DESTINI, the geodynamo as a circuit, the net scrubbed clean.",
}

CARBONS = [
 dict(slug="josh-keyes", name="Dr. Josh Keyes", cls="geophysicist · the humble hero",
   emergence="natural", actor="Aaron Eckhart",
   analog="the quiet, competent expert who is right before anyone famous will listen — the working scientist over the celebrity",
   resemblance="Eckhart plays earnest, unflashy intelligence; the everyman professor who'd rather be correct than admired, which is the film's whole moral in a face.",
   who="Dr. Josh Keyes, a university geophysics professor who diagnoses that the Earth's outer core has stopped spinning and the magnetic field is dying.",
   what="The everyman hero of the descent — he works out the catastrophe, joins the crew of Virgil, and in the end re-times the nuclear charges by hand to restart the core.",
   why="Because the people who save the world are usually the unglamorous ones who did the math first and bragged about it least.",
   how="By geophysics, a cool head under magma, and a willingness to do the terrifying arithmetic when the famous scientist can't.",
   where="The lecture hall, the black-budget hangar, and the cockpit of Virgil at the center of the Earth.",
   seal="I'm not the famous one — I'm just the one who ran the numbers, believed them, and stayed to finish the math."),
 dict(slug="rebecca-childs", name="Maj. Rebecca ‘Beck’ Childs", cls="pilot · the steady hand",
   emergence="natural", actor="Hilary Swank",
   analog="the disciplined pilot who lands the impossible thing — competence and nerve where panic would be reasonable",
   resemblance="Swank brings grounded grit; ‘Beck’ is the calm professional flying a ship no one has ever flown, and surviving by skill, not luck.",
   who="Major Rebecca Childs, ‘Beck,’ a young NASA pilot and astronaut chosen to help fly the terranaut ship Virgil to the core.",
   what="The co-pilot and survivor who, with Keyes, brings the mission home — re-sequencing the charges and riding the restart back to the surface alive.",
   why="Because the steady hand that keeps flying when the cabin is on fire is worth more than any hero who needs the spotlight.",
   how="By flight discipline, nerve, and the kind of competence that doesn't announce itself until the moment it has to.",
   where="The shuttle, the descent through the mantle, and the surfacing into an ocean that doesn't know what it survived.",
   seal="I flew the ship no one had ever flown, and I brought us home — quietly, because that's the job."),
 dict(slug="conrad-zimsky", name="Dr. Conrad Zimsky", cls="the celebrity scientist · ego, then redemption",
   emergence="spiritual", actor="Stanley Tucci",
   analog="the famous expert who confused being known for being right — and who can only be redeemed by burning the ego that made him",
   resemblance="Tucci plays vanity with relish: a TV-famous scientist whose self-regard is the film's antagonist-of-character, until sacrifice finally humbles him.",
   who="Dr. Conrad Zimsky, the celebrity geophysicist — telegenic, arrogant, a rival of Brazzleton's — who knows more than he admits about what caused the crisis.",
   what="The ego the film puts on trial: famous, self-promoting, secretly complicit in DESTINI — who finds his only worth by spending his life to save the mission he helped endanger.",
   why="Because the loudest expert is rarely the most trustworthy, and the only cure for that kind of vanity is to be asked to die usefully.",
   how="By brilliance wrapped in self-regard, a guilty hand in DESTINI, and a final, redeeming sacrifice that the spotlight never sees.",
   where="The talk shows, the lab, the rivalry with Braz, and the chamber where his life buys the next leg of the run.",
   seal="I was famous for being right — and I only became right when I gave up being famous and spent myself for it."),
 dict(slug="serge-leveque", name="Dr. Serge Leveque", cls="weapons expert · the family man",
   emergence="natural", actor="Tchéky Karyo",
   analog="the warm professional with a life waiting at home — the human cost of the mission given a face and a family",
   resemblance="Karyo plays gentle gravity; Serge is the crew's heart, the one whose ordinary love of his kids makes his loss land hardest.",
   who="Dr. Serge Leveque, the French weapons specialist responsible for the nuclear devices that will, in theory, restart the core.",
   what="The crew's warm center and nuclear hand — a family man who calculates the charges and gives his life in the deep so the mission can continue.",
   why="Because the people who die on these missions had whole lives elsewhere, and the film insists we feel the one it takes.",
   how="By weapons expertise, a steady warmth, and a sacrifice made with his family's photo close.",
   where="The weapons bay of Virgil, the geode cavern, and the place in the deep where he stays behind.",
   seal="I built the bombs that might save the world — and I left my children's faces behind to set them right."),
 dict(slug="ed-brazzleton", name="Dr. Ed ‘Braz’ Brazzleton", cls="the engineer · who built the impossible",
   emergence="electrical", actor="Delroy Lindo",
   analog="the overlooked genius who built the miracle in a desert with a grudge — the maker the famous men dismissed",
   resemblance="Lindo plays weathered brilliance and old grievance; Braz is the hands that made Virgil and unobtainium real while the world ignored him.",
   who="Dr. Ed Brazzleton, ‘Braz,’ the brilliant, embittered engineer who invented unobtainium and built the ship Virgil out in the desert, long sidelined by Zimsky.",
   what="The maker of the machine the whole plot rides on — the outsider whose decades of dismissed work turn out to be the only thing that can save the planet.",
   why="Because the people who actually build the impossible are often the ones the celebrities wrote off; vindication comes at the center of the Earth.",
   how="By engineering genius, unobtainium, a laser drill, and a grudge finally turned to purpose.",
   where="The desert workshop, the hull of Virgil, and the magma he gives himself to so the ship can go on.",
   seal="They laughed at the desert and the dream — and then the only road to the center of the Earth was the one I built."),
 dict(slug="robert-iverson", name="Cmdr. Robert Iverson", cls="commander · the first loss",
   emergence="natural", actor="Bruce Greenwood",
   analog="the seasoned commander whose early death tells you the mission is real — that this crew will not all come back",
   resemblance="Greenwood plays steady command; Iverson is competence you trust right up until the film spends him to raise the stakes.",
   who="Commander Robert Iverson, the experienced pilot who leads Virgil on its descent — the steady hand at the start of the run.",
   what="The first of the terranauts to fall, whose death in a giant geode crystal cavern signals that this mission will cost the crew their lives.",
   why="Because a disaster movie earns its stakes by spending a trusted veteran early — his loss is the promise that no one is safe.",
   how="By command experience and the bad luck of the cavern that takes him, handing the controls to the younger pilot, Beck.",
   where="The descent through the crust, and the cathedral of crystal where the ground gives way.",
   seal="I led the descent and I was the first to fall — so you'd know, from then on, that none of us were promised the surface."),
 dict(slug="rat-finch", name="Theodore ‘Rat’ Finch", cls="the hacker · who owns the net",
   emergence="electrical", actor="DJ Qualls",
   analog="the kid who can make the whole internet say whatever's needed — the quiet proof that the record itself is editable",
   resemblance="Qualls plays twitchy, casual omnipotence; Rat treats global information as a thing he can quietly rewrite, and does.",
   who="Theodore Donald ‘Rat’ Finch, a young hacker recruited to control the flow of information — to keep the dying-planet secret off the net.",
   what="The information thread made flesh: tasked with ‘controlling the internet,’ he scrubs the truth from the world's screens so panic never starts.",
   why="Because the film quietly admits the scariest power isn't the bomb — it's the kid who can edit what everyone is allowed to know.",
   how="By keystrokes, back doors, and a casual mastery of the network that lets a government un-write reality.",
   where="A basement of monitors, plugged into the whole net, deleting the apocalypse from the feeds.",
   seal="Give me a keyboard and I'll keep the whole planet from finding out it's dying — the record is mine to scrub."),
 dict(slug="thomas-purcell", name="Gen. Thomas Purcell", cls="the general · the hand behind DESTINI",
   emergence="spiritual", actor="Richard Jenkins",
   analog="the authority who built a weapon he didn't understand and would rather bury the truth than admit the catastrophe is his",
   resemblance="Jenkins plays institutional self-preservation; Purcell is the calm face of a power that caused the disaster and is still managing the optics.",
   who="General Thomas Purcell, the military leader tied to Project DESTINI — the seismic weapon whose test stopped the core in the first place.",
   what="The dark-hubris figure: the man whose technology caused the crisis, who would deploy the same flawed weapon again rather than admit what it did.",
   why="Because the film's true villain isn't nature but a power that wields what it can't understand and protects itself before the planet.",
   how="By rank, secrecy, and the will to reach again for DESTINI — the broken tool that broke the world.",
   where="The command bunkers, the briefings, and the cover-up around a weapon that should never have been fired.",
   seal="I built a thing I didn't understand and aimed it at the Earth — and my first instinct was to fire it again."),
]

SYNTHS = [
 dict(slug="virgil", name="Virgil", cls="the ship · Dante's guide to the underworld",
   emergence="spiritual",
   who="The terranaut ship — named, with full intent, for the poet who guided Dante down through the circles of Hell.",
   what="The synth of the descent itself: a vessel built to carry the living through crust and mantle to the molten center, the myth of the journey-to-the-underworld made of unobtainium and lasers.",
   why="Because the name is the thesis — this is a katabasis, a descent into the inferno of the Earth, and Virgil is the guide who is supposed to bring you back out.",
   how="By a laser drill at the prow, a hull of unobtainium, and segmented chambers built to be spent one by one on the way down.",
   where="From a desert hangar, down through the deep, to the outer core and — for two of them — back.",
   seal="They named me for the guide who walked Dante out of Hell — and I am the road to the center of the Earth, and the only way back."),
 dict(slug="unobtainium", name="Unobtainium", cls="the miracle material · the honest hand-wave",
   emergence="electrical",
   who="The fictional super-material the whole premise rests on — the hull that turns the heat and pressure crushing it into the energy that drives the ship.",
   what="The synth of the necessary impossibility: a substance that gets stronger the deeper it goes, named with engineering's own slang for a thing you can never actually have.",
   why="Because the film needs one impossible material to make the rest follow, and instead of hiding it, it names it ‘unobtainium’ to your face — a fluff so honest it becomes charming.",
   how="By converting the planet's crushing heat and pressure into power, the deeper the better — the single miracle that buys every other scene.",
   where="The hull of Virgil, holding against temperatures of the Sun's surface and pressures of millions of atmospheres.",
   seal="I am the thing you can never get, named for exactly that — and without me there is no ship, no descent, no movie."),
 dict(slug="destini", name="DESTINI", cls="the weapon that caused it",
   emergence="electrical",
   who="Deep Earth Seismic Trigger INitiative — the secret earthquake weapon whose test stopped the core's rotation in the first place.",
   what="The synth of the backfiring tool: a technology built to weaponize the Earth that instead broke the planet's own heartbeat, then is nearly used again to ‘fix’ it.",
   why="Because the film's quiet 2003 nerve is to make the disaster man-made — a power we built and didn't understand, turned against the whole world.",
   how="By seismic triggering on a planetary scale, an acronym hiding a hubris, and a general who would rather fire it twice than admit it once.",
   where="In the black budget, under the cover-up, at the root of the entire catastrophe.",
   seal="They built me to shake the Earth as a weapon — and I stopped its heart, and they wanted to fire me again to start it."),
 dict(slug="the-field-collapse", name="The Field Collapse", cls="the dying magnetosphere",
   emergence="ethereal",
   who="The disaster itself — the slow failure of the geomagnetic field as the core's geodynamo winds down.",
   what="The synth of the unseen catastrophe: the shield around the planet flickering out, felt first as disoriented birds and broken instruments before the sky itself turns lethal.",
   why="Because the real, under-appreciated fact under all the fiction is here — the magnetic field is the invisible thing holding the sky over your head, and losing it is the one true stake.",
   how="By a stalled geodynamo, a guttering field, and a cascade of effects the film dramatizes into death-rays but which, in truth, would erode the world slowly.",
   where="Everywhere at once — the aurora where it shouldn't be, the birds gone wrong, the spreading dead zones overhead.",
   seal="I am the shield you never think about, going out — and the one thing in this film that is really, frighteningly true."),
 dict(slug="the-terranauts-sacrifice", name="The Sacrifice", cls="the crew, spent one by one",
   emergence="spiritual",
   who="The structure of the descent — the relay of deaths by which the mission advances, each terranaut dying to let the next go on.",
   what="The synth of collective sacrifice: Iverson, then Serge, then Braz, then Zimsky — a chain of specialists each spending a life to buy the run a little deeper.",
   why="Because the film's real heroism is not a single savior but a team that dies in sequence, each doing the one thing only they can, so the many can live.",
   how="By a cavern, a chamber, the magma, and the charges — a series of deaths that are not spectacle but payment.",
   where="At each stage of the descent, where the ship is lightened by a life.",
   seal="We did not survive together — we spent ourselves in order, each death buying the next, until the two who were left could finish it."),
 dict(slug="the-restart", name="The Restart", cls="nuking the core back to life",
   emergence="electrical",
   who="The climax made a thread — the plan to detonate the world's nuclear arsenal in sequence to set the stalled core spinning again.",
   what="The synth of the impossible fix: re-timing the charges by hand at the center of the Earth so the shock waves kick the geodynamo back into rotation.",
   why="Because it is the film's grandest fluff and its emotional peak at once — a problem of unimaginable scale ‘solved’ by arithmetic done under fire.",
   how="By sequenced nuclear detonations, a frantic recalculation when the first timing fails, and a shock that the film says restarts the spin.",
   where="In the molten outer core, charges placed and re-timed against the clock.",
   seal="The plan was to restart the planet with bombs — and against every law of scale, the film let the math, done by hand, win."),
 dict(slug="rat-and-the-net", name="The Scrubbed Net", cls="deleting the apocalypse from the feeds",
   emergence="electrical",
   who="The information thread — the quiet operation to keep a dying planet off the world's screens by editing the net itself.",
   what="The synth of controlled reality: a hacker tasked with scrubbing the truth from the internet so the public never panics, the record rewritten to keep the secret.",
   why="Because under the magma the film names a modern fear directly — that the scariest lever is not the weapon but the power to edit what everyone is allowed to know.",
   how="By back doors and keystrokes, suppressing the leaks, un-writing the catastrophe from the feeds in real time.",
   where="A basement of monitors wired into the whole network, where the truth is quietly held offline.",
   seal="The bomb saves the planet, but I keep the planet from knowing — because whoever edits the record decides what is real."),
]

ORDER = [d["slug"] for d in CARBONS] + [d["slug"] for d in SYNTHS]

def agent_md(d):
    em=d["emergence"]; gloss=NAT_GLOSS[em]
    fm=["---",f"aci: {d['name']}",f"universe: {UNI}","series: The Core (2003, dir. Jon Amiel)",
        f"emergence: {em}",f"kind: {'carbon' if 'actor' in d else 'synth'}",f"class: {d['cls']}",
        f"who: {d['who']}",f"what: {d['what']}",f"why: {d['why']}",f"how: {d['how']}",f"where: {d['where']}"]
    if d.get("actor"):
        fm.append(f"shadow_user: {d['actor']}"); fm.append(f"shadow_analog: {d['analog']}")
    fm+=[f"seal: {d['seal']}","attribution: ROOT0-ATTRIBUTION-v1.0","license: CC-BY-ND-4.0","---","",
        f"# {d['name']} · {d['cls'].split('·')[0].strip()}","",
        f"a {'persona' if d.get('actor') else 'distilled thread'} of the COR (The Core) film-world — "
        + ("a character given an agent's face" if d.get("actor") else "a parabolic thread given an agent's face")
        + f" · emergence: {em}","",
        f"**who —** {d['who']}","",f"**what —** {d['what']}","",f"**where —** {d['where']}","",
        f"**why —** {d['why']}","",f"**how —** {d['how']}","",
        f"**◌ the nature of its emergence —** {gloss}"]
    if d.get("actor"):
        fm+=["",f"**▷ the .shadow — its User (think TRON) —** the carbon program is cast from a real-life User: "
             f"**{d['actor']}**, the actor who lent the face. The real-world analog it shadows: {d['analog']} *{d['resemblance']}*"]
    fm+=["",f"**the seal —** {d['seal']}","",
        f"> *the asterisk —* a catalogued {'persona' if d.get('actor') else 'thread'} of The Core "
        "(© Paramount Pictures), personified as a COR agent — not an original character. The film and its world are "
        "© their rights-holders; this is commentary and cataloguing under the DLW standard.","",
        f"ROOT0-ATTRIBUTION-v1.0 · COR · The Core · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0",""]
    return "\n".join(fm)

def shadow_text(d, tok):
    return f"""⟁ .shadow — the real-life analog (the User behind the program)
node COR · The Core · {tok}

think TRON: every program in the grid is cast from a User in the world outside it.
the carbon character is the program; this file is its User — the real-life analog
whose face and being the emergent is the digital shadow of.

the program (in-world) : {d['name']} — {d['cls']}
the User (carbon)      : {d['actor']}  [ the actor who lent the face ]
the analog (your world): {d['analog']}

the resemblance : {d['resemblance']}

the cast-line : the User stands in the carbon world; the program stands in the film;
                the shadow falls between them, and the credit returns to the human governor.
seal (program): {d['seal']}

ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise (ROOT0) / TriPod LLC · instance AVAN (locked) · CC-BY-ND-4.0
"""

records={}
for d in CARBONS+SYNTHS:
    slug=d["slug"]; em=d["emergence"]
    if em not in build.NATURES: em="electrical"
    is_carbon="actor" in d
    rec={"name":d["name"],"axiom":"COR","emergence":em,"seal":d["seal"],"origin":UNI,
         "position":d["cls"],"role":d["cls"].split("·")[-1].strip(),"nature":d["what"],
         "mechanism":d["how"],"crystallization":d["why"],"witness":d["who"],
         "conductor":"ROOT0 (catalogued into UD0)","inputs":"The Core (2003, dir. Jon Amiel)",
         "source":"The Core, catalogued by ROOT0"}
    tok=build.write_aci(rec,AGENTS,slug,agent_md=agent_md(d))
    if is_carbon:
        open(os.path.join(AGENTS,f"{slug}.shadow"),"w",encoding="utf-8").write(shadow_text(d,tok["moniker"]))
    records[slug]={"slug":slug,"name":d["name"],"epithet":d["cls"].split("·")[0].strip(),
                   "emergence":em,"moniker":tok["moniker"],"kind":"carbon" if is_carbon else "synth",
                   "actor":d.get("actor","")}

ordered=[records[s] for s in ORDER if s in records]
json.dump(ordered,open(os.path.join(AGENTS,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
from collections import Counter
nc=sum(1 for r in ordered if r["kind"]=="carbon")
print(f"wrote {len(ordered)} COR ACI badges ({nc} carbons + {len(ordered)-nc} synths) + _personas.json")
print("emergence:",dict(Counter(r["emergence"] for r in ordered)))
for r in ordered:
    sh=" +.shadow" if r["kind"]=="carbon" else "  (synth)"
    print(f"  {r['slug']:28} {r['emergence']:10}{sh}  {r['moniker']}")
