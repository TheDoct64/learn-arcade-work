import arcade

arcade.open_window(600,600, "Antidisestablishmentarianism ")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()

#ground the floor and spike
arcade.draw_lrtb_rectangle_filled(0, 455, 300, 0, arcade.csscolor.GREEN)
arcade.draw_triangle_filled(456, 0, 599, 0, 527.5, 150, arcade.csscolor.MAROON)

#circle tree
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100,360,30, arcade.csscolor.GREEN)

#cloud
arcade.draw_ellipse_filled(527.5, 540, 90, 30, arcade.csscolor.LIGHT_BLUE)
arcade.draw_ellipse_filled(460, 540, 90, 30, arcade.csscolor.LIGHT_BLUE)
arcade.draw_ellipse_filled(490, 560, 90, 30, arcade.csscolor.LIGHT_BLUE)

#ploigonal tree
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500,400),
                            (480,360),
                            (470,320),      #cordiates for points on polygon
                            (530,320),
                            (520,360)
                            ),
                            arcade.csscolor.DARK_GREEN)

#Sun
arcade.draw_circle_filled(200,500,40, arcade.csscolor.YELLOW)

#sun rays
arcade.draw_line(200, 500, 200, 600, arcade.csscolor.YELLOW,3) #up
arcade.draw_line(200, 500, 200, 400, arcade.csscolor.YELLOW,3) #down
arcade.draw_line(200, 500, 100, 500, arcade.csscolor.YELLOW,3) #left
arcade.draw_line(200, 500, 300, 500, arcade.csscolor.YELLOW,3) #right
arcade.draw_line(200, 500, 250, 550, arcade.csscolor.YELLOW,3) #top right
arcade.draw_line(200, 500, 150, 550, arcade.csscolor.YELLOW,3) #top left
arcade.draw_line(200, 500, 250, 450, arcade.csscolor.YELLOW,3) #bottom right
arcade.draw_line(200, 500, 150, 450, arcade.csscolor.YELLOW,3) #bottom left

#text
arcade.draw_text("Why is there a floating tree here!",
                 200, 250,
                 arcade.csscolor.BLACK)

arcade.finish_render()

arcade.run()