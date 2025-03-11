from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsAuthorizationSystem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authorizationSystemId: Optional[str] = Field(alias="authorizationSystemId",default=None,)
	authorizationSystemName: Optional[str] = Field(alias="authorizationSystemName",default=None,)
	authorizationSystemType: Optional[str] = Field(alias="authorizationSystemType",default=None,)
	dataCollectionInfo: Optional[DataCollectionInfo] = Field(alias="dataCollectionInfo",default=None,)
	associatedIdentities: Optional[AwsAssociatedIdentities] = Field(alias="associatedIdentities",default=None,)
	actions: Optional[list[AwsAuthorizationSystemTypeAction]] = Field(alias="actions",default=None,)
	policies: Optional[list[AwsPolicy]] = Field(alias="policies",default=None,)
	resources: Optional[list[AwsAuthorizationSystemResource]] = Field(alias="resources",default=None,)
	services: Optional[list[AuthorizationSystemTypeService]] = Field(alias="services",default=None,)

from .data_collection_info import DataCollectionInfo
from .aws_associated_identities import AwsAssociatedIdentities
from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
from .aws_policy import AwsPolicy
from .aws_authorization_system_resource import AwsAuthorizationSystemResource
from .authorization_system_type_service import AuthorizationSystemTypeService

