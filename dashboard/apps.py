from django.apps import AppConfig

MODULE_NAME = "dashboard"

DEFAULT_CFG = {

}


class DashboardConfig(AppConfig):
    name = MODULE_NAME


    def __load_config(self, cfg):
        for field in cfg:
            if hasattr(DashboardConfig, field):
                setattr(DashboardConfig, field, cfg[field])

    def ready(self):
        from core.models import ModuleConfiguration
        cfg = ModuleConfiguration.get_or_default(MODULE_NAME, DEFAULT_CFG)
        self.__load_config(cfg)