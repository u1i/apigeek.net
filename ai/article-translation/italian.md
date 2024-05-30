# Il Risveglio della Forza dell'AI

Ricordate quando il GPT di OpenAI era la scelta predefinita per la maggior parte dei progetti di AI? Ora, il panorama dell'AI è stato stravolto in pochi mesi, con giganti della tecnologia come Meta, Microsoft, Databricks e Apple che hanno rilasciato i propri modelli aperti. Vediamo come questa nuova era di scelta e accessibilità sta cambiando il modo in cui costruiamo applicazioni intelligenti, perché non esiste una soluzione unica per tutti e come è possibile navigare in questo panorama in rapida evoluzione per trovare l'approccio migliore che si adatti alle vostre esigenze.

Fino alla fine dell'anno scorso, se mi avessero chiesto di costruire applicazioni intelligenti utilizzando l'AI, avrei ammesso con riluttanza che il GPT di OpenAI era probabilmente l'unica opzione praticabile all'epoca. Era come avere una cassetta degli attrezzi con un solo strumento, o diciamo molti strumenti potenti, ma tutti della stessa marca, con le stesse limitazioni e peculiarità. Conosco a fondo la famiglia GPT, avendo lavorato con GPT-2, GPT-3 e tutte le varianti .5 e turbo. Non fraintendetemi, sono fantastici, ma come ho detto, sono tutti di una sola azienda. Ho già scritto in precedenza sulla necessità di un piano B. Cosa succede quando l'API del vostro modello di linguaggio di grandi dimensioni viene improvvisamente deprecata e sostituita con una nuova?

## Rivoluzione dei Modelli di AI: Emerge un Ecosistema Diversificato

Ma poi, in pochi mesi, tutto è cambiato. Anthropic e Google hanno rilasciato modelli di AI avanzati quasi altrettanto capaci di quelli di OpenAI. Ancora più significativo, giganti della tecnologia come Meta, Apple e Microsoft hanno reso open source i loro modelli e li hanno resi disponibili per il download. Ciò significa che potete eseguirli sulla vostra infrastruttura invece di accedervi solo tramite API, cosa che alcuni non gradiscono poiché implica l'invio dei vostri dati verso l'ignoto.

Improvvisamente, la mia cassetta degli attrezzi era piena di nuovi strumenti luccicanti, ognuno con le proprie caratteristiche e capacità uniche, e il panorama dei modelli di AI si era trasformato in un ecosistema diversificato. Alcuni di questi nuovi modelli aperti, come Llama 3, sono ora potenti quanto il GPT di solo 1,5 anni fa e alcuni, incredibilmente, potrebbero persino funzionare sul mio MacBook Air! Era come guardare un mondo in bianco e nero esplodere improvvisamente a colori mentre l'AI diventava più accessibile e versatile che mai. Diamo un'occhiata ad alcuni dei rilasci più importanti degli ultimi mesi.

## Recenti Progressi nei Grandi Modelli di Linguaggio

* Google Gemini (6 dicembre 2023): La lineup di modelli avanzati di Google, incluse le versioni 1.0, 1.5 (Pro e Ultra) con finestre di contesto fino a 1 milione di token - ho lavorato parecchio con questi e mi piace davvero come si stanno evolvendo.

* Mixtral di Mistral (11 dicembre 2023): rilascio di Mixtral 8x7B, un modello di mistura di esperti sparsi (SMoE) di alta qualità con pesi aperti che eguaglia o supera GPT3.5 sulla maggior parte dei benchmark standard. Fino a quel momento non avevo esplorato molto i modelli Mistral.

* Gemma di Google (21 febbraio 2024): Una famiglia di modelli aperti leggeri e all'avanguardia costruiti sulla stessa ricerca e tecnologia dei modelli Gemini di Google, rendendo l'AI avanzata più accessibile agli sviluppatori. Sono modelli notevolmente piccoli e quando li ho provati, ho realizzato che per alcuni casi d'uso, abbiamo davvero solo bisogno di un motore che possa comprendere il linguaggio e interagire con gli utenti. Ora, possiamo avere quelle capacità integrate in un software che posso eseguire sulla mia macchina e non ho bisogno di dipendere da OpenAI.

* Anthropic Claude 3 (4 marzo 2024): Le ultime offerte di Anthropic includono Haiku, Sonnet e Opus, e ho avuto la fortuna di avere accesso alla ricerca su questi modelli per un po' di tempo ormai. Secondo me, sono le alternative più potenti ai modelli di OpenAI al momento. Soprattutto Opus si sente caldo, coinvolgente ed è un modello incredibile per costruire personalità digitali che possono impegnarsi in conversazioni intellettuali profonde e mostrare capacità di ragionamento avanzate.

* Grok di X (rilasciato il 18 marzo 2024): Annunciato come un "modello di linguaggio open source", l'azienda ha rilasciato solo i pesi al pubblico, senza codice o molta documentazione, lasciando molti sviluppatori incerti sulle sue reali capacità e usabilità. Mi piacerebbe provarlo, ma al momento è troppo grande per essere eseguito sul mio hardware o sul cloud.

* MM1 di Apple (rilasciato il 19 marzo 2024): un grande modello di linguaggio multimodale che indica chiaramente il fatto che Apple sta prendendo l'AI molto sul serio. Non ho ancora avuto l'opportunità di provarlo.

* DBRX di Databricks (27 marzo 2024): Un modello aperto che introduce un'architettura di mistura di esperti a grana fine (MoE), ottenendo prestazioni impressionanti con meno parametri rispetto a GPT. Questo potrebbe essere molto interessante per le aziende enterprise, poiché dà loro la possibilità di eseguire potenti modelli di AI sulla propria infrastruttura. L'attenzione di Databricks alle esigenze aziendali come la conformità dei dati e la capacità di ottimizzare i modelli per casi d'uso specifici rende DBRX un'opzione attraente per molte imprese.

* Llama 3 di Meta (18 aprile 2024): L'ultimo modello aperto di Meta, addestrato su un enorme set di dati e che offre prestazioni paragonabili a quelle di GPT di solo 1,5 anni fa. Sono molto, molto impressionato dalla qualità dell'output, da come reagisce ai prompt personalizzati e da quanto sia versatile e utilizzabile. Certo, avevo visto LLama 2 prima ma non l'avevo usato molto. Facebook, WhatsApp e Instagram ora hanno capacità integrate alimentate da LLama 3. Quando si pensa a quanto sia un enorme problema per le aziende di AI ottenere dati freschi per addestrare i loro modelli in questo momento, si consideri quanti miliardi di utenti hanno queste piattaforme. Meta è in un'ottima posizione. L'apprendimento per rinforzo con feedback umano è la chiave per rendere i modelli di AI più intelligenti e creare la prossima generazione.

* Phi-3 di Microsoft (23 aprile 2024): Una famiglia di piccoli modelli di linguaggio (SLM) progettati per efficienza e prestazioni, particolarmente adatti per l'edge computing e scenari offline. Ho apprezzato il mio primo set di interazioni con i modelli Phi-3 e credo che troveranno una forte nicchia nelle applicazioni che danno priorità a velocità, privacy e capacità del dispositivo rispetto alla potenza grezza.

Questa timeline mostra il rapido ritmo dell'innovazione e la crescente diversità del panorama dei modelli di AI in pochi mesi. Ogni rilascio porta nuove capacità, architetture e potenziali casi d'uso, offrendo agli sviluppatori e alle aziende una ricchezza di opzioni tra cui scegliere.

## OpenAI e l'Ascesa di Architetture AI più Efficienti

Ma dov'è OpenAI in tutto questo? L'azienda che gestisce l'ultra prominente ChatGPT e domina ancora la maggior parte del panorama dell'AI con i suoi modelli GPT è stata notevolmente assente dall'ondata di rilasci recenti (se si ignora l'annuncio di SORA per un momento). Mentre potrebbero lavorare su GPT-5 dietro le quinte, è chiaro che alcune delle architetture più recenti, in particolare quelle che utilizzano tecniche di mistura di esperti (MoE), stanno iniziando a sfidare il predominio di GPT.
Modelli come DBRX e Llama 3 hanno dimostrato che è possibile ottenere prestazioni impressionanti con meno parametri e architetture più efficienti. E il passaggio a modelli MoE, che possono fornire risultati migliori con requisiti infrastrutturali più piccoli, sta effettivamente mangiando il pranzo di OpenAI erodendo il vantaggio competitivo che GPT deteneva una volta.

Quindi, come navighiamo in questa nuova era di scelta e accessibilità dei modelli di AI per trovare la soluzione migliore per le nostre esigenze?

## Sfruttare la Diversità dei Modelli di AI

Mentre navighiamo in questa nuova era di scelta e accessibilità dei modelli di AI, è essenziale riconoscere che non esiste una soluzione unica per tutti. Proprio come i nostri cervelli impiegano sistemi diversi per vari compiti, che vanno dall'automatico e inconscio (come allacciarsi le scarpe) al deliberato e analitico (come risolvere un problema matematico complesso), possiamo sfruttare diversi modelli di AI per scopi specifici.

Nel suo libro "Pensieri lenti e veloci", lo psicologo Daniel Kahneman introduce il concetto di due sistemi distinti nelle nostre menti: il Sistema 1, che opera automaticamente e rapidamente, e il Sistema 2, che alloca l'attenzione ad attività mentali più impegnative. Possiamo applicare questo framework al mondo dei modelli di AI, utilizzando modelli più piccoli ed efficienti per attività che richiedono risposte rapide e risorse computazionali minime (simili al Sistema 1) e modelli più grandi e complessi per attività che richiedono un ragionamento e un'analisi più approfonditi (simili al Sistema 2).
Inoltre, possiamo combinare modelli che eccellono in compiti specifici per creare sistemi di AI potenti e sfaccettati.

Ad esempio, potremmo utilizzare un modello come Phi-3 per l'edge computing e scenari offline, Gemma per l'elaborazione leggera sui dispositivi e DBRX o Llama 3 per attività più complesse basate sul cloud. Comprendendo i punti di forza e di debolezza di ogni modello e combinandoli strategicamente, possiamo costruire applicazioni di AI più efficienti, efficaci e adattabili a una vasta gamma di casi d'uso.

## Potete Utilizzare un Approccio Flessibile e Informato

In definitiva, la chiave del successo in questo nuovo panorama è affrontare la selezione e l'implementazione dei modelli di AI con una mentalità flessibile e informata. Rimanendo aggiornati sugli ultimi sviluppi, sperimentando diversi modelli e considerando attentamente le esigenze e i vincoli specifici di ogni progetto, gli sviluppatori e le aziende possono sfruttare il potere di questa nuova era dell'AI evitando le insidie di un'eccessiva dipendenza da un singolo modello o fornitore.
È un momento entusiasmante per l'AI e, mentre andiamo avanti, abbracciamo la diversità e l'accessibilità del panorama dei modelli di AI, poiché questo rappresenta chiaramente un passo significativo in avanti nella democratizzazione e nell'avanzamento dell'intelligenza artificiale.Add to Co