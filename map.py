"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-06
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

Ce fichier fait partie du projet `ocp3`
"""
import os

# CONFIGURATION

# Elements dispo dans le labyrinthe
MAZE_ELEMENTS = {'wall': '.',
                 'exit': 'U',
                 'robo': 'X',
                 'void': ' '}
# Messages d'erreurs
ERR_ = "#!@?# Oups… "
ERR_MAP_FILE = ERR_ + "carte «{}» inaccessible!"

MIN_MAP_SIDE = 3

MSG_DISCLAMER = "Bienvenue dans Roboc."
MSG_START_GAME = "Votre partie commence"
MSG_END_GAME = "Fin du jeu."

class Map:
    """
    Fourni les moyens necessaire a l'utilisation d'un fichier carte.

    Controle de coherance sur la carte choise, deplace le robo en
    fonction des commandes du joueur jusqu'en fin de partie.
    """

    def __init__(self, map_file):
        """
        Initialisation de la carte utilise

        Instancie un objet Map avec les attributs suivant:

        :var int status: Etat de l'objet apres le deplacement
        :var str status_message: Message relatif au deplacement
        :var int _column_nb: Nbre de colonne du labyrinte (1ere ligne)
        :var str _data_text: Contenu du labyrinte
        :var str _element_under_robo: Element sous le robot
        :var int _line_nb: Nbre de ligne du labyrinte
        :var int _robo_position: position du robo dans _data_text

        :param map_file: fichier «carte» avec chemin relatif
        :rtype map: str()
        :return: None
        """
        # Chargement du fichier carte choisi
        if os.path.isfile(map_file) is True:
            with open(map_file, "r") as map_data:

                # contenu de la carte en texte
                self._data_text = map_data.read()

                # contenu de la carte ligne a ligne
                map_data_list = self._data_text.splitlines()

            # nbre de colonne de la 1ere ligne de la carte
            try:
                self._column_nb = len(map_data_list[0]) + 1
            except IndexError:
                self._column_nb = 0

            # nbre de ligne de la carte
            try:
                self._line_nb = len(map_data_list)
            except IndexError:
                self._line_nb = 0

            # position du robot
            self._robo_position = self._data_text.find(
                MAZE_ELEMENTS['robo']
            )

            # element «sous» le robo, au depart
            self._element_under_robo = MAZE_ELEMENTS['void']

            # Add map checking here

            self.status = True
            self.status_message = MSG_START_GAME

        # Erreur de chargement du fichier
        else:
            self.status = False
            self.status_message = ERR_MAP_FILE.format(map_file)

    def map_print(self):
        """ Affiche la carte avec la position de jeu courante """
        print(self._data_text)
