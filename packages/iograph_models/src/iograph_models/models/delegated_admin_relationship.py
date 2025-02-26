from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class DelegatedAdminRelationship(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	accessDetails: Optional[DelegatedAdminAccessDetails] = Field(default=None,alias="accessDetails",)
	activatedDateTime: Optional[datetime] = Field(default=None,alias="activatedDateTime",)
	autoExtendDuration: Optional[str] = Field(default=None,alias="autoExtendDuration",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	customer: Optional[DelegatedAdminRelationshipCustomerParticipant] = Field(default=None,alias="customer",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	duration: Optional[str] = Field(default=None,alias="duration",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	status: Optional[DelegatedAdminRelationshipStatus] = Field(default=None,alias="status",)
	accessAssignments: list[DelegatedAdminAccessAssignment] = Field(alias="accessAssignments",)
	operations: list[DelegatedAdminRelationshipOperation] = Field(alias="operations",)
	requests: list[DelegatedAdminRelationshipRequest] = Field(alias="requests",)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.resellerDelegatedAdminRelationship":
				from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship
				return ResellerDelegatedAdminRelationship.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .delegated_admin_access_details import DelegatedAdminAccessDetails
from .delegated_admin_relationship_customer_participant import DelegatedAdminRelationshipCustomerParticipant
from .delegated_admin_relationship_status import DelegatedAdminRelationshipStatus
from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest

