from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PrivilegeManagementElevationRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.privilegeManagementElevationRequest"] = Field(alias="@odata.type", default="#microsoft.graph.privilegeManagementElevationRequest")
	applicationDetail: Optional[ElevationRequestApplicationDetail] = Field(alias="applicationDetail", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	requestCreatedDateTime: Optional[datetime] = Field(alias="requestCreatedDateTime", default=None,)
	requestedByUserId: Optional[str] = Field(alias="requestedByUserId", default=None,)
	requestedByUserPrincipalName: Optional[str] = Field(alias="requestedByUserPrincipalName", default=None,)
	requestedOnDeviceId: Optional[str] = Field(alias="requestedOnDeviceId", default=None,)
	requestExpiryDateTime: Optional[datetime] = Field(alias="requestExpiryDateTime", default=None,)
	requestJustification: Optional[str] = Field(alias="requestJustification", default=None,)
	requestLastModifiedDateTime: Optional[datetime] = Field(alias="requestLastModifiedDateTime", default=None,)
	reviewCompletedByUserId: Optional[str] = Field(alias="reviewCompletedByUserId", default=None,)
	reviewCompletedByUserPrincipalName: Optional[str] = Field(alias="reviewCompletedByUserPrincipalName", default=None,)
	reviewCompletedDateTime: Optional[datetime] = Field(alias="reviewCompletedDateTime", default=None,)
	reviewerJustification: Optional[str] = Field(alias="reviewerJustification", default=None,)
	status: Optional[ElevationRequestState | str] = Field(alias="status", default=None,)

from .elevation_request_application_detail import ElevationRequestApplicationDetail
from .elevation_request_state import ElevationRequestState
