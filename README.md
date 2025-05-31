# SHOM_InfoMarée

Intégration personnalisée Home Assistant pour récupérer les horaires de marée depuis le site officiel du SHOM via une API.

## 🧭 Fonctionnalités

- Affiche la prochaine marée (haute ou basse)
- Heure et hauteur de la marée
- Compatible avec l’interface graphique Home Assistant
- Rafraîchissement automatique des données

## 🔧 Installation

### Méthode 1 : via HACS (recommandée)

1. Dans HACS, ajoutez ce dépôt comme `Custom repository` de type `Integration`.
2. Recherchez “SHOM InfoMarée” et installez.
3. Redémarrez Home Assistant.

### Méthode 2 : manuelle

1. Copiez le dossier `shom_infomaree` dans : config/custom_components/shom_infomaree/

2. Redémarrez Home Assistant.

## ⚙️ Configuration

### Via l’interface

- Paramètres > Appareils & Services > Ajouter une intégration > SHOM InfoMarée

### Paramètres requis

- **Clé API** : obtenue depuis [https://data.shom.fr](https://data.shom.fr)
- **ID Station** : identifiant numérique d’un port/marégraphe
- **Nom personnalisé** (facultatif)

## 💡 Exemple d'entité

```yaml
sensor.prochaine_maree_a_brest:
state: "PM"
attributes:
 heure: "2025-06-01T03:21:00+02:00"
 hauteur: 5.3
 station: "010001"


