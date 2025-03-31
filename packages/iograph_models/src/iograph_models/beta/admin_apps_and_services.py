from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AdminAppsAndServices(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.adminAppsAndServices"] = Field(alias="@odata.type",)
	settings: Optional[AppsAndServicesSettings] = Field(alias="settings", default=None,)

from .apps_and_services_settings import AppsAndServicesSettings
