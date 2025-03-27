from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InformationProtectionPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	labels: Optional[list[InformationProtectionLabel]] = Field(alias="labels", default=None,)

from .information_protection_label import InformationProtectionLabel

