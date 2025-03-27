from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationCombinationConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[Fido2CombinationConfiguration, X509CertificateCombinationConfiguration],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .fido2_combination_configuration import Fido2CombinationConfiguration
from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration

