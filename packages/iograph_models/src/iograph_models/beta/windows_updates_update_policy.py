from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesUpdatePolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	complianceChangeRules: Optional[list[Annotated[Union[WindowsUpdatesContentApprovalRule],Field(discriminator="odata_type")]]] = Field(alias="complianceChangeRules", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deploymentSettings: Optional[WindowsUpdatesDeploymentSettings] = Field(alias="deploymentSettings", default=None,)
	audience: Optional[WindowsUpdatesDeploymentAudience] = Field(alias="audience", default=None,)
	complianceChanges: Optional[list[Annotated[Union[WindowsUpdatesContentApproval],Field(discriminator="odata_type")]]] = Field(alias="complianceChanges", default=None,)

from .windows_updates_content_approval_rule import WindowsUpdatesContentApprovalRule
from .windows_updates_deployment_settings import WindowsUpdatesDeploymentSettings
from .windows_updates_deployment_audience import WindowsUpdatesDeploymentAudience
from .windows_updates_content_approval import WindowsUpdatesContentApproval

