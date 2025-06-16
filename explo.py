import pandas as pd
from scipy.interpolate import griddata
import openpyxl

# Define file paths
precip_file = r"C:\Users\Nayan preetham\OneDrive\Desktop\Explo\files\precipitation data.xlsx"  # Replace with your file path
district_file = r"C:\Users\Nayan preetham\OneDrive\Documents\PROJECTS\Chhattisgarh_Districts.xlsx"  # Replace with your file path
output_file = r"C:\Users\Nayan preetham\OneDrive\Documents\PROJECTS\final output.xlsx" # Output file path

# Load the precipitation data
precip_df = pd.read_excel(precip_file)

# Strip spaces from column names to avoid errors
precip_df.columns = precip_df.columns.str.strip()

# Check the columns in the DataFrame
print("Precipitation Data Columns:", precip_df.columns)

# Load the district coordinates
district_df = pd.read_excel(district_file)

# Strip spaces from column names in district data
district_df.columns = district_df.columns.str.strip()

# Check the columns in the district DataFrame
print("District Data Columns:", district_df.columns)

# Prepare an output Excel writer
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Loop through each year in the precipitation data
    for year in sorted(precip_df['Year'].unique()):
        print(f"Processing year {year}")
        
        # Filter rows for the current year
        year_df = precip_df[precip_df['Year'] == year]
        
        # Prepare lists to store latitudes, longitudes, and precipitation data for interpolation
        latitudes = year_df['Latitude'].values
        longitudes = year_df['Longitude'].values
        monthly_precip = year_df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']].values
        annual_precip = year_df['Ann'].values
        
        # Interpolation for each district's coordinates
        interpolated_data = []
        for _, district_row in district_df.iterrows():
            district_name = district_row['District']  # Replace with actual column name if necessary
            district_lat = district_row['Latitude']
            district_lon = district_row['Longitude']
            
            # Interpolate monthly precipitation
            monthly_interp = griddata(
                (longitudes, latitudes), monthly_precip,
                (district_lon, district_lat), method='linear'
            )
            
            # Interpolate annual precipitation
            annual_interp = griddata(
                (longitudes, latitudes), annual_precip,
                (district_lon, district_lat), method='linear'
            )
            
            # Store the results for the current district
            interpolated_data.append([district_name] + list(monthly_interp.flatten()) + [annual_interp])
        
        # Create a DataFrame for the current year
        interpolated_df = pd.DataFrame(
            interpolated_data,
            columns=['District', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Ann']
        )
        
        # Write the data for the current year to the output file
        interpolated_df.to_excel(writer, sheet_name=f"Year_{year}", index=False)
        
    print(f"Output saved to {output_file}")

