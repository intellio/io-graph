from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CertificateAuthorityAsEntity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.certificateAuthorityAsEntity"] = Field(alias="@odata.type",)
	certificate: Optional[str] = Field(alias="certificate", default=None,)
	isRootAuthority: Optional[bool] = Field(alias="isRootAuthority", default=None,)
	issuer: Optional[str] = Field(alias="issuer", default=None,)
	issuerSubjectKeyIdentifier: Optional[str] = Field(alias="issuerSubjectKeyIdentifier", default=None,)

