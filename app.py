import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
from pathlib import Path
import os
import numpy as np
from PIL import Image

TEXTS = {
    "en": {
        "title": "YOLOv10 Object Detection",
        "subtitle": "Upload an image or video and get object detection results!",
        "upload": "Choose an image or video",
        "original_image": "Original Image",
        "uploaded_image": "Uploaded Image",
        "detection_results": "Detection Results",
        "detected_objects": "Detected Objects",
        "detection_details": "Detection Details",
        "detected_count": "Detected {} objects:",
        "confidence": "Confidence",
        "no_objects": "No objects detected",
        "processing_video": "Processing Video...",
        "processing_frame": "Processing frame {}/{}",
        "processed_frames": "✅ Processed {} frames!",
        "download_button": "📥 Download Processed Video",
        "error_video": "❌ Failed to create output video. The file is empty or doesn't exist.",
        "error_occurred": "An error occurred: {}",
        "output_path": "Output path: {}",
        "file_exists": "File exists: {}",
        "file_size": "File size: {} bytes",
        "language": "Language"
    },
    "fr": {
        "title": "Détection des Objets YOLOv10",
        "subtitle": "Téléchargez une image ou une vidéo et obtenez les résultats de détection d'objets !",
        "upload": "Choisir une image ou une vidéo",
        "original_image": "Image Originale",
        "uploaded_image": "Image Téléchargée",
        "detection_results": "Résultats de Détection",
        "detected_objects": "Objets Détectés",
        "detection_details": "Détails de Détection",
        "detected_count": "{} objets détectés :",
        "confidence": "Confiance",
        "no_objects": "Aucun objet détecté",
        "processing_video": "Traitement de la Vidéo...",
        "processing_frame": "Traitement de l'image {}/{}",
        "processed_frames": "✅ {} images traitées !",
        "download_button": "📥 Télécharger la Vidéo Traitée",
        "error_video": "❌ Échec de la création de la vidéo de sortie. Le fichier est vide ou n'existe pas.",
        "error_occurred": "Une erreur s'est produite : {}",
        "output_path": "Chemin de sortie : {}",
        "file_exists": "Le fichier existe : {}",
        "file_size": "Taille du fichier : {} octets",
        "language": "Langue"
    }
}

@st.cache_resource
def load_model():
    return YOLO("yolov10n.pt")

model = load_model()

st.sidebar.header("⚙️ Settings / Paramètres")
language = st.sidebar.radio(
    "Language / Langue:",
    options=["en", "fr"],
    format_func=lambda x: "English" if x == "en" else "Français",
    horizontal=True
)

t = TEXTS[language]

st.title(t["title"])
st.write(t["subtitle"])

uploaded_file = st.file_uploader(t["upload"], type=["jpg","png","jpeg","mp4","avi"])

if uploaded_file is not None:
    file_ext = uploaded_file.name.split('.')[-1].lower()

    if file_ext in ["jpg", "png", "jpeg"]:
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        
        st.subheader(t["original_image"])
        st.image(image, caption=t["uploaded_image"], use_container_width=True)
        
        st.subheader(t["detection_results"])
        results = model(image_np)
        
        result_img = results[0].plot()  
        
        result_img_rgb = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
        
        st.image(result_img_rgb, caption=t["detected_objects"], use_container_width=True)
        
        st.subheader(t["detection_details"])
        boxes = results[0].boxes
        if len(boxes) > 0:
            st.write(f"**{t['detected_count'].format(len(boxes))}**")
            for i, box in enumerate(boxes):
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                class_name = results[0].names[class_id]
                st.write(f"{i+1}. **{class_name}** - {t['confidence']}: {confidence:.2%}")
        else:
            st.write(t["no_objects"])
    
    elif file_ext in ["mp4", "avi"]:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}")
        temp_file.write(uploaded_file.read())
        temp_file.close()
        temp_file_path = temp_file.name
        
        try:
            st.subheader(t["processing_video"])
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            cap = cv2.VideoCapture(temp_file_path)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            cap.release()
            
            output_dir = Path("output")
            output_dir.mkdir(exist_ok=True)
            output_path = output_dir / "detected_video.mp4"
            
            if output_path.exists():
                os.remove(output_path)
            
            fourcc = cv2.VideoWriter_fourcc(*'avc1')  
            out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
            
            if not out.isOpened():
                st.error("Failed to create video writer. Trying alternative codec...")
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
            
            cap = cv2.VideoCapture(temp_file_path)
            frame_count = 0
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                results = model(frame, verbose=False)
                
                annotated_frame = results[0].plot()
                
                out.write(annotated_frame)
                
                frame_count += 1
                if frame_count % 10 == 0:  
                    progress = frame_count / total_frames
                    progress_bar.progress(progress)
                    status_text.text(t["processing_frame"].format(frame_count, total_frames))
            
            cap.release()
            out.release()
            
            progress_bar.empty()
            status_text.empty()
            
            if output_path.exists() and output_path.stat().st_size > 0:
                st.subheader(t["detection_results"])
                st.success(t["processed_frames"].format(frame_count))
                
                with open(output_path, 'rb') as video_file:
                    video_bytes = video_file.read()
                    st.video(video_bytes)
                
                st.download_button(
                    label=t["download_button"],
                    data=video_bytes,
                    file_name="detected_video.mp4",
                    mime="video/mp4"
                )
            else:
                st.error(t["error_video"])
                st.info(t["output_path"].format(output_path))
                st.info(t["file_exists"].format(output_path.exists()))
                if output_path.exists():
                    st.info(t["file_size"].format(output_path.stat().st_size))
            
        except Exception as e:
            st.error(t["error_occurred"].format(str(e)))
            import traceback
            st.code(traceback.format_exc())
            
        finally:
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)