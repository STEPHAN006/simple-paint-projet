from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView


class Gestionnaire(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        titre = Label(text="Mes tâches", font_size=24, size_hint_y=None, height=50)
        self.add_widget(titre)

        zone_saisie = BoxLayout(size_hint_y=None, height=45, spacing=5)

        self.champ_tache = TextInput(
            hint_text="Écrire une tâche",
            multiline=False
        )

        bouton_ajouter = Button(text="Ajouter", size_hint_x=0.3)
        bouton_ajouter.bind(on_press=self.ajouter_tache)

        zone_saisie.add_widget(self.champ_tache)
        zone_saisie.add_widget(bouton_ajouter)
        self.add_widget(zone_saisie)

        self.liste_taches = BoxLayout(
            orientation="vertical",
            spacing=5,
            size_hint_y=None
        )
        self.liste_taches.bind(
            minimum_height=self.liste_taches.setter("height")
        )

        defiler = ScrollView()
        defiler.add_widget(self.liste_taches)
        self.add_widget(defiler)

    def ajouter_tache(self, bouton):
        texte = self.champ_tache.text.strip()

        if texte != "":
            self.creer_ligne(texte)
            self.champ_tache.text = ""

    def creer_ligne(self, texte):
        ligne = BoxLayout(size_hint_y=None, height=45, spacing=5)

        nom_tache = Label(text=texte)
        bouton_terminee = Button(text="Terminée", size_hint_x=0.35)
        bouton_supprimer = Button(text="Supprimer", size_hint_x=0.35)

        bouton_terminee.bind(
            on_press=lambda bouton: self.terminer_tache(nom_tache, bouton)
        )
        bouton_supprimer.bind(
            on_press=lambda bouton: self.supprimer_tache(ligne)
        )

        ligne.add_widget(nom_tache)
        ligne.add_widget(bouton_terminee)
        ligne.add_widget(bouton_supprimer)

        self.liste_taches.add_widget(ligne)

    def terminer_tache(self, nom_tache, bouton):
        nom_tache.text = "✓ " + nom_tache.text
        bouton.disabled = True

    def supprimer_tache(self, ligne):
        self.liste_taches.remove_widget(ligne)


class ApplicationTaches(App):

    def build(self):
        return Gestionnaire()


if __name__ == "__main__":
    ApplicationTaches().run()
