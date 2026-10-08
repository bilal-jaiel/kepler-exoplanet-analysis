# Dataset: Kepler Objects of Interest (KOI), cumulative table

| | |
|---|---|
| Source | NASA Exoplanet Archive, KOI cumulative table, as distributed on Kaggle: [Kepler Exoplanet Search Results](https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results) |
| Column definitions | [NASA Exoplanet Archive: KOI table columns](https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html) |
| Background | [NASA: Kepler mission](https://science.nasa.gov/mission/kepler/in-depth/) · [NASA: planet types](https://science.nasa.gov/exoplanets/planet-types/) |

## Files

| File | Rows × columns | Description |
|---|---|---|
| `cumulative.csv` | 9,564 × 50 | Raw cumulative KOI table |
| `cumulative_cleaned.csv` | 7,994 × 25 | Cleaned table produced by `notebooks/01_exploratory_and_multivariate_analysis.ipynb` (columns with no information or near-empty removed, rows with missing values dropped) |

Class balance (`koi_disposition`):

| | FALSE POSITIVE | CONFIRMED | CANDIDATE |
|---|---:|---:|---:|
| raw | 5,023 | 2,293 | 2,248 |
| cleaned | 3,921 | 2,281 | 1,792 |

## Main columns

- rowid: Unique identifier for each row in the dataset.
- kepid: Kepler ID, a unique identifier for the target star.
- kepoi_name: KOI name assigned by Kepler; identifies a target with at least one transit-like signal consistent with a planetary transit hypothesis.
- kepler_name: Official name of the planet if confirmed or validated.
- koi_disposition: Literature disposition of the KOI; can be CANDIDATE, FALSE POSITIVE, NOT DISPOSITIONED, or CONFIRMED.
- koi_pdisposition: Kepler pipeline disposition; can be CANDIDATE, FALSE POSITIVE, or NOT DISPOSITIONED.
- koi_score: Confidence score (0 to 1) for the KOI disposition; higher for more confident candidates, lower for false positives.
- koi_fpflag_nt / koi_fpflag_ss / koi_fpflag_co / koi_fpflag_ec: Flags indicating potential false positives from various analysis methods.
- koi_period: Orbital period of the candidate (days).
- koi_period_err1 / koi_period_err2: Errors on the orbital period.
- koi_time0bk: Time of first observed transit (Barycentric Kepler Julian Date).
- koi_time0bk_err1 / koi_time0bk_err2: Errors on the transit time.
- koi_impact: Transit impact parameter (distance from center of stellar disk in stellar radii).
- koi_impact_err1 / koi_impact_err2: Errors on impact parameter.
- koi_duration: Transit duration (hours).
- koi_duration_err1 / koi_duration_err2: Errors on transit duration.
- koi_depth: Transit depth (ppm).
- koi_depth_err1 / koi_depth_err2: Errors on transit depth.
- koi_prad: Planetary radius (Earth radii).
- koi_prad_err1 / koi_prad_err2: Errors on planetary radius.
- koi_teq: Equilibrium temperature of the planet (Kelvin).
- koi_teq_err1 / koi_teq_err2: Errors on equilibrium temperature.
- koi_insol: Insolation flux received by the planet (Earth flux units).
- koi_insol_err1 / koi_insol_err2: Errors on insolation flux.
- koi_model_snr: Signal-to-noise ratio from model fitting.
- koi_tce_plnt_num: Number of planets detected in the system.
- koi_tce_delivname: Name of the TCE (threshold crossing event) delivery file.
- koi_steff: Stellar effective temperature (Kelvin).
- koi_steff_err1 / koi_steff_err2: Errors on stellar temperature.
- koi_slogg: Stellar surface gravity (log g).
- koi_slogg_err1 / koi_slogg_err2: Errors on surface gravity.
- koi_srad: Stellar radius (solar radii).
- koi_srad_err1 / koi_srad_err2: Errors on stellar radius.
- ra / dec: Right ascension and declination of the target star (degrees).
- koi_kepmag: Kepler magnitude (brightness of the star).
