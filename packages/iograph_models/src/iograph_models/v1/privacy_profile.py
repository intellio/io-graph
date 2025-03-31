from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrivacyProfile(BaseModel):
	contactEmail: Optional[str] = Field(alias="contactEmail", default=None,)
	statementUrl: Optional[str] = Field(alias="statementUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

