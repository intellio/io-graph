from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AppleManagedIdentityProvider(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.appleManagedIdentityProvider"] = Field(alias="@odata.type", default="#microsoft.graph.appleManagedIdentityProvider")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	certificateData: Optional[str] = Field(alias="certificateData", default=None,)
	developerId: Optional[str] = Field(alias="developerId", default=None,)
	keyId: Optional[str] = Field(alias="keyId", default=None,)
	serviceId: Optional[str] = Field(alias="serviceId", default=None,)

