from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DataSubject(BaseModel):
	email: Optional[str] = Field(alias="email", default=None,)
	firstName: Optional[str] = Field(alias="firstName", default=None,)
	lastName: Optional[str] = Field(alias="lastName", default=None,)
	residency: Optional[str] = Field(alias="residency", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


