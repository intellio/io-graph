from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AadSource(BaseModel):
	identityProviderType: Optional[str] = Field(alias="identityProviderType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	domain: Optional[str] = Field(alias="domain",default=None,)


