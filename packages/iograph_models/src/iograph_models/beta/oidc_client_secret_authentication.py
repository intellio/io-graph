from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OidcClientSecretAuthentication(BaseModel):
	odata_type: Literal["#microsoft.graph.oidcClientSecretAuthentication"] = Field(alias="@odata.type", default="#microsoft.graph.oidcClientSecretAuthentication")
	clientSecret: Optional[str] = Field(alias="clientSecret", default=None,)

