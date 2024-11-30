import cdsapi

dataset = "reanalysis-era5-single-levels"

#Reanalysis combines model data with observations from across the world into a globally complete and consistent dataset using the laws of physics.
request = {
    "product_type": ["reanalysis"],
    "variable": [
        "10m_u_component_of_wind",
        "10m_v_component_of_wind",
        "2m_temperature",
        "surface_pressure",
        "total_precipitation",
        "skin_temperature",
        "100m_u_component_of_wind",
        "100m_v_component_of_wind",
        "mean_convective_precipitation_rate",
        "mean_evaporation_rate",
        "mean_potential_evaporation_rate",
        "mean_snowfall_rate",
        "mean_surface_runoff_rate",
        "mean_total_precipitation_rate",
        "clear_sky_direct_solar_radiation_at_surface",
        "surface_latent_heat_flux",
        "top_net_solar_radiation",
        "top_net_thermal_radiation",
        "cloud_base_height",
        "high_cloud_cover",
        "low_cloud_cover",
        "medium_cloud_cover",
        "total_cloud_cover",
        "total_column_cloud_ice_water",
        "total_column_cloud_liquid_water",
        "evaporation",
        "runoff",
        "convective_precipitation",
        "precipitation_type",
        "total_column_rain_water",
        "convective_snowfall",
        "snow_density",
        "snow_depth",
        "snow_evaporation",
        "snowfall",
        "soil_temperature_level_1",
        "soil_type",
        "air_density_over_the_oceans",
        "zero_degree_level"
    ],
    "year": ["2024"],
    "month": [
        "01"
    ],
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12",
        "13", "14", "15",
        "16", "17", "18",
        "19", "20", "21",
        "22", "23", "24",
        "25", "26", "27",
        "28", "29", "30",
        "31"
    ],
    "time": [
        "00:00", "01:00", "02:00",
        "03:00", "04:00", "05:00",
        "06:00", "07:00", "08:00",
        "09:00", "10:00", "11:00",
        "12:00", "13:00", "14:00",
        "15:00", "16:00", "17:00",
        "18:00", "19:00", "20:00",
        "21:00", "22:00", "23:00"
    ],
    "data_format": "grib",
    "download_format": "unarchived"
}
client = cdsapi.Client()
client.retrieve(dataset, request, target="January_2024.grib").download()