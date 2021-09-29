import math

def main():
    
    name = "Picnic"
    radius = 6.83
    height = 10.16
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#1 {name} {storage_efficiency:.1f} ")

    name = "Tall"
    radius = 7.78
    height = 11.91
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#1 {name} {storage_efficiency:.1f} ")

    name = ""
    radius = 8.73
    height = 11.59
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#2 {storage_efficiency:.1f} ")

    name = ""
    radius = 10.32
    height = 11.91
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#2.5 {storage_efficiency:.1f} ")

    name = "Cylinder"
    radius = 8.73
    height = 11.59
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#3 {name} {storage_efficiency:.1f} ")

    name = ""
    radius = 13.02
    height = 14.29
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#5 {storage_efficiency:.1f} ")

    name = ""
    radius = 5.40
    height = 8.89
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#6Z {storage_efficiency:.1f} ")

    name = "short"
    radius = 6.83
    height = 7.62
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#8Z {name} {storage_efficiency:.1f} ")

    name = ""
    radius = 15.72
    height = 17.78
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#10 {storage_efficiency:.1f} ")

    name = ""
    radius = 6.83
    height = 12.38
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#211 {storage_efficiency:.1f} ")

    name = ""
    radius = 7.62
    height = 11.27
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#300 {storage_efficiency:.1f} ")

    name = ""
    radius = 8.10
    height = 11.11
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"#300 {storage_efficiency:.1f} ")

def cylinder_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

def cylinder_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

main()
