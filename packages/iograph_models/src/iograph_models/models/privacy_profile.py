from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrivacyProfile(BaseModel):
	contactEmail: Optional[str] = Field(default=None,alias="contactEmail",)
	statementUrl: Optional[str] = Field(default=None,alias="statementUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


