from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10NetworkBoundaryConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Windows10NetworkBoundaryConfiguration]] = Field(alias="value", default=None,)

from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration
