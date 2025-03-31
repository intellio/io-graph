from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoftGraphDataConnectConsent(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftGraphDataConnectConsent"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftGraphDataConnectConsent")

