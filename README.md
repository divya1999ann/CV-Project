# 📡 Satellite-Based Vegetation Monitoring (NDVI)

An interactive Earth Observation (EO) web application for analyzing vegetation health using **Sentinel-2 multispectral satellite imagery**. The app computes **NDVI (Normalized Difference Vegetation Index)** from multi-band data and applies **image processing techniques** to enhance visualization for environmental monitoring.


## 🌍 Project Overview

This project demonstrates an **applied remote sensing workflow** commonly used in the space and geospatial sectors. Using Sentinel-2 imagery, the application transforms raw satellite data into **actionable vegetation insights** through NDVI computation and spatial filtering.

The app is designed as a lightweight, deployable **SaaS-style EO tool**, showcasing how satellite-acquired data can be processed, visualized, and interpreted in an operational context.



## ✨ Features

- Upload and process **Sentinel-2 multi-band NumPy (`.npy`) files**
- Compute **NDVI** using Red (B04) and Near-Infrared (B08) bands
- Apply **Gaussian spatial smoothing** (image processing) with real-time user control
- Visualize:
  - Raw NDVI
  - Smoothed NDVI
- Display summary statistics (mean, min, max NDVI)
- Fully deployable **Streamlit web application**



## 🛰 Data Source

- **Satellite:** Sentinel-2 (ESA Copernicus Programme)  
- **Product Level:** Level-2A (surface reflectance)  
- **Bands Used:**
  - B04 – Red (10 m)
  - B08 – Near Infrared (10 m)

Sample data is provided as a preprocessed multi-band NumPy array for efficient loading and web deployment.



## 🧠 Technical Approach

1. Load multi-band Sentinel-2 imagery stored as a NumPy array  
2. Extract Red (B04) and NIR (B08) bands  
3. Compute NDVI using the standard remote sensing formula  
4. Apply **Gaussian filtering** to reduce spatial noise  
5. Render interactive visualizations and summary statistics  

This workflow mirrors real-world EO pipelines used in **biodiversity, biomass, and land-use monitoring**.



## 🛠 Tech Stack

- **Language:** Python  
- **Libraries:**  
  - NumPy (numerical processing)  
  - SciPy (image processing)  
  - Matplotlib (visualization)  
  - Streamlit (web deployment)  
- **Domain:** Earth Observation, Remote Sensing, Image Processing  

---

## ▶️ Running the App Locally

```bash
pip install -r requirements.txt
streamlit run app.py
