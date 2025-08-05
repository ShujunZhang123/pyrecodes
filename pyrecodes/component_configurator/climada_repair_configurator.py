from pyrecodes.component_configurator.r2d_repair_configurator import R2DBuildingRepairConfigurator
from pyrecodes.constants import METER_TO_MILE, INCH_TO_MILE, FEET_TO_MILE


class CLIMADABuildingRepairConfigurator(R2DBuildingRepairConfigurator):
    """
    | Class that configures the parameters of the repair and financing activity of CLIMADA building components. 
    
    | These parameters are repair duration, repair cost and repair resource demand.
    """

    def get_repair_demand(self, component_DS: int) -> None:
        """
        Repair demand is the number of housing unit in the building.
        """
        housing_units = self.component.number_of_units
        return housing_units
    
    def set_repair_time(self, component_data: dict) -> None:
        """
        Do not set repair demand here, use the default value from the component library.
        """
        pass

    def set_repair_cost(self, component_data: dict, recovery_demand_setter: callable) -> None:
        pass                     
            