from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventExternalRegistrationInformation(BaseModel):
	referrer: Optional[str] = Field(default=None,alias="referrer",)
	registrationId: Optional[str] = Field(default=None,alias="registrationId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


