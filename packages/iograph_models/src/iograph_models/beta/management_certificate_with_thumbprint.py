from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagementCertificateWithThumbprint(BaseModel):
	certificate: Optional[str] = Field(alias="certificate",default=None,)
	thumbprint: Optional[str] = Field(alias="thumbprint",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


