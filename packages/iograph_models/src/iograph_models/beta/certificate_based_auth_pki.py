from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CertificateBasedAuthPki(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.certificateBasedAuthPki"] = Field(alias="@odata.type", default="#microsoft.graph.certificateBasedAuthPki")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	statusDetails: Optional[str] = Field(alias="statusDetails", default=None,)
	certificateAuthorities: Optional[list[CertificateAuthorityDetail]] = Field(alias="certificateAuthorities", default=None,)

from .certificate_authority_detail import CertificateAuthorityDetail
