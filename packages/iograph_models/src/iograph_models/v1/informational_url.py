from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InformationalUrl(BaseModel):
	logoUrl: Optional[str] = Field(alias="logoUrl", default=None,)
	marketingUrl: Optional[str] = Field(alias="marketingUrl", default=None,)
	privacyStatementUrl: Optional[str] = Field(alias="privacyStatementUrl", default=None,)
	supportUrl: Optional[str] = Field(alias="supportUrl", default=None,)
	termsOfServiceUrl: Optional[str] = Field(alias="termsOfServiceUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


