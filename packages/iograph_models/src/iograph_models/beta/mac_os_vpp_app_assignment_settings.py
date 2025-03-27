from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class MacOsVppAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.macOsVppAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.macOsVppAppAssignmentSettings")
	preventAutoAppUpdate: Optional[bool] = Field(alias="preventAutoAppUpdate", default=None,)
	preventManagedAppBackup: Optional[bool] = Field(alias="preventManagedAppBackup", default=None,)
	uninstallOnDeviceRemoval: Optional[bool] = Field(alias="uninstallOnDeviceRemoval", default=None,)
	useDeviceLicensing: Optional[bool] = Field(alias="useDeviceLicensing", default=None,)


