import tkinter as tk
import math

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)

    # drawing the sky
    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom)

    # drawing the ground
    draw_ground(canvas, scene_left, scene_top, scene_right, scene_bottom)

    # drawing the clouds
    draw_clouds(canvas, 100, 30, scale=1)
    draw_clouds(canvas, 140, 54, scale=1)
    draw_clouds(canvas, 60, 95, scale=1)

    #drawing the sun
    draw_sun(canvas, 600, 50, scale=1)

    # This is tree 1
    tree_center = scene_left + 200
    tree_top = scene_top + 100
    tree_height = 300
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    # This is tree 2
    tree_center = scene_left + 400
    tree_top = scene_top + 100
    tree_height = 300
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    # This is the building
    house_center = scene_left + 630
    house_top = scene_top + 100
    house_height = 300
    draw_house(canvas, house_center, house_top, house_height)

    # Window 1
    window_center = scene_left + 560
    window_top = scene_top + 50
    window_height = 300  
    draw_windows(canvas, window_center, window_top, window_height)

    # Window 2
    window_center = scene_left + 700
    window_top = scene_top + 50
    window_height = 300  
    draw_windows(canvas, window_center, window_top, window_height)

    # Window 3
    window_center = scene_left + 560
    window_top = scene_top + -20
    window_height = 300  
    draw_windows(canvas, window_center, window_top, window_height)

    # Window 4
    window_center = scene_left + 700
    window_top = scene_top + -20
    window_height = 300  
    draw_windows(canvas, window_center, window_top, window_height)

    # Drawing the door
    door_center = scene_left + 630
    door_top = scene_top + 100
    door_height = 300  
    draw_door(canvas, door_center, door_top, door_height)

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


def draw_sky(canvas, left, top, right, bottom):
    
    for i in range(top, bottom):
        canvas.create_line(left, i, right, i, fill="deepSkyBlue")
    
    for i in range(left, right):
        canvas.create_line(i, top, i, bottom, fill="deepSkyBlue")

def draw_clouds(canvas, clouds_left, clouds_top, scale=1):
    clouds_width = 100 * scale
    clouds_height = 50 * scale

    clouds_right = clouds_left + (clouds_width / 0.5)
    clouds_bottom = clouds_top + (clouds_height / 0.5)
    clouds_center_x = clouds_left + (clouds_width / 2)
    clouds_center_y = clouds_top + (clouds_height / 2)


    canvas.create_oval(clouds_left, clouds_top, clouds_right, clouds_bottom, fill="white", width=False)

def draw_sun(canvas, sun_left, sun_top, scale=1):
    sun_width = 100 * scale
    sun_height = 100 * scale
    ray_length = 90 * scale
    ray_width = 3 * scale
    ray_count = 12

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)


    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill="#FFF784", width=False)
    
    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width=ray_width, fill="#FFF784")

def draw_ground(canvas, left, top, right, bottom):
    top = 400
    bottom = 500

    for i in range(top, bottom):
        canvas.create_line(left, i, right, i, fill="limegreen")

    for i in range(left, right):
        canvas.create_line(i, top, i, bottom, fill="limegreen")

def draw_pine_tree(canvas, peak_x, peak_y, height):
    
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
        trunk_right, trunk_bottom,
        outline="gray20", width=1, fill="tan4")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
        skirt_right, skirt_bottom,
        skirt_left, skirt_bottom,
        outline="gray20", width=1, fill="dark green")

def draw_house(canvas, tip_point_x, tip_point_y, height):
    building_width = height / 1.5
    building_height = height / 1.5
    building_left = tip_point_x - building_width / 1.5
    building_right = tip_point_x + building_width / 1.5
    building_bottom = tip_point_y + height
    rect_height = height - building_height
    rect_bottom = tip_point_y + rect_height
    
    canvas.create_rectangle(building_left, rect_bottom, building_right, building_bottom, outline="grey", width=1, fill="grey")
    
def draw_windows(canvas, tip_point_x, tip_point_y, height):
    window_width = height / 2
    window_height = height / 10
    window_left = tip_point_x - window_width / 8
    window_right = tip_point_x + window_width / 8
    window_bottom = tip_point_y + height
    block_height = height - window_height
    block_bottom = tip_point_y + block_height
    
    canvas.create_rectangle(window_left, block_bottom, window_right, window_bottom, outline="white", width=1, fill="lightgrey")

def draw_door(canvas, tip_point_x, tip_point_y, height):
    door_width = height / 2
    door_height = height / 4
    door_left = tip_point_x - door_width / 8
    door_right = tip_point_x + door_width / 8
    door_bottom = tip_point_y + height
    open_height = height - door_height
    open_bottom = tip_point_y + open_height
    
    canvas.create_rectangle(door_left, open_bottom, door_right, door_bottom, outline="black", width=1, fill="black")
    

# def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    
#     text_horizontal_margin = 20
#     text_vertical_margin = 10
#     # Draw horizontal
#     for i in range(top, bottom, grid_spacing):
#         canvas.create_line(left, i, right, i)
#         canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")

#     for i in range(left, right, grid_spacing):
#         canvas.create_line(i, top, i, bottom)
#         canvas.create_text(i, top + text_vertical_margin, text=f"{i}")
# Call the main function so that
# this program will start executing.
main()