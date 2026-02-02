import streamlit as st
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

st.set_page_config(page_title="EO NDVI Monitor", layout="centered")

st.title("🌍 Satellite-Based Vegetation Monitoring")
st.write("Compute, smooth, and segment NDVI from Sentinel-2 imagery")

# Upload EO bands
red_file = st.file_uploader("Upload Sentinel-2 Red Band (B04)", type=["tif"])
nir_file = st.file_uploader("Upload Sentinel-2 NIR Band (B08)", type=["tif"])

# Image processing controls
sigma = st.slider(
    "Gaussian smoothing strength (σ)",
    min_value=0.0,
    max_value=3.0,
    value=1.0,
    step=0.5
)

veg_threshold = st.slider(
    "Vegetation NDVI threshold",
    min_value=0.0,
    max_value=0.8,
    value=0.3,
    step=0.05
)

def load_band(file):
    with rasterio.open(file) as src:
        return src.read(1).astype("float32")

if red_file and nir_file:
    if st.button("Run EO Analysis"):
        red = load_band(red_file)
        nir = load_band(nir_file)

        # NDVI computation
        ndvi = (nir - red) / (nir + red)
        ndvi = np.clip(ndvi, -1, 1)

        # Spatial smoothing
        if sigma > 0:
            ndvi_processed = gaussian_filter(ndvi, sigma=sigma)
        else:
            ndvi_processed = ndvi

        # Vegetation segmentation
        vegetation_mask = ndvi_processed > veg_threshold

        # --- Plot NDVI ---
        fig1, ax1 = plt.subplots()
        im1 = ax1.imshow(ndvi_processed, cmap="RdYlGn")
        ax1.set_title("Processed NDVI")
        ax1.axis("off")
        plt.colorbar(im1, ax=ax1, label="NDVI")
        st.pyplot(fig1)

        # --- Plot Vegetation Mask ---
        fig2, ax2 = plt.subplots()
        ax2.imshow(vegetation_mask, cmap="Greens")
        ax2.set_title("Vegetation Segmentation")
        ax2.axis("off")
        st.pyplot(fig2)

        # --- Stats ---
        st.subheader("NDVI Statistics (Processed)")
        st.write(f"Mean NDVI: {np.nanmean(ndvi_processed):.2f}")
        st.write(f"Vegetated area (%): {vegetation_mask.mean() * 100:.1f}%")
