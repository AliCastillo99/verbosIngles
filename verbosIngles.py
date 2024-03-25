import random
import colorama as color
import gtts as gTTs
from io import BytesIO
import pygame 

lenguajeMXN = 'es-es'
lenguajeEU = 'en-us'

# referencia (https://pythonprogramming.altervista.org/how-chatgpt-solved-this-error-and-made-the-pc-speak/)
def speak(text):
    mp3_fo = BytesIO()
    tts = gTTs.gTTS(text, lang=lenguajeEU)
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    sound = pygame.mixer.Sound(mp3_fo)
    sound.play()

pygame.init()
pygame.mixer.init()



regular = ['Presente', 'Pasado']
irregular = ['Pasado', 'Presente', 'Participio']
count = 0
#   Presente y Pasado
verbosRegulares = {'Evadir':['Avoid','Avoided'], 'Atacar':['Attack ','Attacked'],'Disculparse':['Apologize','Apologized'],
                   'Creer':['Believe','Believed'], 'Completar':['Complete','Completed'], 'Cocinar':['Cook','Cooked'],
                   'Llamar':['Call','Called'], 'Disfrutar':['Enjoy','Enjoyed'], 'Seguir':['Follow','Followed'],
                   'Adivinar ':['Guess','Guessed'], 'Estudiar':['Study','Studied'], 'Hablar':['Talk','Talked'],
                   'Tocar':['Touch','Touched']}

#   Pasado, Presente y participi
verbosIrregulares = {'Despierto':['Awoke','Awake','Awoken'], 'Ser, estar':['Was/Were','Be','Been'],
                     'Empezar':['Began','Begin','Begun'], 'Venir':['Came','Come','Come'], 'Beber':['Drank','Drink','Drunk'],
                     'Comer':['Ate','Eat','Eaten'], 'Volar':['Flew','Fly','Flown'], 'Dar':['Gave','Give','Given'],
                     'Tener':['Had','Have','Had'], 'Mantener':['Kept','Keep','Kept'], 'Significar':['Meant','Mean','Meant'],
                     'Pagar':['Paid','Pay','Paid'], 'Leer':['Read','Read','Read'], 'Ver':['Saw','See','Seen'],
                     'Hablar':['Spoke','Speak','Spoken'], 'Tomar':['Took','Take','Taken'], 'Entender':['Understood','Understand','Understood'],
                     'Despertar':['Woke','Wake','Woken'], 'Escribir':['Wrote','Write','Written'],
                     'Forma':['Wayed','Way','Way'], 'Lejos/Lejano':['Away','Away','Away']}

verbosTH = {'pensar/pensamiento':['Though','Think','Will think'], 'Aunque':['thought','Think','Will thinking'],
            'Dura@':['Toughed','Tough','Will tough']}

adjetivos = {'Agradable':'Agreeable', 'Ambicioso':'Aspiring', 'Consciente':'Aware', 'Horrible':'Awful', 'Ciego':'Blind', 'Benevolente':'Benevolent', 'Valiente':'Brave',
             'Calma':'Calm', 'Cariñoso':'Caring', 'Desafiante':'Challenging', 'Cautivador':'Captivating', 'Carismatico':'Charismatic', 'Encantador':'Charming', 'Alegre':'Cherrful',
             'Sordo':'Deaf', 'Delicioso':'Delicious', 'Decente':'Decent', 'Atrevido':'Daring', 'Digno':'Dignified', 'Obediente':'Dutiful', 'Embarazoso':'Embarrassed', 'Elegante':'Elegant',
             'Poco':'Few', 'Fiel':'Faithful', 'Indulgente':'Forgiving', 'Contundente':'Forecful', 'Avaro':'Greedy', 'Contento':'Gald',
             'Dificil':'Difficult', 'Ansios@':'Eager', 'Encantad@':'Delighted', 'Orgullos@':'Proud', 'Dispuest@':'Willing', 'Determinad@':'Determined', 
             'Asustad@':'Afraid', 'Avergonzado':'Ashamed'}

adverbios = {'Bad':'Badly', 'Careful':'Carefully', 'Careless':'Carelessly', 'Easy':'Easily', 'Honest':'Honestly', 'Quick':'Quickly', 'Good':'Well'}


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
tipo = int(input('Regulares -> 1, Irregulares -> 2,  VerbosTH ->3, Adjetivos ->4 \n'))

match tipo:
    case 1:
        print('-----Regulares----')
        datos = verbosRegulares
        tiempos = ['Presente', 'Pasado']
        step = 1

    case 2:
        print('-----Irregulares----')
        datos = verbosIrregulares
        tiempos = ['Pasado', 'Presente', 'Futuro']
        step = 2
    case 3:
        print('-----VerbosTH----')
        datos = verbosTH
        tiempos = ['Pasado', 'Presente', 'Futuro']
        step = 2

    case 4:
        print('-----Adjetivos----')
        datos = adjetivos
        tiempos = ['English']
        step = 1



#Verbos irregulares eh irregulares

while count < 20 and (tipo == 1 or tipo == 2 or tipo==3):
    print(f'---------------------------{count+1}---------------------------------')

    verbos = datos.keys()
    keys = list(verbos)
    verbo = random.choice(keys) #   Escoge aleatoriamente los keys
    print('verbo: ',verbo)
    ppf = random.randrange(0, 2, step) # Pasado, presente, futuro

    verboIngles =  datos[verbo][ppf]

    #print('verboIngles: ', verboIngles)
    palabra = input(f'¿Cúal es la palabra "{verbo}" en "{tiempos[ppf]}"?\n')
    if palabra == verboIngles.lower():
        speak(verboIngles)
        datos.pop(verbo)
        print(color.Fore.RED +'Muy bien ✔✔✔'), print(color.Style.RESET_ALL)
        count += 1
    else:
        speak(verboIngles)
        print(color.Fore.RED +'El verbo era: ', verboIngles), print(color.Style.RESET_ALL)
        print('intenta de nuevo ')
else:
    while count <10:
        print(f'---------------------------{count + 1}---------------------------------')
        keys = list(datos.keys())
        seleccion = random.choice(keys) #   Escoge aleatoriamente los keys
        print(f'palabra: {seleccion}')
        significado = datos[seleccion]

        #print('verboIngles: ', verboIngles)
        palabra = input(f'¿Cúal es la palabra "{seleccion}" en English"?\n')
        if palabra == significado.lower():
            speak(significado)
            datos.pop(seleccion)
            print('Muy bien ✔✔✔')
            count += 1
        else:
            speak(significado)
            print('El verbo era: ', significado)
            print('intenta de nuevo ')
