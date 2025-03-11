from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalDomainFederation(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	domainName: Optional[str] = Field(alias="domainName",default=None,)
	issuerUri: Optional[str] = Field(alias="issuerUri",default=None,)


