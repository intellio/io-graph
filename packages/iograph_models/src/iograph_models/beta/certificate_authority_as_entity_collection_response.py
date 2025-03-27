from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CertificateAuthorityAsEntityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CertificateAuthorityAsEntity]] = Field(alias="value", default=None,)

from .certificate_authority_as_entity import CertificateAuthorityAsEntity

