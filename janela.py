from typing import Sequence
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


import sample_class

# Fazer tudo o que esta aqui em baixo com 
# vbox pois grid preenche toda a janela, e ja que
# vamos colocar uma parte de insercao de sequencia
# e outra parte de labels, com os resultados
# vamos usar vbox nas duas partes 



class Janela(Gtk.Window):
    def __init__(self):
        super().__init__(title="Minha Janela")
        self.set_size_request(800, 400)

        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(10)
         
        self.seq_text = Gtk.Label()
        self.seq_text.set_label("Teste de label:   ")


        self.entrada = Gtk.Entry()
        self.entrada.set_placeholder_text("Insira sua sequência aqui...")


        self.botao_calcula = Gtk.Button()
        self.botao_calcula.set_label("Calcula")
        self.botao_salva = Gtk.Button()
        self.botao_salva.set_label("Salvar")

        self.botao_salva.connect("clicked", self.salvar)
        self.botao_calcula.connect("clicked", self.calcular)


         
         
        self.grid.attach(self.seq_text,       1, 1, 1, 1)
        self.grid.attach(self.entrada,        2, 1, 1, 1)
        self.grid.attach(self.botao_calcula,  2, 3, 1, 1)
        self.grid.attach(self.botao_salva,    1, 3, 1, 1)



        self.add(self.grid)
    
    #passa o objeto janela como 1 parametro e o objeto botao no 2
    def calcular(aux1, aux2):
        # print(f"butao calcula pressionado\n aux1:{aux1} \naux2:    {aux2}")
        # print(sample_class.Bomam(aux1.entrada.get_text()))
        
        seq = aux1.entrada.get_text()

        print(f"Hidrofobicidade:             {sample_class.hidrofobicidade(seq):.3f}")
        print(f"Valor da carga:              {sample_class.carga(seq)}")
        print(f"Valor do ponto isoeletrico:  {sample_class.ponto_isoeletrico(seq):.3f}")
        print(f"Valor do peso Molecular:     {sample_class.peso_molecular(seq):.3f}")
        print(f"Valor de Bomam:              {sample_class.Bomam(seq):.3f}\n")
    
    def salvar(janela, botao):
        print("Implementar funcao para salvar num arquivo txt todas as propriedades fisico-quimicas")


if __name__ == '__main__':
    jan = Janela()
    jan.connect('destroy', Gtk.main_quit)
    jan.show_all()
    Gtk.main()
