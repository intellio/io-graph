from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	policyConfigurationIngestionType: Optional[GroupPolicyConfigurationIngestionType | str] = Field(alias="policyConfigurationIngestionType", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	assignments: Optional[list[GroupPolicyConfigurationAssignment]] = Field(alias="assignments", default=None,)
	definitionValues: Optional[list[GroupPolicyDefinitionValue]] = Field(alias="definitionValues", default=None,)

from .group_policy_configuration_ingestion_type import GroupPolicyConfigurationIngestionType
from .group_policy_configuration_assignment import GroupPolicyConfigurationAssignment
from .group_policy_definition_value import GroupPolicyDefinitionValue

