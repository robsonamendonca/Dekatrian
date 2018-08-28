# coding: utf-8
from datetime import date

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from infra.regras.data import Data
from kivy.uix.button import Button


class AreaData(BoxLayout):
    """Classe que define a area que mostra as datas na aplicação."""

    def define_datas(self):

        dataSelecionada = self.aplicacao.dataSelecionada
        self.dia = dataSelecionada.dia_numero_mes
        self.mes = dataSelecionada.mes_nome+" ("+dataSelecionada.mes_numero+")"
        self.ano = dataSelecionada.ano
        self.dataGregoriana = dataSelecionada.data

    def __init__(self, **kwargs):
        super(AreaData, self).__init__(**kwargs)
        self.aplicacao = App.get_running_app()
        self.aplicacao.bind(dataSelecionada=self.mudouDataSelecionada)

        self.define_datas()

    def on_press_dia(self):
        tela = self.aplicacao.tela.ids.tela_secundaria
        tela.remove_widget(tela)
        texto = Button(text="teste")
        tela.add_widget(texto)
        print(tela)
        print("ola")

    def mudouDataSelecionada(self, app, classMudou):
        self.define_datas()
        self.mostra_datas()

    def mostra_datas(self):

        self.ids.dia.text = self.dia
        self.ids.mes.text = self.mes
        self.ids.ano.text = self.ano
        self.ids.dataGregoriana.text = self.dataGregoriana

__author__ = "Lário dos Santos Diniz"
