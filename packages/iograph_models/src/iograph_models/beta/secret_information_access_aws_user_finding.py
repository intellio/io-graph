from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecretInformationAccessAwsUserFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	identityDetails: Optional[IdentityDetails] = Field(alias="identityDetails",default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex",default=None,)
	secretInformationWebServices: Optional[AwsSecretInformationWebServices | str] = Field(alias="secretInformationWebServices",default=None,)
	identity: SerializeAsAny[Optional[AuthorizationSystemIdentity]] = Field(alias="identity",default=None,)

from .identity_details import IdentityDetails
from .permissions_creep_index import PermissionsCreepIndex
from .aws_secret_information_web_services import AwsSecretInformationWebServices
from .authorization_system_identity import AuthorizationSystemIdentity

