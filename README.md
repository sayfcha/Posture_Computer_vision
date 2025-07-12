
#  Correcteur de posture – Vision par ordinateur

## Pourquoi ce projet ?

Comme beaucoup, je passe plusieurs heures par jour assis devant mon ordi pour étudier, coder ou bosser sur des projets. Et au fil du temps, j’ai remarqué un truc : même en essayant de bien m’asseoir, je finis souvent par me retrouver avec la tête penchée, le dos voûté ou les épaules affaissées. Bref, une mauvaise posture.

C’est pas super pour le dos, ni pour la concentration. Du coup, je me suis dit : pourquoi ne pas coder un programme qui **détecte automatiquement ma posture** via la webcam, et qui me **prévient quand elle se dégrade** ?

## L’idée

Utiliser la vision par ordinateur (avec OpenCV + MediaPipe) pour :
- détecter ma posture en temps réel,
- repérer quand elle devient mauvaise,
- et me notifier que je dois me redresser.

Un genre d’assistant silencieux qui veille sur ma colonne vertébrale.

## Ce que fait le programme pour l’instant

- Accès à la webcam
- Détection en temps réel des **points clés du haut du corps** (nez, épaules, hanches, etc.)
- Affichage des landmarks sur la vidéo
- Extraction des coordonnées utiles pour analyser la posture

C’est la **base technique**. L’analyse de posture arrive juste après.

## Ce que je prévois d’ajouter

- Détection automatique des mauvaises postures (ex : tête trop penchée, épaules désalignées)
- Alerte visuelle (ou sonore) quand c’est le cas
- Historique des erreurs de posture
- Éventuellement un petit score ou des stats

## Requirements 
 
installer les packages essentiels suivant pour pouvoir executer le programme:

```bash
pip install opencv-python mediapipe 


## Lancer le programme

```bash
python main.py




