# SwitchInputCount

Un script Python qui compte les appuis sur chaque touche du clavier et certaines de la souris.

Le GUI ne fonctionne que si la page est HOST sur un serveur local. 

## Fontionnement :

  [Vous devez de python 3.10 ou supérieur, et de tous les librairies importées dans "count.pyw" ("main.py" étant le script de test et d'affichage console du fichier de sauvegarde]
  
  * Lancez "count.pyw" pour enregistrer les touches.
  
  * Pour lire le fichier de sauvegarde simplement : executer "main.py".


### Pour lancer le script de comptage automatiquement au lancement de l'ordinateur : placer un raccourci de "count.pyw" le dossier de démarage (shell:startup dans Win+R).

Plus de fonctionnalités seront devellopées à l'avenir...


## Notes :
* Si aucun fichier de sauvegarde n'est trouvé le script en créer un. Ce dernier ajouetera une variable et une valeur à chaque fois qu'une touche sera pressée pour la première fois.
* L'interface graphique en HTML étant peu pratique, un convertisseur vers CSV executable par Excel est en devellpement.
