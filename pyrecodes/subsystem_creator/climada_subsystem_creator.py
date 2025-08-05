from pyrecodes.subsystem_creator.r2d_subsystem_creator import R2DSubsystemCreator
from pyrecodes.component.component import Component
from pyrecodes.utilities import read_json_file, create_component_geometry_as_point
from pyrecodes.component_configurator import climada_component_configurator

class CLIMADASubsystemCreator(R2DSubsystemCreator):
    """
    Create a System based on CLIMADA's JSON output file.
    """

    def create_components_in_localities(self) -> list[Component]:
        return self.create_components()
    
    def get_component_configurator_class(self, component_type: str) -> type:
        return getattr(climada_component_configurator, f'CLIMADA{component_type}Configurator')
    
    def get_exposure_file(self) -> dict:
        return read_json_file(self.parameters['ExposureFile'])
    
    def get_damage_file(self) -> dict:
        return read_json_file(self.damage_input['Parameters']['DamageFile'])
    
    def get_component_geometry(self, component_info):
        return create_component_geometry_as_point([component_info['GeneralInformation']['Longitude'], component_info['GeneralInformation']['Latitude']])