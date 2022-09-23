#importo i vari moduli necessari 
import nltk 
import sys
from nltk import bigrams
import math

#funzione che legge i file
def leggifiles(file0):              #unico parametro: il file da aprire e leggere
    fileInput=open(file0, mode="r", encoding="utf-8")  #file viene aperto
    raw=fileInput.read()      #contenuto del file viene assegnato alla variabile raw
    return raw               #restituisce raw

#funzione che tokenizza il testo
def tokenizza(frasi): #come parametro: la lista di frasi del testo
    tokens=[] #creo una lista vuota in cui andrò a inserire tutti i token 
    for frase in frasi:  #per ogni frase della lista
        token=nltk.word_tokenize(frase)   #tokenizzo la frase e assegno l'insieme di token a una variabile
        tokens=tokens+token   #aggiungo la lista di token della frase (token) alla lista dei token totali
    return tokens #restituisco la lista dei token totali

#funzione che annota il testo con le parti del discorso 
def annota(frasi): #come parametro: la lista delle frasi del testo
    tokens=[]      #creo una lista vuota per i token
    tokensPOS=[]    #creo una lista vuota per le coppie di token-PoS
    for frase in frasi:              #per ogni frase contenuta nella lista passata come parametro
        token=nltk.word_tokenize(frase)       #tokenizzo la frase
        tokens=tokens+token                #aggiungo i token della frase alla lista tokens
        postoken=nltk.pos_tag(token)      #annoto tutti i token della frase con la PoS
        tokensPOS=tokensPOS+postoken        #aggiungo l'insieme di token annotati con la PoS alla lista di token totale annotati con PoS
    return tokensPOS     #restituisco la lista di token annotati con la PoS 

#funzione che estrae le singole PoS contenute in un testo
def estraiListaPOS(testoannotato):    #parametro: il testo annotato con le PoS(lista di coppie token-PoS)
    listaPOS=[]   #creo una lista vuota dove inserirò tutte le PoS che trovo nel testo
    for bigramma in testoannotato:   #per ogni bigramma(coppia toke-PoS) contenuto nel testo annotato
        pos=bigramma[1]   #assegno il secondo elemento del bigramma(PoS) a una variabile
        listaPOS.append(pos)  #aggiungo la PoS trovata alla lista listaPOS
    return listaPOS  #restituisco la lista contenente tutte le PoS del testo 

#funzione che mi stampa le 10 PoS più frequenti del corpus
def freq_POS(testoPoStaggato, listaPoS):  #parametri: il testo annotato e la lista delle PoS distinte contenute nel testo 
    for i in range(10):  #per 10 volte
        j=0   #indice che mi serve per indicare la posizione delle PoS nella lista delle PoS inizializzato a 0
        freq_max=0  #variabile il cui valore alla fine del ciclo for sarà la frequenza del PoS più frequente inzializzato a 0
        for pos in listaPoS:   #per tutti gli elementi(PoS) contenuti nella lista listaPoS 
            contapos=0   #contatore delle occorrenze 
            for bigramma in testoPoStaggato:  #per ogni bigramma(coppia token-PoS) contenuto nel testo annotato
                if bigramma[1]==pos:  #se il secondo elemento del bigramma corrisponde alla PoS 
                    contapos=contapos+1  #aggiungo 1 al contatore delle occorrenze 
            if contapos>freq_max:  #se il contatore ha valore più alto della variabile freq_max
                freq_max=contapos  #assegno il valore del contatore alla varaibile freq_max
                pos_max=pos    #assegno alla variabile pos_max la PoS con frequenza massima
                indicepos_max=j   #assegno il valore dell'indice j a una variabile 
            j=j+1 #aggiungo 1 a j
        #stampo i vari valori ottenuti 
        print()
        print(" ", i+1, ".",  "\"", pos_max, "\"")
        print(" Frequenza:", freq_max)
        del listaPoS[indicepos_max]  #elimino dalla lista delle PoS del testo quella che ho identificato come PoS con frequenza massima, così facendo all'iterazione seguente non mi prende la stessa PoS come massima

#funzione che mi stampa i sotantivi più frequenti del corpus
def sotantiviPiuFrequenti(testoPoStaggato):  #parametro: il testo annotato
    tagSostantivi=["NN", "NNPS", "NNP", "NNS"]  #creo una lista con i diversi tag che identificano i sostantivi
    bigrammidistinti=list(set(testoPoStaggato))  #estraggo dal testo annotato la lista di coppie distinte token-PoS 
    for i in range(20):   #per 20 volte
        freq_max=0   #variabile che indica la frequenza massima inizializzata a 0
        j=0  #indice inizializzato a 0 che mi serve per identificare la posizione dell'elemento
        for bigramma in bigrammidistinti:   #per ogni bigramma(coppia token-PoS) contenuto nella lista bigrammidistinti
            if bigramma[1] in tagSostantivi:  #se il secondo elemento del bigramma corrisponde a uno dei tag dei sostantivi
                occorrenzabigramma=testoPoStaggato.count(bigramma)   #conto le occorrenze di quel bigramma nel testo
                if occorrenzabigramma>freq_max:  #se le occorrenze avessero un valore più alto della frequenza massima trovata finora 
                    sostantivomax=bigramma[0]  #assegno il token sostantivo (primo elemento della coppia) a una variabile
                    freq_max=occorrenzabigramma  #assegno a una variabile la frequenza dell'elemento
                    indicesost_max=j    #assegno al dell'indice j a una variabile 
            j=j+1 #incremento j di 1
        #stampo i risultati
        print()
        print(" ", i+1, ".", "\"", sostantivomax, "\"")
        print(" Frequenza:", freq_max)
        del bigrammidistinti[indicesost_max]  #elimino l'elemento coppia token-PoS dalla lista per ottenere nelle prossime iterazioni gli elementi con frequenza massima dopo questo


#funzione che mi stampa i verbi più frequenti del corpus
#uguale a quella soprastante
def verbiPiuFrequenti(testoPoStaggato):
    tagVerbi=["VB", "VBD", "VBG", "VBN", "VBP", "VBZ" ]  #cambia solo la lista dei tag, in quanto questa volta cerchiamo i verbi
    bigrammidistinti=list(set(testoPoStaggato))
    for i in range(20):
        freq_max=0
        j=0
        for bigramma in bigrammidistinti:
            if bigramma[1] in tagVerbi:
                occorrenzabigramma=testoPoStaggato.count(bigramma)
                if occorrenzabigramma>freq_max:
                    verbomax=bigramma[0]
                    freq_max=occorrenzabigramma
                    indicesost_max=j
            j=j+1
        print()
        print(" ", i+1, ". \"", verbomax, "\"")
        print(" Frequenza:", freq_max)
        del bigrammidistinti[indicesost_max]


#funzione che mi estrae tutti i bigrammi composti da un sostantivo e un verbo                    
def sostantivoVerbo(testoPoStaggato, bigrammi):  #parametri: testo annotato, lista dei bigrammi del testo
    bigrammidistinti=list(set(bigrammi))   #creo una lista con i bigrammi singoli distinti
    tagVerbi=["VB", "VBD", "VBG", "VBN", "VBP", "VBZ" ]  #definisco una lista con tutti i tag  che corrispondono ai verbi
    tagSostantivi=["NN", "NNPS", "NNP", "NNS"]  #definisco una lista con tutti i tag che corrispondono ai sostantivi
    listaBigrammiSostantivoVerbo=[]  #creo una lista vuota dove andrò ad aggiungere tutti i bigrammi composti da un sostantivo e un verbo
    i=0  #indice per iterazione 
    while i<len(testoPoStaggato)-1:  #itero per il numero di coppie token-PoS contenute nel testo 
        Pos1=testoPoStaggato[i][1]  #assegno a una variabile il primo elemento della coppia i che corrisponde alla PoS
        Pos2=testoPoStaggato[i+1][1] #stessa cosa per con il primo elemento della coppia seguente i+1
        if Pos1 in tagSostantivi and Pos2 in tagVerbi:   #se la PoS del primo elemento è un sostantivo e la PoS del secondo elemento è un verbo
            word1=testoPoStaggato[i][0]   #assegno a una variabile il token corrispondente
            word2=testoPoStaggato[i+1][0]   #stessa cosa per l'elemento seguente
            for bigramma in bigrammidistinti:  #per ogni bigramma nella lista dei bigrammi distinti del testo
                if bigramma[0]==word1 and bigramma[1]==word2:   #se la prima e la seconda parola corrispondono ai token estratti
                    listaBigrammiSostantivoVerbo.append(bigramma)   #aggiungo il bigramma alla lista dei bigrammi di coppie sostantivo verbo
        i=i+1 #incremento i di 1 
    return listaBigrammiSostantivoVerbo  #restituisco la lista con i bigrammi composti da un sostantivo e un verbo

#funzione che mi estrae tutti i bigrammi composti da un aggettivo e un sostantivo
#uguale alla funzione sopra 
def aggettivoSostantivo(testoPoStaggato, bigrammi):
    bigrammidistinti=list(set(bigrammi))
    tagAggettivi=["JJ", "JJR", "JJS"]           #cambiano le liste dei tag:  tag degli aggettivi
    tagSostantivi=["NN", "NNPS", "NNP", "NNS"]    #tag dei sostantivi
    listaBigrammiAggettivoSostantivo=[]
    i=0
    while i<len(testoPoStaggato)-1:
        Pos1=testoPoStaggato[i][1]
        Pos2=testoPoStaggato[i+1][1]
        if Pos1 in tagAggettivi and Pos2 in tagSostantivi:
            word1=testoPoStaggato[i][0]
            word2=testoPoStaggato[i+1][0]
            for bigramma in bigrammidistinti:
                if bigramma[0]==word1 and bigramma[1]==word2:
                    listaBigrammiAggettivoSostantivo.append(bigramma)
        i=i+1
    return listaBigrammiAggettivoSostantivo


#funzione che mi stampa i 20 bigrammi composti da un sostantivo e un verbo più frequenti
def sostantivoVerboFreq(listaSostVerbi):  #parametro: la lista di tutti i bigrammi sostantivo-verbo estratti tramite la funzione sostantivoVerbo
    distribuzione_freq=nltk.FreqDist(listaSostVerbi)  #calcolo la distribuzione di frequenza dei bigrammi
    primi20=distribuzione_freq.most_common(20)  #creo una lista con solo i primi 20 elementi (in quanto erano già ordinati x frequenza)
    i=1 #uso un indice per il ranking dei bigrammi in base alla frequenza
    for elem in primi20:  #per ogni bigramma nella lista contenente i 20 bigrammi più frequenti
        print()
        print(" ", i, ".", "Bigramma:", elem[0])  #stampo il primo elemento del bigramma(sostantivo)
        print(" Frequenza:", elem[1])  #stampo il secondo elemento del bigramma(verbo)
        i=i+1 #incremento indice di 1


#funzione che mi stampa i 20 bigrammi composti da un aggettivo e un sostantivo più frequenti
#uguale alla funzione sopra
def aggettivoSostantivoFreq(listaAggSost):
    distribuzione_freq=nltk.FreqDist(listaAggSost)
    primi20=distribuzione_freq.most_common(20)
    i=1
    for elem in primi20:
        print()
        print(" ", i, ". Bigramma", elem[0])
        print(" Frequenza:", elem[1])
        i=i+1
        
#funzione che mi calcola la probabilità condizionata di un bigramma
def probCOND(bigramma, listabigrammi, corpus):   #parametri: il bigramma di cui vogliamo sapere la probabilità , la lista intera di bigrammi del testo e la lista di token
    freq_bigramma=listabigrammi.count(bigramma)  #calcolo la frequenza del bigramma contando quante volte appare nella lista intera di bigrammi
    freq_A=corpus.count(bigramma[0])  #calcolo la frequenza del primo elemento del bigramma nel testo
    prob_condizionata=freq_bigramma/freq_A  #divido la frequenza del bigramma per la frequenza del primo elemento del bigramma ottenendo così la probabilità condizionata
    return prob_condizionata #restituisco la probabilità condizionata

#funzione che mi calcola la probabilità congiunta
def probCONG(bigramma, listabigrammi, corpus):  #parametri: bigramma di cui vogliamo sapere la probabilità, lista intera di bigrammi del testo e la lista di token
    freq_bigramma=listabigrammi.count(bigramma)  #calcolo la frequenza del bigramma all'interno del corpus
    prob_congiunta=freq_bigramma/len(corpus)  #calcolo la probabilità congiunta: frequenza del bigramma divisa per la lunghezza del corpus
    return prob_congiunta  #restituisco la probabilità congiunta

#funzione che mi calcola la Local Mutual Information di un bigramma
def LmutualInformation(bigramma, listabigrammi, corpus): #parametri: bigramma di cui vogliamo sapere la LMI, la lista dei bigrammi e la lista dei token
    prob_bigramma=probCONG(bigramma, listabigrammi, corpus) #calcolo la probabilità congiunta del bigramma
    freq_bigramma=listabigrammi.count(bigramma) #calcolo la frequenza del bigramma all'interno del testo
    freq_A=corpus.count(bigramma[0]) #calcolo la frequenza del primo elemento del bigramma all'interno del testo
    freq_B=corpus.count(bigramma[1])  #calcolo la frequenza del secondo elemento del bigramma all'interno del testo
    prob_A=freq_A/len(corpus) #calcolo la probabilità del primo elemento del bigramma
    prob_B=freq_B/len(corpus)  #calcolo la probabilità del secondo elemento del bigramma
    calcolo=prob_bigramma/(prob_A*prob_B)  #calcolo la mutual information
    MI=math.log(calcolo, 2)  #calcolo la mutual information
    LMI=MI*freq_bigramma  #calcolo la local mututal information
    return LMI #restituisco la local mutual information

#funzione che mi stampa i 20 bigrammi con probabilità condizionata più alta
def probCondMAX(listabigrammi,corpus):   #parametri: lista dei bigrammi, lista dei token
    bigrammidistinti=list(set(listabigrammi))  #creo una lista con tutti i singoli bigrammi distinti del testo
    for i in range(20):  #per 20 volte
        probmax=0   #inizializzo la variabile probmax, variabile che sta a indicare la probabilità condizionata più alta 
        j=0   #inizializzo una variabile che utilizzerò come indice per identificare la posizione del bigramma nel testo che sto analizzando
        for bigramma in bigrammidistinti:  #per ogni bigramma contenuto nella lista dei bigrammi distinti 
            freqA=corpus.count(bigramma[0])  #calcolo la frequenza del primo elemento del bigramma nel testo
            freqB=corpus.count(bigramma[1])  #calcolo la frequenza del secondo elemento del bigramma nel testo
            if freqA>3 and freqB>3:   #se i due elementi distinti hanno frequenza maggiore di 3 nel testo
                probcond=probCOND(bigramma, listabigrammi, corpus)  #calcolo la probabilità condizionata del bigramma
                if probcond>probmax:  #se questo è più alta di quella massima vista finora
                    probmax=probcond  #assegno a probmax la probabilità del bigramma 
                    bigrammamax=bigramma  #assegno a una variabile il bigramma con probabilità massima
                    indicebigramma=j   #assegno a una variabile l'indice del bigramma
            j=j+1  #incremento j di 1 
        print("\n Bigramma", i+1, ": \"",  bigrammamax[0], ",", bigrammamax[1] , "\"")  #stampo il bigramma con probabilità massima
        print(" probabilità condizionata:", probmax)  #stamo la sua probabilità 
        del bigrammidistinti[indicebigramma]  #elimino dalla lista dei bigrammi distinti il bigramma identificato come bigramma con probabilità massima
        
#funzione che mi stampa i 20 bigrammi con probabilità congiunta più alta
#uguale a quella sopra ma chiama la funzione di probabilità congiunta
def probCongMAX(listabigrammi, corpus):  
    bigrammidistinti=list(set(listabigrammi))
    for i in range(20):
        probmax=0
        j=0
        for bigramma in bigrammidistinti:
            freqA=corpus.count(bigramma[0])
            freqB=corpus.count(bigramma[1])
            if freqA>3 and freqB>3:
                probcong=probCONG(bigramma, listabigrammi, corpus)  #cambia solo il tipo di informazione che cerchiamo
                if probcong>probmax:
                    probmax=probcong
                    bigrammamax=bigramma
                    indicebigramma=j
            j=j+1
        print("\n Bigramma", i+1, ": \"", bigrammamax[0], ",", bigrammamax[1], "\"")
        print(" probabilità congiunta:", probmax)
        del bigrammidistinti[indicebigramma]

#funzione che mi stampa i 20 bigrammi con LMI più alta
#uguale alle ultime due ma chiama la funzione che calcola la local mutual information
def mutualInformationMAX(listabigrammi, corpus):
    bigrammidistinti=list(set(listabigrammi))
    for i in range(20):
        MImax=0  
        j=0
        for bigramma in bigrammidistinti:
            freqA=corpus.count(bigramma[0])
            freqB=corpus.count(bigramma[1])
            if freqA>3 and freqB>3:
                mutualinformation=LmutualInformation(bigramma, listabigrammi, corpus)   #cambia solo il tipo di informazione che cerchiamo
                if mutualinformation>MImax:
                    MImax=mutualinformation
                    bigrammamax=bigramma
                    indicebigramma=j
            j=j+1
        print("\n Bigramma", i+1, ": \"", bigrammamax[0], ",", bigrammamax[1], "\"")
        print(" Local Mutual Information:", MImax)
        del bigrammidistinti[indicebigramma]

#funzione che mi calcola la probabiilità di una frase con un modello markoviano di ordine 1 con l'add one smoothing   
def modellodimarkov1(distribuzioneToken, distribuzioneBigrammi, bigrammiFrase, lunghezzacorpus, vocabolario):  #parametri: distribuzione di frequenza dei token, distribuzione di frequenza dei bigrammi, lista dei bigrammi della frase, lunghezza del corpus e vocabolario(lista delle parole tipo)
    card_vocabolario=len(vocabolario)  #calcoliamo la cardinalità del vocabolario
    token1=bigrammiFrase[0][0]  #assegno a una variabile come valore il primo elemento(token) che del primo bigramma della frasea
    prob_frase=distribuzioneToken[token1]+1/lunghezzacorpus+card_vocabolario   #calcolo la probabilità del primo token della frase 
    for bigramma in bigrammiFrase:   #per ogni bigramma della frase
        freq_bigramma=distribuzioneBigrammi[bigramma]   #assegno a una variabile la frequenza del bigramma
        freq_A=distribuzioneToken[bigramma[0]]    #assegno a una variabiile la frequenza del primo elemento(token) del bigramma
        prob_condizionata=(freq_bigramma+1)/(freq_A+card_vocabolario)  #calcolo la probabilità condizionata del bigramma con l'add one smoothing 
        prob_frase=prob_frase*prob_condizionata #moltiplico per le altre probabilità calcolate
    return prob_frase #restituisco la probabilità della frase

#funzione che mi estrae tutte le frasi di lunghezza n dal corpus
def estraiFrasiDiLunghezza(n, listafrasi): #parametri: n che identifica il numero di token da cui devono essere composte le frasi, la lista di frasi del corpus
    listafrasiLunghezzaN=[]  #creo una lista in cui andrò ad inserire tutte le frasi lunghe n
    for frase in listafrasi:   #per ogni frase nella lista delle frasi
        frasetokenizzata=nltk.word_tokenize(frase)  #tokenizzo la frase
        if len(frasetokenizzata)==n:  #se il numero di frasi corrisponde ad n
            listafrasiLunghezzaN.append(frase)  #aggiungo alla lista la frase
    return listafrasiLunghezzaN  #restituisco la lista delle frasi lunghe n

#funzione che mi estrae i nomi propri di persona contenuti in un testo
def estraiNomiPersona(alberoNE):  #parametri: testo annotato con le entità nominate (struttura ad albero)
    listaNomiPersona=[] #creo una lista vuota in cui andrò ad inserire tutti i token che sono nomi propri di persona
    for nodo in alberoNE:  #per ogni nodo nell'albero
        NE=''  #assegno una stringa vuota alla variabile NE
        labelname="PERSON"  #assegno il tag che identifica il tipo di entità nominata a una variabile in questo caso il nome proprio di persona
        if hasattr(nodo, 'label'):  #se il nodo ha l'attributo label
            if nodo.label()==labelname:   #se l'etichetta del nodo è uguale al tag di nomi propri di persona
                for foglie in nodo.leaves():  #scorro le foglie del nodo
                    NE=NE+' '+foglie[0]  #aggiungo il token alla variabile 
                listaNomiPersona.append(NE)  #aggiungo alla lista NE (il nome proprio di persona identificato)
    return listaNomiPersona  #restituisco la lista di tutti i nomi propri di persona trovati

#funzione che mi estrai i nomi propri di luogo contenuti in un testo
#uguale a quella sopra
def estraiNomiLuogo(alberoNE):
    listaNomiLuogo=[]
    for nodo in alberoNE:
        NE=''
        labelname="GPE"   #cambia solo il tag, in base a ciò che stiamo cercando, in questo caso GPE sta per nome proprio di luogo
        if hasattr(nodo, 'label'):
            if nodo.label()==labelname:
                for foglie in nodo.leaves():
                    NE=NE+' '+foglie[0]
                listaNomiLuogo.append(NE)
    return listaNomiLuogo


#funzione che mi stampa i primi 15 elementi della lista delle entià nominate di interessa
def NEFreq(listaNE):  #parametro: lista delle entità nominate di interesse 
    distribuzione_freq=nltk.FreqDist(listaNE)  #estraggo la distribuzione di frequenza degli elementi della lista di interesse
    primi15=distribuzione_freq.most_common(15)  #mi creo una lista con solo i primi 15 elementi (sono già ordinati in ordine di frequenza discendente)
    i=1  #utilizzo i come indice di ranking
    for elem in primi15:  #per ogni elemento nella lista primi15
        #stampo gli elementi
        print()
        print(" ", i, ".", elem[0])  
        print(" Frequenza:", elem[1])
        i=i+1  #incremento i di 1
    
        
#funzione principale
def main(testo1, testo2):
    #funzione in cui chiamo le funzioni per estrarre le informazioni che mi interessano
    corpus1=leggifiles(testo1)
    corpus2=leggifiles(testo2)
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    frasi1=sent_tokenizer.tokenize(corpus1)
    frasi2=sent_tokenizer.tokenize(corpus2)
    alltokens1=tokenizza(frasi1)
    alltokens2=tokenizza(frasi2)
    alltokensPOS1=annota(frasi1)
    alltokensPOS2=annota(frasi2)
    listaPOS1=estraiListaPOS(alltokensPOS1)
    listaPOS2=estraiListaPOS(alltokensPOS2)
    listaPOSdistinti1=list(set(listaPOS1))
    listaPOSdistinti2=list(set(listaPOS2))
    vocab1=list(set(alltokens1))
    vocab2=list(set(alltokens2))
    bigrammi1=list(bigrams(alltokens1))
    bigrammi2=list(bigrams(alltokens2))
    distr_frequenzaToken1=nltk.FreqDist(alltokens1)
    distr_frequenzaBigrammi1=nltk.FreqDist(bigrammi1)
    distr_frequenzaToken2=nltk.FreqDist(alltokens2)
    distr_frequenzaBigrammi2=nltk.FreqDist(bigrammi2)
    lunghezzaCorpus1=len(alltokens1)
    lunghezzaCorpus2=len(alltokens2)
    alberoNE1=nltk.ne_chunk(alltokensPOS1)
    alberoNE2=nltk.ne_chunk(alltokensPOS2)
    listaNomiPersona1=estraiNomiPersona(alberoNE1)
    listaNomiPersona2=estraiNomiPersona(alberoNE2)
    listaNomiLuogo1=estraiNomiLuogo(alberoNE1)
    listaNomiLuogo2=estraiNomiLuogo(alberoNE2)
    #stampo i vari risultati
    print(" PART OF SPEECH TAGGING")
    print()
    print(" Le 10 PoS più frequenti del corpus 1:")
    freq_POS(alltokensPOS1, listaPOSdistinti1)
    print()
    print(" Le 10 PoS più frequenti del corpus 2:")
    freq_POS(alltokensPOS2, listaPOSdistinti2)
    print()
    print(" I 20 Sostantivi più frequenti del corpus 1:")
    sotantiviPiuFrequenti(alltokensPOS1)
    print()
    print(" I 20 Sostantivi più frequenti del corpus 2:")
    sotantiviPiuFrequenti(alltokensPOS2)
    print()
    print("---------------------------------------------------------------------------------------------------------------------\n")
    print()
    print(" I 20 Verbi più frequenti del corpus 1:")
    verbiPiuFrequenti(alltokensPOS1)
    print()
    print(" I 20 Verbi più frequenti del corpus 2:")
    verbiPiuFrequenti(alltokensPOS2)
    print()
    print("---------------------------------------------------------------------------------------------------------------------\n")
    print(" I 20 bigrammi Sostantivo-Verbo più frequenti del corpus 1:")
    SVlista1=sostantivoVerbo(alltokensPOS1, bigrammi1)
    sostantivoVerboFreq(SVlista1)
    print()
    print(" I 20 bigrammi Sostantivo-Verbo più frequenti del corpus 2:")
    SVlista2=sostantivoVerbo(alltokensPOS2, bigrammi2)
    sostantivoVerboFreq(SVlista2)
    print()
    print("---------------------------------------------------------------------------------------------------------------------\n")
    print(" I 20 bigrammi Aggettivo-Sostantivo più frequenti del corpus 1:")
    ASlista1=aggettivoSostantivo(alltokensPOS1, bigrammi1)
    aggettivoSostantivoFreq(ASlista1)
    print()
    print(" I 20 bigrammi Aggettivo-Sostantivo più frequenti del corpus 2:")
    ASlista2=aggettivoSostantivo(alltokensPOS2, bigrammi2)
    aggettivoSostantivoFreq(ASlista2)
    print()

    
    print(" PROBABILITA' CONGIUNTA DI BIGRAMMI\n")
    print(" I 20 bigrammi del corpus 1 con probabilità congiunta massima:")
    probCongMAX(bigrammi1, alltokens1)
    print("--------------------------------------------------------------------------------------------------------------------\n")
    print(" I 20 bigrammi del corpus 2 con probabilità congiunta massima:")
    probCongMAX(bigrammi2, alltokens2)
    print("\n PROBABILITA' CONDIZIONATA DI BIGRAMMI:\n")
    print(" I 20 bigrammi del corpus 1 con probabilità condizionata massima:")
    probCondMAX(bigrammi1, alltokens1)
    print("--------------------------------------------------------------------------------------------------------------------\n")
    print(" I 20 bigrammi del corpus 2 con probabilità condizionata massima:")
    probCondMAX(bigrammi2, alltokens2)
    print("\n LOCAL MUTUAL INFORMATION DI BIGRAMMI:\n")
    print(" I 20 bigrammi del corpus 1 con mutual information massima:")
    mutualInformationMAX(bigrammi1, alltokens1)
    print("---------------------------------------------------------------------------------------------------------------------\n")
    print(" I 20 bigrammi del corpus 2 con Local mutual information massima:")
    mutualInformationMAX(bigrammi1, alltokens2)
    print("--------------------------------------------------------------------------------------------------------------------")
    print()
    print(" FRASI CON PROBABILITA' MASSIMA DI LUNGHEZZA 8 - 15")
    print()
    for i in range(8,16):  #per un range da 8 a 15
        #estraggo le frasi di lunghezza i
        listafrasi1=estraiFrasiDiLunghezza(i, frasi1)
        listafrasi2=estraiFrasiDiLunghezza(i, frasi2)
        probmax1=0
        probmax2=0
        #per ogni frase nella lista delle frasi 
        for frase in listafrasi1:
            frasetokenizzata=nltk.word_tokenize(frase)
            bigrammifrase=list(bigrams(frasetokenizzata))
            #calcolo la probabilità della frase chiamando la funzione modellodimarkov1
            probfrase=modellodimarkov1(distr_frequenzaToken1, distr_frequenzaBigrammi1, bigrammifrase, lunghezzaCorpus1, vocab1)
            #se la probabilità della frase è più alta di quella massima
            if probfrase>probmax1:
                probmax1=probfrase
                frasemax1=frase
        #stampo la frase di lunghezza n con probabilità massima
        print(" La frase del corpus 1 di lunghezza", i, "con probabilità massima è:")
        print(frasemax1)
        print(" Probabilità:", probmax1)
        print()
        #stessa cosa per la lista delle frasi del secondo corpus
        for frase in listafrasi2:
            frasetokenizzata=nltk.word_tokenize(frase)
            bigrammifrase=list(bigrams(frasetokenizzata))
            probfrase=modellodimarkov1(distr_frequenzaToken2, distr_frequenzaBigrammi2, bigrammifrase, lunghezzaCorpus2, vocab2)
            if probfrase>probmax2:
                probmax2=probfrase
                frasemax2=frase
        print(" La frase del corpus 2 di lunghezza", i, "con probabilità massima è:")
        print(frasemax2)
        print(" Probabilità:", probmax2)
        print()
    print("------------------------------------------------------------------------------------------------------------------\n")
    print(" NAMED ENTITY TAGGING")
    print()
    print(" I 15 nomi propri di persona più frequenti del corpus 1: \n")
    NEFreq(listaNomiPersona1)
    print()
    print(" I 15 Nomi propri di persona più frequenti del corpus 2: \n")
    NEFreq(listaNomiPersona2)
    print("------------------------------------------------------------------------------------------------------------------\n")
    print(" I 15 nomi propri di luogo più frequenti del corpus 1: \n")
    NEFreq(listaNomiLuogo1)
    print()
    print(" I 15 nomi propri di luogo più frequenti del corpus 2: \n")
    NEFreq(listaNomiLuogo2)
   
    
        

    
main(sys.argv[1], sys.argv[2])
