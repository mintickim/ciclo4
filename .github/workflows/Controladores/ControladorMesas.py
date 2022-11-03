from Repositorios.RepositorioMesas import RepositorioMesas
from Modelos.Mesas import mesa
class ControladorMesas():
    def __init__(self):
        self.RepositorioMesas = RepositorioMesas()
    def index(self):
        return self.RepositorioMesas.findAll()
    def create(self,infoMesa):
        nuevoMesa=Mesa(infoMesa)
        return self.RepositorioMesas.save(nuevaMesa)
    def show(self,id):
        Mesa= Mesa(self.RepositorioMesas.findById(id))
        return Mesa.__dict__
    def update(self,id,infoMesa):
        MesaActual =Mesa(self.RepositorioMesas.findById(id))
        MesaActual.cincritas=infoMesa["numero de cedulas"]
        MesaActual.VCandidatoA = infoMesa["Votos por Candidato A"]
        MesaActual.VCandidatoB = infoMesa["Votos por Candidato B"]
        return self.RepositorioMesas.save(MesaActual)
    def delete(self,id):
        return self.RepositorioMesas.delete(id)