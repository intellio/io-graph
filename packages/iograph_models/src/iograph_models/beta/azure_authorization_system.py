from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AzureAuthorizationSystem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authorizationSystemId: Optional[str] = Field(alias="authorizationSystemId",default=None,)
	authorizationSystemName: Optional[str] = Field(alias="authorizationSystemName",default=None,)
	authorizationSystemType: Optional[str] = Field(alias="authorizationSystemType",default=None,)
	dataCollectionInfo: Optional[DataCollectionInfo] = Field(alias="dataCollectionInfo",default=None,)
	associatedIdentities: Optional[AzureAssociatedIdentities] = Field(alias="associatedIdentities",default=None,)
	actions: Optional[list[AzureAuthorizationSystemTypeAction]] = Field(alias="actions",default=None,)
	resources: Optional[list[AzureAuthorizationSystemResource]] = Field(alias="resources",default=None,)
	roleDefinitions: Optional[list[AzureRoleDefinition]] = Field(alias="roleDefinitions",default=None,)
	services: Optional[list[AuthorizationSystemTypeService]] = Field(alias="services",default=None,)

from .data_collection_info import DataCollectionInfo
from .azure_associated_identities import AzureAssociatedIdentities
from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
from .azure_authorization_system_resource import AzureAuthorizationSystemResource
from .azure_role_definition import AzureRoleDefinition
from .authorization_system_type_service import AuthorizationSystemTypeService

