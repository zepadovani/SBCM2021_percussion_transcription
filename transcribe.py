import abjad
import os
import pandas as pd
import abjadext.nauert as nauert
import numpy as np

testtemplate = False


#### LilyPond general voice, staff, score strucuture

## output dir
outdir = os.getcwd() + "/out_dir/"

#stylesheet include
includes = ['ilys/variables.ily','ilys/common_layout.ily']

##voices / staff 1: cymbals + cowbell
smallcymbVoice = abjad.Voice(name="smallcymb")
largecymbVoice = abjad.Voice(name="largecymb")
cowVoice = abjad.Voice(name="cow")

abjad.override(smallcymbVoice).Stem.direction = r"#up"
abjad.override(largecymbVoice).Stem.direction = r"#up"
abjad.override(cowVoice).Stem.direction = r"#down"

abjad.override(smallcymbVoice).NoteHead.style = r"#'cross"
abjad.override(largecymbVoice).NoteHead.style = r"#'cross"

cym_cowStaff = abjad.Staff([largecymbVoice,smallcymbVoice,cowVoice], name="cym_cow", simultaneous=True)
string = r"""\markup{\fontsize #-1 { \sans \column{ "large cymbal" "small cymbal" "cowbell" }}}"""
markup = abjad.Markup(string, literal=True)
abjad.setting(cym_cowStaff).instrumentName = abjad.Markup(markup)
abjad.override(cym_cowStaff).StaffSymbol.line_count = 3
abjad.override(cym_cowStaff).StaffSymbol.line_positions = r"""#'(-4 0 4)"""



### some notes to test + Clef
if testtemplate:
    cowVoice.extend(r"f4")
    smallcymbVoice.extend(r"c'4")
    largecymbVoice.extend(r"g'4 g' g' g' g' g' g'")
    leaves = abjad.select(cym_cowStaff).leaves()
    abjad.attach(abjad.Clef("percussion"), leaves[0])



##voices / staff 1: conga + bongo
bongoVoice = abjad.Voice(name="bongo")
congaVoice = abjad.Voice(name="conga")

conga_bongoStaff = abjad.Staff(name="conga_bongo")

conga_bongoStaff = abjad.Staff([bongoVoice,congaVoice], name="conga_bongo", simultaneous=True)
string = r"""\markup{\fontsize #-1 {\sans \column{ "bongo" "conga" }}}"""
markup = abjad.Markup(string, literal=True)
abjad.setting(conga_bongoStaff).instrumentName = abjad.Markup(markup)
abjad.override(conga_bongoStaff).StaffSymbol.line_count = 2
abjad.override(conga_bongoStaff).StaffSymbol.line_positions = r"""#'(-4 4)"""

abjad.override(bongoVoice).Stem.direction = r"#up"
abjad.override(congaVoice).Stem.direction = r"#down"


### some notes to test + Clef
if testtemplate:
    bongoVoice.extend(r"g'4 g' g' g'")
    congaVoice.extend(r"f4 f f f f f f")
    leaves = abjad.select(conga_bongoStaff).leaves()
    abjad.attach(abjad.Clef("percussion"), leaves[0])


##voices / staff 3: Large Tom + Snare
tomVoice = abjad.Voice(name="tom")
snareVoice = abjad.Voice(name="snare")

tom_snareStaff = abjad.Staff([snareVoice,tomVoice], name="tom_snare", simultaneous=True)
string = r"""\markup{\fontsize #-1 {\sans \column{ "snare drum" "large tom" }}}"""
markup = abjad.Markup(string, literal=True)
abjad.setting(tom_snareStaff).instrumentName = abjad.Markup(markup)
abjad.override(tom_snareStaff).StaffSymbol.line_count = 2
abjad.override(tom_snareStaff).StaffSymbol.line_positions = r"""#'(-4 4)"""

abjad.override(snareVoice).Stem.direction = r"#up"
abjad.override(tomVoice).Stem.direction = r"#down"

### some notes to test + Clef
if testtemplate:
    snareVoice.extend(r"g'4 g' g' g'")
    tomVoice.extend(r"f4 f f f f f f")
    leaves = abjad.select(tom_snareStaff).leaves()
    abjad.attach(abjad.Clef("percussion"), leaves[0])

##voices / staff 4:  Shaker + Cabassa
shakerVoice = abjad.Voice(name="shaker")
cabassaVoice = abjad.Voice(name="cabassaV")

shaker_cabassaStaff = abjad.Staff([cabassaVoice,shakerVoice], name="shaker_cabassa", simultaneous=True)
string = r"""\markup{\fontsize #-1 {\sans \column{ "cabassa" "metal shaker" }}}"""
markup = abjad.Markup(string, literal=True)
abjad.setting(shaker_cabassaStaff).instrumentName = abjad.Markup(markup)
abjad.override(shaker_cabassaStaff).StaffSymbol.line_count = 2
abjad.override(shaker_cabassaStaff).StaffSymbol.line_positions = r"""#'(-4 4)"""

abjad.override(cabassaVoice).Stem.direction = r"#up"
abjad.override(shakerVoice).Stem.direction = r"#down"
abjad.override(cabassaVoice).NoteHead.style = r"#'xcircle"
abjad.override(shakerVoice).NoteHead.style = r"#'xcircle"


### some notes to test + Clef
if testtemplate:
    cabassaVoice.extend(r"g'4 g' g' g'")
    shakerVoice.extend(r"f4 f f f f f f")
    leaves = abjad.select(shaker_cabassaStaff).leaves()
    abjad.attach(abjad.Clef("percussion"), leaves[0])


### 2: process csv data
csvfolder = os.getcwd() + "/stuff/"
csvfolder
csvfile = csvfolder + "dadosParaNotacao_REVISADO.csv"

df = pd.read_csv(csvfile)

#inicializa lista de instrumentos
instrList = []

#funções aplicadas às colunas do dataframe para readequar nome dos samples de destino e converter sample a milissegundos
def splitstring(instr):
    r"""
    separar nome da amostra do tipo (trans ou dsr)
    """
    instr = instr.split('-')
    instrList.append(instr[0])
    return instr

def sampleToMs(number,sr=44100):
    r"""
    converte sample para milissegundo
    """
    div = sr/1000
    return number/div

#funções auxiliares
def x2dx(ls):
    r"""
    return points from intervals
    """
    size = len(ls)
    out = []
    for i in np.arange(1,size):
        item = ls[i]-ls[i-1]
        out.append(item)
    return out

def dx2x(ls,init=0):
    r"""
    return intervals from points
    """
    size = len(ls)
    out = [init]
    for i in np.arange(0,size):
        out.append(out[-1]+ls[i])
    return out

# aplica funções às colunas correspondentes do dataframe de origem
df['targetSegOnset'] = df['targetSegOnset'].apply(sampleToMs)
df['targetSegSize'] = df['targetSegSize'].apply(sampleToMs)
df['corpusSegOnset'] = df['corpusSegOnset'].apply(sampleToMs)
df['corpusSegSize'] = df['corpusSegSize'].apply(sampleToMs)
df['CorpusSoundSeg'] = df['CorpusSoundSeg'].apply(splitstring)

#transforma lista de instrumentos em dicionário (a ser utilizado para guardar dados de notação)
instrDict = dict.fromkeys(instrList)

#adiciona campos relacionados à notação para cada instrumento + modo de ataque
# instrDict['Cowbell'] = {'voice': 'cowVoice', 'note': r"f", 'markups': None, 'dyn': None}
# instrDict['CymbalSmallStrike'] = {'voice': 'smallcymbVoice', 'note': r"c'", 'markups': None, 'dyn': None}
# instrDict['CymbalSmallChoke'] = {'voice': 'smallcymbVoice', 'note': r"c'", 'markups': [r"""\markup{\bold " ,"}"""], 'dyn': None}
# instrDict['CymbalBigStrike'] = {'voice': 'largecymbVoice', 'note': r"g'", 'markups': None, 'dyn': None}
# instrDict['BongoSlap'] = {'voice': 'bongoVoice', 'note': r"g'", 'markups': [r"""\markup{\sans "sl."}"""], 'dyn': None}
# instrDict['BongoMuff'] = {'voice': 'bongoVoice', 'note': r"g'", 'markups': [r"""\markup{\sans "mf."}"""], 'dyn': None}
# instrDict['CongaSlap'] = {'voice': 'congaVoice', 'note': r"f", 'markups': [r"""\markup{\sans "sl."}"""], 'dyn': None}
# instrDict['CongaMuff'] = {'voice': 'congaVoice', 'note': r"f", 'markups': [r"""\markup{\sans "mf."}"""], 'dyn': None}
# instrDict['SnareDrumOpen'] = {'voice': 'snareVoice', 'note': r"g'", 'markups': [r"""\markup{\flageolet}"""], 'dyn': None}
# instrDict['SnareDrumDampen'] = {'voice': 'snareVoice', 'note': r"g'", 'markups': [r"""\markup{+}"""], 'dyn': None}
# instrDict['TomHugeLow'] = {'voice': 'tomVoice', 'note': r"f", 'markups': None, 'dyn': None}
# instrDict['MetalShaker'] = {'voice': 'shakerVoice', 'note': r"f", 'markups': None, 'dyn': None}
# instrDict['CabassaLittleShaker'] = {'voice': 'cabassaVoice', 'note': r"g'", 'markups': None, 'dyn': None}

instrDict['Cowbell'] = {'voice': 'cowVoice', 'note': r"f", 'markups': None, 'dyn': None}
instrDict['CymbalSmallStrike'] = {'voice': 'smallcymbVoice', 'note': r"c'", 'markups': None, 'dyn': None}
instrDict['CymbalSmallChoke'] = {'voice': 'smallcymbVoice', 'note': r"c'", 'markups': [r"""\markup{\bold " ,"}"""], 'dyn': None}
instrDict['CymbalBigStrike'] = {'voice': 'largecymbVoice', 'note': r"g'", 'markups': None, 'dyn': None}
instrDict['BongoSlap'] = {'voice': 'bongoVoice', 'note': r"g'", 'markups': [r"""\markup{\sans "sl."}"""], 'dyn': None}
instrDict['BongoMuff'] = {'voice': 'bongoVoice', 'note': r"g'", 'markups': [r"""\markup{\sans "mf."}"""], 'dyn': None}
instrDict['CongaSlap'] = {'voice': 'congaVoice', 'note': r"f", 'markups': [r"""\markup{\sans "sl."}"""], 'dyn': None}
instrDict['CongaMuff'] = {'voice': 'congaVoice', 'note': r"f", 'markups': [r"""\markup{\sans "mf."}"""], 'dyn': None}
instrDict['SnareDrumOpen'] = {'voice': 'snareVoice', 'note': r"g'", 'markups': [r"""\markup{\fontsize #-2 \musicglyph #"scripts.flageolet"}"""], 'dyn': None}
instrDict['SnareDrumDampen'] = {'voice': 'snareVoice', 'note': r"g'", 'markups': [r"""\markup{+}"""], 'dyn': None}
instrDict['TomHugeLow'] = {'voice': 'tomVoice', 'note': r"f", 'markups': None, 'dyn': None}
instrDict['MetalShaker'] = {'voice': 'shakerVoice', 'note': r"f", 'markups': None, 'dyn': None}
instrDict['CabassaLittleShaker'] = {'voice': 'cabassaVoice', 'note': r"g'", 'markups': None, 'dyn': None}


# lista geral de dados a serem quantizados
lsToQuantize = [ ]
lsToQuantize

# percorre dataframe original e guarda na lista lsToQuantize: [onset, duração, instrumento]
for i in range(int(len(df.index)/2)):
    tridx = i*2
    dsridx = i*2+1

    trname = df.iloc[tridx]['CorpusSoundSeg'][0]
    dftronset = df.iloc[tridx]['targetSegOnset']
    dftrdur = df.iloc[tridx]['targetSegSize']

    dsrname = df.iloc[dsridx]['CorpusSoundSeg'][0]
    dfdsronset = df.iloc[dsridx]['targetSegOnset']
    dfdsrdur = df.iloc[dsridx]['targetSegSize']

    #garantir duração mínima para transientes
    if (dftrdur < 125):
        dftrdur = 125

    trList = [float(dftronset), float(dftrdur), trname]
    dsrList = [float(dftronset), float(dftrdur+dfdsrdur), dsrname]

    lsToQuantize.append(trList)
    lsToQuantize.append(dsrList)
    # trToQuantize.append(trList)
    # dsrToQuantize.append(dsrList)


#transforma lista lsToQuantize em DataFrame
dfToQuantize = pd.DataFrame({
    'onset': pd.Series(dtype='float'),
    'dur': pd.Series(dtype='float'),
    'instrument': pd.Series(dtype='str')})

dfToQuantize = pd.DataFrame(lsToQuantize, columns=['onset', 'dur', 'instrument'])

#calcula ponto final, em milissegundos, do trecho a ser transcrito
maxTimePoint = sum(list(dfToQuantize.iloc[len(dfToQuantize.index) - 1][0:2]))

#cria um DataFrame por intrumento (incluindo múltiplos modos de ataque desse instrumento)
dfCowbell = dfToQuantize[dfToQuantize['instrument'] == 'Cowbell']
dfCymbalSmall = (dfToQuantize[dfToQuantize['instrument'].isin(['CymbalSmallStrike', 'CymbalSmallChoke'])])
dfCymbalBig = (dfToQuantize[dfToQuantize['instrument'].isin(['CymbalBigStrike', 'CymbalBigChoke'])])

dfBongo = (dfToQuantize[dfToQuantize['instrument'].isin(['BongoSlap', 'BongoMuff'])])
dfConga = (dfToQuantize[dfToQuantize['instrument'].isin(['CongaSlap', 'CongaMuff'])])

dfSnareDrum  = (dfToQuantize[dfToQuantize['instrument'].isin(['SnareDrumOpen', 'SnareDrumDampen'])])
dfTom = dfToQuantize[dfToQuantize['instrument'] == 'TomHugeLow']

dfMetalShaker = dfToQuantize[dfToQuantize['instrument'] == 'MetalShaker']
dfCabassaLittleShaker = dfToQuantize[dfToQuantize['instrument'] == 'CabassaLittleShaker']
dfCowbell

dfAndVoice = [
    (dfCowbell,cowVoice),
    (dfCymbalSmall,smallcymbVoice),
    (dfCymbalBig,largecymbVoice),
    (dfBongo,bongoVoice),
    (dfConga,congaVoice),
    (dfSnareDrum,snareVoice),
    (dfTom,tomVoice),
    (dfMetalShaker,shakerVoice),
    (dfCabassaLittleShaker,cabassaVoice)
    ]



# abjad.NamedPitch(instrDict['TomHugeLow']['note']).number

def instrDf2DurPitch(df):
    r"""
    recebe DataFrame de um instrumento e retorna lista com durações, pitches (numéricos) e string (key para instrDict).
    primeiros dois itens são utilizados no quantizador nauert, último é utilizado para gerar markups adequados
    """
    size = len(df.index)

    lastEnd = 0
    outDurs = []
    outPitch = []
    outInstr = []

    for i in np.arange(0,size):
        row = list(df.iloc[i])
        if i == 0:
            if row[0] > 0: #se onset inicial for maior que 0, iniciar lista de durações a quantizar
                outDurs.append(row[0])
                outPitch.append(None)
                # outInstr.append(None)
                lastEnd = row[0]
            outDurs.append(row[1])
            outPitch.append(abjad.NamedPitch(instrDict[row[2]]['note']).number)
            outInstr.append(row[2])
            lastEnd = lastEnd + row[1]
        else:
            if (row[0] - lastEnd) > 0: # se existe pausa entre último ataque e o atual
                outDurs.append(row[0] - lastEnd)
                outPitch.append(None)
                # outInstr.append(None)
                lastEnd = row[0]
            outDurs.append(row[1])
            outPitch.append(abjad.NamedPitch(instrDict[row[2]]['note']).number)
            outInstr.append(row[2])
            lastEnd = lastEnd + row[1]

    if lastEnd < maxTimePoint:
        outDurs.append(maxTimePoint-lastEnd)
        outPitch.append(None)
        # outInstr.append(None)
        # lastEnd = maxTimePoint

    return [outDurs,outPitch,outInstr]


### parâmetros de quantização
# tempo
tempo = abjad.MetronomeMark((1, 4), 60)

# lista de compassos
time_signatures = (0, {"time_signature": abjad.TimeSignature((1, 4))}) #0: ponto em que o time_signature será inserido

## estrutura de divisões possíveis do pulso
search_tree=nauert.UnweightedSearchTree(
    definition={
        2: {
            2: {
                2: None,
                },
            },
        3: None
        },
    )

q_schema = nauert.MeasurewiseQSchema(
    time_signatures,
    tempo=tempo,
    search_tree=search_tree
)

quantizer = nauert.Quantizer()

markupstrings = []




def voiceFromQuantizeInstr(dfVoice):
    dfV = dfVoice[0]
    voice = dfVoice[1]

    durPitchString = instrDf2DurPitch(dfV)
    durs = durPitchString[0]
    pitches = durPitchString[1]
    string = durPitchString[2] ### ainda ver como aplicar...
    pairs = tuple(zip(durs, pitches))
    sequence = nauert.QEventSequence.from_millisecond_pitch_pairs(pairs)
    result = quantizer(sequence,q_schema)

    voice.extend(result)

    lties = abjad.select(voice).logical_ties(pitched=True)

    for i, note in enumerate(lties):
        key = string[i]
        markupstring = instrDict[key]['markups']

        if markupstring:
            # print(markupstring[0])
            markup = abjad.Markup(markupstring[0], literal=True)
            nota = note[0]
            abjad.attach(markup, nota)
            # print(type(nota))



for i in dfAndVoice:
    voiceFromQuantizeInstr(i)


staffs = [cym_cowStaff, conga_bongoStaff, tom_snareStaff, shaker_cabassaStaff]
#
# #CymbalSmall
# staffs[3][1]
#
# (markupstrings[-2][1] != None)
# len(markupstrings[-2])
#
#
# staffs[3][1]
# an_iterator = filter(lambda el: el != None, markupstrings[-2])
# x = list(an_iterator)
# len(x)
# #### ISSO!
# len(abjad.select(staffs[3][1]).logical_ties(pitched=True))
#
# result = abjad.select(staffs[0][1]).leaves(pitched=True)
# print(result)
# result = result.group_by()
# len(result.top())
# len(result[0]) ### todas as notas...
#
# markupstrings[1]
#
#
# staffs[0][2]
# len(staffs[0][2])
# len(markupstrings[0])
#
# result = abjad.select(staffs[0][2]).leaves(pitched=True)
# result = result.group_by()
#
# len(result[0])

for staff in staffs:
    leaves = abjad.select(staff).leaves()
    abjad.attach(abjad.Clef("percussion"), leaves[0])



## StaffGroup
percStaffGroup = abjad.StaffGroup(
    staffs,
    lilypond_type="StaffGroup",
    name="Percussion",
)

score = abjad.Score([percStaffGroup], name="Score")
lilypond_file = abjad.LilyPondFile(items=[score],includes=includes)
abjad.show(lilypond_file)

abjad.persist.as_ly(lilypond_file, outdir+"out.ly")
abjad.persist.as_pdf(lilypond_file, outdir+"out.pdf")

# gerar_arquivo ly
# abjad.persist.as_ly(lilypond_file, outdir+"out.ly")
