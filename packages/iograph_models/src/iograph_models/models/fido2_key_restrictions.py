from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Fido2KeyRestrictions(BaseModel):
	aaGuids: Optional[list[str]] = Field(alias="aaGuids",default=None,)
	enforcementType: Optional[str | Fido2RestrictionEnforcementType] = Field(alias="enforcementType",default=None,)
	isEnforced: Optional[bool] = Field(alias="isEnforced",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .fido2_restriction_enforcement_type import Fido2RestrictionEnforcementType

