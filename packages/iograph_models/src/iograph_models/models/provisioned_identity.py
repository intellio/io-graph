from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProvisionedIdentity(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	details: Optional[DetailsInfo] = Field(default=None,alias="details",)
	identityType: Optional[str] = Field(default=None,alias="identityType",)

from .details_info import DetailsInfo

