from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MacOsVppAppAssignedLicense(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.macOsVppAppAssignedLicense"] = Field(alias="@odata.type", default="#microsoft.graph.macOsVppAppAssignedLicense")
	userEmailAddress: Optional[str] = Field(alias="userEmailAddress", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

