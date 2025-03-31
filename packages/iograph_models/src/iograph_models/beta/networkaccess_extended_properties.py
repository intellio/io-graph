from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessExtendedProperties(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.extendedProperties"] = Field(alias="@odata.type",)

