# -*- coding: utf-8 -*-



from odoo import api, fields, models, _
import datetime


class centroscolegios(models.Model):
	_name='centros.colegios'
	nombre = fields.Text('Nombre del centro', required=True)
	idCentro = fields.Integer('Id del centro', required=True)
	educacion = fields.Selection([('publico', 'Publico'),('privado','Privado'),
			('concertado','Concertado')])
	aulaCentro = fields.Char('Aula del centro', required=True)
	profesoresCentro = fields.Text('Profesores', required=True)
	materiales = fields.Char('Materiales', required=True)
	
class centrosprofesores(models.Model):
	_name='centros.profesores'
	
	
	@api.depends('nacimiento','edad')
	def _edad(self):
		self.edad=datetime.date.today().year - self.nacimiento.year
	
		
            
	nombreProfe = fields.Text('Nombre de profesor', required=True)
	apellido = fields.Text('Apellido profesor', required=True)
	nacimiento = fields.Date('Año nacimiento', required=True, default=fields.Date.context_today)
    edad = fields.Integer('Años', compute='_edad')
    director = fields.Boolean('Director')
    centro = fields.Many2one('centros.colegios', 'Centro', required=True)
    aula = fields.Many2one('centros.aulas', 'idAulas', required=True)
    	
    	
class centrosaulas(models.Model):
	_name='centros.aulas'
	idAula = fields.Integer('Id aula', required=True)
	profesorNombre = fields.Many2one('centros.profesores', 'Profesor', required=True)
	delegado = fields.Boolean('Delegado')
	bilingue = fields.Boolean('Bilingue')
	
