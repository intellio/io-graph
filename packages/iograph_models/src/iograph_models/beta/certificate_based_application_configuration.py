from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CertificateBasedApplicationConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.certificateBasedApplicationConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.certificateBasedApplicationConfiguration")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	trustedCertificateAuthorities: Optional[list[CertificateAuthorityAsEntity]] = Field(alias="trustedCertificateAuthorities", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

from .certificate_authority_as_entity import CertificateAuthorityAsEntity
