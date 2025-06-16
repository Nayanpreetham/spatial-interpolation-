This project performs spatial interpolation of precipitation data across the districts of Chhattisgarh, India, using the Ordinary Kriging method in Python. The goal is to create a continuous rainfall distribution surface from discrete observation points (station-level data), enabling better understanding of spatial rainfall variability for climatological and hydrological applications.

The analysis involves importing district-level rainfall data, preprocessing and analyzing it, modeling spatial autocorrelation using semivariograms, and applying geostatistical interpolation via the Kriging method. The output is a gridded rainfall surface that estimates precipitation at unsampled locations, based on nearby observed values.

Methodology
1.Data Collection & Preprocessing:
Precipitation data with latitude and longitude coordinates was collected for multiple districts in Chhattisgarh. Missing or inconsistent values were handled, and the dataset was cleaned for further geostatistical analysis.

2.Exploratory Data Analysis:
Basic statistical summaries were used to understand the spatial distribution and variability in rainfall. A shapefile of Chhattisgarh districts was used to define geographic boundaries for grid generation and masking.

3.Semivariogram Modeling:
A semivariogram was generated to quantify spatial dependence and determine the range, sill, and nugget. This model helped in understanding how rainfall similarity decays with distance, and was used to configure the Kriging interpolation.

4.Kriging Interpolation:
Using the OrdinaryKriging function from the pykrige Python package, rainfall values were interpolated over a regular grid across Chhattisgarh. This allowed estimation of rainfall at locations where no measurements were available.

5.Validation:
Model performance was evaluated using error metrics like Root Mean Square Error (RMSE) and Mean Absolute Error (MAE) through cross-validation techniques. This helped assess the reliability of predictions and ensured the robustness of the interpolation.

Outcome
The project successfully generated a gridded precipitation surface over Chhattisgarh using the Kriging interpolation method. The model accurately captured spatial trends in rainfall, providing a strong base for climate analysis, hydrological modeling, and policy-level planning. Kriging's use of spatial autocorrelation made it more reliable than simpler interpolation methods like IDW or linear interpolation.
