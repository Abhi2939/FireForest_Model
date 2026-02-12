def compute_spread_radius(severity,wind_speed,vegetation_density):

    if severity == "Low":
        base = 300
    elif severity == "Medium":
        base = 800
    else:
        base = 1500

    wind_multiplier = 1 + (wind_speed / 40)
    veg_multiplier = 1 + vegetation_density

    return int(base*wind_multiplier*veg_multiplier)
