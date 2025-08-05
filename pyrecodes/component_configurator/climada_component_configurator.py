from pyrecodes.component_configurator.r2d_component_configurator import R2DBuildingConfigurator
from pyrecodes.component_configurator.climada_repair_configurator import CLIMADABuildingRepairConfigurator
from pyrecodes.component.component import Component

DAMAGE_STATE_MAPPING = {
    'None': 0,
    'Slight': 1,
    'Moderate': 2,
    'Extensive': 3,
    'Complete': 4
}

class CLIMADABuildingConfigurator(R2DBuildingConfigurator):

    SYSTEM_LEVEL_DATA = ['START_TIME_STEP', 'MAX_TIME_STEP', 'MAX_REPAIR_CREW_DEMAND_PER_BUILDING',
                        'REPAIR_CREW_DEMAND_PER_SQFT',
                        'DEFAULT_REPAIR_DURATION_DICT', 'DEMAND_PER_PERSON', 'HOUSING_RESOURCES',
                        'SQFT_PER_PERSON']
    
    def set_parameters(self, component: Component, locality: list, component_data: dict, component_DS: int): 
        self.set_number_of_units(component, component_data)
        super().set_parameters(component, locality, component_data, component_DS)   
        return component

    def get_damage_state(self, damage_info: dict) -> str:
        return DAMAGE_STATE_MAPPING.get(damage_info['DamageState'], 0)
    
    def set_repair_configurator(self, component):
        self.repair_configurator = CLIMADABuildingRepairConfigurator(component, self.system_level_data)

    def set_geometry(self, component, building_data: dict):
        self.set_building_footprint(component, building_data)

    def set_building_footprint(self, component, building_data):
        component.footprint = building_data['Information']['GeneralInformation']['Footprint']

    def set_aim_id(self, component, component_data):
        component.aim_id = component_data['Information']['GeneralInformation']['FootprintID']

    def set_number_of_units(self, component, building_data: dict):
        component.number_of_units = building_data['Information']['GeneralInformation']['NumberOfUnits']

    def get_building_housing_capacity(self, building_data: dict) -> int:  
        return int(building_data['Information']['GeneralInformation']['PlanArea'] / self.system_level_data['SQFT_PER_PERSON'])





