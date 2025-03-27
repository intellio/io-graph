from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AadSource(BaseModel):
	identityProviderType: Optional[str] = Field(alias="identityProviderType", default=None,)
	odata_type: Literal["#microsoft.graph.aadSource"] = Field(alias="@odata.type", default="#microsoft.graph.aadSource")
	domain: Optional[str] = Field(alias="domain", default=None,)


