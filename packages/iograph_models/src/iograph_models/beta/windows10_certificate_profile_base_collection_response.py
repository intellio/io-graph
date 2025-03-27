from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10CertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[Windows10PkcsCertificateProfile],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile

