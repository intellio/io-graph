from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ProvisioningSystem(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.provisioningSystem"] = Field(alias="@odata.type", default="#microsoft.graph.provisioningSystem")
	details: Optional[DetailsInfo] = Field(alias="details", default=None,)

from .details_info import DetailsInfo
