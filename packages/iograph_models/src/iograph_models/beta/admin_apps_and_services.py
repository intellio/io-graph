from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AdminAppsAndServices(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	settings: Optional[AppsAndServicesSettings] = Field(alias="settings",default=None,)

from .apps_and_services_settings import AppsAndServicesSettings

