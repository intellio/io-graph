from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TrustedCertificateAuthorityBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[TrustedCertificateAuthorityBase]]] = Field(alias="value",default=None,)

from .trusted_certificate_authority_base import TrustedCertificateAuthorityBase

