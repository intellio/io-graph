from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamMemberSettings(BaseModel):
	allowAddRemoveApps: Optional[bool] = Field(default=None,alias="allowAddRemoveApps",)
	allowCreatePrivateChannels: Optional[bool] = Field(default=None,alias="allowCreatePrivateChannels",)
	allowCreateUpdateChannels: Optional[bool] = Field(default=None,alias="allowCreateUpdateChannels",)
	allowCreateUpdateRemoveConnectors: Optional[bool] = Field(default=None,alias="allowCreateUpdateRemoveConnectors",)
	allowCreateUpdateRemoveTabs: Optional[bool] = Field(default=None,alias="allowCreateUpdateRemoveTabs",)
	allowDeleteChannels: Optional[bool] = Field(default=None,alias="allowDeleteChannels",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


