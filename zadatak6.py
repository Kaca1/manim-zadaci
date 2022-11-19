from manim import *
from pathlib import Path

class ba(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=60 * DEGREES, theta=-20 * DEGREES,zoom=0.7) # kamera gleda u donju lijevu ivicu kocke (kao da je gornja lijeva)
        glavna_cube = Cube(side_length=4, fill_opacity=0.2, fill_color='#58C4DD', stroke_width=3) # referenciona kocka za redanje malih kockica

# ==================ovo treba u neku petlju skontati=================================================================================
    # UP desno ili lijevo; OUT gore dole; RIGHT napred nazad
        manja = Cube(side_length=4/3, fill_opacity=0.8, fill_color='#BDB76B', stroke_width=3)

        # ------donji lejer----
        # prvi red od gledaoca
        manja1 = manja.copy().move_to((4/3)*RIGHT - (4/3)*UP - (4/3)*OUT)
        manja2 = manja.copy().move_to((4/3)*RIGHT - (4/3)*OUT)
        manja3 = manja.copy().move_to((4/3)*RIGHT + (4/3)*UP - (4/3)*OUT)
        # drugi red od gledaoca
        manja4 = manja.copy().move_to(- (4/3)*UP - (4/3)*OUT)
        manja5 = manja.copy().move_to(- (4/3)*OUT)
        manja6 = manja.copy().move_to(+ (4/3)*UP - (4/3)*OUT)
        # treci red od gledaoca
        manja7 = manja.copy().move_to(-(4/3)*RIGHT - (4/3)*UP - (4/3)*OUT)
        manja8 = manja.copy().move_to(-(4/3)*RIGHT - (4/3)*OUT)
        manja9 = manja.copy().move_to(-(4/3)*RIGHT + (4/3)*UP - (4/3)*OUT)

        # ------srednji lejer----
        # prvi red od gledaoca
        manja11 = manja.copy().move_to((4/3)*RIGHT - (4/3)*UP)
        manja22 = manja.copy().move_to((4/3)*RIGHT)
        manja33 = manja.copy().move_to((4/3)*RIGHT + (4/3)*UP)
        # drugi red od gledaoca
        manja44 = manja.copy().move_to(- (4/3)*UP)
        manja55 = manja.copy()
        manja66 = manja.copy().move_to(+ (4/3)*UP)
        # treci red od gledaoca
        manja77 = manja.copy().move_to(-(4/3)*RIGHT - (4/3)*UP)
        manja88 = manja.copy().move_to(-(4/3)*RIGHT)
        manja99 = manja.copy().move_to(-(4/3)*RIGHT + (4/3)*UP)

        # ------gornji lejer----
        # prvi red od gledaoca
        manja111 = manja.copy().move_to((4/3)*RIGHT - (4/3)*UP + (4/3)*OUT)
        manja222 = manja.copy().move_to((4/3)*RIGHT + (4/3)*OUT)
        manja333 = manja.copy().move_to((4/3)*RIGHT + (4/3)*UP + (4/3)*OUT)
        # drugi red od gledaoca
        manja444 = manja.copy().move_to(- (4/3)*UP + (4/3)*OUT)
        manja555 = manja.copy().move_to(+ (4/3)*OUT)
        manja666 = manja.copy().move_to(+ (4/3)*UP + (4/3)*OUT)
        # treci red od gledaoca
        manja777 = manja.copy().move_to(-(4/3)*RIGHT - (4/3)*UP + (4/3)*OUT)
        manja888 = manja.copy().move_to(-(4/3)*RIGHT + (4/3)*OUT)
        manja999 = manja.copy().move_to(-(4/3)*RIGHT + (4/3)*UP + (4/3)*OUT)
# ===============================================================================
    # grupisemo i kreiramo tekst koji ide kroz animaciju
        cubes = Group(#glavna_cube, 
        manja9, manja8, manja7, manja6, manja5, manja4, manja3, manja2, manja1, 
        manja99, manja88, manja77, manja66, manja55, manja44, manja33, manja22, manja11,
        manja999, manja888, manja777, manja666, manja555, manja444, manja333, manja222, manja111)

        corners = Group(manja1, manja111, manja3, manja333, manja7, manja777, manja9, manja999)
        
        text1 = Text("Postoji li put od ćoska kocke 3x3x3 do centra tako da prolazi kroz sve kockice \n"+
        "jednom? (Hamiltonov put)", font_size=28)
    
        text2 = Text("Pretpostavimo da postoji. Tada bi mogli takav put razvući u ovako povezan niz.")

        text3 = Text("Obojimo svaku drugu kockicu.")

        text4 = Text("Primjetimo da bi u ovom slučaju, sa 27 kockica, \n"+
        "prva i posljednja kockica u nizu (ili na putu) bile obojene istom bojom.")

        text5 = Text("Sad od tih kockica formiramo ponovo 3x3x3 kocku tako da\n"+
        "su susjedne kockice obojene različitim bojama.")

        text6 = Text("Primjetimo da su kockice u ćoskovima žute te da će \n"+
        "naredna kockica na putu do centra biti plava.")

        text7 = Text("Na osnovu niza od maloprije znamo da ako postoji put od ćoska do centra\n"+
        "onda bi kockice bile obojene istom bojom, žutom.")

        text8 = Text("Ali kockica u centru je plava!")
        
        text = Group(text1, text2, text3, text4, text5, text6, text7, text8)
        
        for i in text:
            i.font_size = 28
            i.to_corner(UL)
        
        self.camera.add_fixed_in_frame_mobjects(text)

#===============animacije============================
    # TREBA DODATI BROJAC I POKAZATI DA SE KRAJNJA BOJA MIJENJA U ZAVISNOSTI DA LI JE PARAN
    # ILI NEPARAN BROJ KOCKICA U NIZU. IDEJA:FREJM ZADNJE KOCKICE MOZE DA SETA NAZAD ILI SLICNO.
       
        self.play(Write(text1))
        self.play(AnimationGroup(*[FadeIn(o, shift= -2*OUT) for o in cubes], lag_ratio=0.20)) # kockice ulaze padajuci sa neba
        self.wait(2)

        [i.save_state() for i in cubes] # cuvam stanje da bi vratila boje poslije
        self.play(corners.animate.set_color(BLUE))
        self.play(cubes.animate.space_out_submobjects(factor=2)) # sirimo kockicu da vidimo centralnu
        self.play(manja55.animate.set_color(RED))
        self.wait(1)

        # vracamo ih u pocetno stanjes
        self.play(cubes.animate.space_out_submobjects(factor=1/2)) 
        self.play(AnimationGroup(*[i.animate.restore() for i in cubes])) # (za sve kocke jer bolje izgleda)
        self.wait(2)
        
        [c.generate_target() for c in cubes] # pamtimo stanje trenutno, stavljamo u target varijablu

        self.play(text1.animate.become(text2))
        self.wait(2)

        # pomjeramo kameru tako da vidimo grid od kockica frontalno, istovremeno se pravi taj grid
        self.move_camera(phi=0, theta=-90*DEGREES, zoom=0.7,
        added_anims=[cubes.animate.arrange_in_grid(rows=3, cols=9, buff=0.7, 
        row_heights=[2,2,2])])
    
        self.play(cubes.animate.shift(-UP)) # pomjeramo grid malo dolje zbog estetike

        # prave se linije koje povezuju kockice da izgleda kao put, za dve horizontalne moram posebno
        # (ideja: mozda ako bi kockice bile dobro poredane kao u grupi i na slici ne bi morala praviti te linije posebno)
        lines=[]
        for i in range (26):
            if i not in [8,17]:
                lines.append(Line(color= PURE_GREEN,start=cubes[i+1].get_left(), end=cubes[i].get_right()))
            elif i==8:
                lines.append(Line(color= PURE_GREEN,start=cubes[8+9].get_edge_center(UP), end=cubes[8].get_bottom()))
            elif i==17:
                lines.append(Line(color= PURE_GREEN,start=cubes[9+9].get_edge_center(UP), end=cubes[9].get_bottom()))
            
        self.play(*[Write(l, reverse=False) for l in lines]) # nastaju linije, s lijeva na desno istovremeno
        self.play(text1.animate.become(text3))
        self.wait(2)

        # bojimo naizmjenicno kockice u gridu 
        # (ideja: ova petlja moze ljepse da se napise, bez k i duplo krace koda)
        """
        mislim da ovako moze:
        color = [YELLOW_E, TEAL_E]
        for i in range(27):
            cubes[i].set_color(color[i%2])
            cubes[i].target.set_color(color[i%2])
            self.wait(0.07)

        """ 
        k=0
        for i in cubes:
            if k==0:
                i.set_color(YELLOW_E) # postavljamo za kockicu
                i.target.set_color(YELLOW_E) # postavljamo za kockicu sacuvanu na polaozaju za 3x3x3
                self.wait(0.07)
                k=1
            else:
                i.set_color(TEAL_E)
                i.target.set_color(TEAL_E)
                self.wait(0.07)
                k=0

        self.wait(2)

        # ovde iz nekog razloga tekst se izmjesa ako idem sa .become funkcijom
        self.remove(text1)
        self.play(Write(text4))
        self.wait(3)
        
        # pravimo frejm kockicu za pocetnu i krajnju kockicu u nizu
        cube_frame1 = Cube(color=PURE_GREEN, fill_opacity=0.2, stroke_width=1)
        cube_frame1.move_to(manja9)

        cube_frame2 = Cube(color=PURE_GREEN, fill_opacity=0.2, stroke_width=1)
        cube_frame2.move_to(manja111)

        self.play(*[Create(cube_frame1), Create(cube_frame2)])
        self.wait(4)

        self.play(text4.animate.become(text5))
        self.wait(2)

        # frejmovi i linije nestaju i kockice se transformisu u proslo stanje tj 3x3x3 kocku
        # i kamera se vraca u proslo stanje
        self.play(*[FadeOut(*lines), FadeOut(cube_frame1), FadeOut(cube_frame2)])
        self.move_camera(phi=60 * DEGREES, theta=-20 * DEGREES, 
        zoom=0.7, added_anims=[MoveToTarget(c) for c in cubes])
        self.wait(2)

        self.play(text4.animate.become(text6))
        self.wait(3)

        [i.save_state() for i in cubes] # ponovo cuvamo stanje zbog boje
        self.play(manja111.animate.set_color(YELLOW_C))
        self.wait(2)

        self.play(AnimationGroup(*[i.animate.restore() for i in cubes])) # vracamo boju
        self.wait(2)

        self.play(*[ manja11.animate.set_color(BLUE_E),
                    manja222.animate.set_color(BLUE_E),
                    manja444.animate.set_color(BLUE_E) ])
        self.wait(2)

        self.play(AnimationGroup(*[i.animate.restore() for i in cubes])) # vracamo boju
        self.wait(2)

        self.play(text4.animate.become(text7))
        self.wait(3)

        # sirimo kocku i pokazujemo boju centralne kocke da je plava
        self.play(cubes.animate.space_out_submobjects(factor=2))
        self.play(manja55.animate.set_color(BLUE_E))
        self.play(text4.animate.become(text8))
        self.play(manja55.animate.set_color(TEAL_D))
        self.wait(3)

        self.play(cubes.animate.space_out_submobjects(factor=1/2)) # vracamo kocku u normalu
        self.wait(2)





        

