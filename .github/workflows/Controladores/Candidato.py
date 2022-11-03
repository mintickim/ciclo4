from Respositorio.RepositorioCandidato import RespositorioCandidato
from Respositorio.RepositorioPartido import RespositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido


class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RespositorioCandidato()
        self.repositorioPartido = RespositorioPartido()
    def index(self):
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        nuevoCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.numresolucion = infoCandidato["numresolucion"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        candidatoActual.cedula = infoCandidato["cedula"]
        return self.repositorioCandidato.save(candidatoActual)

    def delete(self,id):
        return self.repositorioCandidato.delete(id)


    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(partidoActual) 
