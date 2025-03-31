from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ProvisionedIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.provisionedIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.provisionedIdentity")
	details: Optional[DetailsInfo] = Field(alias="details", default=None,)
	identityType: Optional[str] = Field(alias="identityType", default=None,)

from .details_info import DetailsInfo
