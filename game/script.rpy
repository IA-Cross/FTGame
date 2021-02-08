# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Desconocido")
define i = Character(_("Yo"), color= "0099FF")
define l = Character(_("Lucy"), color= "#FFE920")
define n = Character("Natsu")
define h = Character("Happy")
define mk = Character(_("Makarov"), color= "FFFF00")
define ms = Character(_("Mirajane"), color= "C79BF2")
image barra = "Barra.jpg"
image ms1 = "Mirajane_Strauss.png"
image Prota = "Protagonista.png"
image cuarto lucy = "Lobby_in_Lucy's_house.jpg"
image magnolia = "Magnolia.jpg"
image lucy1 = "Lucy1.png"
image portachico = "protachico.png"
image negro = "negro.jpg"
image makarov1 = "MakarovUno.jpg"
image makarov2 = "Makarov_Joven.png"
image makarov = "makarov_dreyar_render_by_asanoroxkeigo-d5biit7.png"
image aldea1 = "Merveille's_Village.png"
image calle = "callesdemagnolia.jpg"
image habitación1 = "habitación1.jpg"
image Gremio = "Gremio.jpg"
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene imagen uno

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.
    
    scene negro with dissolve
    play music "04 - Tsuioku ~Mezameru Tamashii~.mp3"
    
    
    show Prota with dissolve
    "Cuando era pequeño vivía en un pueblo tranquilo" with dissolve
    "hasta que un día apareció una bestia enorme." with dissolve
    "Destruía todo lo que veía, desde plantaciones hasta casas y edificios." with dissolve
    "La gente ya cansada de vivir así, acordaron hacer una petición a un gremio de magos, famosos por causar
       gran destrucción y ser fieros luchadores, el gremio era llamado {w}{b}Fairy Tail.{/b}" with dissolve
    "Una mañana apareció un hombre bajito y de pelo amarillo, decía ser del gremio, así que los adultos lo llevaron a donde
       estaba la bestia, yo los seguí a lo lejos y escondido." with dissolve
    "Al llegar pidió que todos se alejaran para que pudiera comenzar" with dissolve
    "El hombre de la nada comenzó a crecer hasta volverse del tamaño de una montaña"
    hide Prota with dissolve
    play music "08 - Makarov.mp3"
    scene makarov1 with dissolve
    "y atacó a una enorme bestia mágica con una sonrisa y ojos llenos de emoción, 
       aunque la bestia era más fuerte él, nunca tuvo siquiera el pensamiento de rendirse en ningún momento."
    "El monstruo se recuperó rapidamente y arremetió con un fuerte golpe de cola"
    "Hubo un gran intercambio de golpes, donde no se veía un claro ganador"
    "La batalla fue reñida, pero el mago encontrando una abertura en su defensa 
     logró conectar muchos puñetazos logrando lanzarlo por los aires perdiendolo en el horizonte." with dissolve
    
    "Cansado y herido volvío a su tamaño normal"
    play music "29 - Kizuna.mp3"
    scene aldea1 with dissolve
    "De la emoción me caí en unas ramas secas, gracias a eso me vio
       escondido detrás de una roca, lentamente se acercó y me dijo:"
    show makarov2 with dissolve
    e "Por tu cara, parece que te gustó"
    i "¿Señor, no le dio miedo esa cosa?"
    e "No importa si daba miedo, un mago de Fairy Tail jamás huye, y no importa lo fuerte que sea, lo importante es que le hagas frente.
       Recuerda eso cada vez que te enfrentes a algo."
    hide makarov2 with dissolve
    i "Desde entonces sueño con convertirme en un mago poderoso y unirme al gremio de ese gigante"
    scene negro with dissolve
    
    "11 AÑOS DESPUÉS"
    
    
    scene magnolia with dissolve
    play music "20 - Lucy no Theme.mp3"
    show Prota with dissolve
    
    "Por fin podré entrar a un gremio."
    "Después de un largo camino por fin he llegado a Magnolia"
    i "¡Fairy Tail {w=2}allá voy!"
    "Primero lo primero"
    i  "Necesito buscar ha alguien del gremio..."
    show negro with dissolve
    scene calle
    hide negro with dissolve
    
    "Ya ha pasado mucho y no veo a nadie..."
    "Ha! Por fin!
     Creo que la de allá es Lucy... aunque no se si de verdad es ella"
    "¿Debería hablarle?"
    menu:
     "Vamos":
        i "Le hablaré!"
        jump lucy
        
     "Mejor no":
        jump juvia
    label lucy:
    i "Lucy!!! Hola!"
    
    hide Prota with dissolve
    show lucy1 with dissolve:
        ypos 200 xpos 800
    
    l "Hola! ¿Quién eres?"
    i "Soy solo un mago nuevo en la ciudad"
    i "¿Eres de Fairy Tail cierto?"
    l "Si, es un gremio asombroso"
    i "Guao! es mi sueño unirme a tu gremio, de hecho a eso he venido"
    i "¿Cómo pudiste entrar tú? ¿Hay algún requisito o algo?"
    l "Pues realmente tuve suerte, en una ciudad cercana me encontré a Natsu y el me recomendó"
    l "Como tú también fue mi sueño desde pequeña"
    l "Una vez de chica, el carruaje donde viajaba se descontroló, tenia mucho miedo,
       pero de repente sentí que alguién lo detuvo."
    l "No me dejó verle la cara pero ví en su mano la marca de Fairy Tail"
    l "Ahora que lo pienso... se parecia mucho a la mia..."
    l "Pero bueno dejando eso de lado.{p}¿quieres que te ayude a entrar?"
    
    menu:
        "¿¡Enserio!? Claro!":
         l "Genial, si lo necesitas te ayudaré."
        "no, gracias":
         l "Bueno, como tú quieras."
    l "Bien, supogo que querras instalarte en la ciudad primero
     así que nos vemos en el gremio "
    i "Si, claro nos vemos!"
    "Es cierto, entre tanta emoción olvidé buscar una habitación" with dissolve
    "Creo que en la otra calle había una habitación en renta"
    scene habitación1 with fade
    "No es mucho, pero me es suficiente"
    "Aunque ya me quedé sin dinero, ojalá no sea un problema"
    "Dejaré mis cosas y me dirigiré al gremio, ojalá no sea tan dificil que me acepten"
    
    play music "29 - Kizuna.mp3"
    scene calle with dissolve
    "La verdad me he aventurado a esta ciudad guiado por mi entusiasmo"
    "Realmente no me he detenido mucho a pensar en el cómo causar una buena primera impresión 
    al maestro del gremio y así aumentar mis posibilidades para poder entrar."
    "Hace mucho que esperaba que este día llegara, pero por alguna razón nunca me puse a pensar en lo que haría."
    "Bueno, hoy es un momento decisivo así que lo afrontaré sin miedo y… con improvisación. 
     Allá voy Fairy Tail!!"
    
    scene negro with dissolve
    play music "01 - FAIRY TAIL Main Theme.mp3"
    scene Gremio with dissolve
    "¡Guao que grande!"
    "De solo verlo me estoy emocionando, estoy impaciente con hablar con el maestro Makarov"
    "Allá va"
    i "¡Maestro Makarov! Puedo hablar con usted un momento, me interesaría muchísimo unirme a su gremio."
    "Talves me apresuré un poco, pero es que ya no aguanto las ansias"
    show makarov with dissolve:
        ypos 200 xpos 800
    mk "Claro chico, pasa y habla con Mirajane Strauss 
        ella te hará una pequeña entrevista y te explicará cómo funciona todo" 
    mk "La podrás encontrar en la barra del bar; y si después de esto ella te da su visto bueno ven a hablar conmigo."
    i "¡Claro! Muchas gracias"
    hide makarov with dissolve
    "Genial, al parecer empecé muy bien, solo queda esa entrevista."
    "Estoy nerviosísimo… aunque será mejor que no tarde, entre ya y la busque"
    scene barra with dissolve
    "¡Es increíble! Es también gigante por dentro, aunque si no supiera que es un gremio de magos, 
     pensaría que es solo un bar enorme, hay muchos tomando y hay mucho ruído, donde estará la barra… ha allá"
    i "Hola ¿qué tal? Busco a Mirajane Strauss"
    ms "Soy yo, ¿qué se te ofrece?"
    play music "18 - Nakama Tachi.mp3"
    show ms1 with dissolve:
        ypos 200 xpos 800
    i "Excelente, me presento mi nombre es  ----- mucho gusto y me gustaría unirme a su gremio, hablé con el maestro 
       y me dijo que te buscara para que me hicieras una entrevista."
    ms "¡Un chico nuevo excelente! estaré encantada de explicarte todo, solo dame un momento que termine con algunas cosas y te atiendo."
    i "Claro, esperaré"
    "Me le quedo viendo un momento mientras ella limpia los vasos usados y sirve más bebidas."
    "Es bastante guapa y además tiene una voz muy dulce"
    "Ahora que me doy cuenta hay muchas chicas bastante bellas en este gremio, creo que esto es todo un bonus"
    "¡Que me pasa! no me puedo distraer, en este momento tengo que concentrarme en la entrevista, ya después podré
     pensar en ese tipo de cosas"
    "Ahora si ¿en qué estaba?"
    "Aquí acaba la demo, si quieres contribuir con tu opinión acerca de las funciones y el como podría acabar
    escribeme en mis redes sociales"
    "Youtube: FuryBlade Producciones
    Twitter: @lagger177 o Facebook: FuryBlade"

    # This ends the game.

    return
