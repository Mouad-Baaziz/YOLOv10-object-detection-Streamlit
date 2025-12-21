import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
from pathlib import Path
import os
import numpy as np
from PIL import Image

# Load YOLOv10 model
@st.cache_resource
def load_model():
    return YOLO("yolov10n.pt")

model = load_model()

st.title("YOLOv10 Object Detection Web App")
st.write("Upload an image or video and get object detection results!")

# File uploader
uploaded_file = st.file_uploader("Choose an image or video", type=["jpg","png","jpeg","mp4","avi"])

if uploaded_file is not None:
    file_ext = uploaded_file.name.split('.')[-1].lower()

    if file_ext in ["jpg", "png", "jpeg"]:
        # Read image directly
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        
        # Display original image
        st.subheader("Original Image")
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        # Process image
        st.subheader("Detection Results")
        results = model(image_np)
        
        # Plot results with bounding boxes
        result_img = results[0].plot()  # This creates the image with boxes
        
        # Convert BGR to RGB (OpenCV uses BGR, Streamlit expects RGB)
        result_img_rgb = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
        
        st.image(result_img_rgb, caption="Detected Objects", use_container_width=True)
        
        # Display detection details
        st.subheader("Detection Details")
        boxes = results[0].boxes
        if len(boxes) > 0:
            st.write(f"**Detected {len(boxes)} objects:**")
            for i, box in enumerate(boxes):
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                class_name = results[0].names[class_id]
                st.write(f"{i+1}. **{class_name}** - Confidence: {confidence:.2%}")
        else:
            st.write("No objects detected")
    
    elif file_ext in ["mp4", "avi"]:
        # Save uploaded file temporarily
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}")
        temp_file.write(uploaded_file.read())
        temp_file.close()
        temp_file_path = temp_file.name
        
        try:
            st.subheader("Processing Video...")
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Open video to get properties
            cap = cv2.VideoCapture(temp_file_path)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            cap.release()
            
            # Create output directory
            output_dir = Path("output")
            output_dir.mkdir(exist_ok=True)
            output_path = output_dir / "detected_video.mp4"
            
            # Remove old output if exists
            if output_path.exists():
                os.remove(output_path)
            
            # Setup video writer with H264 codec (more compatible)
            fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H264 codec
            out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
            
            # Check if video writer opened successfully
            if not out.isOpened():
                st.error("Failed to create video writer. Trying alternative codec...")
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
            
            # Process video frame by frame
            cap = cv2.VideoCapture(temp_file_path)
            frame_count = 0
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Run detection on frame
                results = model(frame, verbose=False)
                
                # Plot results on frame
                annotated_frame = results[0].plot()
                
                # Write frame
                out.write(annotated_frame)
                
                # Update progress
                frame_count += 1
                if frame_count % 10 == 0:  # Update every 10 frames for performance
                    progress = frame_count / total_frames
                    progress_bar.progress(progress)
                    status_text.text(f"Processing frame {frame_count}/{total_frames}")
            
            cap.release()
            out.release()
            
            progress_bar.empty()
            status_text.empty()
            
            # Verify output file exists and has content
            if output_path.exists() and output_path.stat().st_size > 0:
                st.subheader("Detection Results")
                st.success(f"✅ Processed {frame_count} frames!")
                
                # Read and display video
                with open(output_path, 'rb') as video_file:
                    video_bytes = video_file.read()
                    st.video(video_bytes)
                
                # Provide download button
                st.download_button(
                    label="📥 Download Processed Video",
                    data=video_bytes,
                    file_name="detected_video.mp4",
                    mime="video/mp4"
                )
            else:
                st.error("❌ Failed to create output video. The file is empty or doesn't exist.")
                st.info(f"Output path: {output_path}")
                st.info(f"File exists: {output_path.exists()}")
                if output_path.exists():
                    st.info(f"File size: {output_path.stat().st_size} bytes")
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            import traceback
            st.code(traceback.format_exc())
            
        finally:
            # Clean up temporary file
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)