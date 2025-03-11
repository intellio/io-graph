from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UpdatePostRequest(BaseModel):
	addedPolicySetItems: SerializeAsAny[Optional[list[PolicySetItem]]] = Field(alias="addedPolicySetItems",default=None,)
	updatedPolicySetItems: SerializeAsAny[Optional[list[PolicySetItem]]] = Field(alias="updatedPolicySetItems",default=None,)
	deletedPolicySetItems: Optional[list[str]] = Field(alias="deletedPolicySetItems",default=None,)
	assignments: Optional[list[PolicySetAssignment]] = Field(alias="assignments",default=None,)

from .policy_set_item import PolicySetItem
from .policy_set_item import PolicySetItem
from .policy_set_assignment import PolicySetAssignment

