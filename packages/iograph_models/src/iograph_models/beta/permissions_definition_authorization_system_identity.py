from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class PermissionsDefinitionAuthorizationSystemIdentity(BaseModel):
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	identityType: Optional[PermissionsDefinitionIdentityType | str] = Field(alias="identityType", default=None,)
	source: Optional[Union[AwsIdentitySource, EdIdentitySource, LocalIdentitySource, SamlIdentitySource]] = Field(alias="source", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .permissions_definition_identity_type import PermissionsDefinitionIdentityType
from .aws_identity_source import AwsIdentitySource
from .ed_identity_source import EdIdentitySource
from .local_identity_source import LocalIdentitySource
from .saml_identity_source import SamlIdentitySource
