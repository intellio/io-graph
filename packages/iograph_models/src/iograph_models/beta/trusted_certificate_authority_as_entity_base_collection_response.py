from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TrustedCertificateAuthorityAsEntityBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[TrustedCertificateAuthorityAsEntityBase]]] = Field(alias="value",default=None,)

from .trusted_certificate_authority_as_entity_base import TrustedCertificateAuthorityAsEntityBase

