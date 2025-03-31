from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamMemberSettings(BaseModel):
	allowAddRemoveApps: Optional[bool] = Field(alias="allowAddRemoveApps", default=None,)
	allowCreatePrivateChannels: Optional[bool] = Field(alias="allowCreatePrivateChannels", default=None,)
	allowCreateUpdateChannels: Optional[bool] = Field(alias="allowCreateUpdateChannels", default=None,)
	allowCreateUpdateRemoveConnectors: Optional[bool] = Field(alias="allowCreateUpdateRemoveConnectors", default=None,)
	allowCreateUpdateRemoveTabs: Optional[bool] = Field(alias="allowCreateUpdateRemoveTabs", default=None,)
	allowDeleteChannels: Optional[bool] = Field(alias="allowDeleteChannels", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

