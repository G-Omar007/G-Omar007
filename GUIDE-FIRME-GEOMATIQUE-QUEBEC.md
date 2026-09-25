# Guide : créer une firme en géomatique au Québec

> Guide de démarrage pratique. Les montants et seuils changent souvent : vérifiez-les
> toujours sur le site officiel indiqué avant de faire une démarche.

---

## 1. Définir votre créneau (et savoir ce qui est réglementé)

C'est **la première décision**, parce qu'elle détermine les permis dont vous aurez besoin.

| Créneau | Réglementé ? | Ce qu'il faut |
|---|---|---|
| **Arpentage foncier** : certificat de localisation, bornage, piquetage, cadastre, description technique | **Oui, actes réservés** | Être membre de l'**Ordre des arpenteurs-géomètres du Québec (OAGQ)**, ou embaucher/s'associer avec un arpenteur-géomètre. Une société qui exerce la profession doit respecter les règles de l'Ordre sur l'exercice en société. |
| SIG, cartographie, analyse spatiale, géodonnées municipales | Non | Aucun permis particulier |
| Levés topographiques et relevés pour l'ingénierie, sans limites de propriété | Non (en général) | Titre de **technologue professionnel (T.P.)** à l'OTPQ recommandé, pas obligatoire |
| Photogrammétrie et relevés par drone, LiDAR | Non pour la géomatique, **oui pour le vol** | Certificat de pilote de drone de **Transports Canada** (voir section 4) |
| Télédétection, imagerie satellite | Non | — |
| Développement logiciel et géo-web (WebSIG, applications, API) | Non | — |
| Scan 3D, BIM, jumeaux numériques | Non | — |

**Conseil :** sans permis d'arpenteur-géomètre, commencez par des services non réservés
(SIG, drone, cartographie, BIM). Vous pourrez offrir l'arpentage foncier plus tard en vous
associant avec un a.-g.

---

## 2. Choisir la forme juridique

| Forme | Avantages | Inconvénients |
|---|---|---|
| **Entreprise individuelle** | Simple, peu coûteuse, idéale pour tester le marché | Responsabilité personnelle illimitée |
| **Société par actions (inc.) provinciale** (Registraire des entreprises du Québec) | Responsabilité limitée, taux d'impôt des PME, crédibilité auprès des clients | Plus de frais comptables, déclarations annuelles |
| **Société par actions fédérale** (Corporations Canada) | Protection du nom partout au Canada | Il faut **aussi** s'immatriculer au Québec (REQ) |
| **Société en nom collectif (S.E.N.C.)** | Pour démarrer à plusieurs | Responsabilité solidaire des associés |

**Recommandation courante :** une société par actions provinciale si vous visez des
contrats avec des municipalités, des ministères ou des firmes d'ingénierie, puisque la
responsabilité professionnelle et la crédibilité comptent. Consultez un comptable (CPA)
avant de choisir.

**Démarches :**
1. Vérifier que le nom est disponible (recherche au **Registre des entreprises du Québec**). Le nom doit être conforme à la **Charte de la langue française**.
2. Immatriculer ou constituer l'entreprise au **REQ** : vous obtenez un **NEQ** (numéro d'entreprise du Québec).
3. Ouvrir un compte bancaire d'entreprise.

---

## 3. Inscriptions fiscales et obligations d'employeur

- **TPS/TVH et TVQ** : inscription obligatoire dès que vos revenus taxables dépassent
  **30 000 $** sur quatre trimestres consécutifs. Au Québec, c'est **Revenu Québec** qui gère
  les deux. L'inscription volontaire dès le début permet de récupérer les taxes payées sur
  l'équipement (drone, GNSS, logiciels).
- **Numéro d'entreprise (NE) fédéral** auprès de l'ARC (souvent obtenu automatiquement lors de l'immatriculation).
- **Si vous embauchez** : inscription aux retenues à la source (Revenu Québec et ARC), à la
  **CNESST**, au RQAP et au RRQ, ainsi qu'aux normes du travail.
- **Loi 25 (protection des renseignements personnels)** : désigner un responsable de la
  protection des renseignements personnels. C'est important en géomatique, puisque les
  adresses, les images aériennes et les données foncières peuvent être des renseignements
  personnels.

---

## 4. Drones (si vous faites de la photogrammétrie ou du LiDAR aérien)

Règles de **Transports Canada** (RAC partie IX) :
- **Immatriculer** tout drone de 250 g à 25 kg.
- **Certificat de pilote de drone** :
  - **Opérations de base** : examen en ligne.
  - **Opérations avancées** : examen, puis révision en vol. Ce certificat est nécessaire
    en espace aérien contrôlé (près des aéroports) et près des personnes. **En pratique,
    il est indispensable pour du travail commercial.**
  - Pour les vols **au-delà de la portée visuelle (BVLOS)** et les opérations complexes,
    il existe un cadre distinct (niveau 1 complexe). Vérifiez les exigences à jour sur le
    site de Transports Canada.
- Utiliser l'outil **NAV Drone** (NAV CANADA) pour les autorisations en espace contrôlé.
- Souscrire une **assurance responsabilité drone** (souvent exigée par les clients).

---

## 5. Assurances

- **Responsabilité professionnelle (erreurs et omissions)** : essentielle, puisqu'une
  erreur de coordonnées peut coûter cher à un client. Elle est obligatoire pour les
  membres d'un ordre professionnel.
- **Responsabilité civile générale** (travail sur chantier).
- **Assurance des biens et de l'équipement** : station totale, GNSS RTK, drone et scanneur
  laser représentent souvent des dizaines de milliers de dollars.
- **Cyberrisques** (hébergement des données des clients).

---

## 6. Équipement et logiciels (ordre de grandeur)

| Poste | Options | Budget indicatif |
|---|---|---|
| SIG | **QGIS** (gratuit), ArcGIS Pro (Esri Canada) | 0 $ à plusieurs milliers $/an |
| GNSS RTK | Emlid, Trimble, Leica, Topcon, Septentrio | 5 000 $ à 40 000 $ |
| Corrections RTK | Réseaux RTK commerciaux au Québec, ou votre propre base | Abonnement annuel |
| Drone de cartographie | DJI (vérifiez les restrictions des clients publics sur les marques), Wingtra, senseFly | 3 000 $ à 60 000 $ et plus |
| Photogrammétrie | Pix4D, Agisoft Metashape, DJI Terra | 0 $ à 5 000 $/an |
| Nuages de points | CloudCompare (gratuit), TerraSolid, Global Mapper | Variable |
| Station totale | Trimble, Leica, Topcon | 10 000 $ à 50 000 $ |
| Poste de travail | Processeur puissant, 64 Go de RAM, carte graphique | 3 000 $ à 6 000 $ |

**Astuce :** louez l'équipement coûteux (station totale, LiDAR) au début, et achetez-le
quand vous avez des contrats récurrents.

**Normes à maîtriser au Québec :** NAD83(SCRS), projection **MTM** (fuseaux 3 à 10) et UTM,
les points géodésiques du Québec (réseau géodésique du MRNF), et les **données ouvertes**
(Données Québec, Géoindex, Adresses Québec, LiDAR provincial du MRNF).

---

## 7. Financement

| Source | Pour qui |
|---|---|
| **Futurpreneur Canada** | Entrepreneurs de 18 à 39 ans : prêt et mentorat |
| **BDC** (Banque de développement du Canada) | Prêts de démarrage et d'équipement |
| **Investissement Québec** | Prêts et garanties |
| **Services Québec : Soutien au travail autonome (STA)** | Revenu de soutien pendant le démarrage (sous conditions) |
| **Fonds locaux d'investissement / MRC / PME MTL / Accès entreprise Québec** | Prêts et subventions locales, accompagnement |
| **Caisses Desjardins / banques** | Financement d'équipement |
| **PARI-CNRC** | Si vous développez une technologie (logiciel, IA géospatiale) |
| **Crédits RS&DE (fédéral et Québec)** | R-D en traitement de données, IA, algorithmes |
| **Mitacs** | Stagiaires universitaires subventionnés (Laval, Sherbrooke, UQAM, ETS, INRS) |

Autres soutiens : consultez le **Réseau Accès entreprise Québec** de votre MRC et
**Entreprises Québec** (entreprises.quebec), le guichet unique du gouvernement.

---

## 8. Trouver des clients au Québec

**Marchés porteurs :**
- **Municipalités et MRC** : matrice graphique, rôles d'évaluation, réseaux d'aqueduc et d'égout, inventaires d'actifs, plans d'urbanisme.
- **Firmes d'ingénierie** (sous-traitance) : levés, drone, modélisation 3D.
- **Hydro-Québec, ministère des Transports et de la Mobilité durable (MTMD), MRNF, ministère de l'Environnement.**
- **Mines et Plan Nord** : volumétrie de stocks, suivi de fosses.
- **Foresterie** : inventaires, LiDAR, cartographie écoforestière.
- **Environnement** : milieux humides, zones inondables (un marché en forte croissance depuis les nouvelles cartographies des zones inondables).
- **Agriculture de précision.**
- **Construction et immobilier** : BIM, suivi de chantier, volumes.

**Contrats publics :**
- Les appels d'offres publics sont sur **SEAO** (seao.gouv.qc.ca) : inscrivez-vous.
- Au-delà de certains seuils, une **autorisation de l'Autorité des marchés publics (AMP)**
  est requise pour conclure des contrats publics. Vérifiez les seuils en vigueur.
- Les petits contrats municipaux se donnent souvent **de gré à gré**, sous le seuil
  d'appel d'offres : rencontrez directement les responsables de la géomatique des MRC.

**Réseautage :**
- **AGMQ** (Association de géomatique municipale du Québec) : très utile pour le marché municipal.
- **Association canadienne des sciences géomatiques (ACSG / CIG)**.
- **OTPQ** et **OAGQ**.
- Colloques : congrès de l'AGMQ, Esri Canada User Conference, événements de l'Ordre.
- **LinkedIn** : publiez des études de cas (avant/après, cartes, modèles 3D).

---

## 9. Plan d'action : 90 premiers jours

**Mois 1 : fondations**
- [ ] Choisir le créneau et valider 2 ou 3 clients potentiels (appels, rencontres)
- [ ] Rédiger un plan d'affaires simple (le gabarit de la BDC ou de Futurpreneur suffit)
- [ ] Rencontrer un conseiller d'Accès entreprise Québec (gratuit) et un comptable
- [ ] Choisir le nom, vérifier sa disponibilité et réserver le nom de domaine

**Mois 2 : légal et financement**
- [ ] Immatriculer ou constituer l'entreprise au REQ (NEQ)
- [ ] S'inscrire à la TPS/TVQ et ouvrir un compte bancaire d'entreprise
- [ ] Souscrire les assurances
- [ ] Obtenir le certificat de pilote de drone avancé (si applicable)
- [ ] Déposer les demandes de financement

**Mois 3 : lancement commercial**
- [ ] Site web avec un portfolio : 3 projets démonstratifs faits à partir de données ouvertes du Québec
- [ ] Grille tarifaire (taux horaire, prix au km² ou à l'hectare pour le drone, forfaits)
- [ ] Inscription à SEAO et contact direct avec 20 MRC ou municipalités et 10 firmes d'ingénierie
- [ ] Modèles d'offre de service, de contrat et de conditions générales (propriété des données, limites de responsabilité, précision garantie)

---

## 10. Contacts utiles

- Entreprises Québec (guichet unique) : https://www.quebec.ca/entreprises-et-travailleurs-autonomes
- Registraire des entreprises du Québec : https://www.registreentreprises.gouv.qc.ca
- Revenu Québec, entreprises : https://www.revenuquebec.ca
- Ordre des arpenteurs-géomètres du Québec : https://oagq.qc.ca
- Ordre des technologues professionnels du Québec : https://otpq.qc.ca
- Transports Canada, drones : https://tc.canada.ca/fr/aviation/securite-drones
- SEAO : https://seao.gouv.qc.ca
- Autorité des marchés publics : https://amp.quebec
- Données Québec : https://www.donneesquebec.ca
- Futurpreneur : https://www.futurpreneur.ca
- BDC : https://www.bdc.ca

---

*Ce guide est informatif et ne remplace pas l'avis d'un avocat, d'un notaire ou d'un comptable.*
