from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class GcpAuthorizationSystem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.gcpAuthorizationSystem"] = Field(alias="@odata.type", default="#microsoft.graph.gcpAuthorizationSystem")
	authorizationSystemId: Optional[str] = Field(alias="authorizationSystemId", default=None,)
	authorizationSystemName: Optional[str] = Field(alias="authorizationSystemName", default=None,)
	authorizationSystemType: Optional[str] = Field(alias="authorizationSystemType", default=None,)
	dataCollectionInfo: Optional[DataCollectionInfo] = Field(alias="dataCollectionInfo", default=None,)
	associatedIdentities: Optional[GcpAssociatedIdentities] = Field(alias="associatedIdentities", default=None,)
	actions: Optional[list[GcpAuthorizationSystemTypeAction]] = Field(alias="actions", default=None,)
	resources: Optional[list[GcpAuthorizationSystemResource]] = Field(alias="resources", default=None,)
	roles: Optional[list[GcpRole]] = Field(alias="roles", default=None,)
	services: Optional[list[AuthorizationSystemTypeService]] = Field(alias="services", default=None,)

from .data_collection_info import DataCollectionInfo
from .gcp_associated_identities import GcpAssociatedIdentities
from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
from .gcp_role import GcpRole
from .authorization_system_type_service import AuthorizationSystemTypeService
