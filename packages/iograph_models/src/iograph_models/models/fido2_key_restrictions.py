from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Fido2KeyRestrictions(BaseModel):
	aaGuids: list[Optional[str]] = Field(alias="aaGuids",)
	enforcementType: Optional[Fido2RestrictionEnforcementType] = Field(default=None,alias="enforcementType",)
	isEnforced: Optional[bool] = Field(default=None,alias="isEnforced",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .fido2_restriction_enforcement_type import Fido2RestrictionEnforcementType

