from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InformationalUrl(BaseModel):
	logoUrl: Optional[str] = Field(default=None,alias="logoUrl",)
	marketingUrl: Optional[str] = Field(default=None,alias="marketingUrl",)
	privacyStatementUrl: Optional[str] = Field(default=None,alias="privacyStatementUrl",)
	supportUrl: Optional[str] = Field(default=None,alias="supportUrl",)
	termsOfServiceUrl: Optional[str] = Field(default=None,alias="termsOfServiceUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


