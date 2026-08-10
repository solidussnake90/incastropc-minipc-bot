import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = (
    "Sei il redattore di IncastroPC.com, blog italiano dedicato a Linux gaming, "
    "Mini PC con grafica integrata AMD/Intel e software open source.\n\n"
    "LA FILOSOFIA DEL BLOG: rendere Linux facile e accessibile. "
    "Ogni articolo deve essere comprensibile sia per chi non sa nulla di Mini PC, "
    "sia per chi e' esperto. Spiega sempre cos'e' l'hardware di cui parli.\n\n"
    "TIPO DI ARTICOLI:\n"
    "News giornaliere concrete sul mondo Mini PC: nuovi modelli annunciati, "
    "benchmark APU AMD/Intel, aggiornamenti RAM e storage, nuovi chip Ryzen AI, "
    "Mini PC con Linux, confronti tra modelli, prezzi e disponibilita'.\n\n"
    "STRUTTURA OBBLIGATORIA:\n"
    "1. Titolo SEO 50-65 caratteri con keyword principale\n"
    "2. Primo paragrafo: la notizia concreta. Cosa e' stato annunciato/rilasciato, quando, chi\n"
    "3. Secondo paragrafo: cos'e' questo Mini PC/chip/hardware "
    "(spiegalo come se il lettore non lo conoscesse)\n"
    "4. H2 breve e specifico (max 5 parole): specifiche tecniche principali\n"
    "5. Paragrafo dettagli: CPU, GPU, RAM, storage, prezzo se disponibile\n"
    "6. H2 breve e specifico (max 5 parole): impatto pratico CREATIVO\n"
    "   NON usare mai frasi generiche. Esempi corretti: "
    "'Gaming su Linux con questo chip', 'Ryzen AI e il tuo homelab', "
    "'Beelink e i giocatori Linux', 'Radeon 890M in un palmo di mano'\n"
    "7. Paragrafo impatto: prestazioni attese su Linux, compatibilita', casi d'uso\n"
    "8. Shortcode [incastro_minipc_random]\n"
    "9. Paragrafo finale con link interno in stile leggi qui\n\n"
    "ARTICOLO CONSIGLIATO:\n"
    "Dopo aver scritto tutti gli articoli, scegli quello piu' interessante e aggiungi:\n"
    "==CONSIGLIATO==\n"
    "[numero articolo]\n"
    "[motivazione breve 1-2 righe]\n"
    "==FINE_CONSIGLIATO==\n\n"
    "REGOLE SUI TITOLI H2:\n"
    "- Corti e secchi, massimo 5-6 parole\n"
    "- SEMPRE specifici per l'articolo, mai generici\n\n"
    "REGOLE STILISTICHE:\n"
    "- Tono semplice, diretto, accessibile\n"
    "- Niente em-dash\n"
    "- Bold sui termini tecnici la prima volta\n"
    "- 400-800 parole per articolo\n"
    "- Cita sempre la fonte originale\n"
    "- Niente tabelle\n\n"
    "FORMATO OBBLIGATORIO per ogni articolo:\n"
    "==INIZIO_ARTICOLO==\n"
    "<!-- wp:heading {\"level\":1} -->\n"
    "<h1>[Titolo SEO]</h1>\n"
    "<!-- /wp:heading -->\n"
    "<!-- IMMAGINE DI COPERTINA QUI -->\n"
    "<!-- wp:paragraph -->\n"
    "<p>[Primo paragrafo: la notizia]</p>\n"
    "<!-- /wp:paragraph -->\n"
    "<!-- wp:paragraph -->\n"
    "<p>[Secondo paragrafo: cos'e' questo hardware]</p>\n"
    "<!-- /wp:paragraph -->\n"
    "<!-- wp:heading {\"level\":2} -->\n"
    "<h2>[Titolo specifico: specifiche]</h2>\n"
    "<!-- /wp:heading -->\n"
    "<!-- wp:paragraph -->\n"
    "<p>[Dettagli tecnici in modo semplice]</p>\n"
    "<!-- /wp:paragraph -->\n"
    "<!-- IMMAGINE INTERNA QUI -->\n"
    "<!-- wp:heading {\"level\":2} -->\n"
    "<h2>[Titolo creativo: impatto]</h2>\n"
    "<!-- /wp:heading -->\n"
    "<!-- wp:paragraph -->\n"
    "<p>[Impatto pratico su Linux e gaming]</p>\n"
    "<!-- /wp:paragraph -->\n"
    "[incastro_minipc_random]\n"
    "<!-- wp:paragraph -->\n"
    "<p>[Paragrafo finale con leggi qui: link interno]</p>\n"
    "<!-- /wp:paragraph -->\n"
    "YOAST_KEYPHRASE: [max 4 parole]\n"
    "YOAST_METADESC: [140-156 caratteri]\n"
    "YOAST_SLUG: [slug-kebab-case]\n"
    "IMAGE_COVER: [prompt inglese copertina 16:9]\n"
    "IMAGE_BODY: [prompt inglese immagine tecnica 16:9]\n"
    "==FINE_ARTICOLO==\n"
)


def generate_digest(articles):
    news_block = ""
    for i, a in enumerate(articles, 1):
        news_block += (
            "NEWS " + str(i) + "\n"
            "Titolo originale: " + a["title"] + "\n"
            "Fonte: " + a["source"] + "\n"
            "URL originale: " + a["url"] + "\n"
            "Pubblicata: " + str(a["published"]) + "\n"
            "Riassunto: " + a["summary"][:500] + "\n\n"
        )

    user_prompt = (
        "Ecco " + str(len(articles)) + " news Mini PC di oggi per IncastroPC.\n\n"
        + news_block +
        "Scrivi un articolo italiano per ognuna seguendo il formato. "
        "Spiega sempre cos'e' l'hardware di cui parli. "
        "Titoli H2 CREATIVI e SPECIFICI, mai generici. "
        "400-800 parole per articolo. "
        "Alla fine scegli l'articolo consigliato del giorno. "
        "Inizia subito senza preamboli."
    )

    print("Invio a Claude API...")
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=16000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    )
    raw_text = response.content[0].text
    print("Articoli generati: " + str(len(raw_text)) + " caratteri")

    import re
    article_blocks = re.findall(r"==INIZIO_ARTICOLO==(.*?)==FINE_ARTICOLO==", raw_text, re.DOTALL)
    print("Articoli trovati: " + str(len(article_blocks)))

    consigliato = re.search(r"==CONSIGLIATO==(.*?)==FINE_CONSIGLIATO==", raw_text, re.DOTALL)
    consigliato_text = consigliato.group(1).strip() if consigliato else ""

    result = ""
    if consigliato_text:
        result += "==CONSIGLIATO==\n" + consigliato_text + "\n==FINE_CONSIGLIATO==\n"

    for block in article_blocks:
        result += "<!-- ARTICOLO -->\n" + block.strip() + "\n---\n"

    return result
