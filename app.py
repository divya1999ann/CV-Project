import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

st.set_page_config(page_title="EO NDVI Monitor", layout="centered")

st.title("🌍 Sentinel-2 NDVI from NumPy file")
st.write("Upload a multi-band Sentinel-2 NumPy file (`all_bands.npy`) and compute NDVI.")

# File uploader
uploaded_file = st.file_uploader("Upload all_bands.npy", type=["npy"])

def compute_ndvi_from_npy(file):
    # Load multi-band array
    arr = np.load(file)  # shape: (bands, height, width)
    
    # Sentinel-2 band order (common convention):
    # B01, B02, B03, B04, B05, B06, B07, B08, B8A, B09, B10, B11, B12
    red = arr[3].astype("float32")  # B04 (Red)
    nir = arr[7].astype("float32")  # B08 (NIR)

    # NDVI computation
    ndvi = (nir - red) / (nir + red)
    ndvi = np.clip(ndvi, -1, 1)

    # Gaussian smoothing (image processing)
    ndvi_smoothed = gaussian_filter(ndvi, sigma=1)

    return ndvi, ndvi_smoothed

if uploaded_file:
    ndvi, ndvi_smooth = compute_ndvi_from_npy(uploaded_file)

    # Plot raw NDVI
    fig, ax = plt.subplots(figsize=(6, 6))
    im = ax.imshow(ndvi, cmap="RdYlGn")
    ax.set_title("Raw NDVI")
    ax.axis("off")
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="NDVI")
    st.pyplot(fig)

    # Plot smoothed NDVI
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    im2 = ax2.imshow(ndvi_smooth, cmap="RdYlGn")
    ax2.set_title("Smoothed NDVI (Gaussian Filter)")
    ax2.axis("off")
    plt.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04, label="NDVI")
    st.pyplot(fig2)

    # NDVI summary stats
    st.subheader("NDVI Summary (Smoothed)")
    st.write(f"Mean NDVI: {np.nanmean(ndvi_smooth):.2f}")
    st.write(f"Min NDVI: {np.nanmin(ndvi_smooth):.2f}")
    st.write(f"Max NDVI: {np.nanmax(ndvi_smooth):.2f}")
