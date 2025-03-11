from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnterpriseCodeSigningCertificateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[EnterpriseCodeSigningCertificate]] = Field(alias="value",default=None,)

from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate

