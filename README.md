# YOLOv10 Object Detection Web App 🎯

[English](#english) | [Français](#français)

---

## English

### 🚀 Live Demo
[**Try it now on Streamlit Cloud!**](your-app-url-here)

### 📝 Description
A powerful web application for real-time object detection using YOLOv10. Upload images or videos and get instant detection results with bounding boxes and confidence scores.

### ✨ Features
- 🖼️ **Image Detection**: Upload JPG, PNG, or JPEG images
- 🎥 **Video Detection**: Process MP4 and AVI videos frame-by-frame
- 🌍 **Bilingual Interface**: Switch between English and French
- 📊 **Detailed Results**: View detected objects with confidence scores
- 💾 **Download Results**: Download processed videos with annotations
- ⚡ **Fast Processing**: Powered by YOLOv10n (nano model)

### 🛠️ Technologies Used
- **Streamlit**: Web application framework
- **YOLOv10**: State-of-the-art object detection model
- **OpenCV**: Image and video processing
- **Python**: Backend programming

### 📦 Installation

#### Prerequisites
- Python 3.8 or higher
- pip package manager

#### Local Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/yolov10-object-detection-streamlit.git
cd yolov10-object-detection-streamlit
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

### 📄 Project Structure
```
yolov10-object-detection-streamlit/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── packages.txt          # System dependencies for deployment
└── README.md             # This file
```

### 📋 Requirements
```txt
streamlit
ultralytics
opencv-python-headless
pillow
numpy
```

### 🌐 Deployment
This app is deployed on **Streamlit Community Cloud** (free tier).

To deploy your own version:
1. Fork this repository
2. Sign up at [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub account
4. Select your forked repository
5. Click "Deploy"!

### 🎯 Supported Objects
YOLOv10 can detect 80+ object classes including:
- People, vehicles, animals
- Common objects (chairs, tables, phones, etc.)
- Sports equipment
- And many more!

### 🤝 Contributing
Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

### 📝 License
This project is open source and available under the MIT License.

### 👤 Author
**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)

### 🙏 Acknowledgments
- [Ultralytics YOLOv10](https://github.com/THU-MIG/yolov10)
- [Streamlit](https://streamlit.io/)

---

## Français

### 🚀 Démo en Direct
[**Essayez maintenant sur Streamlit Cloud !**](your-app-url-here)

### 📝 Description
Une application web puissante pour la détection d'objets en temps réel utilisant YOLOv10. Téléchargez des images ou des vidéos et obtenez instantanément des résultats de détection avec des boîtes englobantes et des scores de confiance.

### ✨ Fonctionnalités
- 🖼️ **Détection d'Images**: Téléchargez des images JPG, PNG ou JPEG
- 🎥 **Détection Vidéo**: Traitez des vidéos MP4 et AVI image par image
- 🌍 **Interface Bilingue**: Basculez entre l'anglais et le français
- 📊 **Résultats Détaillés**: Visualisez les objets détectés avec scores de confiance
- 💾 **Télécharger les Résultats**: Téléchargez les vidéos traitées avec annotations
- ⚡ **Traitement Rapide**: Propulsé par YOLOv10n (modèle nano)

### 🛠️ Technologies Utilisées
- **Streamlit**: Framework d'application web
- **YOLOv10**: Modèle de détection d'objets de pointe
- **OpenCV**: Traitement d'images et de vidéos
- **Python**: Programmation backend

### 📦 Installation

#### Prérequis
- Python 3.8 ou supérieur
- Gestionnaire de paquets pip

#### Configuration Locale
1. Clonez le dépôt :
```bash
git clone https://github.com/yourusername/yolov10-object-detection-streamlit.git
cd yolov10-object-detection-streamlit
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancez l'application :
```bash
streamlit run app.py
```

4. Ouvrez votre navigateur et accédez à `http://localhost:8501`

### 📄 Structure du Projet
```
yolov10-object-detection-streamlit/
├── app.py                 # Fichier principal de l'application
├── requirements.txt       # Dépendances Python
├── packages.txt          # Dépendances système pour le déploiement
└── README.md             # Ce fichier
```

### 📋 Dépendances
```txt
streamlit
ultralytics
opencv-python-headless
pillow
numpy
```

### 🌐 Déploiement
Cette application est déployée sur **Streamlit Community Cloud** (niveau gratuit).

Pour déployer votre propre version :
1. Forkez ce dépôt
2. Inscrivez-vous sur [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connectez votre compte GitHub
4. Sélectionnez votre dépôt forké
5. Cliquez sur "Deploy" !

### 🎯 Objets Supportés
YOLOv10 peut détecter plus de 80 classes d'objets incluant :
- Personnes, véhicules, animaux
- Objets communs (chaises, tables, téléphones, etc.)
- Équipement sportif
- Et bien plus encore !

### 🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Suggérer de nouvelles fonctionnalités
- Soumettre des pull requests

### 📝 Licence
Ce projet est open source et disponible sous la licence MIT.

### 👤 Auteur
**Votre Nom**
- GitHub: [@yourusername](https://github.com/yourusername)

### 🙏 Remerciements
- [Ultralytics YOLOv10](https://github.com/THU-MIG/yolov10)
- [Streamlit](https://streamlit.io/)

---

## 📸 Screenshots / Captures d'écran

### Image Detection / Détection d'Image
![Image Detection](screenshots/image-detection.png)

### Video Processing / Traitement Vidéo
![Video Processing](screenshots/video-processing.png)

### Language Switch / Changement de Langue
![Language Switch](screenshots/language-switch.png)

---

## 🐛 Known Issues / Problèmes Connus
- Large video files may take longer to process / Les fichiers vidéo volumineux peuvent prendre plus de temps à traiter
- First run downloads the YOLOv10 model (~6MB) / La première exécution télécharge le modèle YOLOv10 (~6MB)

## 🔮 Future Improvements / Améliorations Futures
- [ ] Add more language options / Ajouter plus d'options de langue
- [ ] Support for webcam input / Support pour l'entrée webcam
- [ ] Custom model upload / Téléchargement de modèle personnalisé
- [ ] Batch processing / Traitement par lots
- [ ] Export results to CSV / Exporter les résultats en CSV

---

**⭐ If you found this project helpful, please consider giving it a star!**

**⭐ Si vous avez trouvé ce projet utile, pensez à lui donner une étoile !**

Streamlit link : https://mouad-baaziz-yolov10-object-detection-app.streamlit.app/
