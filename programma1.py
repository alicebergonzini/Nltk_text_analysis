import sys
import nltk

#funzione che legge i file
def leggifiles(file0):  #parametro: file di interesse
    fileInput=open(file0, mode="r", encoding="utf-8")  #apro il file
    raw=fileInput.read()  #assegno il contenuto del file a una variabile
    return raw  #restituisco il contenuto del file

#funzione che tokenizza un corpus
def tokenizza(frasi):  #parametro: lista delle frasi del corpus
    tokens=[]  #lista vuota in cui andrò a inserire i token di ogni frase
    for frase in frasi:  #per ogni frase 
        token=nltk.word_tokenize(frase)  #tokenizzo la frase
        tokens=tokens+token  #aggiungo i token alla lista di token totali
    return tokens


#funzione che fra il PoStagging del corpus
def annota(frasi):  #parametro: lista delle frasi del corpus
    tokens=[]
    tokensPOS=[]  #lista vuote in cui andrò a inserire tutte le coppie token-PoS
    for frase in frasi: #per ogni frase
        token=nltk.word_tokenize(frase)  #tokenizzo frase
        tokens=tokens+token
        postoken=nltk.pos_tag(token)  #postaggo i token della frase
        tokensPOS=tokensPOS+postoken  #aggiungo i token pos taggati (coppie token PoS) alla lista
    return tokensPOS #restituisco la lista delle coppie token PoS

#funzione che confronta la lunghezza dei corpus e stampa i risultati
def confrontaToken(corpus1, corpus2):  #parametri: lunghezza dei corpus
    lungCorpus1=len(corpus1) #estraggo il numero di token
    lungCorpus2=len(corpus2)
    if lungCorpus1 > lungCorpus2:  #se la lunghezza del corpus 1 è maggiore della lunghezza del corpus 2
        print("Il primo corpus è più lungo del secondo corpus(più token)")
    elif lungCorpus1 < lungCorpus2:  #se la lunghezza del corpus 2 è maggiore della lunghezza del corpus 1
        print("Il secondo corpus è più lungo del primo corpus(più token)")
    else:
        print("I due corpus hanno lo stesso numero di token")
    print("Lunghezza del corpus 1:", lungCorpus1)
    print("Lunghezza del corpus 2:", lungCorpus2)
    print()


#funzione che confronta il numero di frasi contenuto nei corpus 
def confrontaFrasi(frasiC1, frasiC2):  #lista delle frasi di entrambi i corpus
    numfrasi1=len(frasiC1)  #estraggo il numero delle frasi
    numfrasi2=len(frasiC2) 
    if numfrasi1 > numfrasi2:  #confronta il numero delle frasi e stampo i risultati
        print("Il primo corpus ha più frasi del secondo corpus")
    elif numfrasi1 < numfrasi2:
        print("Il secondo corpus ha più frasi del primo corpus")
    else:
        print("I due corpus hanno lo stesso numero di frasi")
    print("Numero di frasi del corpus 1:", numfrasi1)
    print("Numero di frasi del corpus 2:", numfrasi2)
    print()

#funzione che calola la lunghezza media delle frasi
def calcolamediaF(frasi):
    cont=0  #contatore
    totalefrasi=len(frasi)  #estraggo il numero delle frasi
    for frase in frasi:  #per ogni frase contenuta nella lista frasi
        tokens=nltk.word_tokenize(frase)  #tokenizzo la frase
        lunghezzafrase=len(tokens)  #estraggo la lunghezza della frase
        cont=cont+lunghezzafrase  #la sommo alle altre lunghezze
    lunghezzamedia=cont/totalefrasi  #faccio la media, dividendo la somma delle lunghezza per il numero totale di frasi
    return lunghezzamedia   #restituisco la lunghezza media

def calcolamediaT(tokens):
    cont=0
    totaletoken=len(tokens)
    for token in tokens:
        lunghezzatoken=len(token)
        cont=cont+lunghezzatoken
    lunghezzamedia=cont/totaletoken
    return lunghezzamedia

#funzione che confronta le medie delle frasi e stampa i risultati
def confrontaMedieF(media1, media2):
    if media1 > media2:
        print("La lunghezza media delle frasi del corpus 1 è maggiore della lunghezza media delle frasi del corpus 2")
    elif media1 < media2:
        print("La lunghezza media delle frasi  del corpus 2 è maggiore della lunghezza media delle frasi  del corpus 1")
    else:
        print("La lunghezza media delle frasi dei due corpus è uguale")
    print("Lunghezza Media delle frasi del corpus 1:", media1)
    print("Lunghezza Media delle frasi del corpus 2:", media2)
    print()
    
#funzione che confronta le medie dei token e stampa i risultati
def confrontaMedieT(media1, media2):
    if media1 > media2:
        print("La lunghezza media dei token del corpus 1 è maggiore della lunghezza media dei token del corpus 2")
    elif media1 < media2:
        print("La lunghezza media dei token  del corpus 2 è maggiore della lunghezza media dei token  del corpus 1")
    else:
        print("La lunghezza media dei token dei due corpus è uguale")
    print("Lunghezza Media dei token del corpus 1:", media1)
    print("Lunghezza Media dei token del corpus 2:", media2)
    print()

#funzione che confronta i vocabolari e stampa i risultati
def confrontaV(V1, V2):
    if V1 > V2:
        print("il vocabolario del corpus 1 è più ricco del vocabolario del corpus2.")
    elif V2 > V1:
        print("il vocabolario del corpus 2 è più ricco del vocabolario del corpus1.")
    else:
        print("i vocabolari dei due corpus presentano lo stesso numero di parole tipo.")
    print("Grandezza del vocabolario del corpus 1:", V1)
    print("Grandezza del vocabolario del corpus 2:", V2)
    print()

#funzione che confronta le Type Token Ratio e ne stampa i risultati
def confrontaTTR(ttr1, ttr2):
    if ttr1 > ttr2:
        print("il primo corpus ha una Type Token Ratio più alta del secondo corpus.")
    elif ttr1 < ttr2:
        print("il secondo corpus ha una Type Token Ratio più alta del primo corpus.")
    else:
        print("i due corpus hanno Type Token Ratio uguale.")
    print("TTR del corpus 1:", ttr1)
    print("TTR del corpus 2:", ttr2)
    print()

#funzione che calcola le classi di frequenza all'aumentare del corpus
def calcolaCDF(corpus, frequenza):  #parametri: lista token e classe di frequenza che vogliamo calcolare (n come classe di frequenza n)
    i=500 #inizializzo l'indice i a 500 token
    while i<len(corpus): #finché i è minore della lunghezza del corpus
        cardCDF=0  #inizializzo la cardinalità della classe di frequenza a 0
        corpusRIF=corpus[:i]  #assegno a una variabile il corpus da 0 a i token
        vocabRIF=list(set(corpusRIF))  #calcolo il vocabolario del corpus da 0 a i token
        for token in vocabRIF:  #per ogni token nel vocabolario del corpus da 0 a i token
            freq=corpusRIF.count(token)  #conto le occorrenze del token nel corpus da 0 a i token
            if freq==frequenza:  #se la frequenza è uguale al numero che abbiamo passato come parametro
                cardCDF=cardCDF+1  #aggiungo uno alla variabile che mi conta la cardinalità della classe di frequenza
        #stampo i risultati
        print("Corpus=", i)
        print("Numero di parole con frequenza", frequenza, "=", cardCDF, "\n")
        #incremento di 500
        i=i+500

#funzione che mi calcola la media di sostantivi nelle frasi
def calcolaMediaSostantiviFrasi(listafrasi):  #parametro: lista delle frasi
    poscorrette=["NN", "NNPS", "NNP", "NNS"]  #creo una lista con i tag che identificano i sostantivi nel PoStagging
    totalePOS=0  #variabile che somma il numero sostantivi trovati in ogni frase
    for frase in listafrasi: #per ogni frase nella lista delle frasi
        contapos=0  #variabile che conta i sostantivi in una frase
        posFrase=[]  #creo una lista che conterrà le PoS di tutti i token della frase
        frasetokenizzata=nltk.word_tokenize(frase)  #tokenizzo la frase
        frasepostaggata=nltk.pos_tag(frasetokenizzata)  #postaggo la frase
        for bigramma in frasepostaggata:  #per ogni bigramma nella frase annotata
            posFrase.append(bigramma[1])  #aggiungo il secondo elemento del bigramma(ovvero la PoS) alla mia lista contente le PoS della fras
        for pos in posFrase:  #per ogni PoS nella lista posFrase
            if pos in poscorrette:  #se la PoS(l'etichetta) è contenuta nella lista dei tag dei sostantivi
                contapos=contapos+1  #aggiungo uno al contatore dei sostantivi
        totalePOS=totalePOS+contapos  #sommo il tutto
    mediapos=totalePOS/len(listafrasi)  #divido la somma per il numero delle frasi ottenendo così la media
    return mediapos  #resituisco la media

#funzione che mi calcola la media di verbi nelle frasi
#uguale a quella sopra 
def calcolaMediaVerbiFrasi(listafrasi):  
    poscorrette=["VB", "VBD", "VBG", "VBN", "VBP", "VBZ", ]  #cambia solo la lista dei tag, in quanto cerchiamo i verbi
    totalePOS=0
    for frase in listafrasi:
        contapos=0
        posFrase=[]
        frasetokenizzata=nltk.word_tokenize(frase)
        frasepostaggata=nltk.pos_tag(frasetokenizzata)
        for bigramma in frasepostaggata:
            posFrase.append(bigramma[1])
        for pos in posFrase:
            if pos in poscorrette:
                contapos=contapos+1
        totalePOS=totalePOS+contapos
    mediapos=totalePOS/len(listafrasi)
    return mediapos

#funzione che conta tutti gli aggettivi nel corpus
def contaAggettivi(corpusPoSTaggato): #parametro: il testo annotato con le parti del discorso
    tagAggettivi=["JJ", "JJR", "JJS"]  #lista con tutti i tag che identificano gli aggettivi
    totaleAggettivi=0  #contatore di aggettivi
    for bigramma in corpusPoSTaggato:  #per ogni bigramma(coppia token-PoS) nel testo annotato
        if bigramma[1] in tagAggettivi:  #se il secondo elemento del bigramma è contenuto nella lista dei tag degli aggettivi
            totaleAggettivi=totaleAggettivi+1  #aggiungo uno al contatore degli aggettivi
    return totaleAggettivi #restituisco il numero totale di aggettivi nel corpus

#le 4 funzioni seguenti sono uguali, cambiano solo le liste con i tag che identificano le PoS

def contaSostantivi(corpusPoSTaggato):
    tagSostantivi=["NN", "NNPS", "NNP", "NNS"]
    totaleSostantivi=0
    for bigramma in corpusPoSTaggato:
        if bigramma[1] in tagSostantivi:
            totaleSostantivi=totaleSostantivi+1
    return totaleSostantivi

def contaVerbi(corpusPoSTaggato):
    tagVerbi=["VB", "VBD", "VBG", "VBN", "VBP", "VBZ" ]
    totaleVerbi=0
    for bigramma in corpusPoSTaggato:
        if bigramma[1] in tagVerbi:
            totaleVerbi=totaleVerbi+1
    return totaleVerbi

def contaAvverbi(corpusPoSTaggato):
    tagAvverbi=["RB", "RBR", "RBS"]
    totaleAvverbi=0
    for bigramma in corpusPoSTaggato:
        if bigramma[1] in tagAvverbi:
            totaleAvverbi=totaleAvverbi+1
    return totaleAvverbi

def contaPunteggiatura(corpusPoSTaggato):
    tagPunteggiatura=[",", "."]
    totale=0
    for bigramma in corpusPoSTaggato:
        if bigramma[1] in tagPunteggiatura:
            totale=totale+1
    return totale

#funzione principale
def main(testo1, testo2):
    #chiamo le funzioni per ottenere le informazioni di interesse
    corpus1=leggifiles(testo1)
    corpus2=leggifiles(testo2)
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    frasi1=sent_tokenizer.tokenize(corpus1)
    frasi2=sent_tokenizer.tokenize(corpus2)
    alltokens1=tokenizza(frasi1)
    alltokens2=tokenizza(frasi2)
    alltokensPOS1=annota(frasi1)
    alltokensPOS2=annota(frasi2)
    vocab1=list(set(alltokens1))
    vocab2=list(set(alltokens2))
    TTR1=len(vocab1)/len(alltokens1) 
    TTR2=len(vocab2)/len(alltokens2)
    #stampo risultati ottenuti
    print("Lunghezza in token:")
    confrontaToken(alltokens1, alltokens2)
    print("Lunghezza in frasi:")
    confrontaFrasi(frasi1, frasi2)
    mediaFrasi1=calcolamediaF(frasi1)
    mediaFrasi2=calcolamediaF(frasi2)
    print("Lunghezza media delle frasi:")
    confrontaMedieF(mediaFrasi1, mediaFrasi2)
    mediaToken1=calcolamediaT(alltokens1)
    mediaToken2=calcolamediaT(alltokens2)
    print("Lunghezza media dei token:")
    confrontaMedieT(mediaToken1, mediaToken2)
    print("Ricchezza del vocabolario:")
    confrontaV(len(vocab1), len(vocab2))
    print("Indice di ricchezza lessicale(TTR):")
    confrontaTTR(TTR1, TTR2)
    print("----------------------------------------------------------------------------------\n")
    print("Distribuzione delle classi di frequenza del corpus 1 all'aumentare del corpus:\n")
    print("----------------Classe di frequenza V1----------------\n")
    calcolaCDF(alltokens1, 1)
    print("----------------Classe di frequenza V5----------------\n")
    calcolaCDF(alltokens1, 5)
    print("----------------Classe di frequenza V10----------------\n")
    calcolaCDF(alltokens1, 10)
    print("----------------------------------------------------------------------------------\n")
    print("Distribuzione delle classi di frequenza del corpus 2 all'aumentare del corpus:\n")
    print("----------------Classe di frequenza V1----------------\n")
    calcolaCDF(alltokens2, 1)
    print("----------------Classe di frequenza V5----------------\n")
    calcolaCDF(alltokens2, 5)
    print("----------------Classe di frequenza V10----------------\n")
    calcolaCDF(alltokens2, 10)
    mediaSostantiviFrasi1=calcolaMediaSostantiviFrasi(frasi1)
    mediaSostantiviFrasi2=calcolaMediaSostantiviFrasi(frasi2)
    mediaVerbiFrasi1=calcolaMediaVerbiFrasi(frasi1)
    mediaVerbiFrasi2=calcolaMediaVerbiFrasi(frasi2)
    print("----------------------------------------------------------------------------------")
    print("Media di sostantivi per frase:")
    #confronto le medie dei sostantivi per frase nei corpus
    if mediaSostantiviFrasi1>mediaSostantiviFrasi2:
        print("La media di sostantivi per frase è più alta nel corpus 1.")
    elif mediaSostantiviFrasi1==mediaSostantiviFrasi2:
        print("La media di sostantivi per frase è uguale per entrambi i corpus.")
    else:
        print("La media di sostantivi per frase è più alta nel corpus 2.")
    print("la media di sostantivi nelle frasi del corpus 1 è:", mediaSostantiviFrasi1)
    print("la media di sostantivi nelle frasi del corpus 2 è:", mediaSostantiviFrasi2)
    print()
    print("Media di verbi per frase:")
    #confronto le medie dei verbi per frase nei corpus
    if mediaVerbiFrasi1>mediaVerbiFrasi2:
        print("La media di verbi per frase è più alta nel corpus 1.")
    elif mediaVerbiFrasi1==mediaVerbiFrasi2:
        print("La media di verbi per frase è uguale per entrambi i corpus.")
    else:
        print("La media di verbi per frase è più alta nel corpus 2.")
    print("la media di verbi nelle frasi del corpus 1 è:", mediaVerbiFrasi1)
    print("la media di verbi nelle frasi del corpus 2 è:", mediaVerbiFrasi2)
    numeroAggettivi1=contaAggettivi(alltokensPOS1)
    numeroAggettivi2=contaAggettivi(alltokensPOS2)
    numeroSostantivi1=contaSostantivi(alltokensPOS1)
    numeroSostantivi2=contaSostantivi(alltokensPOS2)
    numeroVerbi1=contaVerbi(alltokensPOS1)
    numeroVerbi2=contaVerbi(alltokensPOS2)
    numeroAvverbi1=contaAvverbi(alltokensPOS1)
    numeroAvverbi2=contaAvverbi(alltokensPOS2)
    numeroPunteggiatura1=contaPunteggiatura(alltokensPOS1)
    numeroPunteggiatura2=contaPunteggiatura(alltokensPOS2)
    lungCorpusNoPunteggiatura1=len(alltokens1)-numeroPunteggiatura1
    lungCorpusNoPunteggiatura2=len(alltokens2)-numeroPunteggiatura2
    #calcolo le densità lessicali
    densitaLessicale1=(numeroAggettivi1 + numeroSostantivi1 + numeroVerbi1 + numeroAvverbi1)/lungCorpusNoPunteggiatura1
    densitaLessicale2=(numeroAggettivi2 + numeroSostantivi2 + numeroVerbi2 + numeroAvverbi2)/lungCorpusNoPunteggiatura2
    print("-------------------------------------------------------------------------------------")
    print("Confronto densità lessicale, inteso come il rapporto tra numero di sostantivi, verbi, aggettivi, avverbi e la lunghezza in token del corpus meno i segni di punteggiatura")
    #confronto le densità lessicali dei due corpus
    if densitaLessicale1>densitaLessicale2:
        print("Il corpus 1 ha una densità lessicale maggiore del corpus 2.")
    elif densitaLessicale1==densitaLessicale2:
        print("La densità lessicale è uguale per entrambi i corpus.")
    else:
        print("Il corpus 2 ha una densità lessicale maggiore del corpus 1.")
    print("Densità lessicale corpus 1:", densitaLessicale1)
    print("Densità lessicale corpus2:", densitaLessicale2)

main(sys.argv[1], sys.argv[2])
