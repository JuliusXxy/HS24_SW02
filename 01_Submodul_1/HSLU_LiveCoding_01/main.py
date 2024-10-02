import Processors.config_processor as conf_pro
import Processors.ifc_processor as ifc_p
import Processors.export_processor as exp_p

#Globale Variablen - Listen
glb_conf_lst = []
glb_conf_folder = ""
glb_export_lst = []

def start_func():
    #Hauptfunktion zum Ausführen

    print("Hauptprogramm gestartet")

    glb_conf_set = conf_pro.read_source_data()
    #glb_conf_lst = glb_conf_set[0]
    #glb_conf_folder = glb_conf_set[1]

    #glb_export_lst = ifc_p.process_ifc_data(glb_conf_lst)
    #exp_p.export_data(glb_export_lst, glb_conf_lst, glb_conf_folder)


#Als Hauptprogramm ausführen
if __name__ == '__main__':
    start_func()