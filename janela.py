from calendar import TUESDAY
from hashlib import new
from pickle import TRUE
from struct import pack
#from tkinter import E, HORIZONTAL
#from tkinter.tix import Tree
from typing import Sequence
import os

import gi
from matplotlib.pyplot import grid

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


import sample_class

# Fazer tudo o que esta aqui em baixo com 
# vbox pois grid preenche toda a janela, e ja que
# vamos colocar uma parte de insercao de sequencia
# e outra parte de labels, com os resultados
# vamos usar vbox nas duas partes 



# Usar de exemplo para testes: MTTVVSRTFRDAGQALSLDL



class Janela(Gtk.Window):
    def __init__(self):
        super().__init__(title="ModLamp Grafico")
        self.set_size_request(800, 400)

        # grid1
        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(10)
        self.grid.set_column_homogeneous(True)
         
        self.seq_text = Gtk.Label()
        self.seq_text.set_label("Sequência:")


        self.entrada = Gtk.Entry()
        self.entrada.set_placeholder_text("Insira sua sequência aqui...")

        # Grid para dividir ao meio a janela e depois anexar os itens nessa box
        self.box_base =Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, homogeneous=True)
        # self.box_base.set_row_spacing(10)
        # self.box_base.set_column_homogeneous(True)

        self.add(self.box_base)


        # grid2
        self.grid2 = Gtk.Grid()
        self.grid2.set_row_spacing(10)
        self.grid2.set_column_homogeneous(True)


        # MELHORAR
        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=13, homogeneous=True)
        
        # Vetor com as caracteristicas fisico-quimicas
        self.text_p = []

        self.text_p.append(Gtk.Label(label="Hidrofobicidade:           ", selectable=TRUE))
        self.text_p.append(Gtk.Label(label="Valor da carga:            ", selectable=TRUE))
        self.text_p.append(Gtk.Label(label="Valor do ponto isoelétrico:", selectable=TRUE))
        self.text_p.append(Gtk.Label(label="Valor do peso Molecular:   ", selectable=TRUE))
        self.text_p.append(Gtk.Label(label="Valor de Bomam:            ", selectable=TRUE))
        self.text_p.append(Gtk.Label(label="Tamanho da sequência:      ", selectable=TRUE))


        # Anexando os textos a janela
        for i in range( len(self.text_p) ):
            vbox1.pack_start(self.text_p[i], TRUE, TRUE, 0)



        self.grid2.attach(vbox1, 0, 0, 1, 1)
        


        # Vbox da frente
        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=13, homogeneous=True)
        self.textVetor = []

        for i in range(0,6):
            self.textVetor.append(Gtk.Label(label="Digite sua sequência", selectable=TRUE))


        for i in range(0,6):
            vbox2.pack_start(self.textVetor[i], TRUE, TRUE, 0)


        self.grid2.attach(vbox2, 1, 0, 1, 1)



        # Escalas
        self.nome_escalas = ["AASI", "eisenberg", "gravy", "argos", "MSS", "MSW", "pepcats", "polarity", "PPCALI", "TM_tend", "refractivity",]

        # ComboBox
        self.comboBox = Gtk.ComboBoxText()
        for i in self.nome_escalas:
            self.comboBox.append_text(i)

        self.comboBox.connect("changed", self.troca_escala, self)



        self.botao_calcula = Gtk.Button()
        self.botao_calcula.set_label("Calcula")
        self.botao_salva = Gtk.Button()
        self.botao_salva.set_label("Salvar")

        self.botao_salva.connect("clicked", self.salvar, self)
        self.botao_calcula.connect("clicked", self.calcular, self)
         
         
        # Grid
        self.grid.attach(self.seq_text,       1, 1, 1, 1)
        self.grid.attach(self.entrada,        2, 1, 1, 1)
        self.grid.attach(self.botao_calcula,  2, 3, 1, 1)
        self.grid.attach(self.botao_salva,    1, 3, 1, 1)


        # Anexando grids na Box de divisao da janela
        self.box_base.pack_start(self.grid, True, True, 0)
        self.box_base.pack_start(self.grid2, True, True, 0)

        # ComboBox
        #self.grid.attach(self.comboBox, 3,1,1,1)



        #self.add(self.grid)
        #self.add(vbox1)
    
    #####################################################################################################
    #Passa o objeto janela como 1 parametro e o objeto botao no 2
    def calcular(aux1, aux2, self):
        # print(f"butao calcula pressionado\n aux1:{aux1} \naux2:    {aux2}")
        # print(sample_class.Bomam(aux1.entrada.get_text()))

        if aux1.entrada.get_text().upper() is not None and aux1.entrada.get_text().isalpha():
            try:
                # Pega texto digitado e salva em seq e, transforma tudo em caixa alta
                seq = aux1.entrada.get_text().upper()


                # print(f"Hidrofobicidade:             {sample_class.hidrofobicidade(seq):.3f}")
                # print(f"Valor da carga:              {sample_class.carga(seq)}")
                # print(f"Valor do ponto isoeletrico:  {sample_class.ponto_isoeletrico(seq):.3f}")
                # print(f"Valor do peso Molecular:     {sample_class.peso_molecular(seq):.3f}")
                # print(f"Valor de Bomam:              {sample_class.Bomam(seq):.3f}\n")


                self.textVetor[0].set_label( f"{sample_class.hidrofobicidade(seq):.3f}"   )
                self.textVetor[1].set_label( f"{sample_class.carga(seq):.3f}"             )
                self.textVetor[2].set_label( f"{sample_class.ponto_isoeletrico(seq):.3f}" )
                self.textVetor[3].set_label( f"{sample_class.peso_molecular(seq):.3f}"    )
                self.textVetor[4].set_label( f"{sample_class.Bomam(seq):.3f}"             )
                self.textVetor[5].set_label( f"{len(seq)}"             )


            except ValueError:
                print("Insira uma sequência válida")
                print(ValueError)

        else:
            print("Insira uma sequência válida")
            #print(ValueError)

    #####################################################################################################
    def salvar(janela, botao, self):
        #nome_do_usuario = os.getlogin()

        try:
            os.mkdir("Resultados_ModLamp")
            os.chdir("Resultados_ModLamp")

        # Caso ja exista o diretorio, o programa ira entrar no diretorio ja existente
        except FileExistsError:
            #print("OIE BB!")
            os.chdir("Resultados_ModLamp")
        
        # Caso nao exista exibe mensagem de erro
        except FileNotFoundError:
            print("Erro na mudanca de diretorio, diretorio nao encontrado!")
        
        #print(os.listdir())


        nome = "Resultados_da_sequencia_" + self.entrada.get_text().upper()
        arquivo = open(nome,"w+")

        arquivo.write(str(self.text_p[0].get_text() +"            " + self.textVetor[0].get_text() + "\n"))
        arquivo.write(str(self.text_p[1].get_text() +"            " + self.textVetor[1].get_text() + "\n"))
        arquivo.write(str(self.text_p[2].get_text() +"            " + self.textVetor[2].get_text() + "\n"))
        arquivo.write(str(self.text_p[3].get_text() +"            " + self.textVetor[3].get_text() + "\n"))
        arquivo.write(str(self.text_p[4].get_text() +"            " + self.textVetor[4].get_text() + "\n"))
        arquivo.write(str(self.text_p[5].get_text() +"            " + self.textVetor[5].get_text() + "\n"))

        arquivo.close()
        os.chdir("..")
        
    #####################################################################################################
    # N da para trocar a escala, pois usa PeptideDescriptor e os calculos
    # sao feitos com o GlobalDescriptor
    def troca_escala(aux1, aux2, self):
        escala_selecionada = self.comboBox.get_active_text()

        print(f"Escala selecionada -> {self.comboBox.get_active_text()}")
        #sample_class.descriptors.PeptideDescriptor(scalename=escala_selecionada)

    #####################################################################################################
if __name__ == '__main__':
    jan = Janela()
    jan.connect('destroy', Gtk.main_quit)
    jan.show_all()
    Gtk.main()
