from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesContentApprovalRule(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastEvaluatedDateTime: Optional[datetime] = Field(alias="lastEvaluatedDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.contentApprovalRule"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.contentApprovalRule")
	contentFilter: Optional[Union[WindowsUpdatesSoftwareUpdateFilter, WindowsUpdatesWindowsUpdateFilter, WindowsUpdatesDriverUpdateFilter, WindowsUpdatesQualityUpdateFilter]] = Field(alias="contentFilter", default=None,discriminator="odata_type", )
	durationBeforeDeploymentStart: Optional[str] = Field(alias="durationBeforeDeploymentStart", default=None,)

from .windows_updates_software_update_filter import WindowsUpdatesSoftwareUpdateFilter
from .windows_updates_windows_update_filter import WindowsUpdatesWindowsUpdateFilter
from .windows_updates_driver_update_filter import WindowsUpdatesDriverUpdateFilter
from .windows_updates_quality_update_filter import WindowsUpdatesQualityUpdateFilter

