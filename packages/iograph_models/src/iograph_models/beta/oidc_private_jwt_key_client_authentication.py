from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class OidcPrivateJwtKeyClientAuthentication(BaseModel):
	odata_type: Literal["#microsoft.graph.oidcPrivateJwtKeyClientAuthentication"] = Field(alias="@odata.type", default="#microsoft.graph.oidcPrivateJwtKeyClientAuthentication")

