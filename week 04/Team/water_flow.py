#Author : Diogo Rangel Dos Santos
# Water Flow Calculations

def water_column_height(tower_height, tank_height):
    """Calculate the water column height from tower height and tank wall height."""
    return tower_height + (3 * tank_height / 4)

def pressure_gain_from_water_height(height):
    """Calculate the pressure gain from a water column height."""
    water_density= 998.2
    gravity = 9.80665
    return (water_density * gravity * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity ):
    """Calculate the pressure loss due to friction in a pipe."""
    if pipe_diameter == 0 or pipe_length == 0 or friction_factor == 0 or fluid_velocity == 0:
        return 0.0
    water_density = 998.2
    return (-friction_factor * pipe_length * water_density * (fluid_velocity ** 2)) / (2000 * pipe_diameter)