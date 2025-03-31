from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NetworkLocationDetail(BaseModel):
	networkNames: Optional[list[str]] = Field(alias="networkNames", default=None,)
	networkType: Optional[NetworkType | str] = Field(alias="networkType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .network_type import NetworkType
