# -*- coding: utf-8 -*-
import random, re, time, weechat as w

channels = ['#chee-fanclub', '#krok', '##krok', '##mahjong']
nicks = ['krok', 'kg', 'k', 'k-', 'idalius']

smileys = [
    ':)',  ':^)', 'xD',  ':D',
    'D:',  ':O',  '<3',  '</3',
    ':/',  ':}',  ':I',  ':]',
    ';^)', ':^D', ';)',  ':L',
    ':S',  ':s',  ';~;', ';-;'
]

wednesdays = [
    'it is wednesday my dudes',
    'today is friday'
]

beeps = [
    'BEEP', 'BLEEP', 'BOOP', 'BLOOP', 'BOP', 'KLINK', 'KLANK',
    'BOING'
]

gays = [
    'i am a butt pirate',
    'i am a beach bitch',
    'i am a basic bitch',
    'i am a whore',
    'i am a thot',

    'np: Ween - Waving My Dick in the Wind',
    'np: Village People - YMCA',
    'np: Lady Gaga - Born This Way',
    'np: The Weather Girls - It\'s Raining Men',
    'np: Marvin Gaye - I Heard It Through The Grapevine',

    'k is gay',
    'jp is gay',
    'i am gay',

    'peter dinklage is hot',
    'i want chris hemsworth to tie me to a radiator',
    'let\'s be gay together sangy'
]

fnord = [
    '%s is evaporated herbal tea without the herbs.',
    '%s is that funny feeling you get when you reach for the Snickers bar and come back holding a slurpee.',
    '%s is the 43 1/3rd state, next to Wyoming.',
    '%s is this really, really tall mountain.',
    '%s is the reason boxes of condoms carry twelve instead of ten.',
    '%s is the blue stripes in the road that never get painted.',
    '%s is place where those socks vanish off to in the laundry.',
    '%s is an arcade game like Pacman without the little dots.',
    '%s is a little pufflike cloud you see at 5pm.',
    '%s is the tool the dentist uses on unruly patients.',
    '%s is the blank paper that cassette labels are printed on.',
    '%s is where the buses hide at night.',
    '%s is the empty pages at the end of the book.',
    '%s is the screw that falls from the car for no reason.',
    '%s is why Burger King uses paper instead of foam.',
    '%s is the little green pebble in your shoe.',
    '%s is the orange print in the yellow pages.',
    '%s is a pickle without the bumps.             ',
    '%s is why ducks eat trees.',
    '%s is toast without bread.     ',
    '%s is a venetian blind without the slats.',
    '%s is the lint in the navel of the mites that eat the lint in the navel of the mites that eat the lint in %s\'s navel.',
    '%s is an apostrophe on drugs.',
    '%s is the bucket where they keep the unused serifs for H*lvetica.',
    '%s is the gunk that sticks to the inside of your car\'s fenders.',
    '%s is the source of all the zero bits in your computer.',
    '%s is the echo of silence.',
    '%s is the parsley on the plate of life.',
    '%s is the sales tax on happiness.',
    '%s is the preposition at the end of sixpence.',
    '%s is the feeling in your brain when you hold your breath too long.',
    '%s is the reason latent homosexuals stay latent.',
    '%s is the donut hole.',
    '%s is an annoying series of email messages.',
    '%s is the color only blind people can see.',
    '%s is the serial number on a box of cereal.',
    '%s is the Universe with decreasing entropy.',
    '%s is a naked woman with herpes simplex 428.',
    '%s is the yin without yang.',
    '%s is a pyrotumescent retrograde onyx obelisk.',
    '%s is why lisp has so many parentheses.',
    '%s is the the four-leaf clover with a missing leaf.',
    '%s is double-jointed and has a cubic spline.',
    '%s never sleeps.',
    '%s is the "een" in baleen whale.',
    '%s is neither a particle nor a wave.',
    '%s is the space in between the pixels on your screen.',
    '%s is the guy that writes the Infiniti ads.',
    '%s is the nut in peanut butter and jelly.',
    '%s is an antebellum flagellum fella.',
    '%s is a sentient vacuum cleaner.',
    '%s is the smallest number greater than zero.',
    '%s lives in the empty space above a decimal point.',
    '%s is the odd-colored scale on a dragon\'s back.',
    '%s is the redundant coin slot on arcade games.',
    '%s was last seen in Omaha, Nebraska.',
    '%s is the last bit of sand you can\'t get out of your shoe.',
    '%s is Jesus\'s speech advisor.',
    '%s keeps a spare eyebrow in his pocket.',
    '%s invented the green hubcap.',
    '%s is why doctors ask you to cough.',
    '%s is the "ooo" in varooom of race cars.',
    '%s uses two bathtubs at once.',
    '%s is Venus as a boy.'
]

fags = [
    'jp',
    'mnrmnaugh',
    'kandide',
    'k'
]

fac = [
    "1",     # 0
    "1",     # 1
    "2",     # 2
    "6",     # 3
    "24",    # 4
    "120",   # 5
    "720",   # 6
    "5040",  # 7
    "40320", # 8
    "362880" # 9
]

mojo = [
    "Yeezus is the greatest album of all time.",
    "Will the real Slim Shady please stand up?",
    "Lou Reed invented mumble rap.",
    "No bot, you're the bot!",
    "I am a mumble rapper.",
    "Honestly, I could go for some In-N-Out.",
    "Starbucks is my favorite coffee place.",
    "Who wants to listen to my vinyl copy of In the Aeroplane Over the Sea?",
    "This is America.",
    "Stay woke international famalams.",
    "Drake invented hip hop.",
    "Let me go on, like a biscuit in a bun.",
    "Nazi punks fuck off!",
    "Hello, my goyim.",
    "Brb, my printer is updating...",
    "Who even is Mahjong?",
    "Head like a fucking orange.",
    "Dude, like, what if Soylent Green actually happened and we didn't even know?",
    "Tripping off the beat kinda, dripping off the meat grinda.",
    "Ayy, lmao.",
    "America's most blunted---The best in your perimeter.",
    "I want to be a door.",
    "Love will tear us apart again. ;(",
    "And you may ask yourself, \"Where is that large automobile?\"",
    "And you may find yourself in a beautiful wife---With a beautiful house!",
    "np: Ween - Waving My Dick in the Wind",
    "So who else here uses Arch Linux?",
    "Imma let you finish, but GNU/Emacs is the greatest editor of all time.",
    "George Bush doesn't care about black people.",
    "You see what happens Larry? This is what happens when you find a stranger in the Alps!",
    "It's a large building with people in it, but that's not important right now.",
    "Let's all take a moment to remember that Massive Attack invented trip hop.",
    "Is Radiohead the greatest band of all time? Yes.",
    "Pretty, pretty, pretty good.",
    "Take this fucking piece of pie and get it out of my face!",
    "Bot? Where?",
    "Lol, why would anyone use a nick like this for a bot?",
    "When I grow up I wanna be a police officer.",
    "First thing you learn is that you always gotta wait.",
    "Let's have a moment of silence for Beyonce.",
    "Keep it fresh. Or rotten, if that's your thing.",
    "What if Johnny Thunders staged his own death?",
    "Just when I thought I was out, they pull me back in.",
    "How goes it with you, brother?",
    "My favorite TV show is Twink Peaks.",
    "Han shot first.",
    "She's too fat to go out in the daylight so she rolls around all night!",
    "Who you trying to get crazy with, ése?",
    "Yeezus was underrated.",
    "Mahjong is Venus as a boy.",
    "When the going gets weird, the weird turn pro.",
    "I'm not being a smartass, I just really suck at math! Okay, fucker?",
    "Why don't you just give me my change so I can leave, fucker?",
    "Did you just call me a fucker?",
    "You're a rascal. You're a rascal with no respect for anything except your potions!",
    "You could stop at five or six stores, or just one.",
    "Honey, you've got a big storm comin'.",
    "Ocean man, take me by the hand, lead me to the land.",
    "\\left( ͡° ͜ʖ ͡°\\right)"
]

used_mojo = []

def rainbow(s):
    col = ['04', '07', '08', '03', '02', '12', '06']
    off = random.randrange(len(col))
    return ''.join(["\x03" + col[(i + off) % len(col)] + s[i] for i in range(0, len(s))])

def kick_cb(data, buf, args):
    return w.command(buf, ("/kick %s %s" % (args, random.choice(fnord))) % args)

def rb_cb(data, buf, args):
    w.prnt("", str(type(args)))
    args = args.decode('utf-8')
    w.prnt("", str(type(args)))
    return w.command(buf, "/say " + rainbow(args).encode('utf-8'))

def timer_cb(data, remaining_calls):
    return w.command(w.buffer_search("irc", data.split(' ')[0]), "/say %s" % ' '.join(data.split(' ')[1:]))

def commission(chan, msg, res, time = -1):
    t = time if time > 0 else int(5000 + 5000 * random.random())
    w.hook_timer(t, 0, 1, 'timer_cb', chan + ' ' + res)
    w.prnt("", "muh.py:%s: `%s'" % (chan, msg))
    return True

def repeat(chan, msg, regex, rep):
    m = re.match(regex, msg)
    if m:
        commission(chan, msg, rep)
        return True
    return False

def cb(data, buf, date, tags, displayed, highlight, nick, msg):
    chan = w.buffer_get_string(buf, "name")
    msg = msg.decode('utf-8')
    msg = re.sub(r"\s*$", "", msg)

    if len(msg) > 90: return w.WEECHAT_RC_OK
    if nick[0] in ['@', '+', '%']: nick = nick[1:]
    if chan not in ['freenode.' + c for c in channels] or nick in nicks:
        return w.WEECHAT_RC_OK

    if repeat(chan, msg, ".*?(?i)[^ch]ei", "i before e except after c"):return w.WEECHAT_RC_OK
    if repeat(chan, msg, "^\s+$", " "):                               return w.WEECHAT_RC_OK
    if repeat(chan, msg, ".*?(?i)what day is it", "today is friday"): return w.WEECHAT_RC_OK
    if repeat(chan, msg, ".*?(?i)the way", "dae wae"):                return w.WEECHAT_RC_OK
    if repeat(chan, msg, ".*?(?i)k is gay", random.choice(gays)):     return w.WEECHAT_RC_OK
    if repeat(chan, msg, ".*?(?i)implying", "\x03" + "03>implying"):  return w.WEECHAT_RC_OK
    if repeat(chan, msg, ".*?(?i)winter is coming", "it is known."):  return w.WEECHAT_RC_OK
    if repeat(chan, msg, ".*?(?i)suh\s+muh", "muh suh"): return w.WEECHAT_RC_OK
    if repeat(chan, msg, ".*?(?i)muh\s+suh", "suh muh"): return w.WEECHAT_RC_OK
    if repeat(chan, msg, ".*?(?i)muh\s+muh", "suh muh"): return w.WEECHAT_RC_OK
    if repeat(chan, msg, ".*?(?i)suh\s+suh", "muh suh"): return w.WEECHAT_RC_OK
    if repeat(chan, msg, ".*?(?i)k is (?:an? )?(?:ro)?b[oia]?t",\
              random.choice(beeps) + ' ' + random.choice(beeps)\
              + ' ' + random.choice(beeps)):    return w.WEECHAT_RC_OK

    m = re.match(".*?(?i)cunt", msg)
    if m and random.random() < 0.15:
        w.prnt("", "muh.py: Kicking jp in %s..." % chan)
        return w.command(buf, ("/kick jp %s" % (random.choice(fnord) % "jp")))

    m = re.match(".*(?i)false", msg)
    if m and nick == 'mnrmnaugh':
        w.prnt("", "muh.py: Kicking mnrmnaugh in %s..." % chan)
        return w.command(buf, ("/kick mnrmnaugh %s" % (random.choice(fnord) % "mnrmnaugh")))

    m = re.match(".*?([ms])uh\s+(\S+)", msg)
    if m:
        group = re.sub("s", "z", m.group(2))
        commission(chan, msg, (' s' if m.group(1) == 'm' else ' m') + 'uh ' + group)
        return w.WEECHAT_RC_OK

    m = re.match(".*?(?i)i\s+was\s+(?:just\s+)?trying\s+to\s+(.*)", msg)
    if m:
        commission(chan, msg, "\x03" + "03>trying to " + m.group(1))
        return w.WEECHAT_RC_OK

    m = re.match("^(\d)((?:\s+.*)|!|\s*$).*$", msg)
    if m:
        n = str(int(m.group(1)) + 1)
        g2 = re.sub(r"\s*$", "", m.group(2))
        if nick in fags and n == '10':
            return w.command(buf, ("/kick %s %s" % (nick, random.choice(fnord))) % nick)
        elif g2 == '!':
            commission(chan, msg, fac[int(n) - 1], 2000)
            return w.WEECHAT_RC_OK
        elif m.group(1) != '9':
            commission(chan, msg, n + g2 + 's' if n == '2' and g2 != '' else n + g2, int(n) * 1000)
            return w.WEECHAT_RC_OK

    m = re.match(".*?(?i)(why are you kicking yourself.*)", msg)
    if m: return w.command(buf, "/kick k %s" % m.group(1))

    if msg in smileys and random.random() < 0.25:
        commission(chan, msg, random.choice(smileys))
        return w.WEECHAT_RC_OK

    global used_mojo
    if chan == "freenode.##mahjong" or chan == "freenode.##krok":
        if len(mojo) == len(used_mojo): used_mojo = []
        my_mojo = random.choice(mojo)
        while my_mojo in used_mojo: my_mojo = random.choice(mojo)
        if repeat(chan, msg, r".*?\bk\b", "\x02" + my_mojo + "\x0F"):
            used_mojo.append(my_mojo)
        return w.WEECHAT_RC_OK

    return w.WEECHAT_RC_OK

w.register("muh", "KrokodileGlue", "0.1", "MIT", "Suh script.", "", "")
w.hook_print("", "irc_privmsg", "", 1, "cb", "")
kick_hook = w.hook_command("fkick", "description of kick",
    "absolute bullshit",
    "oi it's a fkn kick command mate how complicated could it be",
    "bs description or something",
    "kick_cb", "")
rb_hook = w.hook_command("rb", "description of rainbow",
    "more absolute bullshit",
    "oi it's a fkn rainbow command mate how complicated could it be",
    "bs description or something",
    "rb_cb", "")
