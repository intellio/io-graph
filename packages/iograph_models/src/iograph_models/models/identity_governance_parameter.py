from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceParameter(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	values: Optional[list[str]] = Field(default=None,alias="values",)
	valueType: Optional[IdentityGovernanceValueType] = Field(default=None,alias="valueType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_governance_value_type import IdentityGovernanceValueType

