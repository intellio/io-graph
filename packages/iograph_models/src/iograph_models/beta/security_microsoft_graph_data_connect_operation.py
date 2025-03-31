from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoftGraphDataConnectOperation(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftGraphDataConnectOperation"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftGraphDataConnectOperation")

