from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesContentApproval(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.contentApproval"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.contentApproval")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isRevoked: Optional[bool] = Field(alias="isRevoked", default=None,)
	revokedDateTime: Optional[datetime] = Field(alias="revokedDateTime", default=None,)
	updatePolicy: Optional[WindowsUpdatesUpdatePolicy] = Field(alias="updatePolicy", default=None,)
	content: Optional[Union[WindowsUpdatesCatalogContent]] = Field(alias="content", default=None,discriminator="odata_type", )
	deploymentSettings: Optional[WindowsUpdatesDeploymentSettings] = Field(alias="deploymentSettings", default=None,)
	deployments: Optional[list[WindowsUpdatesDeployment]] = Field(alias="deployments", default=None,)

from .windows_updates_update_policy import WindowsUpdatesUpdatePolicy
from .windows_updates_catalog_content import WindowsUpdatesCatalogContent
from .windows_updates_deployment_settings import WindowsUpdatesDeploymentSettings
from .windows_updates_deployment import WindowsUpdatesDeployment

