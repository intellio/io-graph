from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerSilentCertificateAccess(BaseModel):
	packageId: Optional[str] = Field(alias="packageId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


