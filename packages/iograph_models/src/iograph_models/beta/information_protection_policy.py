from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class InformationProtectionPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.informationProtectionPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.informationProtectionPolicy")
	labels: Optional[list[InformationProtectionLabel]] = Field(alias="labels", default=None,)

from .information_protection_label import InformationProtectionLabel
