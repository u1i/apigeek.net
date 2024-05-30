# Het Ontwaken van de AI-Kracht

Herinner je je nog dat OpenAI's GPT de standaardkeuze was voor de meeste AI-projecten? Nu is het AI-landschap in slechts een paar maanden op zijn kop gezet, met tech-giganten als Meta, Microsoft, Databricks en Apple die hun eigen open modellen uitbrengen. Laten we eens kijken hoe dit nieuwe tijdperk van keuze en toegankelijkheid de manier verandert waarop we slimme applicaties bouwen, waarom er geen one-size-fits-all oplossing is, en hoe je kunt navigeren in dit snel evoluerende landschap om de beste aanpak te vinden die bij jouw behoeften past.

Tot eind vorig jaar zou ik, als me werd gevraagd naar het bouwen van slimme applicaties met AI, met tegenzin hebben toegegeven dat OpenAI's GPT waarschijnlijk de enige haalbare optie was op dat moment. Het was alsof je een gereedschapskist had met maar één tool - of laten we zeggen veel krachtige tools, maar allemaal van hetzelfde merk, met dezelfde beperkingen en eigenaardigheden. Ik ben diepgaand bekend met de GPT-familie, na gewerkt te hebben met GPT-2, GPT-3, en alle .5 en turbo-varianten. Begrijp me niet verkeerd, ze zijn geweldig, maar zoals ik al zei, het is allemaal van één bedrijf. Ik heb eerder geschreven over de noodzaak van een plan B. Wat gebeurt er als je vertrouwde grote taalmodel API plotseling wordt uitgefaseerd en vervangen door een nieuwe?

## AI Model Revolutie: Een Divers Ecosysteem Ontstaat

Maar toen, in slechts een paar maanden, veranderde alles. Anthropic en Google hebben geavanceerde AI-modellen uitgebracht die bijna net zo capabel zijn als die van OpenAI. Nog belangrijker is dat tech-giganten zoals Meta, Apple en Microsoft hun modellen open source en beschikbaar hebben gemaakt om te downloaden. Dit betekent dat je ze op je eigen infrastructuur kunt draaien in plaats van er alleen via API toegang toe te krijgen, iets waar sommige mensen niet comfortabel mee zijn omdat het betekent dat je je gegevens naar het onbekende stuurt.

Plotseling zat mijn gereedschapskist vol met glimmende nieuwe tools, elk met zijn eigen unieke functies en mogelijkheden, en was het AI-modellandschap veranderd in een divers ecosysteem. Sommige van deze nieuwe open modellen, zoals Llama 3, zijn nu even krachtig als GPT van slechts 1,5 jaar geleden, en sommige konden, ongelooflijk genoeg, zelfs op mijn MacBook Air draaien! Het was alsof ik toekeek hoe een zwart-witte wereld plotseling explodeerde in kleur terwijl AI toegankelijker en veelzijdiger werd dan ooit tevoren. Laten we eens kijken naar enkele van de belangrijkste releases van de afgelopen maanden.

## Recente Ontwikkelingen in Grote Taalmodellen

* Google Gemini (6 december 2023): Google's geavanceerde modellenreeks, waaronder versies 1.0, 1.5 (Pro en Ultra) met contextvensters tot 1 miljoen tokens - ik heb veel met deze gewerkt en hou echt van hoe ze zich ontwikkelen.

* Mixtral van Mistral (11 december 2023): release van Mixtral 8x7B, een hoogwaardig sparse mixture of experts (SMoE) model met open gewichten dat overeenkomt met of beter presteert dan GPT3.5 op de meeste standaard benchmarks. Tot dat moment had ik de Mistral-modellen nog niet veel onderzocht.

* Gemma door Google (21 februari 2024): Een familie van lichtgewicht, state-of-the-art open modellen gebouwd op hetzelfde onderzoek en technologie als Google's Gemini-modellen, waardoor geavanceerde AI toegankelijker wordt voor ontwikkelaars. Het zijn opmerkelijk kleine modellen, en toen ik ze uitprobeerde, realiseerde ik me dat we voor sommige use cases echt alleen maar een engine nodig hebben die taal kan begrijpen en met gebruikers kan communiceren. Nu kunnen we die mogelijkheden ingebouwd hebben in software die ik op mijn eigen machine kan draaien, en heb ik OpenAI niet nodig.

* Anthropic Claude 3 (4 maart 2024): Anthropic's nieuwste aanbod omvat Haiku, Sonnet en Opus, en ik heb het geluk gehad om al enige tijd onderzoekstoegang te hebben tot deze modellen. Naar mijn mening zijn het op dit moment de krachtigste alternatieven voor OpenAI's modellen. Vooral Opus voelt warm, boeiend aan en is een ongelooflijk model voor het bouwen van digitale persoonlijkheden die zich kunnen mengen in diepgaande intellectuele gesprekken en geavanceerde redeneermogelijkheden vertonen.

* Grok door X (uitgebracht op 18 maart 2024): Aangekondigd als een "Open Source taalmodel", heeft het bedrijf alleen gewichten vrijgegeven aan het publiek, zonder code of veel documentatie, waardoor veel ontwikkelaars in het ongewisse blijven over de werkelijke mogelijkheden en bruikbaarheid. Ik zou het graag uitproberen, maar het is op dit moment veel te groot om op mijn eigen hardware of in de cloud te draaien.

* MM1 door Apple (uitgebracht op 19 maart 2024): een multimodaal groot taalmodel dat duidelijk aangeeft dat Apple AI zeer serieus neemt. Ik heb nog niet de kans gehad om het uit te proberen.

* DBRX door Databricks (27 maart 2024): Een open model dat een fijnkorrelige mixture-of-experts (MoE) architectuur introduceert, waarmee indrukwekkende prestaties worden bereikt met minder parameters dan GPT. Dit kan zeer interessant zijn voor enterprise bedrijven, omdat het hen de mogelijkheid geeft om krachtige AI-modellen op hun eigen infrastructuur te draaien. Databricks' focus op de behoeften van ondernemingen, zoals gegevenscompliance en de mogelijkheid om modellen af te stemmen op specifieke use cases, maakt DBRX een aantrekkelijke optie voor veel bedrijven.

* Llama 3 door Meta (18 april 2024): Meta's nieuwste open model, getraind op een enorme dataset en met prestaties die vergelijkbaar zijn met GPT van slechts 1,5 jaar geleden. Ik ben zeer, zeer onder de indruk van de kwaliteit van de output, hoe het reageert op aangepaste prompts, en hoe veelzijdig en bruikbaar het is. Natuurlijk had ik LLama 2 al eerder gezien maar niet veel gebruikt. Facebook, WhatsApp en Instagram hebben nu ingebouwde mogelijkheden aangedreven door LLama 3. Als je bedenkt hoe groot het probleem is voor AI-bedrijven op dit moment om verse gegevens te krijgen om hun modellen te trainen, bedenk dan hoeveel miljarden gebruikers deze platformen hebben. Meta bevindt zich in een geweldige positie. Reinforcement learning met menselijke feedback is de sleutel tot het slimmer maken van AI-modellen en het creëren van de volgende generatie.

* Phi-3 door Microsoft (23 april 2024): Een familie van kleine taalmodellen (SLM's) ontworpen voor efficiëntie en prestaties, bijzonder geschikt voor edge computing en offline scenario's. Ik genoot van mijn eerste reeks interacties met de Phi-3 modellen en ik geloof dat ze een sterke niche zullen vinden in applicaties die prioriteit geven aan snelheid, privacy en apparaatmogelijkheden boven ruwe kracht.

Deze tijdlijn toont het snelle innovatietempo en de toenemende diversiteit van het AI-modellenlandschap in slechts een paar maanden. Elke release brengt nieuwe mogelijkheden, architecturen en potentiële use cases met zich mee, waardoor ontwikkelaars en bedrijven een schat aan opties hebben om uit te kiezen.

# OpenAI en de Opkomst van Efficiëntere AI-Architecturen

Maar waar staat OpenAI in dit alles? Het bedrijf dat het ultra-prominente ChatGPT runt en nog steeds het grootste deel van het AI-landschap domineert met zijn GPT-modellen, was opvallend afwezig in de recente golf van releases (als je de SORA-aankondiging even negeert). Hoewel ze achter de schermen aan GPT-5 kunnen werken, is het duidelijk dat sommige van de nieuwere architecturen, met name die welke gebruik maken van mixture-of-experts (MoE) technieken, de suprematie van GPT beginnen uit te dagen.

Modellen als DBRX en Llama 3 hebben aangetoond dat het mogelijk is om indrukwekkende prestaties te bereiken met minder parameters en efficiëntere architecturen. En de verschuiving naar MoE-modellen, die betere resultaten kunnen opleveren met kleinere infrastructuurvereisten, eet effectief de lunch van OpenAI door het concurrentievoordeel dat GPT ooit had uit te hollen.

Dus - hoe navigeren we in dit nieuwe tijdperk van AI-modelkeuze en toegankelijkheid om de beste pasvorm voor onze behoeften te vinden?

# De Diversiteit van AI-Modellen Benutten

Terwijl we navigeren in dit nieuwe tijdperk van AI-modelkeuze en toegankelijkheid, is het essentieel om te erkennen dat er geen one-size-fits-all oplossing is. Net zoals onze hersenen verschillende systemen gebruiken voor verschillende taken, variërend van het automatische en onbewuste (zoals onze schoenen strikken) tot het weloverwogen en analytische (zoals het oplossen van een complex wiskundig probleem), kunnen we verschillende AI-modellen inzetten voor specifieke doeleinden.

In zijn boek "Ons feilbare denken" introduceert psycholoog Daniel Kahneman het concept van twee verschillende systemen in onze geest: Systeem 1, dat automatisch en snel werkt, en Systeem 2, dat aandacht besteedt aan meer inspannende mentale activiteiten. We kunnen dit raamwerk toepassen op de wereld van AI-modellen, waarbij we kleinere, efficiëntere modellen gebruiken voor taken die snelle reacties en minimale computationele middelen vereisen (vergelijkbaar met Systeem 1) en grotere, complexere modellen voor taken die diepere redenering en analyse vereisen (vergelijkbaar met Systeem 2).

Bovendien kunnen we modellen combineren die uitblinken in specifieke taken om krachtige, veelzijdige AI-systemen te creëren. We zouden bijvoorbeeld een model als Phi-3 kunnen gebruiken voor edge computing en offline scenario's, Gemma voor lichtgewicht on-device verwerking, en DBRX of Llama 3 voor meer complexe, cloudgebaseerde taken. Door de sterke en zwakke punten van elk model te begrijpen en ze strategisch te combineren, kunnen we AI-applicaties bouwen die efficiënter, effectiever en aanpasbaar zijn aan een breed scala van use cases.

## Je Kunt een Flexibele, Geïnformeerde Aanpak Gebruiken

Uiteindelijk is de sleutel tot succes in dit nieuwe landschap het benaderen van AI-modelselectie en -implementatie met een flexibele, geïnformeerde mindset. Door op de hoogte te blijven van de nieuwste ontwikkelingen, te experimenteren met verschillende modellen en zorgvuldig de specifieke behoeften en beperkingen van elk project te overwegen, kunnen ontwikkelaars en bedrijven de kracht van dit nieuwe AI-tijdperk benutten terwijl ze de valkuilen van overmatige afhankelijkheid van een enkel model of leverancier vermijden.

Het is een spannende tijd voor AI, en terwijl we vooruitgaan, laten we de diversiteit en toegankelijkheid van het AI-modellenlandschap omarmen, omdat dit duidelijk een significante stap voorwaarts vertegenwoordigt in de democratisering en vooruitgang van kunstmatige intelligentie.Add to Conversation