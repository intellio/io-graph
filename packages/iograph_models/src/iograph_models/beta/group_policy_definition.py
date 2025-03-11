from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	categoryPath: Optional[str] = Field(alias="categoryPath",default=None,)
	classType: Optional[GroupPolicyDefinitionClassType | str] = Field(alias="classType",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	explainText: Optional[str] = Field(alias="explainText",default=None,)
	groupPolicyCategoryId: Optional[UUID] = Field(alias="groupPolicyCategoryId",default=None,)
	hasRelatedDefinitions: Optional[bool] = Field(alias="hasRelatedDefinitions",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	minDeviceCspVersion: Optional[str] = Field(alias="minDeviceCspVersion",default=None,)
	minUserCspVersion: Optional[str] = Field(alias="minUserCspVersion",default=None,)
	policyType: Optional[GroupPolicyType | str] = Field(alias="policyType",default=None,)
	supportedOn: Optional[str] = Field(alias="supportedOn",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	category: Optional[GroupPolicyCategory] = Field(alias="category",default=None,)
	definitionFile: SerializeAsAny[Optional[GroupPolicyDefinitionFile]] = Field(alias="definitionFile",default=None,)
	nextVersionDefinition: Optional[GroupPolicyDefinition] = Field(alias="nextVersionDefinition",default=None,)
	presentations: SerializeAsAny[Optional[list[GroupPolicyPresentation]]] = Field(alias="presentations",default=None,)
	previousVersionDefinition: Optional[GroupPolicyDefinition] = Field(alias="previousVersionDefinition",default=None,)

from .group_policy_definition_class_type import GroupPolicyDefinitionClassType
from .group_policy_type import GroupPolicyType
from .group_policy_category import GroupPolicyCategory
from .group_policy_definition_file import GroupPolicyDefinitionFile
from .group_policy_presentation import GroupPolicyPresentation

