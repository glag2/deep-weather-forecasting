import cdsapi

dataset = "reanalysis-era5-single-levels"
request = {
    "product_type": [
        "reanalysis",
        "ensemble_members",
        "ensemble_mean",
        "ensemble_spread"
    ],
    "variable": [
        "10m_u_component_of_wind",
        "10m_v_component_of_wind",
        "2m_temperature",
        "surface_pressure",
        "total_precipitation",
        "skin_temperature",
        "100m_u_component_of_wind",
        "100m_v_component_of_wind",
        "clear_sky_direct_solar_radiation_at_surface",
        "surface_net_solar_radiation",
        "surface_net_thermal_radiation",
        "high_cloud_cover",
        "low_cloud_cover",
        "medium_cloud_cover",
        "total_cloud_cover",
        "total_column_cloud_ice_water",
        "total_column_cloud_liquid_water",
        "convective_precipitation",
        "convective_rain_rate",
        "precipitation_type",
        "snow_density",
        "snowfall",
        "temperature_of_snow_layer",
        "soil_temperature_level_4",
        "soil_type",
        "vertical_integral_of_kinetic_energy",
        "vertical_integral_of_potential_internal_and_latent_energy",
        "convective_available_potential_energy",
        "friction_velocity",
        "zero_degree_level",
        "evaporation",
        "potential_evaporation"
    ],
    "year": ["2023"],
    "month": ["12"],
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
        "28", "29", "30"
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
    "download_format": "zip",
    "area": [75, -40, 10, 60]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()