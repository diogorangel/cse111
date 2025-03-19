import math
def compute_volume(radius, height):
    return math.pi * (radius ** 2) * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area

def compute_cost_efficiency(radius, height, cost):
    volume = compute_volume(radius, height)
    return volume / cost

def main():
    cans = [
        ("#1 Picnic", 6.83, 10.16, 0.28),
        ("#1 Tall", 7.78, 11.91, 0.43),
        ("#2", 8.73, 11.59, 0.45),
        ("#2.5", 10.32, 11.91, 0.61),
        ("#3 Cylinder", 10.79, 17.78, 0.86),
        ("#5", 13.02, 14.29, 0.83),
        ("#6Z", 5.40, 8.89, 0.22),
        ("#8Z short", 6.83, 7.62, 0.26),
        ("#10", 15.72, 17.78, 1.53),
        ("#211", 6.83, 12.38, 0.34),
        ("#300", 7.62, 11.27, 0.38),
        ("#303", 8.10, 11.11, 0.42)
    ]
    
    best_storage_efficiency = 0
    best_cost_efficiency = 0
    best_storage_can = ""
    best_cost_can = ""
    
    print(f"{'Can Size':<15}{'Storage Efficiency':>20}{'Cost Efficiency':>20}")
    for name, radius, height, cost in cans:
        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)
        print(f"{name:<15}{storage_efficiency:>20.4f}{cost_efficiency:>20.4f}")
        
        if storage_efficiency > best_storage_efficiency:
            best_storage_efficiency = storage_efficiency
            best_storage_can = name
        
        if cost_efficiency > best_cost_efficiency:
            best_cost_efficiency = cost_efficiency
            best_cost_can = name
    
    print(f"\nCan with best storage efficiency: {best_storage_can} ({best_storage_efficiency:.4f})")
    print(f"Can with best cost efficiency: {best_cost_can} ({best_cost_efficiency:.4f})")

if __name__ == "__main__":
    main()
