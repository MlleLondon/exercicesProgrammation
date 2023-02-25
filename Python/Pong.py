import turtle as tl

class PONG:
    def __init__(self):
        #Toutes les fonctions a afficher sur l'écran#
        self.creation_fenetre()
        self.raquetteGauche()
        self.raquetteDroite()
        self.creation_balle()
        self.touches()
        self.jeu()

    def creation_fenetre(self):
        #Création de la fenêtre d'affichage#
        self.root=tl.Screen()
        self.root.title('Jeu de Pong')
        self.root.bgcolor("black")
        self.root.setup(width=600, height=400)
        self.root.tracer(0)

    def raquetteGauche(self):
        #On créer la raquette gauche
        self.raquette_gauche=tl.Turtle()
        self.raquette_gauche.speed(0)
        self.raquette_gauche.shape('square')
        self.raquette_gauche.color('red')
        self.raquette_gauche.shapesize(stretch_wid=7, stretch_len=1.2)
        self.raquette_gauche.penup()
        self.raquette_gauche.goto(-280,0)
    def raquetteDroite(self):
        #On créer la raquette droite
        self.raquette_droite=tl.Turtle()
        self.raquette_droite.speed(0)
        self.raquette_droite.shape('square')
        self.raquette_droite.color('white')
        self.raquette_droite.shapesize(stretch_wid=7, stretch_len=1.2)
        self.raquette_droite.penup()
        self.raquette_droite.goto(280,0)
    
    def creation_balle(self):
        #On créer la balle 
        self.balle=tl.Turtle()
        self.balle.speed(0)
        self.balle.shape('circle')
        self.balle.color('green')
        self.balle.penup()
        self.balle.goto(5,5)
        self.balle_direction_x=0.1
        self.balle_direction_y=0.1

    #Déplacements bas et haut des deux raquettes#
    def raquette_gauche_haut(self):
        y=self.raquette_gauche.ycor()
        y=y+20
        self.raquette_gauche.sety(y)
    def raquette_gauche_bas(self):
        y=self.raquette_gauche.ycor()
        y=y-20
        self.raquette_gauche.sety(y)
    
    def raquette_droite_haut(self):
        y=self.raquette_droite.ycor()
        y=y+20
        self.raquette_droite.sety(y)
    def raquette_droite_bas(self):
        y=self.raquette_droite.ycor()
        y=y-20
        self.raquette_droite.sety(y)
    
    def touches(self):
        #Définir les touches du clavier et les associer à une action de jeu#
        self.root.listen()
        self.root.onkey(self.raquette_gauche_haut,"z")
        self.root.onkey(self.raquette_gauche_bas,"s")
        self.root.onkey(self.raquette_droite_haut,"Up")
        self.root.onkey(self.raquette_droite_bas,"Down")

    def jeu(self):
        while True:
            self.root.update()
            #Déplacement de la balle#
            self.balle.setx(self.balle.xcor()+self.balle_direction_x)
            self.balle.sety(self.balle.ycor()+self.balle_direction_y)

            if self.balle.ycor()>190:
                self.balle.sety(190)
                self.balle_direction_y *=-1
            
            if self.balle.ycor()<-190:
                self.balle.sety(-190)
                self.balle_direction_y *=-1
            
            if self.balle.xcor()>260:
                self.balle_direction_x *=-1
            
            if self.balle.xcor()<-260:
                self.balle_direction_x *=-1
            
            if(self.balle.xcor()>210) and (self.balle.xcor()<220) and (self.balle.ycor()<self.raquette_droite.ycor()+40 and self.balle.ycor()>self.raquette_droite.ycor()-40):
                self.balle.setx(210)
                self.balle_direction_x *=-1

            if(self.balle.xcor()>-210) and (self.balle.xcor()<-220) and (self.balle.ycor()<self.raquette_droite.ycor()+40 and self.balle.ycor()>self.raquette_droite.ycor()-40):
                self.balle.setx(-210)
                self.balle_direction_x *=-1
    

def main():
    PONG()
if __name__ == '__main__':
    main()
