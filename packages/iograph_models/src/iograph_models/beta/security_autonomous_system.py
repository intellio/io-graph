from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAutonomousSystem(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	number: Optional[int] = Field(alias="number",default=None,)
	organization: Optional[str] = Field(alias="organization",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


