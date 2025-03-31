from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AwsAuthorizationSystemTypeAction(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.awsAuthorizationSystemTypeAction"] = Field(alias="@odata.type",)
	actionType: Optional[AuthorizationSystemActionType | str] = Field(alias="actionType", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	resourceTypes: Optional[list[str]] = Field(alias="resourceTypes", default=None,)
	severity: Optional[AuthorizationSystemActionSeverity | str] = Field(alias="severity", default=None,)
	service: Optional[AuthorizationSystemTypeService] = Field(alias="service", default=None,)

from .authorization_system_action_type import AuthorizationSystemActionType
from .authorization_system_action_severity import AuthorizationSystemActionSeverity
from .authorization_system_type_service import AuthorizationSystemTypeService
