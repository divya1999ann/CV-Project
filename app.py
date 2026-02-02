import streamlit as st
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from rasterio.io import MemoryFile

st.set_page_config(page_title="EO NDVI Monitor", layout="centered")

st.title("🌍 Satellite-Based Vegetation Monitoring")
st.write("Compute and analyze NDVI from Sentinel-2 imagery")

red_file = st.file_uploader("Upload Sentinel-2 Red Band (B04)", type=["tif"])
nir_file = st.file_uploader("Upload Sentinel-2 NIR Band (B08)", type=["tif"])

def load_band(uploaded_file):
    with MemoryFile(uploaded_file.read()) as memfile:
        with memfile.open() as dataset:
            return dataset.read(1).astype("float32")

if red_file and nir_file:
    if st.button("Run NDVI Analysis"):
        red = load_band(red_file)
        nir = load_band(nir_file)

        ndvi = (nir - red) / (nir + red)
        ndvi = np.clip(ndvi, -1, 1)

        ndvi_smoothed = gaussian_filter(ndvi, sigma=1)

        fig1, ax1 = plt.subplots()
        im1 = ax1.imshow(ndvi, cmap="RdYlGn")
        ax1.set_title("Raw NDVI")
        ax1.axis("off")
        plt.colorbar(im1, ax=ax1, label="NDVI")
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots()
        im2 = ax2.imshow(ndvi_smoothed, cmap="RdYlGn")
        ax2.set_title("Smoothed NDVI (Gaussian Filter)")
        ax2.axis("off")
        plt.colorbar(im2, ax=ax2, label="NDVI")
        st.pyplot(fig2)

        st.subheader("NDVI Summary (Smoothed)")
        st.write(f"Mean NDVI: {np.nanmean(ndvi_smoothed):.2f}")
        st.write(f"Min NDVI: {np.nanmin(ndvi_smoothed):.2f}")
        st.write(f"Max NDVI: {np.nanmax(ndvi_smoothed):.2f}")
