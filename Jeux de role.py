#from interface import *
from interface_V3 import *
from random import randint
tab_nom=['Minotaure', 'Méduse', 'Chimère', 'Cerbère', 'Kraken', 'Dracula', 'Frankenstein', 'Pennywise ', 'Xénomorphe ', 'Cthulhu', 'Bowser', 'Ganondorf', 'Pyramid Head ', 'Darkrai ', 'Diablo', 'Slenderman', 'Baba Yaga', 'SCP-173', 'Titan colossal ', 'Loup-garou', 'Basilic', 'Sphinx', 'Harpie', 'Hydre de Lerne', 'Griffon', 'Yéti', 'Wendigo', 'Kitsune', 'Oni', 'Chupacabra', 'King Kong', 'Predator', 'Gremlins', 'Freddy Krueger', 'The Thing', 'Sephiroth ', 'Ridley ', 'Pyramid Head ', 'Dark Samus ', 'Giratina ', 'Loup-Garou', 'SCP-096', 'Titan colossal ', 'The Rake', 'Herobrine ', 'Djinn', 'Golem', 'Fenrir', 'Jörmungandr', 'La Bête du Gévaudan', 'Les Nazgûl ', 'Balrog ', 'Shelob ', 'Basilic ', 'Les Détraqueurs ', 'Enderman ', 'Wither ', 'Eater of Worlds ', 'Ludwig ', 'The Devourer ', 'L’Homme-Papillon ', 'Le Croque-Mitaine', 'SCP-173 ', 'La Llorona', 'La Tarasque', 'Tatzelwurm', 'Skvader', 'Hanako-san', 'Draugr', 'Revenant ', 'Le Roi des Rats', 'Bête de Bray Road', 'The Rake ', 'Vecna ', 'Zalgo', 'Tarasque', 'Amarok', 'Tlaltecuhtli', 'Pukwudgie', 'Kappa', 'L’Homme Invisible', 'Le Loup-Garou de Londres', 'Godzilla', 'Cthulhu ', 'Pennywise ', 'Springtrap', 'Giygas', 'Doom Slayer', 'The Flood', 'Nemesis ', 'Sirène Maléfique', 'Golem de Glace', 'Faucheuse', 'L’Ankou', 'Mimic', 'Géant de Pierre', 'Satyre Maléfique', 'Chimère ', 'Roc ', 'Manananggal', 'Goule', 'Spectre du Pont', 'Le Hollandais Volant', 'L’ombre Rampante', 'Kelpie', 'Bête du Dartmoor', 'Serpent à Plumes ', 'Tikbalang', 'Chevalier Squelette ']
tab_attaque=['Chargebestiale', 'Coupdehache', 'Rugissementintimidant', 'Piétinementécrasant', 'Frénésieberserk', 'Frappedecorne', 'Regardpétrifiant', 'Fouetdeserpents', 'Morsurevenimeuse', 'Charmemortel', 'InvocationdeGorgones', 'Jetd’acide', 'Flammesdraconiques', 'Morsuredelion', 'Dardempoisonné', 'Griffesaiguisées', 'Hurlementterrifiant', 'Sautféroce', 'Triplemorsureinfernale', 'FlammedesEnfers', 'CrocduStyx', 'Rugissementspectral', 'Regarddugardien', 'Morsureempoisonnée', 'Tentaculesécrasants', 'Torrentabyssal', 'Étreintesuffocante', 'Hurlementdesprofondeurs', 'Jetd’encreaveuglant', 'Vaguedestructrice', 'Morsurevampirique', 'Hypnose', 'Transformationenchauve-souris', 'Invocationdeloups', 'Régénérationsanguine', 'Ombrefurtive', 'Poingécrasant', 'Criderage', 'Résistanceélectrique', 'Lancerbrutal', 'Souffledevapeur', 'Chargeincontrôlée', 'Peurincarnée', 'Métamorphoseterrifiante', 'Manipulationmentale', 'Griffedeclowndémoniaque', 'Lévitationsurnaturelle', 'Téléportationsinistre', 'Morsureinterne', 'Griffesacérées', 'Queueperforante', 'Acidesanguin', 'Agilitéextrême', 'Embuscadefurtive', 'Tentaculescauchemardesques', 'Foliecosmique', 'Hurlementabyssal', 'Brumesurnaturelle', 'Regardapocalyptique', 'InvocationdesProfonds', 'Souffledefeu', 'Chargecarapace', 'Sautécrasant', 'PoingduroiKoopa', 'Ondedechoc', 'Lancerdehache', 'Frappemaléfique', 'Onded’énergieténébreuse', 'Épéespectrale', 'Invocationdesombres', 'Coupdepiedbrutal', 'Téléportation', 'Tranchemacabre', 'Lenteurimplacable', 'Regardoppressant', 'Rugissementspectral', 'Poidsécrasant', 'Lameensanglantée', 'Trounoir', 'Hypnose', 'Chocmental', 'Vortexnocturne', 'Lamespectrale', 'Éclipseobscure', 'Flammeinfernale', 'Explosiondémoniaque', 'Griffesduchaos', 'Cridedamnation', 'Invocationdedémons', 'Téléportation', 'Élongationdesmembres', 'Téléportation', 'Regardhypnotique', 'Présenceoppressante', 'Manipulationmentale', 'Crisilencieux', 'Voldesorcière', 'Griffecrochue', 'Malédictionobscure', 'Bouledefeumystique', 'Invocationdespectres', 'Métamorphoseanimale', 'Téléportationinstantanée', 'Frappebrisée', 'Immobilitémeurtrière', 'Présenceangoissante', 'Résistanceextrême', 'Assautéclair', 'Coupdepiedtitanesque', 'Ondedechoc', 'Rugissementdestructeur', 'Régénérationrapide', 'Poingécrasant', 'Murdeflammes', 'Morsuredévastatrice', 'Griffestranchantes', 'Hurlementdelalune', 'Chargebestiale', 'Instinctprimal', 'Rageberserk', 'Regardmortel', 'Jetdepoison', 'Sifflementparalysant', 'Camouflagereptilien', 'Morsurevenimeuse', 'Fouetdequeue', 'Énigmemaudite', 'Griffesantiques', 'Regardperçant', 'Ventdudésert', 'Volmajestueux', 'Rugissementmystique', 'Serresacérées', 'Hurlementstrident', 'Venttranchant', 'Vitessefulgurante', 'Pluiedeplumesempoisonnées', 'Volenpiqué', 'Multiplicationdestêtes', 'Morsuresempoisonnées', 'Régénérationrapide', 'Jetd’acide', 'Constrictionserpentine', 'Hurlementdeterreur', 'Serresroyales', 'Criperçant', 'Chargecéleste', 'Coupd’ailestranchant', 'Regardperçant', 'Prisemortelle', 'Poingdeglace', 'Souffleglacial', 'Camouflageneigeux', 'Rugissementterrifiant', 'Projectiondeneige', 'Chargefurieuse', 'Griffescauchemardesques', 'Hurlementdel’esprit', 'Faiminsatiable', 'Vitessesurnaturelle', 'Ombrefurtive', 'Possessionmaléfique', 'Flammesspirituelles', 'Illusionstrompeuses', 'Métamorphose', 'Coupdequeuefoudroyant', 'Hypnosemagique', 'Téléportationinstantanée', 'Marteaudémoniaque', 'Rugissementinfernal', 'Frappebrutale', 'Auraterrifiante', 'Peauindestructible', 'Invocationdefeuspectral', 'Morsurevampirique', 'Agilitésurnaturelle', 'Griffesacérées', 'Regardperçant', 'Criperçant', 'Sautmortel', 'Poingtitanesque', 'Rugissementbestial', 'Lancerd’objets', 'Chargedestructrice', 'Étreinteécrasante', 'Agilitéprimale', 'Tirauplasma', 'Camouflageoptique', 'Lamerétractable', 'Visionthermique', 'Frappebrutale', 'Piègeexplosif', 'Griffuressournoises', 'Sautmalicieux', 'Multiplication', 'Électricitéstatique', 'Morsurerapide', 'Ombrefurtive', 'Griffesoniriques', 'Manipulationdescauchemars', 'Téléportationdanslerêve', 'Éclatmaléfique', 'Illusionterrifiante', 'Contrôledelapeur', 'Métamorphose', 'Assimilationbiologique', 'Tentaculesperçants', 'Camouflageparfait', 'Résistanceextrême', 'Hurlementdeterreur', 'LameMasamune', 'Supernova', 'Téléportation', 'Barrièremagique', 'Invocationdemétéores', 'Regarddivin', 'Griffesperçantes', 'Souffledeplasma', 'Chargeaérienne', 'Morsurepuissante', 'Lancerdequeue', 'Évasionrapide', 'Tranchageaugrandcouteau', 'Marcheoppressante', 'Crispectral', 'Persécutionpsychologique', 'Exécutionbrutale', 'Étreintemaudite', 'Rayonphazon', 'Bouclierénergétique', 'Téléportation', 'Projectiondephazon', 'Lévitation', 'Griffespectrale', 'OmbreduNéant', 'Distorsion', 'Griffesfantomatiques', 'Rugissementspectral', 'Ondedel’Au-Delà', 'Vortexdimensionnel', 'Morsureféroce', 'Griffestranchantes', 'Hurlementlunaire', 'Instinctsauvage', 'Chargebestiale', 'Rageberserk', 'Sprintterrifiant', 'Cridedouleur', 'Démembrementinstantané', 'Résistancesurhumaine', 'Rageinarrêtable', 'Regardmaudit', 'Coupdepiedtitanesque', 'Ondedechoc', 'Rugissementdestructeur', 'Régénérationrapide', 'Poingécrasant', 'Murdeflammes', 'Griffesmeurtrières', 'Agilitébestiale', 'Cristrident', 'Attaquefurtive', 'Chargedestructrice', 'Morsuredéchirante', 'Hurlementapocalyptique', 'Griffuredivine', 'Frénésieberserk', 'ChargeduRagnarök', 'Regarddeloupancestral', 'Morsureempoisonnée', 'Constrictionocéanique', 'Jetd’acide', 'Vaguedéchaînée', 'Venindelafindumonde', 'Éclipseocéanique', 'Morsurebestiale', 'Hurlementeffrayant', 'Camouflagenocturne', 'Chargerapide', 'Griffesacérées', 'Instinctmeurtrier', 'Lamespectrale', 'Criparalysant', 'Ombremaléfique', 'Invocationdeténèbres', 'Voldevie', 'Apparitionfantomatique', 'Fouetdeflammes', 'Épéeinfernale', 'Rugissementinfernal', 'Ondedechocdémoniaque', 'Résistanceaufeu', 'Sauttitanesque', 'Morsureempoisonnée', 'Jetdetoileparalysant', 'Griffuresrapides', 'Charged’araignéegéante', 'Visiondansl’obscurité', 'Corruptiondesenvirons', 'Malédictiondunéant', 'Morsuresegmentée', 'Reproductionrapide', 'Pluied’acide', 'Corpsserpentin', 'Griffestranchantes', 'Régénérationmonstrueuse', 'Chargebestiale', 'Lamesacrée', 'Hurlementdeterreur', 'Frappedivine', 'Éruptionsanguinaire', 'Agilitéeffrayante', 'Rugissementassourdissant', 'Attaqueenspirale', 'Éclipseabyssale', 'Ombredestructrice', 'Chargeinfernale', 'Tentaculesperçants', 'Prédictionapocalyptique', 'Volrapide', 'Regardhypnotisant', 'Ondedechocpsychique', 'Créationdepeur', 'Disparitioninstantanée', 'Chuchotementsterrifiants', 'Manipulationdescauchemars', 'Mainsgriffues', 'Disparitiondansl’ombre', 'Auraeffrayante', 'Malédictiondesenfants', 'Téléportationinstantanée', 'Brisd’osfatal', 'Présenceeffrayante', 'Mouvementsultra-rapides', 'Torsionducou', 'Indestructibilité', 'Cridedeuilparalysant', 'Apparitionsoudaine', 'Manipulationdeseaux', 'Froidsurnaturel', 'Possessiond’enfants', 'Disparitiondanslebrouillard', 'Carapaceimpénétrable', 'Souffledefeu', 'Chargemassive', 'Rugissementdetitan', 'Queuedévastatrice', 'Piétinementbestial', 'Morsureempoisonnée', 'Griffestranchantes', 'Sautfoudroyant', 'Camouflageforestier', 'Sifflementparalysant', 'Étreintemortelle', 'Coupdebecrapide', 'Griffesacérées', 'Pluiedeplumestranchantes', 'Sautaérien', 'Visionperçante', 'Crid’alerte', 'Apparitionsoudaine', 'Possession', 'Crid’enfantterrifiant', 'Ombrerampante', 'Manipulationdesmiroirs', 'Toucherglacial', 'Épéemaudite', 'Résurrectioninfinie', 'Hurlementspectral', 'Auraglaciale', 'Forcesurnaturelle', 'Frappedesombres', 'Poingspectral', 'Régénérationpost-mortem', 'Regardhanté', 'Malédictiondutrépas', 'Frappemortelle', 'Vitesseeffrayante', 'Malédictiondelapeste', 'Morsuremultiple', 'Cristrident', 'Nuagetoxique', 'Griffesinfectées', 'Esquiverapide', 'Chargebestiale', 'Morsureprofonde', 'Rugissementglaçant', 'Instinctsauvage', 'Grifferapide', 'Agilitémonstrueuse', 'Morsuredévorante', 'Griffurerapide', 'Disparitiondansl’ombre', 'Criglaçant', 'Vuenocturne', 'Camouflagesurnaturel', 'Magienoire', 'Dominationmentale', 'Rayondeténèbres', 'Invocationdemorts']
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Personage:
    def __init__(self,nom,attaque,vie,defance,est_joueur=False):
        self.nom=nom
        self.attaque=attaque
        self.vie=vie
        self.vie_initiale=vie
        self.est_joueur=est_joueur
        self.defance=defance
        
    def est_vivant(self):
        return self.vie>0
    
    def demande_attaque(self):
        txt=""
        nb=1
        for i in self.attaque:
            txt+=f"{nb} ==>{i}       "
            nb+=1
        return txt
    
    
    def regenerrait(self):
        self.vie=self.vie_initiale
        affiche_grande("votre vie est en en etat maximal")
        
    
    def attaquer(self,attaque,enemie):
        affiche_grande(f"{self.nom} attaquer {enemie.nom} avec {attaque}")
        puissance=(self.defance*attaque[1])+(attaque[1]*0.5)
        enemie.vie=enemie.vie-puissance
        affiche_grande(f"il reste {enemie.vie} point de vie a {enemie.nom}")
    
    def affiche(self):
        return f"c'est {self.nom} il a {self.vie} point de vie \nses attaque sont {self.demande_attaque()}"
    def __str__(self):
        return f"c'est {self.nom} il a {self.vie} point de vie \nses attaque sont {self.demande_attaque()}"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def cree_joueur():
    affiche_grande("tu veux cree ton joueur")
    if choix_tab(["oui","non"])==1:
        joueur=["moha",[["feu",6],["l'eau",5],["vent",4],["terre",3],("electricite",2),("glace",1)],40,0.7]
        joueur=Personage(joueur[0],joueur[1],joueur[2],joueur[3],True)
        return joueur
    tob=[]
    nom=input_str("donne moi le nom de votre joueur : ")
    tob.append(nom)
    nb_attaque=20
    tab=[]
    for nb_att in range(6):
        nom=input_str(f"donne le nom de votre {nb_att+1}eme attaque :")
        affiche_grande(f"il vous reste {nb_attaque} point",25)
        puissance=input_int('donne la puissance de votre monster il doit etre entre 1 et 6 :')
        while True:
            if puissance>0 and puissance<7 and nb_attaque>0:
                break
            elif puissance<=0:
                affiche_grande("vous volez faire quoi faite le un peut plus fort",25)
            elif puissance>=7:
                affiche_grande("La c'est tres fort donne au monstre un peut de chace",25)
            elif nb_attaque<=0:
                puissance=1
                affiche_grande("vous etes conne mais je suis gentil",25)
                break
            puissance=input_int('donne la puissance de votre monster il doit etre entre 1 et 6 : ')
        nb_attaque-=puissance
        tab.append((nom,puissance))
    tob.append(tab)
    affiche_tab(tob)
    joueur=Personage(tob[0],tob[1],tob[2],tob[3],True)
    return joueur
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#joueur=cree_joueur()


def cree_chambre():
    chambres=[[] for _ in range(10)]
    for nb_chambre in range(10):
        for _ in range(nb_chambre+1):
            nom=tab_nom[randint(0,len(tab_nom)-1)]
            if nb_chambre<=2:
                vie=randint(0,30)
                deffance=randint(69,100)//100
            elif nb_chambre>2 and nb_chambre<=5:
                vie=randint(25,50)
                deffance=randint(50,80)//100
            elif nb_chambre>5 and nb_chambre<=8:
                vie=randint(40,70)
                deffance=randint(35,60)//100
            elif nb_chambre>8:
                vie=randint(59,90)
                deffance=randint(10,40)//100
            attaques=[]
            for _ in range(6):
                nom_attaque=tab_attaque[randint(0,len(tab_attaque)-1)]
                if nb_chambre<=2:
                    puissance=randint(1,4)
                elif nb_chambre>2 and nb_chambre<=5:
                    puissance=randint(2,8)
                elif nb_chambre>5 and nb_chambre<=8:
                    puissance=randint(4,10)
                elif nb_chambre>8:
                    puissance=randint(6,15)
                attaque=(nom_attaque,puissance)
                attaques.append(attaque)
            chambres[nb_chambre].append(Personage(nom,attaques,vie,deffance))
    return chambres
chambres=cree_chambre()

def chambre(chambres,joueur):
    for chambre in range(len(chambres)):
        affiche_grande(f"vous etes dans la chambre {chambre}",30)
        affiche_grande(f"il y a {len(chambres[chambre])} monstre dans la chambre",25)

        chambres[chambre]=[joueur]+chambres[chambre]
        tour=0
        joueur.regenerrait()
        while len(chambres[chambre])>1:

            liste=[]
            for i in range (len(chambres[chambre])):
                liste.append(f"{i} ==> {chambres[chambre][i].nom} avec {chambres[chambre][i].vie} point de vie")
            if tour%len(chambres[chambre])==0:
                attaque=joueur.attaque[randint(0,5)]
                nb_monstre=choix_tab(liste,1)           
                joueur.attaquer(attaque,chambres[chambre][nb_monstre])
                affiche_grande("dans la chambre il reste :")
                reste=[]
                for i in range (1,len(chambres[chambre])):
                    #affiche_grande(f"{i} ==> {chambres[chambre][i].nom} avec {chambres[chambre][i].vie} point de vie")
                    reste.append(f"{i} ==> {chambres[chambre][i].nom} a {chambres[chambre][i].vie} point de vie")
                affiche_tab(reste)
            else:
                monstre_en_attaque=chambres[chambre][randint(1,len(chambres[chambre]))-1]
                attaque=monstre_en_attaque.attaque[randint(0,5)]
                monstre_en_attaque.attaquer(attaque,joueur)
                affiche_grande("vous allez attaque avec{attaque}")
            tour+=1
            for i in range (len(chambres[chambre])):
                if chambres[chambre][i].vie<=0:
                    affiche_grande(f"{chambres[chambre][i].nom} est mort",25)
                    #print(f"{chambres[chambre][i].nom} est mort")
                    del chambres[chambre][i]
                    break
        affiche_grande("combat fini",30)

joueur=cree_joueur()
chambre(chambres,joueur)




#print(joueur)
#perssonage est mortelle ajoute cas de mort
