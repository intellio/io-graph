from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesDeployment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	content: Optional[Union[WindowsUpdatesCatalogContent]] = Field(alias="content", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	settings: Optional[WindowsUpdatesDeploymentSettings] = Field(alias="settings", default=None,)
	state: Optional[WindowsUpdatesDeploymentState] = Field(alias="state", default=None,)
	audience: Optional[WindowsUpdatesDeploymentAudience] = Field(alias="audience", default=None,)

from .windows_updates_catalog_content import WindowsUpdatesCatalogContent
from .windows_updates_deployment_settings import WindowsUpdatesDeploymentSettings
from .windows_updates_deployment_state import WindowsUpdatesDeploymentState
from .windows_updates_deployment_audience import WindowsUpdatesDeploymentAudience

