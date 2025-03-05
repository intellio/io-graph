from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceParameter(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	values: Optional[list[str]] = Field(alias="values",default=None,)
	valueType: Optional[str | IdentityGovernanceValueType] = Field(alias="valueType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_governance_value_type import IdentityGovernanceValueType

