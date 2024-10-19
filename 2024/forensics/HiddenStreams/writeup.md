# Writeup : Résolution du challenge

## Contexte du challenge

Dans ce challenge forensique, nous avons été confrontés à un fichier EVTX (Event Log) de Windows.

## Étapes de résolution

### 1. Installation des outils nécessaires

Pour analyser le fichier EVTX, j'ai utilisé l'outil python3-evtx :

```bash
sudo apt install python3-evtx
```

### 2. Conversion du fichier EVTX en XML

J'ai utilisé l'outil evtx_dump.py pour convertir le fichier EVTX en format XML plus lisible :

```bash
evtx_dump.py Application.evtx > Application.xml
```

### 3. Analyse du fichier XML

Ayant l'intuition que le flag pourrait être encodé en base64, j'ai cherché des chaînes suspectes dans le fichier XML généré.

### 4. Découverte du flag encodé


```
strings -a Application.xml | grep -i Zmxh
<Data Name="Contents">ZmxhZ3tiZmVmYjg5MTE4MzAzMmY0NGZhOTNkMGM3YmQ0MGRhOX0=  </Data>
```

### 5. Décodage du flag

En décodant cette chaîne base64, nous obtenons le flag :

```
flag{bfefb89118303f44fa93d0c7bd40da9}
```


