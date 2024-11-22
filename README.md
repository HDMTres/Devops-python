# Microservice Calculateur de Santé avec CI/CD sur Azure

## **Objectif**
Ce projet vise à développer un microservice en Python pour le calcul de mesures de santé (**BMI** et **BMR**) à l'aide d'une API REST. L'application est conteneurisée avec Docker, gérée à l'aide d'un **Makefile**, et déployée sur **Azure** via un pipeline CI/CD avec **GitHub Actions**.

---

## **Calculs de Santé**

### **1. Body Mass Index (BMI)** :
Le BMI (Indice de Masse Corporelle) permet d'évaluer si une personne a un poids adapté par rapport à sa taille.

**Formule** :  
\[
BMI = \frac{\text{poids (kg)}}{\text{taille (m)}^2}
\]

### **2. Basal Metabolic Rate (BMR)** :
Le BMR (Taux Métabolique de Base) représente la quantité de calories nécessaires pour maintenir les fonctions vitales au repos.

**Formules (Harris-Benedict)** :  
- **Pour les hommes** :  
\[
BMR = 88.362 + (13.397 \times \text{poids (kg)}) + (4.799 \times \text{taille (cm)}) - (5.677 \times \text{âge (années)})
\]

- **Pour les femmes** :  
\[
BMR = 447.593 + (9.247 \times \text{poids (kg)}) + (3.098 \times \text{taille (cm)}) - (4.330 \times \text{âge (années)})
\]

---

## **Exigences du Projet**

### **1. Développement du Microservice :**
- Développer une API REST Flask avec deux endpoints :
  - **`/bmi`** : Calcule le BMI à partir de la taille (mètres) et du poids (kg).
  - **`/bmr`** : Calcule le BMR à partir de la taille (cm), du poids (kg), de l'âge, et du genre.

### **2. Conteneurisation avec Docker :**
- Créer un fichier `Dockerfile` pour conteneuriser l'application.

### **3. Orchestration avec Makefile :**
- Automatiser les tâches avec un Makefile :
  - **`make init`** : Installer les dépendances.
  - **`make run`** : Lancer l'application.
  - **`make test`** : Exécuter les tests.
  - **`make build`** : Construire l'image Docker.

### **4. Gestion des Dépendances :**
- Gérer les dépendances avec un fichier `requirements.txt`.

### **5. Tests :**
- Écrire des tests unitaires pour valider les calculs de BMI et de BMR, ainsi que les endpoints de l'API.

### **6. CI/CD avec GitHub Actions :**
- Mettre en place un pipeline CI/CD pour :
  - Automatiser les tests lors de chaque push sur la branche principale.
  - Déployer l'application sur **Azure App Service**.

### **7. Déploiement sur Azure :**
- Déployer le microservice conteneurisé sur **Azure App Service**.

---

## **Structure du Projet**

```plaintext
health-calculator-service/
├── app.py                   # API Flask avec endpoints /bmi et /bmr
├── health_utils.py          # Fonctions de calcul pour BMI et BMR
├── requirements.txt         # Fichier des dépendances Python
├── Dockerfile               # Fichier pour conteneuriser l'application
├── Makefile                 # Automatisation des tâches
└── templates/
    └── index.html/
├── tests/
│   └── test_health_utils.py # Tests unitaires pour BMI et BMR
└── .github/
    └── workflows/
        └── ci-cd.yml        # Pipeline CI/CD GitHub Actions
```

# Instructions
## 1. Lancer le Microservice Localement
Cloner ce dépôt :
```bash
git clone https://github.com/<votre-utilisateur>/health-calculator-service.git
cd health-calculator-service
```
Initialiser les dépendances :
```bash
make init
```
Lancer le microservice :
```bash
make run
```
## 2. Conteneurisation avec Docker
### Construire l'image Docker :
```bash

make build
```
Lancer le conteneur Docker :
```bash

docker run -p 5000:5000 health-calculator-service
```
## 3. Exécuter les Tests
Lancer les tests unitaires :
```bash

make test
```