from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ClientCertificateAuthentication(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	certificateList: Optional[list[Pkcs12CertificateInformation]] = Field(alias="certificateList",default=None,)

from .pkcs12_certificate_information import Pkcs12CertificateInformation

