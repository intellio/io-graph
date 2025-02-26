from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DataSubject(BaseModel):
	email: Optional[str] = Field(default=None,alias="email",)
	firstName: Optional[str] = Field(default=None,alias="firstName",)
	lastName: Optional[str] = Field(default=None,alias="lastName",)
	residency: Optional[str] = Field(default=None,alias="residency",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


