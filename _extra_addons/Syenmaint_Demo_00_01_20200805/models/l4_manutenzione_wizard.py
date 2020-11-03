from odoo import models, fields, api
from . import l4_manutenzione
import webbrowser

class l4_manutenzione_wizard(models.TransientModel):
    _name = "wizard"
    _description = "Wizard: Scelta della ripetizione degli eventi"

    """L4 - modello per la creazione del wizard"""
    # IMPORTANTE
    # Wizard records puo' far riferimento ai record regolari o wizard record con many2one fields,
    # ma i record regolari non possono far riferimento ai record del wizard tramite a manu2one field.

    session_id = fields.Many2one("l4_manutenzione", string="Session", required=True)
    #data_id = fields.Date(string="Data appuntamento")
    # campo per la gestione del numero giorni ciclo
    l4sm_day_cyc = fields.Integer(string="Giorni Ciclo")
    # campo che definisce il numero dei cicli
    l4sm_num_cyc = fields.Integer(string="Numero cicli")

   # @api.multi
    #def apianifica_manutenzione(self):
        #l4_manutenzione.l4sm_piano_creato = True
        #l4_manutenzione.pianifica_manutenzione(self.l4sm_num_cyc, self.l4sm_day_cyc)
    @api.multi
    def redirect(self):
        redirectURL = "http://localhost:8069/"
        #webbrowser.open(redirectURL)
        #print('<html>')
        #print('  <head>')
        #print('    <meta http-equiv="refresh" content="0;url=' + str(redirectURL) + '" />')
        #print('  </head>')
        #print('</html>')
