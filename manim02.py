from manim import *

class ArrangeInGrid(ThreeDScene):
    def construct(self):
        boxes = VGroup(*[
            Cube(side_length=4/3, fill_opacity=0.8, fill_color='#BDB76B', stroke_width=3)
        .add(Text(str(i+1)).scale(0.5))
            for i in range(27)
        ])
        self.add(boxes)

        self.set_camera_orientation(phi=0, theta=-90*DEGREES, zoom=0.7)

        boxes.arrange_in_grid(3,9,
            buff=(0.25,0.5),
            #col_alignments="lccccr",
            #row_alignments="uccd",
            col_widths=[*[1.5]*9],
            row_heights=[2,2,2],
            flow_order="dr"
        )

        boxes.shift(-UP)