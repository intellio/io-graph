from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsNotAutopilotReadyDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	autoPilotProfileAssigned: Optional[bool] = Field(alias="autoPilotProfileAssigned", default=None,)
	autoPilotRegistered: Optional[bool] = Field(alias="autoPilotRegistered", default=None,)
	azureAdJoinType: Optional[str] = Field(alias="azureAdJoinType", default=None,)
	azureAdRegistered: Optional[bool] = Field(alias="azureAdRegistered", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	managedBy: Optional[str] = Field(alias="managedBy", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)


