from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Update_definition_valuesPostRequest(BaseModel):
	added: Optional[list[GroupPolicyDefinitionValue]] = Field(alias="added", default=None,)
	updated: Optional[list[GroupPolicyDefinitionValue]] = Field(alias="updated", default=None,)
	deletedIds: Optional[list[str]] = Field(alias="deletedIds", default=None,)

from .group_policy_definition_value import GroupPolicyDefinitionValue
