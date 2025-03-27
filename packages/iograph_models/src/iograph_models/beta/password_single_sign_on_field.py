from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PasswordSingleSignOnField(BaseModel):
	customizedLabel: Optional[str] = Field(alias="customizedLabel", default=None,)
	defaultLabel: Optional[str] = Field(alias="defaultLabel", default=None,)
	fieldId: Optional[str] = Field(alias="fieldId", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


