from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppleManagedIdentityProvider(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	certificateData: Optional[str] = Field(default=None,alias="certificateData",)
	developerId: Optional[str] = Field(default=None,alias="developerId",)
	keyId: Optional[str] = Field(default=None,alias="keyId",)
	serviceId: Optional[str] = Field(default=None,alias="serviceId",)


