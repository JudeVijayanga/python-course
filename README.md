# python-course
# SED generator  
A Python tool to generate spectral energy distributions (SEDs) from galaxy photometry and compute FIR luminosity, dust temperature, and UV luminosity.

## Overview  
This package reads in galaxy photometry (in units of mJy) and produces:
- Total far-infrared (FIR) luminosity (units: L\(_\odot\)) by integrating over the 8 μm to 1000 μm rest-frame range.  
- Dust temperature (units: K) using the modified greybody + power-law SED formulation of Casey (2012). :contentReference[oaicite:1]{index=1}  
- UV luminosity (units: L\(_\odot\)) by selecting the rest-frame luminosity at 1500 Å.

## Key Components  
- `genSED.py` – the main program. Provide observed photometry in mJy and this script orchestrates SED generation and output.  
- `input.py` (sub-package) – handles reading and preprocessing of photometric input data.  
- `checkpoint.py` – module supporting read/write of checkpoint files (e.g., HDF5) for storing intermediate or final results.  
- `sun.py`, `planet.py`, `solarsystem.py`, `utils/` – other modules for broader astrophysical modelling (if relevant to your package structure).

## The Casey (2012) SED Model  
The far-infrared SED is modelled as a combination of a modified greybody and a mid-IR power-law. In simplified form:

\[
S_\nu \propto \left(1 - e^{-\tau(\nu)}\right)\,B_\nu(T)\;+\;A\,\nu^{-\alpha}
\]

where  
- \(B_\nu(T)\) is the Planck function at temperature \(T\).  
- \(\tau(\nu) = (\nu/\nu_0)^\beta\) is the optical depth, with \(\beta\) the dust emissivity index. :contentReference[oaicite:2]{index=2}  
- The power-law term (with slope \(\alpha\)) captures the mid-IR component. :contentReference[oaicite:3]{index=3}  

From Casey (2012), typical values include \(\beta \approx 1.6\) and \(\alpha \approx 2.0\). :contentReference[oaicite:4]{index=4}  

Using this SED, the total FIR luminosity is computed as:

\[
L_{\rm FIR} = 4\pi\,D_L^2\,\int_{\nu_{\rm max}(1000\,\mu\mathrm{m})}^{\nu_{\rm min}(8\,\mu\mathrm{m})} S_\nu\,d\nu
\]

where \(D_L\) is the luminosity distance.

Dust temperature \(T\) is inferred from the SED peak (or directly via fitting) and UV luminosity is derived at rest-frame 1500 Å.

## Usage  
1. Prepare your photometry input in units of mJy (observed frame).  
2. Run:
   ```bash
   python3 genSED.py --input your_photometry_file.csv

