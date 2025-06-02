<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Orange_logo.svg" alt="Orange Logo" width="150"/>
</p>

# Orange UHD TV - Intégration Home Assistant

![hacs badge](https://img.shields.io/badge/HACS-Custom-orange.svg)

Cette intégration permet de **contrôler un décodeur TV UHD d'Orange** directement depuis Home Assistant via le panneau `media_player`.

---

## 🔧 Fonctionnalités

- Allumer / Éteindre le décodeur
- Changer de chaîne
- Contrôler le volume (haut/bas)
- Envoyer des commandes IR personnalisées (par exemple `KEY_OK`, `KEY_UP`, `KEY_DOWN`)
- Support de l’intégration via `config_flow` (UI)

---

## 📦 Installation

### 1. Via [HACS](https://hacs.xyz/)

1. Allez dans **HACS > Intégrations > Trois points (⋮) > Dépôts personnalisés**
2. Ajoutez ce dépôt GitHub :

   ```
   https://github.com/SoFarSoGood86/homeassistant-orange-uhd-tv
   ```

   en tant que **Intégration**.
3. Recherchez `ORANGE UHD TV` dans HACS et installez-la.
4. Redémarrez Home Assistant.
5. Ajoutez l'intégration via **Paramètres > Appareils & Services > Ajouter une intégration > ORANGE UHD TV**

---

### 2. Installation manuelle

1. Téléchargez et extrayez ce dépôt.
2. Copiez le dossier `orange_uhd_tv` dans :
   ```
   custom_components/orange_uhd_tv/
   ```
3. Redémarrez Home Assistant.
4. Ajoutez l’intégration depuis l’interface utilisateur.

---

## ⚙️ Configuration

L’intégration supporte la configuration via l’interface graphique. Si besoin, voici un exemple YAML (optionnel) :

```yaml
media_player:
  - platform: orange_uhd_tv
    host: 192.168.1.20
    token: abcdef123456
```

> **Remarque** : la connexion dépend de votre méthode de communication (IR, HDMI-CEC, HTTP REST ou autre). Le backend doit être modifié en conséquence.

---

## 🛰️ Services personnalisés

L'intégration fournit un service pour envoyer des commandes spécifiques :

```yaml
service: orange_uhd_tv.send_command
data:
  command: "KEY_OK"
```

---

## 🚀 Exemple d'automatisation

Allumer le décodeur Orange UHD tous les jours à 19h :

```yaml
alias: Allumer la TV Orange à 19h
trigger:
  - platform: time
    at: "19:00:00"
action:
  - service: media_player.turn_on
    target:
      entity_id: media_player.orange_uhd_tv
```

---

## ❓ Support & Développement

Développé par **[@SoFarSoGood86](https://github.com/SoFarSoGood86)**  
Pull requests bienvenues !  
Si vous avez besoin de fonctionnalités supplémentaires (contrôle HDMI-CEC, Wi-Fi, infrarouge via ESPHome, etc.), ouvrez une *issue*.

---

## 📄 Licence

Ce projet est sous licence MIT.
